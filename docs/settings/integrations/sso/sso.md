# SSO (Single Sign-On) Integrations

The Qualytics platform provides enterprise-grade authentication integration capabilities, enabling organizations to:

-  Implement secure, frictionless access across all platform components
-  Leverage existing identity providers and authentication workflows
-  Support both cloud-based and on-premise deployment scenarios
-  Maintain compliance with corporate security policies
-  Enable seamless mobile and web-based access
-  Automate user provisioning and access management

These authentication capabilities ensure that Qualytics seamlessly integrates with your organization's identity and access management infrastructure while maintaining the highest security standards.

## SSO for Managed (PaaS/SaaS) Deployments

For Qualytics-managed deployments, SSO is configured by your Qualytics account manager using [Auth0](https://auth0.com/). You register Qualytics as an application in your Identity Provider and share the credentials with Qualytics — we handle the rest.

**For step-by-step setup instructions, see the [SSO Setup Guide](../../../deployments/sso.md).**

Supported Identity Providers include:

- Microsoft Entra ID (Azure Active Directory)
- Okta
- Google Workspace
- PingFederate
- Active Directory / LDAP
- ADFS
- Any OIDC or SAML 2.0 compliant provider


## SSO for On-Premise Deployments

Customer-managed (self-hosted) deployments have two options for authentication:

### Option 1: OIDC — Direct IdP Integration (Recommended)

Customer-managed deployments can directly integrate with their Identity Provider (such as Azure AD / Entra ID, Okta, Keycloak, ForgeRock, etc.) using OpenID Connect (OIDC). Once configured for direct federated authentication using OIDC, the customer's own user login requirements fully govern the authentication process — supporting fully air-gapped deployments with no egress required for operations.

OIDC authentication provides:

- Direct integration with your enterprise IdP — no third-party dependencies
- Full support for air-gapped and on-premises environments
- Three-tier security model (HttpOnly cookies + CSRF, token fingerprinting, DPoP)
- Customizable claims mapping for non-standard IdP configurations

For detailed setup instructions, see the **[OIDC Authentication Configuration Guide](../../../deployments/oidc-configuration.md)**.

### Option 2: Auth0 — Managed by Qualytics

Self-hosted customers can also leverage Auth0 for authentication. With this option, Qualytics manages the Auth0 infrastructure — you simply request Auth0 resources from your account manager and configure the provided credentials in your deployment. Auth0 supports SSO federation with all the enterprise providers listed in the [managed deployments section above](#sso-for-managed-paassaas-deployments).

!!! note
    Auth0 requires network egress to `https://auth.qualytics.io` and is not compatible with fully air-gapped deployments.

For detailed setup instructions, see the **[Auth0 Authentication Setup Guide](../../../deployments/auth0-setup.md)**.
