# How Connections Work

A connection defines how Qualytics authenticates and communicates with your data infrastructure. It stores the credentials, host information, and configuration needed to reach a specific system — whether it is a relational database, a cloud data warehouse, or a file storage bucket.

## Connection Types

Qualytics supports three connection types, each designed for a different class of data source:

| Type | Description | Examples |
| :--- | :--- | :--- |
| **JDBC** | Relational databases and SQL-based warehouses accessed via JDBC drivers. | PostgreSQL, Snowflake, BigQuery, MySQL, Oracle, SQL Server, Redshift, Databricks, Athena, Synapse, Teradata |
| **DFS** | Distributed file systems and cloud object storage. | Amazon S3, Azure Data Lake Storage (ABFS), Google Cloud Storage |
| **Native** | Platform-native integrations that bypass JDBC for optimized access. | Databricks Unity Catalog |

!!! note "Native vs. JDBC"
    Databricks is available as both a **JDBC** and **Native** connector. The JDBC connector uses standard JDBC drivers to query data. The Native connector uses the Databricks Unity Catalog API directly, providing access to catalog metadata and schema discovery without going through JDBC — this is typically faster for schema operations and supports Unity Catalog-specific features.

## Connection vs. Datastore

A connection and a datastore serve different roles:

- A **connection** holds the credentials and endpoint information (host, port, username, password, access keys) needed to authenticate with a system.
- A **datastore** represents a specific data scope within that system (a database + schema for JDBC, a root path for DFS).

This separation means **one connection can be shared across multiple datastores**. For example, a single Snowflake connection (host, role, warehouse, credentials) can serve datastores for `production.public`, `production.sales`, and `production.finance` — each pointing to a different schema.

| Layer | JDBC | DFS | Native |
| :--- | :--- | :--- | :--- |
| **Connection** (shared) | Host, Port, Username, Password, Role, Warehouse | URI, Access Key, Secret Key | Workspace URL, Catalog Name |
| **Datastore** (specific) | Database, Schema | Root Path | Schema |

## Connection Lifecycle

### Creating a Connection

When you add a source datastore with a **new connection**, the connection is created alongside the datastore in a single step:

1. You provide the connection credentials (host, credentials, parameters).
2. You configure the datastore-specific properties (database, schema, or root path).
3. You click **Test Connection** — Qualytics validates connectivity without persisting anything.
4. On success, clicking **Finish** creates both the connection and the datastore.

### Reusing a Connection

When you add a source datastore with an **existing connection**, you skip the credential setup:

1. You select a previously created connection from the dropdown.
2. The connection properties are displayed as **read-only** — they cannot be modified from the datastore form.
3. You only configure the datastore-specific properties (database, schema, or root path).
4. The test connection verifies that the existing credentials can reach the new datastore scope.

!!! info
    Reusing connections ensures credential consistency across datastores and reduces the risk of configuration drift. If the password changes, updating the connection once propagates to all datastores that use it.

### Testing a Connection

The **Test Connection** step validates connectivity without persisting any data:

1. A temporary datastore is built in memory with the provided credentials.
2. The controlplane sends the credentials to the dataplane for a connectivity check.
3. The dataplane attempts to connect (e.g., executes a test SQL query for JDBC, lists objects for DFS).
4. The result is returned — success or an error message describing the failure.

No data is written to the database during this step. The connection and datastore are only persisted after you click **Finish**.

### Editing a Connection

Connection properties can be updated through the [Manage Connections](../../../settings/connections/manage-connections.md){:target="_blank"} page in Settings. When credentials change (e.g., password rotation), the update triggers a re-verification through the dataplane before persisting.

!!! warning
    Editing a connection affects **all datastores** that share it. If you change the host or credentials, every datastore using that connection will use the updated values.

### Deleting a Connection

A connection can only be deleted if it has **no datastores associated** with it. If any datastores still use the connection, the deletion will fail with a `409 Conflict` error — you must delete or reassign those datastores first.

