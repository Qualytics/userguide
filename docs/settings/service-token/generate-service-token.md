# Generate Service Token

Service Tokens are generated when you create a **Service Account** or manually through the **Tokens** management page. These tokens are essential for automating API interactions and securely authenticating requests made by your automated systems.

Let’s get started 🚀

**Step 1:** Log in to your Qualytics account and click the **Settings** button on the left side panel of the interface.

![setting](../../assets/tokens/service-token/settings-1.png)

**Step 2:** By default, you will be navigated to the **Connections** section. Click on the **Tokens** tab.

![tokens](../../assets/tokens/service-token/token-2.png)

**Step 3:** Click on the **Generate Token** button located in the top right corner.

![generate-token](../../assets/tokens/service-token/generate-token-3.png)

A modal window will appear, providing the options for generating the token.

![window](../../assets/tokens/service-token/window-4.png)

**Step 4:** Enter the following values:

| No. | Field | Description | Required |
|-----|--------|-------------|-----------|
| 1 | Name | Enter a descriptive name for the token (e.g., "svc-token-prod", "api-access-prod"). | Yes |
| 2 | Type | Select **Service** for a service account token. | Yes |
| 3 | Service User | Select the service user for which you want to create the token. | Yes |
| 4 | Expiration | Select the expiration period (e.g., 30 Days, 1 Year, Never). | Yes |
| 5 | SCIM Administration Token | Check this box if the token should be restricted to SCIM endpoints only. | Optional |

![value](../../assets/tokens/service-token/values-5.png)

**Step 5:** Once you have entered the values, click on the **Generate** button.

![generate](../../assets/tokens/service-token/generate-6.png)

**Step 6:** After clicking on the Generate button, your token is successfully generated.

![token](../../assets/tokens/service-token/token-7.png)

!!! warning
    Make sure to **download or copy this token**. You won't be able to see it again. Keep your token confidential and avoid sharing it with anyone. Use a password manager or an encrypted vault to store your tokens.

**Step 7:** After copying the token, you can close the modal. The token will now appear in the service tokens list.

![list](../../assets/tokens/service-token/list-8.png)

## Usage of Service Tokens

Once generated, include the service token in the Authorization header of all API requests:

```bash
curl -H "Authorization: Bearer eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9..." \
  https://acme.qualytics.io/api/datastores
```

**Example Python Usage:**

```python
import requests

QUALYTICS_TOKEN = "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9..."
QUALYTICS_API = "https://acme.qualytics.io/api"

headers = {
    "Authorization": f"Bearer {QUALYTICS_TOKEN}",
    "Content-Type": "application/json"
}

response = requests.get(f"{QUALYTICS_API}/datastores", headers=headers)
print(response.json())
```

## Creating a Service Token via API

**Endpoint:**

```bash
POST /user-tokens
Authorization: Bearer {admin_token}
Content-Type: application/json
```

**Request Body:**

```json
{
  "name": "api-production",
  "user_id": 123,
  "expires_in_days": 365
}
```

**Response:**

```json
{
  "id": 456,
  "name": "api-production",
  "active": true,
  "expiration": "2026-11-05T12:34:56Z",
  "bearer_token": "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9...",
  "user": {
    "id": 123,
    "user_id": "api_access@service",
    "name": "API Access",
    "user_type": "Service"
  }
}
```
!!! danger
    Save the `bearer_token` immediately! It cannot be retrieved later.
