Personal API tokens (`PATs`) are unique strings used to authenticate a user on your platform instead of a regular password. The `PATs` are generated only once and need to be copied and stored securely by the user for future use.

 ![Screenshot](../../assets/tokens/settings-tokens-light.png#only-light)
 ![Screenshot](../../assets/tokens/settings-tokens-dark.png#only-dark)

## Benefits of using PATs

* **Enhanced security:** PATs offer an extra layer of security compared to regular passwords. If a PAT is compromised, your account remains secure as the PAT itself can be revoked.
* **Granular access control:** PATs can be assigned specific permissions, limiting the actions a user can perform on your platform. This reduces the risk of accidental or unauthorized modifications.

## Creating Personal API Tokens

### Generating a new PAT

#### Access the Token Generation Page

- Navigate to the designated area for managing API tokens within your system `Settings`/`Tokens`
- Locate and click the button labeled "`Generate New Token`".

#### Configure Token Details

![Screenshot](../../assets/tokens/configure-new-token-light.png#only-light)
![Screenshot](../../assets/tokens/configure-new-token-dark.png#only-dark)

- **Token Name:** Assign a clear and descriptive name to your token.
- **Expiration:** Choose your desired validity period for the token (30 days, 60 days, 90 days, or 1 year). This determines how long the token remains active.

#### Generate the Token

Once you've configured the details, click the "Generate" button.

#### Copy and Secure Your Token

- A new modal window will appear titled "`Token Successfully Generated`".

![Screenshot](../../assets/tokens/generated-token-light.png#only-light)
![Screenshot](../../assets/tokens/generated-token-dark.png#only-dark)

- This window displays the following information:
    - **Token Name:** The name you entered earlier.
    - **Secret (Token):** The generated token string. This is crucial for API access, so make sure to copy it securely.
    - **Warning:** A prominent message reminding you to copy the secret token, as it won't be visible again.
- Locate the "Copy" button and copy the token string to your clipboard.

### Token Listing

This page will display a list that includes your newly created token with the following details:

![Screenshot](../../assets/tokens/tokens-list-light.png#only-light)
![Screenshot](../../assets/tokens/tokens-list-dark.png#only-dark)

- Token Name
- Expiration Date
- Creation Date
- Status (Active)

### Managing Existing Tokens

#### Revoking a Token

The "Tokens" page provides an overview of all your active and revoked PATs. Here's how to manage them:

1. **Locate the Token:** Identify the token you wish to revoke within the "Tokens" list.
2. **Revoke Button:** Look for a clear "Revoke" button associated with each token.
3. **Confirmation:** Before revoking, a confirmation prompt will appear to prevent accidental revocation. Choose "Revoke" to proceed.
4. **Visual Update:** Upon revocation:
    - The token's status color will change to orange.
    - The status text will update to "Revoked".
    - Two new buttons will appear: "Restore" and "Delete".

![Screenshot](../../assets/tokens/tokens-list-revoked-light.png#only-light)
![Screenshot](../../assets/tokens/tokens-list-revoked-dark.png#only-dark)


#### Restoring a Revoked Token

1. **Restore Button:** The "Restore" button becomes available for revoked tokens.
2. **Status Change:** Clicking "Restore" will reactivate the token, changing its status back to "Active" and its color accordingly.

#### Deleting a Token

1. **Delete Button:** A "Delete" button will be visible next to revoked tokens.
2. **Irreversible Action:**  A confirmation prompt will warn you that deleting a token is permanent. Click "Delete" only if you're certain.

#### Important Reminders

* **Secure Storage:** Always store copied tokens in a secure password manager or encrypted vault. Avoid sharing them with anyone.
* **Expiration Best Practices:** Choose appropriate expiration times based on the token's intended use case. Shorter expirations enhance security if the token is compromised.


## Use cases for PATs:

### Automate tasks

PATs can be used by automated tools and scripts to interact with your platform without requiring manual intervention. You can use the PATs to use our Qualytics CLI, see more [here](/userguide/cli/overview-of-qualytics-cli/).


## Important considerations

### Treat PATs like passwords

Keep your PATs confidential and avoid sharing them with anyone.

## Store them securely

Use a password manager or an encrypted vault to store your PATs.

## Revoke compromised tokens 

If you suspect a PAT is compromised, immediately revoke it to prevent unauthorized access.

By following these guidelines, you can leverage PATs to enhance security and streamline workflows within your platform.