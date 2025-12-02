# Best Practices

## Service Account Naming Conventions

Consistent naming conventions are essential for clear audit logs and smooth integrations. Follow these guidelines to keep service account names organized and manageable. Each token name must be unique within its service account, but it does not need to be globally unique.

### Auto-Generated Service Account ID Format

When you create a service account, the system automatically generates a service account ID
based on the name you provide.

**Example:**

- **Original Name:** "Pipeline Automation"
- **Auto-Generated ID:** `pipeline_automation@service`

The system applies the following sanitization rules to generate the ID:

- **Lowercase letters** are used.
- **Spaces** are converted to **underscores**.
- **Special characters** are removed.

### Naming Rules

Follow these rules to ensure consistency and clarity:

- Use lowercase letters.
- Replace spaces with underscores.
- Remove any special characters.

### Best Practices for Naming

**Recommended Naming Examples:**

- `pipeline_automation@service` — Clear and specific purpose.
- `alation_sync@service` — Reflects the integration name.
- `finance_metrics@service` — Indicates the purpose of the service account.

**Names to Avoid:**

- `service1@service` — Not descriptive enough.
- `temp@service` — Unclear and vague.
- `test123@service` — Too generic and unhelpful.

!!! note 
    Service account names appear in audit logs, so it’s essential to choose meaningful names that clearly indicate the purpose of the service account.

## Token Rotation

For security best practices, tokens should be rotated regularly, especially before they expire.

### Token Rotation Process

1. **Create a New Token (at least 30 days before expiration)**  
   Generate a new token for the same service account and give it a clear name (e.g.,`production-integration-2025`).

2. **Share the New Token**  
   Provide the newly generated token to your integration or engineering team.

3. **Update Secrets**  
   Update your environment variables or secrets manager with the new token.

4. **Verify Integration**  
   Confirm that your integration or automation works correctly using the new token.

5. **Monitor Token Usage**  
   Check the Last Used timestamp to ensure the new token is active and the old token is
   no longer in use.

6. **Revoke the Old Token**  
   Once you've confirmed the new token works, revoke the old token to prevent any further
   access.

7. **Observe a Grace Period**  
   Monitor for at least 7 days to ensure no unexpected usage occurs on the old token.

8. **Delete the Old Token**  
   After the grace period, permanently delete the revoked token.

## Role Assignment

Assigning the correct role to a service account is essential for enforcing the principle of least
privilege and ensuring secure integration access.

### Role Guidelines

| **Use Case** | **Recommended Role** | **Rationale** |
|---------|-------------------|-----------|
| **Data catalog sync** (Alation, Atlan) | Manager | Requires access to read datastores, containers, and quality checks |
| **Data pipeline automation** | Editor | Needs permission to trigger operations and create containers |
| **Qualytics CLI automation** | Editor | Must be able to run profiling and scanning operations |
| **Read-only API access** | Member | Only needs to view metrics, anomalies, and quality results |
| **BI tool integration** | Member | Only requires read access to data quality outputs |
| **Full platform automation** | Admin | Requires full control over users, teams, integrations, and platform resources |

### Role Permissions

| **Permission** | **Member** | **Editor** | **Manager** | **Admin** |
|-----------|--------|--------|---------|--------|
| Read data quality results | ✅ | ✅ | ✅ | ✅ |
| View datastores and containers | ✅ | ✅ | ✅ | ✅ |
| Create and modify resources | ❌ | ✅ | ✅ | ✅ |
| View all users and teams | ❌ | ❌ | ✅ | ✅ |
| Manage users and service accounts | ❌ | ❌ | ❌ | ✅ |
| Configure integrations | ❌ | ❌ | ❌ | ✅ |

**Recommendation:** Start with the **Member** role whenever possible, and escalate only if the integration requires additional capabilities.

## Security Guidelines

Proper token management is essential to maintaining a secure environment. The guidelines below outline how to safely store rotate, monitor, and review service tokens across all environments.

### Token Storage

✅ **Do:**

- Use secure secrets managers such as HashiCorp Vault, AWS Secrets Manager, or Azure Key Vault
- Load tokens through environment variables in deployment configurations
- Encrypt tokens at rest
- Rotate tokens on a defined schedule

❌ **Don’t:**

- Commit tokens to Git or any version control system
- Store tokens in plain or unencrypted text files
- Share tokens through email, chat, or other unsecure channels
- Reuse the same token across multiple environments

## Token Expiration Strategy

Set token expiration periods based on environment type:

| **Environment** | **Recommended Expiration** | **Notes** |
|-------------|-------------------------|--------|
| **Production** | 365 days | Begin rotation at least 30 days before expiration |
| **Staging** | 180 days | Shorter duration due to non-production usage |
| **Development** | 90 days | Frequent rotation aligns with active development cycles |
| **Testing** | 7–30 days | Ideal for temporary testing or short-lived workflows |

## Monitoring and Auditing

Regularly monitor token activity to maintain operational security.

1. **Monthly Reviews**
   - Check “Last Used” timestamps for all tokens  
   - Revoke tokens unused for 90+ days  
   - Review each service account’s role to ensure it remains appropriate  

2. **Audit Trail**
   - All API requests log the authenticated service account  
   - `created_by_id` identifies the admin who created the account  
   - Token usage is captured through the `last_used` timestamp  

3. **Alert on Anomalies**
   - Sudden or unexpected token usage  
   - Requests from unfamiliar or suspicious IPs  
   - Repeated failed authentication attempts  

## Access Reviews

Conduct quarterly reviews of all service accounts and tokens.

**Review Checklist:**

- Each service account has a clearly documented purpose  
- Token names accurately reflect their usage  
- No tokens are close to expiration without a rotation plan  
- `last_used` timestamps show expected activity  
- Roles follow the principle of least privilege  
- Team memberships match required access  
- No orphaned tokens exist (tokens tied to deleted service accounts)  

## Security Considerations

Keeping service accounts and tokens secure is critical to protecting your data, infrastructure, and API access. The following guidelines outline recommended practices for handling tokens, responding to incidents, and maintaining compliance.

### Token Security

**Bearer Tokens Are Sensitive**

- Treat every token as securely as a password  
- Anyone with the token can fully authenticate as that service account  
- Tokens are hashed using HMAC-SHA256 before being stored  
- Lost tokens cannot be retrieved—new tokens must be created  

### Immediate Revocation

- Revoke tokens immediately if you suspect compromise  
- Token deletion is a two-step process (revoke → delete)  
- Revoked tokens stop working instantly—no grace period  

## Incident Response

### If a Token Is Compromised

1. **Immediate Actions**
   - Revoke the affected token  
   - Notify your security team  
   - Review audit logs  

2. **Investigation**
   - Analyze all API requests made using the token  
   - Determine scope of unauthorized access  
   - Check if data was altered or exfiltrated  

3. **Remediation**
   - Generate a new token  
   - Update integrations to use the new token  
   - Delete the compromised token  
   - Document the incident  

4. **Prevention**
   - Strengthen storage and handling practices  
   - Improve monitoring and alerts  
   - Provide security training if needed  

## If a Service Account Is Compromised

1. Immediately revoke all tokens  
2. Create a new service account  
3. Audit all actions performed by the compromised account  
4. Rotate any downstream credentials, keys, or integrations  

## Compliance Considerations

### Separation of Duties

- Use dedicated service accounts for production integrations  
- Personal Access Tokens should only be used in development  
- Require admin approval before creating service accounts  
- Document ownership and purpose  

### Least Privilege

- Start with Member role  
- Grant only needed team access  
- Conduct regular permission reviews  
- Document justification for elevated access  
