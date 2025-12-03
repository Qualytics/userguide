# Revoking a Service Token

Revoking a service token immediately disables it without permanently deleting it. This is useful if you suspect the token has been compromised or need to temporarily stop its access.

**Step 1:** Click the **vertical ellipsis (⋮)** next to the service token that you want to revoke, then click on **Revoke** from the dropdown menu.

![revoke](../../assets/tokens/revoking-service-token/revoke-1.png)

**Step 2:** After clicking the **Revoke** button, your service token will be successfully revoked.

![success](../../assets/tokens/revoking-service-token/revoked-2.png)

!!! warning 
    Revoked tokens cannot be used for API authentication. Any systems using this token will immediately lose access.

## Revoking a Token via API

**Endpoint:**

```bash
PUT /user-tokens/{token_id}
Authorization: Bearer {admin_token}
Content-Type: application/json
```

**Request Body:**

```json
{
  "revoke": true
}
```