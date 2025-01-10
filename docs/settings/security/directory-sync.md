# Directory Sync

Directory Sync, also known as User and Group Provisioning, automates the synchronization of users and groups between your identity provider (IDP) and the Qualytics platform. This ensures that your user data is consistent across all systems, improving security and reducing the need for manual updates.

## Directory Sync Overview

Directory Sync automates the management of users and groups by synchronizing information between an identity provider (IDP) and your application. This ensures that access permissions, user attributes, and group memberships are consistently managed across platforms, eliminating the need for manual updates.

### **How Directory Sync Works with SCIM**

SCIM is an open standard protocol designed to simplify the exchange of user identity information. When integrated with Directory Sync, SCIM automates the creation, updating, and de-provisioning of users and groups. SCIM communicates securely between the IDP and your platform’s API using OAuth tokens to ensure only authorized actions are performed.

### General Setup Requirements

To set up Directory Sync, the following are required:

* Administrative access to both the identity provider and Qualytics platform  
* A SCIM-enabled identity provider or custom integration  
* The OAuth client set up in your IDP  
* SCIM URL and OAuth Bearer Token generated from the Qualytics platform

## Getting Started

### Prerequisites for Setting Up Directory Sync

Before setting up Directory Sync, ensure you have the following:

* A SCIM-supported identity provider  
* Administrative privileges for both your IDP and Qualytics  
* A SCIM URL and OAuth Bearer Token, which will be generated from your Qualytics instance

### Quick Start Guide

1. Set up an OAuth client in your IDP.  
2. Configure the SCIM endpoints with the SCIM URL and OAuth Bearer Token.  
3. Assign users and groups to provision in the IDP.  
4. Monitor the synchronization to ensure proper operation.

## What is SCIM?

SCIM is a standardized protocol used to automate the exchange of user identity information between IDPs and service providers. Its goal is to simplify the process of user provisioning and management.

SCIM improves efficiency by automating user lifecycle management (creation, updating, and de-provisioning) and ensures that data remains consistent across platforms. It also enhances security by minimizing manual errors and ensuring proper access control.

SCIM includes endpoints that are configured within your IDP and your platform. It uses OAuth tokens for secure communication between the IDP and the Qualytics API, ensuring that only authorized users can manage identity data.

## Benefits of Using SCIM for User and Group Provisioning

By leveraging **SCIM (System for Cross-domain Identity Management)**, Directory Sync simplifies user management with:

* Automated user provisioning and de-provisioning  
* Reduced manual intervention, improving efficiency and security  
* Real-time updates of user data, ensuring accuracy and compliance
* Support for scaling user management across organizations of any size

**Supported Providers**

Our API supports SCIM 2.0 (System for Cross-domain Identity Management) as defined in RFC 7643 and RFC 7644. It is designed to ensure seamless integration with any SCIM-compliant identity management system, supporting standardized user provisioning, de-provisioning, and lifecycle management. Additionally, we have verified support with the following providers:

* **Microsoft Entra (Azure Active Directory)**  
* **Okta**  
* **OneLogin**  
* **JumpCloud**

**Unsupported Providers**

We do not support **Google Workspace**, as it does not offer SCIM support. Organizations using Google Workspace must use alternate methods for user provisioning.

## Providers

## 1. Microsoft Entra

### Creating an App Registration

**Step 1:** Log in to the Microsoft Azure Portal, and select **“Microsoft Entra ID”** from the main menu.

![login](../../assets/security/directory/login-1.png)

**Step 2:** Click on **“Enterprise Applications”** from the left navigation menu.

![enterprise](../../assets/security/directory/enterprise-2.png)

