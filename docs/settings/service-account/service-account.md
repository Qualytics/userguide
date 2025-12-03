# Service Accounts

Service Accounts provide a secure and centralized way to authenticate automated systems and integrations with the Qualytics API. Unlike Personal Access Tokens (PATs) that are tied to individual users, Service Accounts are synthetic users designed specifically for data pipeline automation, Qualytics API/CLI access, data catalog integrations, and shared automation workflows. They eliminate the security risk of sharing personal tokens, remain active independent of individual user lifecycles, role changes, or access status, and provide clear audit trails for automated system activities.

## What Are Service Accounts?

Service accounts are synthetic user accounts created specifically for automation and integrations. They have the following characteristics:

### Key Characteristics

- **No interactive login:** Service accounts cannot log into the Qualytics web interface  
- **Administrator-managed:** Only administrators can create and manage service accounts  
- **Independent lifecycle:** Service accounts are not tied to individual users  
- **Role-based permissions:** Can be assigned Admin, Manager, Editor, or Member roles  
- **Team membership:** Can be assigned to specific teams for scoped access  

!!! info
    Every automated or system-driven integration should use a Service Account instead of a Personal Access Token.

## Typical Use Cases

- Automated ETL or pipeline execution  
- Metadata sync (Alation, Atlan, etc.)  
- Scheduled or recurring quality scanning  
- API-based workflows  
- Multi-user team automation  

## Service Accounts vs Personal Tokens

Understanding the difference between Service Accounts and Personal Access Tokens is essential for secure and reliable automation.

### Comparison Table  

| Feature | Service Account | Personal Access Token (PAT) |
|--------|-----------------|-----------------------------|
| **Created by** | Administrators only | Individual users (self-service) |
| **Tied to** | Synthetic service user | Human user account |
| **Best for** | Production integrations, data pipelines, and shared automation | Personal development, testing, and ad-hoc API exploration |
| **Lifecycle** | Independent of individual user lifecycles | Dependent on the user’s access status |
| **Management** | Centrally managed by administrators | Managed by the individual user |
| **Audit Trail** | Provides clear, purpose-based identification | Linked to a specific user’s activity |

!!! warning 
    Never use PATs in production pipelines — they will break when the user is offboarded, disabled, or role-changed.

## When to Use Service Accounts

Service Accounts are intended for secure, automated, and shared access to Qualytics. They provide consistent authentication for system-level workflows, ensuring stability and centralized management without dependency on individual user credentials.

### ✅ Use Service Accounts For

- **Data Pipeline Automation:** Use Service Accounts to integrate Qualytics operations  
  within your automated data workflows, such as Airflow, dbt, Azure Data Factory, or other  
  ETL pipelines.

- **Qualytics API Access:** For programmatic interactions with Qualytics, such as managing  
  resources or retrieving data through API calls, Service Accounts offer reliable, long-term  
  access.

- **Qualytics CLI Operations:** Automate data quality workflows and recurring tasks using  
  the Qualytics CLI without relying on personal user tokens.

- **Data Catalog Integrations:** Enable metadata synchronization and data lineage tracking  
  with catalog platforms like Alation, Atlan, or other similar tools.

- **Shared Automation:** Use Service Accounts for any automation or integration shared  
  across multiple team members or systems to maintain consistency, security, and proper  
  audit control.

### ❌ Avoid Using Personal Access Tokens (PATs) For

Personal Access Tokens (PATs) are meant for individual, short-term, or development use only.
Avoid using them in the following scenarios:

- **Shared Data Pipelines:** Tokens should not be shared among users due to security risks. 

- **Production Integrations:** Tokens may become invalid if the associated user is  
  deactivated or their role changes.  

- **Team-wide API or CLI Automations:** Difficult to manage and audit across multiple  
  users.  

- **Long-running Integrations:** PATs are tied to individual user lifecycles and are not  
  suitable for continuous system-level access.

!!! tip
    If an automation is shared or runs in production, always use a Service Account instead of a Personal Access Token (PAT) for improved stability, security, and governance.

## Key Takeaways

### Use Service Accounts for Production Integrations

- Operate independently of individual users, their access changes, or lifecycle events
- Centrally managed by administrators for consistency and control
- Provide clear, purpose-based audit trails
- Strengthen overall security posture

### Administrator Responsibilities

- Create, manage, and maintain service accounts
- Perform regular audits of service tokens
- Enforce token rotation and expiration policies
- Maintain documentation for all integrations and use cases

### Security First

- Store tokens securely using secrets managers
- Assign appropriate expiration periods based on the environment
- Monitor activity through Last Used timestamps
- Revoke immediately if a token is lost or compromised

### Least Privilege Principle

- Grant only the minimum permissions required
- Restrict team membership to just the needed scopes
- Conduct recurring access reviews
- Document justification for any elevated roles

## Quick Reference

| Task | UI Location | API Endpoint | Required Role |
|------|-------------|--------------|----------------|
| Create a service account | Settings → Users | POST /users | Admin |
| Create service token | Users → Generate Token | POST /user-tokens | Admin |
| List service tokens | Settings → Tokens (Service filter) | GET /user-tokens/service | Admin |
| Revoke token | Token Menu → Revoke | PUT /user-tokens/{id} | Admin |
| Delete token | Token Menu → Delete | DELETE /user-tokens/{id} | Admin |

## Create a Service Account

Follow the step-by-step UI workflow or use the API to create Service Accounts for automation workflows.

!!! info
    If you need a deeper walkthrough, you can refer to the [Create a Service Account](./create-service-account.md){target="_blank"} documentation.

!!! info
    For API-based setup, see the [Creating a Service Account via API](create-service-account.md#creating-a-service-account-via-api){target="_blank"} guide for step-by-step instructions.

## Naming Conventions

Learn recommended naming patterns that keep your Service Accounts clean, descriptive, and
audit-friendly.

!!! info
    For a deeper explanation, refer to the [Naming Convention](../service-token/best-practices.md#service-account-naming-conventions){target="_blank"} guide.

## Roles & Access

Understand how roles and team membership control what a Service Account can access across the Qualytics platform. 

!!! info
    To learn more about how roles work, refer to the [Role Assignment](../service-token/best-practices.md#role-assignment){target="_blank"} section.

## Security Guidelines

Review best practices for token storage, expiration, monitoring, and incident response for
secure automation.

!!! info 
    You can find more details in the [Security Guidelines](../service-token/best-practices.md#security-guidelines){target="_blank"} documentation.

