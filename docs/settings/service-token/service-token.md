# What Are Service Tokens

Service Tokens are secure credentials used by Service Accounts to authenticate automated workflows within the Qualytics API. They
act as long-lived access keys, enabling seamless interaction between automation systems and the API without requiring user intervention.

## Key Features of Service Tokens

- **Secure Authentication:** Service Tokens authenticate API requests made by automated systems, ensuring that only authorized applications can access resources.

- **Tied to Service Accounts:** Unlike Personal Access Tokens (PATs), Service Tokens are linked to Service Accounts, which are synthetic users designed for automation.

- **Expiration:** Service Tokens support expiration settings, limiting the lifespan of tokens for added security.

- **Revocation & Restoration:** Tokens can be revoked when no longer needed or if compromised, and can be restored if needed.

- **Multiple Tokens:** Each Service Account can have multiple tokens for different environments or purposes, providing flexibility for automation workflows.

## Benefits of Service Tokens

### Secure Long-Term Authentication

Service Tokens eliminate the need for manual user-based authentication. Once a token is generated, it can be used for long-term, automated access to the API, without requiring human involvement for renewal.

### Role-Based Access Control

Service Tokens are tied to Service Accounts, which can be assigned specific roles and permissions. This ensures that automated systems only have access to the necessary resources based on the defined permissions.

### Scalability

As your automation grows, you can create additional tokens for different purposes or environments, allowing your automated workflows to scale securely.

## How Service Tokens Work

1. **Generate a Service Token:** When a Service Account is created, an administrator generates a Service Token linked to that account. The token can be set to expire after a certain period, such as 30 days, 1 year, etc.

2. **Include Token in API Requests:** The generated token is included in the Authorization header when making API requests
   to authenticate the Service Account.

3. **Token Expiry & Rotation:** Tokens will expire based on the settings, and periodic rotation should be practiced to maintain security.

4. **Revoking & Restoring Tokens:** Tokens that are no longer needed or are suspected to be compromised can be revoked, ensuring that access is stopped immediately. Tokens can be restored if needed.

!!! note 
    Service Tokens are essential for secure and scalable automation workflows. Ensure you follow best practices for token generation, management, and rotation to minimize security risks.