!!! note "Orphaned Connections"
    Connections without any associated datastores remain in the system until explicitly deleted. They are visible in the [Manage Connections](../../../settings/connections/manage-connections.md){:target="_blank"} page and can be reused when creating new datastores.

## Network Requirements

Qualytics requires **direct network access** from the dataplane to your data infrastructure. Consider the following:

- **Firewall rules** — The dataplane IP address must be allowed to connect to your database or storage endpoint. Contact your Qualytics administrator for the dataplane IP range.
- **Private endpoints** — For databases in private VPCs, configure VPC peering, private endpoints, or a VPN tunnel between the dataplane and your network.
- **IP whitelisting** — If your database requires IP whitelisting, add the dataplane IP addresses to the allowlist.
- **Port access** — Ensure the required port is open (e.g., 5432 for PostgreSQL, 443 for Snowflake/BigQuery/S3).

## Secrets Management

Qualytics supports integration with external secrets managers to avoid storing credentials directly. Instead of entering a password, you configure a secrets manager integration and reference secrets using the `${key}` syntax in any connection property.

!!! note "Generic HTTP-Based Integration"
    The secrets management integration is **not limited to HashiCorp Vault**. It works with any secrets manager that exposes a REST API with a login endpoint (POST), token-based authentication, and a secret retrieval endpoint (GET). HashiCorp Vault is the most common provider, but compatible alternatives include AWS Secrets Manager (via API Gateway), Azure Key Vault (via REST API), and CyberArk (via REST).

### How It Works

1. **Authentication**: Qualytics sends a POST request to your secrets manager's login URL with the provided credentials payload.
2. **Token extraction**: The authentication token is extracted from the response using a JSONPath expression.
3. **Secret retrieval**: A GET request is sent to the secret URL with the token in the configured header.
4. **Variable substitution**: The retrieved secrets are used to replace `${key}` references in connection properties at runtime.

### Configuration Fields

| Field | Description |
| :--- | :--- |
| **Login URL** | The authentication endpoint of your secrets manager. |
| **Credentials Payload** | A valid JSON containing the credentials for vault authentication. |
| **Token JSONPath** | JSONPath expression to extract the token from the login response (e.g., `$.auth.client_token`). |
| **Secret URL** | The endpoint where the secret data is stored. |
| **Token Header Name** | The HTTP header name for the authentication token (e.g., `X-Vault-Token`). |
| **Data JSONPath** | JSONPath expression to extract the secret data from the response (e.g., `$.data`). |

!!! note
    Secrets are retrieved dynamically each time the connection is used. This means password rotations in your vault are automatically picked up without updating the Qualytics configuration.

## Authentication Methods

Different connectors support different authentication methods. **Basic** (username and password) is the default method available on all JDBC connectors. The other methods are additional options for specific connectors:

| Method | Description | Connectors |
| :--- | :--- | :--- |
| **Basic** | Username and password. Default for all JDBC connectors. | All JDBC connectors |
| **Keypair** | Private key authentication. | Snowflake |
| **Service Principal** | Azure AD service principal with tenant ID and client secret. | Azure SQL, Synapse, Fabric, Azure Data Lake Storage |
| **OAuth M2M** | Machine-to-machine OAuth flow. | Databricks |
| **Shared Key** | Access key and secret key. | Amazon S3, Azure Blob Storage |
| **Kerberos** | Kerberos ticket-based authentication. | Hive |

## Credential Security

All connection credentials are encrypted at rest using **AES-GCM encryption**. Sensitive fields (passwords, access keys, secret keys, vault credentials) are stored using encrypted column types in the controlplane database.

Credentials are **decrypted only in the controlplane** when preparing a dataplane operation — they are then transmitted securely to the dataplane over an internal TLS-encrypted channel. The dataplane does not persist credentials; it uses them only for the duration of the operation (Sync, Profile, Scan, or Test Connection).
