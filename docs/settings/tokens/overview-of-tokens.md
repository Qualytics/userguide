# Tokens

A token is a secure way to access the Qualytics API instead of using a password. Each user gets a unique Personal API Token (PAT) for authentication. These tokens are created only once, so you need to copy and store them safely because you'll use them to log in and interact with the platform in the future.

Let’s get Started 🚀

## Navigation to Tokens

**Step 1**: Log in to your Qualytics account and click the **Settings** button on the left side panel of the interface. 

![global-setting](../../assets/tokens/global-setting-light-1.png#only-light)
![global-setting](../../assets/tokens/global-setting-dark-1.png#only-dark)

**Step 2**: By default, you will be navigated to the **Tags** section. Click on the **Tokens** tab.

![tokens](../../assets/tokens/tokens-light-2.png#only-light)
![tokens](../../assets/tokens/tokens-dark-2.png#only-dark)

## Generate Token 

Generating a token provides a secure method for authenticating and interacting with your platform, ensuring that only authorized users and applications can access your resources. Personal Access Tokens (PATs) are particularly useful for automated tools and scripts, allowing them to perform tasks without needing manual intervention. By using PATs, you can leverage our Qualytics CLI to streamline data management and operations, making your workflows more efficient and secure.

**Step 1**: Click on the **Generate Token** button located in the top right corner.

![generate-token](../../assets/tokens/generate-token-light-3.png#only-light)
![generate-token](../../assets/tokens/generate-token-dark-3.png#only-dark)

A modal window will appear providing the options for generating the token.

![token-detail](../../assets/tokens/token-detail-light-4.png#only-light)
![token-detail](../../assets/tokens/token-detail-dark-4.png#only-dark)

**Step 2**: Enter the following values:

1. **Name**: Enter the name for the Token ( e.g., DataAccessToken) 
2. **Expiration**: Set the expiration period for the token (e.g., 30 days)

![enter-values](../../assets/tokens/enter-values-light-5.png#only-light)
![enter-values](../../assets/tokens/enter-values-dark-5.png#only-dark)

**Step 3**: Once you have entered the values, then click on the **Generate** button.

![generate-token](../../assets/tokens/generate-token-light-6.png#only-light)
![generate-token](../../assets/tokens/generate-token-dark-6.png#only-dark)

**Step 4**: After clicking on the **Generate** button, your token is successfully generated.

!!! warning 
    Make sure to copy your secret key as you won't be able to see it again. Keep your secret keys confidential and avoid sharing them with anyone. Use a password manager or an encrypted vault to store your secret keys.

![token-generated](../../assets/tokens/token-generated-light-7.png#only-light)
![token-generated](../../assets/tokens/token-generated-dark-7.png#only-dark)

## Token Usage Status

Each personal API token displays a usage status to indicate whether it has been used for interaction with the Qualytics API:

**Last Used**: Its show the token has been successfully used recently and is actively in use.

![Last-Used](../../assets/tokens/last-used-light-7.png#only-light)
![Last-Used](../../assets/tokens/last-used-dark-7.png#only-dark)

**Not Used**: The token has been generated but has not been used for any API requests since creation.

![Last-Used](../../assets/tokens/not-used-light-7.png#only-light)
![Last-Used](../../assets/tokens/not-used-dark-7.png#only-dark)

## Revoke Token

You can revoke your token to prevent unauthorized access or actions, especially if the token has been compromised, is no longer needed, or to enhance security by limiting the duration of access.

**Step 1**: Click the **vertical ellipsis (⋮)** next to the user token, that you want to revoke, then click on **Revoke** from the dropdown menu.

![revoke](../../assets/tokens/revoke-light-8.png#only-light)
![revoke](../../assets/tokens/revoke-dark-8.png#only-dark)

**Step 2**: After clicking the **Revoke** button, your user token will be successfully revoked. A success message will display saying **User token successfully revoked**. Following revocation, the token's status color will change from green to orange.

![revoked-sucessfully](../../assets/tokens/revoked-sucessfully-light-9.png#only-light)
![revoked-sucessfully](../../assets/tokens/revoked-sucessfully-dark-9.png#only-dark)

## Restore Token

You can restore a token to reactivate its access, allowing authorized use again. This is useful if the token was mistakenly revoked or if access needs to be temporarily re-enabled without generating a new token.

**Step 1**: Click the **vertical ellipsis (⋮)** next to the revoked tokens, that you want to restore, then click on the **Restore** button from the dropdown menu.

![restore](../../assets/tokens/restore-light-10.png#only-light)
![restore](../../assets/tokens/restore-dark-10.png#only-dark)

**Step 2**: After clicking on the “Restore” button, your secret token will be restored and a confirmation message will display saying **User token successfully restored**

![token-restored](../../assets/tokens/token-restored-light-11.png#only-light)
![token-restored](../../assets/tokens/token-restored-dark-11.png#only-dark)

## Delete Token

You can delete a token to permanently remove its access, ensuring it cannot be used again. This is important for maintaining security when a token is no longer needed, has been compromised, or to clean up unused tokens in your system.

!!! note 
    You can only delete revoked tokens, not active tokens. If you want to delete an active token, you must first revoke it before you can delete it.

**Step 1**: Click the **vertical ellipsis (⋮)** next to the revoked tokens, that you want to delete, then click on the **Delete** button from the dropdown menu.

![delete](../../assets/tokens/delete-light-12.png#only-light)
![delete](../../assets/tokens/delete-dark-12.png#only-dark)

After clicking the delete button, a confirmation modal window **Delete Token** will appear.

![delete-window](../../assets/tokens/delete-window-light-13.png#only-light)
![delete-window](../../assets/tokens/delete-window-dark-13.png#only-dark)

**Step 2**: Click on the **Delete** button to delete the token.

![click-delete](../../assets/tokens/click-delete-light-14.png#only-light)
![click-delete](../../assets/tokens/click-delete-dark-14.png#only-dark)

After clicking on the **Delete** button, your token will be deleted and a confirmation message will display saying **User token successfully deleted**.

![successfully-deleted](../../assets/tokens/successfully-deleted-light-15.png#only-light)
![successfully-deleted](../../assets/tokens/successfully-deleted-dark-15.png#only-dark)