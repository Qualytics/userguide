# Security

You can easily manage user and team access by assigning roles and permissions within the system. This includes setting up specific access levels and roles for different users and teams. By doing so, you ensure that data and resources are accessed securely and appropriately, with only authorized individuals and groups having the necessary permissions to view or modify them. This helps maintain the integrity and security of your system.

!!! note 
    Only users with the Admin role have the authority to manage global platform settings,  such as user permissions and team access controls.

Let’s get started 🚀

## Navigation to Security

**Step 1**: Log in to your Qualytics account and click the **Settings** button on the left side panel of the interface. 

![global-setting](../../assets/security/global-setting-light-1.png#only-light)
![global-setting](../../assets/security/global-setting-dark-1.png#only-dark)

**Step 2**: By default, you will be navigated to the **Tags** section. Click on the **Security** tab.

![security](../../assets/security/security-light-2.png#only-light)
![security](../../assets/security/security-dark-2.png#only-dark)

## Add Team

You can create a new team for efficient and secure data management. Teams make it easier to control who has access to what, help people work together better, keep things secure with consistent rules, and simplify managing and expanding user groups. You can assign permissions to the team, such as read and write access, by selecting the datastore and enrichment datastore to which you want them to have access. This makes data management easier.

In Qualytics, every user is assigned one of two roles: ```Admin``` or ```Member```.

- **Admin**: Admin users have full access to the system and can manage datastores, teams, and users. This means they can access everything in the application, as well as manage user accounts and team permissions.

- **Member**: Members are normal users with access explicitly granted to them, usually inherited from the teams they are assigned to.

**Step 1**: Click on the **Add Team** button located in the top right corner.

![add-team](../../assets/security/add-team-light-3.png#only-light)
![add-team](../../assets/security/add-team-dark-3.png#only-dark)

**Step 2**: A modal window will appear, providing the options for creating the team. Enter the required values to get started. 

| REF.     | FIELD        | ACTION     | EXAMPLE          |
|----------|--------------|------------|------------------|
|  1.      | Name         | Enter the name of the team  |   Data Insights Team  |
|  2.      | Description  |  Provide a brief description of the team.  |  Analyzes data to provide actionable insights, supporting data-driven decisions  |
|  3.      | Permission | Select the permission level for the team: Write (manage and edit data), Read (view and report) None (no access) | Read/Write |
|  4.      | Users | Add users to the team | John, Michael |
|  5.      | Source Datastores | Grant access to specific source datastores (single or multiple) for the team | Athena |
|  6.      | Enrichment Datastores | Add and grant access to additional enrichment datastores (single or multiple) for the team  | Bank Enrichment |

![team-details](../../assets/security/team-details-light-4.png#only-light)
![team-details](../../assets/security/team-details-dark-4.png#only-dark)

**Step 3**: Click on the **Save** button to save your team.

![save-new-team](../../assets/security/save-new-team-light-5.png#only-light)
![save-new-team](../../assets/security/save-new-team-dark-5.png#only-dark)

After clicking on the **Save** button, your team is created, and a success message will appear saying, **Team successfully created**.

![team-created](../../assets/security/team-created-light-6.png#only-light)
![team-created](../../assets/security/team-created-dark-6.png#only-dark)

## Manage Users

You can easily manage users by assigning roles, teams, and deactivating users who are not active. This ensures that access control is streamlined, security is maintained, and only active users have access to resources.

The **Security** section, visible only to Admins, allows for granting and revoking permissions for Member users.

Access controls in Qualytics are assigned at the datastore level. A non-administrator user (Member) can have one of three levels of access to any datastore connected to Qualytics:

- **Write**: Allows the user to perform operations on and manage the datastore’s metadata.

- **Read**: Allows the user to view and report on the datastore.

- **None**: The datastore is not visible or accessible to the user.

!!! note 
    Permissions are assigned to Teams rather than directly to users. Users inherit the permissions of the teams to which they are assigned.

All users are part of the default Public team, which provides access to all Public Datastores. Admins can create and manage additional teams, assigning both users and datastores to them. When a datastore is assigned to a team, the team is granted either Read or Write access, and all team members inherit this permission.

### View Users

Whenever new users are added to the system, they will appear in the Users list. Click the **Users** tab to view the list of users.

![User](../../assets/security/user-light-7.png#only-light)
![User](../../assets/security/user-dark-7.png#only-dark)

### Edit Users

You can edit user details to update their role, and team assignments, ensuring their access and team information are current and accurate. 

**Step 1**: Click the **vertical ellipsis (⋮)** next to the user name that you want to edit, then click on **Edit** from the dropdown menu.

![edit-user](../../assets/security/edit-user-light-8.png#only-light)
![edit-user](../../assets/security/edit-user-dark-8.png#only-dark)

**Step 2**: Edit the user details as needed, including:

1. Updating their role
2. Assigning them additional teams

!!! note 
    All users are inside the Public team by default and that can't be changed. If users have no default access to any datastore, then no datastores should be assigned to the Public team.

![edit-user-details](../../assets/security/edit-user-details-light-9.png#only-light)
![edit-user-details](../../assets/security/edit-user-details-dark-9.png#only-dark)

**Step 3**: Once you have made the necessary changes, then click on the **Save** button.

![save-user](../../assets/security/save-user-light-10.png#only-light)
![save-user](../../assets/security/save-user-dark-10.png#only-dark)

After clicking the **Save** button, your changes will be updated, and a success message will display saying, **User successfully updated.

![user-updated](../../assets/security/user-updated-light-11.png#only-light)
![user-updated](../../assets/security/user-updated-dark-11.png#only-dark)

### Deactivate Users

You can deactivate users to revoke their access to the system while retaining their account information for future reactivation if needed.

**Step 1**: Click the **vertical ellipsis (⋮)** next to the user name that you want to deactivate, then click on **Deactivate** from the dropdown menu.

![deactivate-user](../../assets/security/deactivate-user-light-12.png#only-light)
![deactivate-user](../../assets/security/deactivate-user-dark-12.png#only-dark)

**Step 2**: A modal window **Deactivate User** will appear.

![deactivate-window](../../assets/security/deactivate-window-light-13.png#only-light)
![deactivate-window](../../assets/security/deactivate-window-dark-13.png#only-dark)

**Step 3**: Enter **deactivate** in the given field (confirmation check) and then click on the **I’M SURE, DEACTIVATE THIS USER** button to deactivate the user.

![confirm-deactivate](../../assets/security/confirm-deactivate-light-14.png#only-light)
![confirm-deactivate](../../assets/security/confirm-deactivate-dark-14.png#only-dark)

### Sort Users

You can sort users by various criteria, such as **Created date**, **Name**, **Role**, and **Teams**, to easily manage and organize user information.

![sort-user](../../assets/security/sort-user-light-15.png#only-light)
![sort-user](../../assets/security/sort-user-dark-15.png#only-dark)

### Filter Users

You can filter the users by their roles and team, to quickly find and manage particular groups of users. 

![filter](../../assets/security/filter-light-16.png#only-light)
![filter](../../assets/security/filter-dark-16.png#only-dark)

## Manage Teams

You can manage teams by editing their permissions, adding or removing users, and adjusting access to source and enrichment datastores. If a team is no longer needed, you can delete it from the system. This ensures that team configurations are always up-to-date and relevant, enhancing overall data management and security. 

### View Team

Whenever new teams are added to the system, they will appear in the Teams list. Click the **Teams** tab to view the list of teams.

![teams](../../assets/security/teams-light-17.png#only-light)
![teams](../../assets/security/teams-dark-17.png#only-dark)

### Edit Team

You can edit a team to update its permissions, manage users within the team, and adjust access to source and enrichment datastores, ensuring the team's configuration is current and effective.

**Step 1**:  Click on the **vertical ellipsis (⋮)** next to the team name that you want to edit, then click on **Edit** from the dropdown menu.

![edit-team](../../assets/security/edit-team-light-18.png#only-light)
![edit-team](../../assets/security/edit-team-dark-18.png#only-dark)

**Step 2**:  Edit the [team details](#add-team) as needed, including updating their permissions, users, source, and enrichment datastores. 

![team-details](../../assets/security/team-details-light-19.png#only-light)
![team-details](../../assets/security/team-details-dark-19.png#only-dark)

**Step 3**: Once you have made the necessary changes, then click on the **Save** button.

![save-team](../../assets/security/save-team-light-20.png#only-light)
![save-team](../../assets/security/save-team-dark-20.png#only-dark)

After clicking on the **Save** button, your team is successfully updated, and a success message will be displayed saying, **Team successfully updated**

![team-updated](../../assets/security/team-updated-light-21.png#only-light)
![team-updated](../../assets/security/team-updated-dark-21.png#only-dark)

### Delete Team 

You can delete a team from the system when it is no longer needed, removing its access and permissions to streamline management and maintain security.

**Step 1**: Click the **vertical ellipsis (⋮)** next to the team name that you want to delete, then click on **Edit** from the dropdown menu. 

![delete-team](../../assets/security/delete-team-light-22.png#only-light)
![delete-team](../../assets/security/delete-team-dark-22.png#only-dark)

A modal window **Delete Team** will appear.

![confirm-delete](../../assets/security/confirm-delete-light-23.png#only-light)
![confirm-delete](../../assets/security/confirm-delete-dark-23.png#only-dark)

**Step 2**: Click on the **Delete** button to delete the team from the system.

![click-delete](../../assets/security/click-delete-light-24.png#only-light)
![click-delete](../../assets/security/click-delete-dark-24.png#only-dark)

### Sort Team

You can sort teams by various criteria, such as name or creation date, to easily organize and manage team information.

![sort-team](../../assets/security/sort-team-light-25.png#only-light)
![sort-team](../../assets/security/sort-team-dark-25.png#only-dark)
