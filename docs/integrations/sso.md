# SSO (Single Sign-On) Integrations

The Qualytics platform provides enterprise-grade authentication integration capabilities, enabling organizations to:

-  Implement secure, frictionless access across all platform components
-  Leverage existing identity providers and authentication workflows
-  Support both cloud-based and on-premise deployment scenarios
-  Maintain compliance with corporate security policies
-  Enable seamless mobile and web-based access
-  Automate user provisioning and access management

These authentication capabilities ensure that Qualytics seamlessly integrates with your organization's identity and access management infrastructure while maintaining the highest security standards.

## SSO for PaaS Deployments

Qualytics platform harnesses the power of [Auth0's Single Sign-On](https://auth0.com/) (SSO) technology to create a frictionless authentication journey for our PaaS users. Once users have successfully logged in to Qualytics, they can conveniently access all linked external applications and services without the need for additional sign-ins. Depending on the application and its compatibility with federated SSO protocols such as SAML, OIDC, or any proprietary authentication methods, Qualytics, with the help of Auth0, establishes a secure connection for user authentication. In essence, SSO allows one central domain to authenticate and then share the session across various other domains. The method of sharing may vary between SSO protocols, but the principle remains constant.

Through Auth0's Integration Network (OIN), Qualytics extends SSO access to an extensive range of supported cloud-based applications. These integrations can utilize OpenID Connect (OIDC), SAML, SWA, or proprietary APIs for SSO. Maintenance of SSO protocols and provisioning APIs is reliably managed by Auth0.

In addition to this, Qualytics also leverages Auth0's capabilities to provide SSO integrations for on-premises web-based applications. You have the option to integrate these applications via SWA or SAML toolkits. In addition, Auth0 supports user provisioning and deprovisioning with applications that publicly offer their provisioning APIs.

Further enhancing our SSO integrations, Qualytics provides seamless access to mobile applications. Whether they are web applications optimized for mobile devices, native iOS apps, or Android apps, users can access web app integrations in the OIN using SSO from any mobile device. These mobile web apps can employ industry-standard OIDC, SAML, or Auth0 SWA technologies. To illustrate, Qualytics, in conjunction with Auth0, can integrate with native applications such as Box Mobile using SAML for registration and OAuth for continuous use.

Auth0 supports the following enterprise providers out of the box:
-  [OAuth2](https://auth0.com/docs/authenticate/identity-providers/social-identity-providers/oauth2)
-   [Active Directory/LDAP](https://auth0.com/docs/authenticate/identity-providers/enterprise-identity-providers/active-directory-ldap)

-   [ADFS](https://auth0.com/docs/authenticate/identity-providers/enterprise-identity-providers/adfs)

-   [Azure Active Directory Native](https://auth0.com/docs/authenticate/identity-providers/enterprise-identity-providers/azure-active-directory-native)

-   [Google Workspace](https://auth0.com/docs/authenticate/identity-providers/enterprise-identity-providers/google-apps)

-   [OpenID Connect](https://auth0.com/docs/authenticate/identity-providers/enterprise-identity-providers/oidc)

-   [Okta](https://auth0.com/docs/authenticate/identity-providers/enterprise-identity-providers/okta)

-   [PingFederate](https://auth0.com/docs/authenticate/identity-providers/enterprise-identity-providers/ping-federate)

-   [SAML](https://auth0.com/docs/authenticate/identity-providers/enterprise-identity-providers/saml)

-   [Azure Active Directory](https://auth0.com/docs/authenticate/identity-providers/enterprise-identity-providers/azure-active-directory/v2)


## SSO for On-Premise Deployments

In addition to the option of leveraging our robust Auth0 support for federated authentication, customer-managed deployments can choose to directly integrated with their IdP (Identity Provider such as Active Directory, ForgeRock, etc) using OpenID Connect (OIDC). Once configured for direct federated authentication using OIDC, the customer's own user login requirements fully govern the authentication process in support of a fully air-gapped deployment of Qualytics with no egress required for operations.
