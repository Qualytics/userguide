# Auth0 Authentication Setup

!!! warning "Self-Hosted Deployments Only"
    This guide is for **customer-managed (self-hosted) deployments** where you manage your own Kubernetes infrastructure. If your Qualytics instance is managed by Qualytics (PaaS/SaaS), see the [SSO Setup Guide](sso.md) instead — your account manager handles authentication configuration for you.

This guide explains how to configure Auth0 authentication for a self-hosted Qualytics deployment. Auth0 is an **alternative authentication method** managed by Qualytics. While [OIDC](oidc-configuration.md) is recommended for most self-hosted deployments, Auth0 is a simpler option for organizations that have internet access from their cluster and prefer a managed authentication service.

## When to Use Auth0 vs OIDC

| Consideration | Auth0 | OIDC |
|---------------|-------|------|
| **Internet access** | Requires egress to `auth.qualytics.io` | No internet access required |
| **Air-gapped support** | Not supported | Fully supported |
| **Setup complexity** | Simpler — Qualytics manages the IdP | Requires IdP configuration by the customer |
| **IdP management** | Managed by Qualytics | Managed by the customer |
| **SSO federation** | Supports SSO through Auth0's integration network | Direct integration with your enterprise IdP |
| **CLI authentication** | Browser-based PKCE flow | Manual token paste |

!!! tip "Recommendation"
    **OIDC is recommended** for self-hosted deployments because it provides direct integration with your enterprise Identity Provider, supports air-gapped environments, and keeps authentication entirely within your network. Use Auth0 if you prefer a managed solution and your cluster has internet access.

## How Auth0 Works for Self-Hosted Deployments

Unlike OIDC (where you configure your own Identity Provider), Auth0 is a managed service where Qualytics handles the authentication infrastructure:

1. **You request** Auth0 resources from Qualytics
2. **Qualytics provisions** an Auth0 organization, client credentials, and SSO connections
3. **You configure** the provided values in your Helm deployment
4. **Qualytics manages** ongoing Auth0 maintenance and updates

## Step 1: Request Auth0 Resources from Qualytics

Contact your [Qualytics account manager](mailto:hello@qualytics.ai) to request Auth0 authentication for your self-hosted deployment. Include the following information in your request:

| Information | Description |
|-------------|-------------|
| **Company name** | Your organization's name |
| **Deployment domain** | The domain where Qualytics will be accessible (e.g., `qualytics.example.com`) |
| **SSO requirements** (optional) | If you want to federate Auth0 with your enterprise IdP (e.g., Azure AD, Okta), specify the IdP and protocol (SAML, OIDC) |
| **User count estimate** | Approximate number of users who will access Qualytics |

### What You Will Receive

After Qualytics provisions your Auth0 resources, your account manager will provide:

| Value | Description |
|-------|-------------|
| `AUTH0_DOMAIN` | Your Auth0 tenant domain (typically `auth.qualytics.io`) |
| `AUTH0_AUDIENCE` | Your API audience identifier |
| `AUTH0_ORGANIZATION` | Your Auth0 organization ID (e.g., `org_abc123`) |
| `AUTH0_CLIENT_ID` | Your SPA client ID (required for UI and CLI authentication) |

## Step 2: Configure Qualytics

Add the Auth0 values provided by Qualytics to your Helm `values.yaml` file:

### Required Settings

| Helm Value | Description |
|------------|-------------|
| `secrets.auth0.auth0_audience` | API audience identifier (provided by Qualytics) |
| `secrets.auth0.auth0_organization` | Auth0 organization ID (provided by Qualytics) |
| `secrets.auth0.auth0_spa_client_id` | SPA client ID (provided by Qualytics) |
| `secrets.auth.jwt_signing_secret` | Secret for signing JWTs (minimum 32 characters — you generate this) |

!!! note
    Auth0 is the default authentication mode (`global.authType: "AUTH0"`), so you do not need to set it explicitly. The Auth0 domain defaults to `auth.qualytics.io`.

### Example `values.yaml` Configuration

```yaml
global:
  dnsRecord: "qualytics.example.com"
  authType: "AUTH0"  # default — can be omitted

secrets:
  auth0:
    auth0_audience: "your-api-audience"
    auth0_organization: "org_your-org-id"
    auth0_spa_client_id: "your-spa-client-id"
  auth:
    jwt_signing_secret: "your-secure-random-string-min-32-chars"
  postgres:
    secrets_passphrase: "your-secure-passphrase"
  rabbitmq:
    rabbitmq_password: "your-secure-password"
```

!!! tip "Generating Secure Secrets"
    Use `openssl rand -base64 32` to generate the `jwt_signing_secret` and other security secrets.

## Step 3: Deploy or Restart

If this is a new deployment, follow the [Self-Hosted Deployment Guide](self-hosted-deployment.md) to deploy Qualytics.

If you are updating an existing deployment:

```bash
helm upgrade qualytics qualytics/qualytics \
  --namespace qualytics \
  -f values.yaml \
  --timeout=20m
```

## Step 4: Verify Authentication

1. Navigate to your Qualytics instance in a browser (e.g., `https://qualytics.example.com`)
2. You should be redirected to the Auth0 login page
3. Authenticate using your credentials (or your enterprise SSO if configured)
4. After successful authentication, you should be redirected back to the Qualytics UI

## Network Requirements

Auth0 authentication requires your cluster to have outbound (egress) access to:

| Endpoint | Purpose |
|----------|---------|
| `https://auth.qualytics.io` | Auth0 authentication service |

!!! warning "Air-Gapped Environments"
    Auth0 is **not compatible** with fully air-gapped deployments. If your environment has no internet access, use [OIDC authentication](oidc-configuration.md) instead.

## SSO Federation Through Auth0

Auth0 supports federating authentication with your enterprise Identity Provider. This means your users can log in to Qualytics using their existing corporate credentials through Auth0.

Supported federation protocols through Auth0:

- OpenID Connect (OIDC)
- SAML 2.0
- Active Directory / LDAP
- Azure Active Directory (Entra ID)
- Google Workspace
- Okta
- PingFederate

To set up SSO federation, include your IdP details when [requesting Auth0 resources](#step-1-request-auth0-resources-from-qualytics) from Qualytics. Your account manager will configure the appropriate connection.

## CLI Authentication

With Auth0, the Qualytics CLI supports **browser-based authentication** using the PKCE (Proof Key for Code Exchange) flow:

1. Run the CLI authentication command
2. A browser window opens automatically
3. Authenticate with Auth0 (or your federated IdP)
4. The CLI receives the token automatically

This provides a smoother CLI experience compared to the manual token paste required with OIDC.

## Troubleshooting

| Symptom | Likely Cause | Solution |
|---------|-------------|----------|
| Cannot reach Auth0 login page | Network egress blocked | Ensure your cluster allows outbound access to `https://auth.qualytics.io` |
| Invalid audience or organization error | Incorrect Auth0 configuration | Verify `secrets.auth0.auth0_audience` and `secrets.auth0.auth0_organization` match what Qualytics provided |
| CLI authentication fails | Missing client ID | Ensure `secrets.auth0.auth0_spa_client_id` is set in your `values.yaml` |
| SSO redirect loop | Misconfigured SSO connection | Contact your [Qualytics account manager](mailto:hello@qualytics.ai) to verify the SSO connection |

!!! info "Need Help?"
    Contact your [Qualytics account manager](mailto:hello@qualytics.ai) for assistance with Auth0 configuration or to request changes to your Auth0 setup.