**Step 3:** If your application is already created, choose it from the list and move to the section [Configuring SCIM Endpoints](#configuring-scim-endpoints). If you haven't created your application yet, click on the **New Application** button.

![new-application](../../assets/security/directory/new-application-3.png)

**Step 4:** Click on the **“Create your own application”** button to create your application.

![create-application](../../assets/security/directory/create-application-4.png)

**Step 5:** Give your application a name (e.g., "Qualytics OAuth Client" or "Qualytics SCIM Client").

![application-name](../../assets/security/directory/application-name-5.png)

**Step 6:** After entering the name for your application, click the **Create** button to finalize the creation of your app.

![create-button](../../assets/security/directory/create-button-6.png)

#### Configuring SCIM Endpoints

**Step 1:** Click on **Provisioning** from the left-hand menu.

![provisioning](../../assets/security/directory/provisioning-7.png)

**Step 2:** A new window will appear, click on the **Get Started** button.

![get-started](../../assets/security/directory/get-started-8.png)

**Step 3:** In the **Provisioning Mode** dropdown, select **“Automatic”** and enter the following details in the **Admin Credentials** section:

1. **Provisioning Mode**: Select **Automatic**.

2. **Tenant URL:**  `https://your-domain.qualytics.io/api/scim/v2` 

3. **Secret Token:** Generate this token from the Qualytics UI when logged in as an admin user. For more information on how to generate tokens in Qualytics, refer to the documentation on [Tokens](https://userguide.qualytics.io/settings/tokens/overview-of-tokens/).

![admin-creds](../../assets/security/directory/admin-creds-9.png)

**Step 4:** Click on the **Test Connection** button to test the connection to see if the credentials are correct.

![test-connection](../../assets/security/directory/test-connection-10.png)

**Step 5:** Expand the **Mappings** section and enable your app to enable group and user attribute mappings. The default mapping should work.

![mapping](../../assets/security/directory/mapping-11.png)

**Step 6:** Expand the Settings section and make the following changes:

1. Select **Sync only assigned users and groups** from the **Scope** dropdown.  
2. Confirm the **Provisioning Status** is set to **On.**

![provisioning-status](../../assets/security/directory/provisioning-status-12.png)

**Step 7:** Click on the **Save** to save the credentials. Now you've successfully configured the Microsoft Entra ID SCIM API integration.

![save-button](../../assets/security/directory/save-button-13.png)

### Assigning Users and Groups for Provisioning

**Step 1:** Click on the **Users and groups** from the left navigation menu and then click **Add user/group**.

![add-user](../../assets/security/directory/add-user-14.png)

**Step 2:** Click on the **None Selected** under the Users and Groups.

![none](../../assets/security/directory/none-15.png)

**Step 3:** From the right side of the screen, select the users and groups you want to assign to the app.

![user-group](../../assets/security/directory/user-group-16.png)

**Step 4:** Once you selected the group and users for your app, click the **“Select”** button.

![select-button](../../assets/security/directory/select-button-17.png)

**Step 5:** Click on the **Assign** button to assign the users and groups to the application.

!!! warning 
    When you assign a group to an application, only users directly in the group will have access. The assignment does not cascade to nested groups.

![assign](../../assets/security/directory/assign-18.png)

## 2. Okta

###  Setting up the OAuth Client in Okta

**Step 1**: Log in to your Okta account using your administrator credentials. From the left-hand navigation menu, click **Applications**, then select **Browse App Catalog**.

![application](../../assets/security/directory/application-19.png)

**Step 2**: In the search bar, type **SCIM 2.0 Test App (OAuth Bearer Token)**, and select the app called **SCIM 2.0 Test App (OAuth Bearer Token)** from the search results.

![search-bar](../../assets/security/directory/search-bar-20.png)

**Step 3**: On the app’s details page, click **Add Integration**.

![add-integration](../../assets/security/directory/add-integration-21.png)

**Step 4**: Enter a name for your application (e.g., "Qualytics SCIM Client").

![name](../../assets/security/directory/name-22.png)

**Step 5:** Click on the **Next** button.

![next-button](../../assets/security/directory/next-button-23.png)

### Configuring SCIM Endpoints

**Step 1**: In the newly created app, go to the **Provisioning** tab and click **Configure API Integration**.

![configure](../../assets/security/directory/configure-24.png)

**Step 2**: Check the box labeled **Enable API Integration**, and enter the following details:

* **SCIM 2.0 Base URL:**  `https://your-domain.qualytics.io/api/scim/v2`  

* **OAuth Bearer Token:** Generate this token from the Qualytics UI when logged in as an admin user. For more information on how to generate tokens in Qualytics, refer to the documentation on [Tokens](https://userguide.qualytics.io/settings/tokens/overview-of-tokens/).

![enable-api](../../assets/security/directory/enable-api-25.png)

**Step 3**: Click **Test API Credentials** to verify the connection. Once the credentials are validated, click **Save**.

![test-creds](../../assets/security/directory/test-creds-26.png)

**Step 4**: A new settings page will appear. Under the **To App** section, enable the following settings:

* **Create Users**  
* **Update User Attributes**  
* **Deactivate Users**

After enabling these settings, your Okta SCIM API integration is successfully configured.

![app-section](../../assets/security/directory/app-section-27.png)

### Assigning users for provisioning

**Step 1:** Click the **Assignments** tab and select **Assign to People** from the dropdown **Assign**.

![assign](../../assets/security/directory/assign-28.png)

**Step 2:** Select the users you want to assign to the app and click the **Assign** button.

![assign-button](../../assets/security/directory/assign-button-29.png)

**Step 3:** After you click the **Assign** button, you'll see a new popup window with various fields. Confirm the field values and click the **Save and Go Back** buttons.

![save-button](../../assets/security/directory/save-button-30.png)

### Assigning groups for provisioning

**Step 1:** Navigate to the tab **Push Groups** and select **Find group by name** from the dropdown Push **Groups**.

![push-group](../../assets/security/directory/push-group-31.png)

**Step 2:** Search for the group you want to assign to the app.

![group](../../assets/security/directory/group-32.png)

**Step 3:** After assigning the group name, then click on the **Save** button.

![save-button](../../assets/security/directory/save-button-33.png)

## 3. OneLogin

### Setting up the OAuth Client in OneLogin

**Step 1**: Log in to your OneLogin account using your administrator credentials. From the top navigation menu, click **Applications**, then select **Add App**.

![add-app](../../assets/security/directory/add-app-34.png)

**Step 2**: In the search bar, type **SCIM** and select the app called **SCIM Provisioner with SAML (SCIM V2 Enterprise)** from the list of apps.

![scim](../../assets/security/directory/scim-35.png)

**Step 3**: Enter a name for your app, then click **Save**. You have successfully created the SCIM app in OneLogin.

![save-button](../../assets/security/directory/save-button-36.png)

### Configuring SCIM Endpoints

**Step 1**: In your created application, navigate to the **Configuration** tab on the left and enter the following information:

* **API Status**: Enable the API status for the integration to work properly. 

* **SCIM Base URL:**  `https://your-domain.qualytics.io/api/scim/v2` 

* **SCIM Bearer Token:** Generate this token from the Qualytics UI when logged in as an admin user. For more information on how to generate tokens in Qualytics, refer to the documentation on [Tokens](https://userguide.qualytics.io/settings/tokens/overview-of-tokens/).

![configure-scim](../../assets/security/directory/configure-scim-37.png)

**Step 2**: Click on the **Save** button to store the credentials.

![save-button](../../assets/security/directory/save-button-38.png)

**Step 3**: Navigate to the **Provisioning** tab, and check the box labeled **Enable Provisioning**.

![provisioning-tab](../../assets/security/directory/provisioning-tab-39.png)

**Step 4:** Click on **Save** to apply the changes.

![save-button](../../assets/security/directory/save-button-40.png)

**Step 5**: Navigate to the **Parameters** tab and select the row for **Groups**.

![parameters-tab](../../assets/security/directory/parameters-tab-41.png)

**Step 5**: A popup window will appear, check the box **Include in User Provisioning**, then click the **Save** button.

![save-button](../../assets/security/directory/save-button-42.png)

### Assigning Users for Provisioning

**Step 1**: To assign users to your app, go to **Users** from the top navigation menu, and select the user you want to assign to the app.

From the User page, click the **Applications** tab on the left, and click the **+ (plus)** sign.

![application-tab](../../assets/security/directory/application-tab-43.png)

**Step 3**: A popup window will show a list of apps. Select the app you created earlier and click **Continue**.

![continue-button](../../assets/security/directory/continue-button-44.png)

**Step 4**: A new modal window will appear, click on the **Save** to confirm the assignment.

![save-button](../../assets/security/directory/save-button-45.png)

**Step 5**: If you see the status **Pending** in the table, click that text. A modal window will appear, where you can click **Approve** to confirm the assignment.

![approve](../../assets/security/directory/approve-46.png)

### Assigning Groups for Provisioning

**Step 1:** To push groups to your app, go to the top navigation menu, click **Users**, select **Roles** from the dropdown, and click **New Role** to create the role.

![new-role](../../assets/security/directory/new-role-47.png)

**Step 2**: Enter a name for the role, select the app you created earlier

![name-role](../../assets/security/directory/name-role-48.png)

**Step 3:** Click on the **“Save”** button.

![save-button](../../assets/security/directory/save-button-49.png)

**Step 4**: Click the **Users** tab for the role and search for the user you want to assign to the role.

![user-button](../../assets/security/directory/user-button-50.png)

**Step 5:** Click the **Add To Role** button to assign the user, then click **Save** to confirm the assignment.

![save-button](../../assets/security/directory/save-button-51.png)

**Step 6:** A modal window will appear, click on the **“Save”** button to confirm the assignment.

![modal-save](../../assets/security/directory/modal-save-52.png)

**Step 7**: Go back to your app and click the **Rule** tab on the left and click the **Add Rule** button.

Give the rule a name. Under the **Actions**, select the **Set Groups in your-app-name** from the dropdown, then select each **role** with values that match **your-app-name**.

![action](../../assets/security/directory/action-53.png)

**Step 8:** Click on the **Save** button.

![save-button](../../assets/security/directory/save-button-54.png)

**Step 9**: Click on the **Users** tab on the left, you may see **Pending** under the provisions state. Click on it to approve the assignment.

![pending](../../assets/security/directory/pending-55.png)

**Step 10**: A modal window will appear, click on the **Approve** to finalize the assignment.

![approve](../../assets/security/directory/approve-56.png)

## 4. JumpCloud

### Configuring SCIM Endpoints

JumpCloud supports SCIM provisioning within an existing SAML application. Follow these steps to configure SCIM provisioning:

**Step 1**: Log in to JumpCloud and either choose an existing SAML application or create a new one. From the left navigation menu, click **SSO** and select your **Custom SAML App.**

![custom](../../assets/security/directory/custom-57.png)

**Step 2**: Click on the tab **Identity Management** within your SAML application.

Under the **SCIM Version**, choose **SCIM 2.0** and enter the following information:

1. **Base URL:** `https://your-domain.qualytics.io/api/scim/v2`

2. **Token Key:** Generate this token from the Qualytics UI when logged in as an admin user. For more information on how to generate tokens in Qualytics, refer to the documentation on [Tokens](https://userguide.qualytics.io/settings/tokens/overview-of-tokens/).  

3. **Test User Email**

![identity](../../assets/security/directory/identity-58.png)

**Step 4**: Click **Test Connection** to ensure the credentials are correct, then click **Activate** to enable SCIM provisioning.

![activate](../../assets/security/directory/activate-59.png)

**Step 5**: Click **Save** to store your settings. Once saved, SCIM provisioning is successfully configured for your JumpCloud SAML application.

![save-button](../../assets/security/directory/save-button-60.png)

## Assigning Users for Provisioning

**Step 1**: Click the tab **User Groups** within your SAML application. You can see all the available groups, select the groups you want to sync, and click **Save**.

![user-group](../../assets/security/directory/user-group-61.png)

If no existing groups are available, click User Groups from the left navigation menu and click on the plus **(+)** icon to create a new group.

![plus-button](../../assets/security/directory/plus-button-62.png)

**Step 2**: Select the Users tab and choose the users you want to assign to the group.

![assign-group](../../assets/security/directory/assign-group-63.png)

**Step 3**: Select the **Applications** tab and choose the app you want to assign the group to.

![application-tab](../../assets/security/directory/application-tab-64.png)
