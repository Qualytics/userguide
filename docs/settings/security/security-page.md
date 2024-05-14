# Qualytics Security page
Introducing Role-based Access Control - a powerful new feature that lets you create teams and limit access to specific datastores. With this feature, you can ensure that only the right people have access to the right data, giving you peace of mind and better control over your information. 

Check out this section to learn how to set up and use Role-based Access Control in your account.

By default, all users have access to all `Public` Datastores. If you want to limit access:

1. Create a new team,
2. Add members,
3. Add Datastores to new team, 
4. Choose whether they should have read or write access,
5. Remove Datastores from Step 3 from `Public`

!!! note
    - Only Admins have the ability to add new datastores, manage users/teams, and access API keys.

## Access Security View

The `Security` section allows users with `administrator` role to manage `Users`, `Teams`, `Datastores` and `API` credentials.

* Find the `Security` section by clicking on `Settings` in the menu bar:

  ![Screenshot](../../assets/notifications/settings-tab-light.png#only-light){: style="width:300px;"}
  ![Screenshot](../../assets/notifications/settings-tab-dark.png#only-dark){: style="width:300px;"}

* In `Settings` find the `Security` tab:

  ![Screenshot](../../assets/security/security-tab-light.png#only-light)
  ![Screenshot](../../assets/security/security-tab-dark.png#only-dark)

## Qualytics Supported Roles

The Qualytics Application supports 2 types of roles: `Admin` and `Member`.

* An `Admin` user has full access to everything in the system and can manage datastores, teams, and users. This means that an `Admin` has the ability to access everything in the application, as well as manage user accounts and team permissions.

* On the other hand, a `Member` user has limited access to the system depending on the `Team` the user belongs to. 
    
## Qualytics Supported permissions

  * A team can have two types of permissions - `Read` and `Write`. 
  * A `Read` permission allows the user to only view the app and add/update comments 
  * while a `Write` permission allows the user to view and manage limited functionalities of the system.

## Security Page: Teams, Users and Datastores

As an `Admin` user, you can see the security page and navigate through the `Users`, `Teams` or `API Keys` tab:

  ![Screenshot](../../assets/security/security-overview-light.png#only-light)
  ![Screenshot](../../assets/security/security-overview-dark.png#only-dark)

### Add a Team
  
1. You can create a new team clicking in the `Add New Team` button:

	![Screenshot](../../assets/security/create-team.png){: style="height:50px;"}

* A modal will open with the fields you can add:
	* **Name**
	* **Description**
	* **Permission** (**Read** or **Write**)
	* **Users**
	* **Datastores**
	* **Enrichment Datastores**

	![Screenshot](../../assets/security/add-team-light.png#only-light){: style="height:400px;"}
	![Screenshot](../../assets/security/add-team-dark.png#only-dark){: style="height:400px;"}


### Manage Teams

* In the `Teams` section you can see all the `teams` 

	![Screenshot](../../assets/security/security-team-overview-light.png#only-light)
	![Screenshot](../../assets/security/security-team-overview-dark.png#only-dark)

* and also edit a specific one:

	![Screenshot](../../assets/security/edit-team-light.png#only-light){: style="height:400px;"}
	![Screenshot](../../assets/security/edit-team-dark.png#only-dark){: style="height:400px;"}

### Manage Users

#### User Roles
* In the `Users` section you can change the `Permission` (`Admin` or `Member`) to:

  ![Screenshot](../../assets/security/edit-user-permission-light.png#only-light){: style="height:300px;"}
  ![Screenshot](../../assets/security/edit-user-permission-dark.png#only-dark){: style="height:300px;"}

#### User Teams
* You can add/remove a `Team` of an `User`:

  ![Screenshot](../../assets/security/edit-user-team-light.png#only-light){: style="height:400px;"}
  ![Screenshot](../../assets/security/edit-user-team-dark.png#only-dark){: style="height:400px;"}

!!! note
    - All users are inside the `Public` team by default and can't be changed. 
    - If you want to change the visibility of the `User` of a specific `Datastore`, you can update the default `Public` team of the `Datastore`.

### User Roles and Permissions

In this section we are defining different user roles and their access levels, detailing what actions users can perform within Qualytics to ensure appropriate access.

!!! info
    A user with the member role can be assigned either write or read permissions.

#### Datastore and Enrichment Datastore

| Action       | Read  | Write | Admin  |
|--------------|-------|-------|--------|
| Listing      |  <div style="text-align:left">:octicons-check-16:</div>    |  <div style="text-align:left">:octicons-check-16:</div>    |   <div style="text-align:left">:octicons-check-16:</div>    |
| Create       |  <div style="text-align:left">:octicons-x-16:</div>    |  <div style="text-align:left">:octicons-check-16:</div>   |   <div style="text-align:left">:octicons-check-16:</div>    |
| Edit         |  <div style="text-align:left">:octicons-x-16:</div>    |  <div style="text-align:left">:octicons-check-16:</div>  |   <div style="text-align:left">:octicons-check-16:</div>    |
| Delete       |  <div style="text-align:left">:octicons-x-16:</div>    |  <div style="text-align:left">:octicons-check-16:</div>   |   <div style="text-align:left">:octicons-check-16:</div>    |


#### Table and File

| Action       | Read  | Write | Admin  |
|--------------|-------|-------|--------|
| Listing      |  <div style="text-align:left">:octicons-check-16:</div>    |  <div style="text-align:left">:octicons-check-16:</div>    |   <div style="text-align:left">:octicons-check-16:</div>    |
| Create       |  <div style="text-align:left">:octicons-x-16:</div>    |  <div style="text-align:left">:octicons-check-16:</div>   |   <div style="text-align:left">:octicons-check-16:</div>    |
| Edit         |  <div style="text-align:left">:octicons-x-16:</div>    |  <div style="text-align:left">:octicons-check-16:</div>  |   <div style="text-align:left">:octicons-check-16:</div>    |
| Delete       |  <div style="text-align:left">:octicons-x-16:</div>    |  <div style="text-align:left">:octicons-check-16:</div>   |   <div style="text-align:left">:octicons-check-16:</div>    |

#### Operation

| Action       | Read  | Write | Admin  |
|--------------|-------|-------|--------|
| Listing      |  <div style="text-align:left">:octicons-check-16:</div>    |  <div style="text-align:left">:octicons-check-16:</div>    | <div style="text-align:left">:octicons-check-16:</div>    
| Run Catalog  |  <div style="text-align:left">:octicons-x-16:</div>        |  <div style="text-align:left">:octicons-check-16:</div>    | <div style="text-align:left">:octicons-check-16:</div>
| Run Profile  |  <div style="text-align:left">:octicons-x-16:</div>        |  <div style="text-align:left">:octicons-check-16:</div>    | <div style="text-align:left">:octicons-check-16:</div>
| Run Scan     |  <div style="text-align:left">:octicons-x-16:</div>        |  <div style="text-align:left">:octicons-check-16:</div>    | <div style="text-align:left">:octicons-check-16:</div>

#### Quality Score Factor Weights

| Action       | Read  | Write | Admin  |
|--------------|-------|-------|--------|
| Listing      |  <div style="text-align:left">:octicons-check-16:</div>    |   <div style="text-align:left">:octicons-check-16:</div>    | <div style="text-align:left">:octicons-check-16:</div>
| Update       |   <div style="text-align:left">:octicons-x-16:</div>   |  <div style="text-align:left">:octicons-check-16:</div>     | <div style="text-align:left">:octicons-check-16:</div>


#### Check

| Action       | Read  | Write | Admin  |
|--------------|-------|-------|--------|
| Listing      |  <div style="text-align:left">:octicons-check-16:</div>    |   <div style="text-align:left">:octicons-check-16:</div>    | <div style="text-align:left">:octicons-check-16:</div>
| Create       |   <div style="text-align:left">:octicons-x-16:</div>   |  <div style="text-align:left">:octicons-check-16:</div>     | <div style="text-align:left">:octicons-check-16:</div>
| Update       |   <div style="text-align:left">:octicons-x-16:</div>   |  <div style="text-align:left">:octicons-check-16:</div>     | <div style="text-align:left">:octicons-check-16:</div>
| Delete       |   <div style="text-align:left">:octicons-x-16:</div>   |  <div style="text-align:left">:octicons-check-16:</div>     | <div style="text-align:left">:octicons-check-16:</div>

#### Check Template

| Action       | Read  | Write | Admin  |
|--------------|-------|-------|--------|
| Listing      |  <div style="text-align:left">:octicons-check-16:</div>    |   <div style="text-align:left">:octicons-check-16:</div>    | <div style="text-align:left">:octicons-check-16:</div>
| Create       |   <div style="text-align:left">:octicons-x-16:</div>   |  <div style="text-align:left">:octicons-x-16:</div>     | <div style="text-align:left">:octicons-check-16:</div>
| Update       |   <div style="text-align:left">:octicons-x-16:</div>   |  <div style="text-align:left">:octicons-x-16:</div>     | <div style="text-align:left">:octicons-check-16:</div>
| Delete       |   <div style="text-align:left">:octicons-x-16:</div>   |  <div style="text-align:left">:octicons-x-16:</div>     | <div style="text-align:left">:octicons-check-16:</div>

#### Anomaly

| Action       | Read  | Write | Admin  |
|--------------|-------|-------|--------|
| Listing      |  <div style="text-align:left">:octicons-check-16:</div>    |   <div style="text-align:left">:octicons-check-16:</div>    | <div style="text-align:left">:octicons-check-16:</div>
| Create       |   <div style="text-align:left">:octicons-x-16:</div>   |  <div style="text-align:left">:octicons-check-16:</div>     | <div style="text-align:left">:octicons-check-16:</div>
| Update       |   <div style="text-align:left">:octicons-x-16:</div>   |  <div style="text-align:left">:octicons-check-16:</div>     | <div style="text-align:left">:octicons-check-16:</div>
| Delete       |   <div style="text-align:left">:octicons-x-16:</div>   |  <div style="text-align:left">:octicons-check-16:</div>     | <div style="text-align:left">:octicons-check-16:</div>

#### Computed File and Computed Table

| Action       | Read  | Write | Admin  |
|--------------|-------|-------|--------|
| Listing      |  <div style="text-align:left">:octicons-check-16:</div>    |   <div style="text-align:left">:octicons-check-16:</div>    | <div style="text-align:left">:octicons-check-16:</div>
| Create       |   <div style="text-align:left">:octicons-x-16:</div>   |  <div style="text-align:left">:octicons-check-16:</div>     | <div style="text-align:left">:octicons-check-16:</div>
| Update       |   <div style="text-align:left">:octicons-x-16:</div>   |  <div style="text-align:left">:octicons-check-16:</div>     | <div style="text-align:left">:octicons-check-16:</div>
| Delete       |   <div style="text-align:left">:octicons-x-16:</div>   |  <div style="text-align:left">:octicons-check-16:</div>     | <div style="text-align:left">:octicons-check-16:</div>

#### Tag

| Action       | Read  | Write | Admin  |
|--------------|-------|-------|--------|
| Listing      |  <div style="text-align:left">:octicons-check-16:</div>    |   <div style="text-align:left">:octicons-check-16:</div>    | <div style="text-align:left">:octicons-check-16:</div>
| Create       |   <div style="text-align:left">:octicons-x-16:</div>   |  <div style="text-align:left">:octicons-x-16:</div>     | <div style="text-align:left">:octicons-check-16:</div>
| Update       |   <div style="text-align:left">:octicons-x-16:</div>   |  <div style="text-align:left">:octicons-x-16:</div>     | <div style="text-align:left">:octicons-check-16:</div>
| Delete       |   <div style="text-align:left">:octicons-x-16:</div>   |  <div style="text-align:left">:octicons-x-16:</div>     | <div style="text-align:left">:octicons-check-16:</div>


#### Notification

| Action       | Read  | Write | Admin  |
|--------------|-------|-------|--------|
| Listing      |   <div style="text-align:left">:octicons-check-16:</div> | <div style="text-align:left">:octicons-check-16:</div> | <div style="text-align:left">:octicons-check-16:</div> 
| Create       |   <div style="text-align:left">:octicons-x-16:</div>     | <div style="text-align:left">:octicons-x-16:</div> | <div style="text-align:left">:octicons-check-16:</div> 
| Update       |   <div style="text-align:left">:octicons-x-16:</div>     |  <div style="text-align:left">:octicons-x-16:</div>     | <div style="text-align:left">:octicons-check-16:</div>
| Delete       |   <div style="text-align:left">:octicons-x-16:</div>     |  <div style="text-align:left">:octicons-x-16:</div>     | <div style="text-align:left">:octicons-check-16:</div>


#### Connection

| Action       | Read  | Write | Admin  |
|--------------|-------|-------|--------|
| Listing      |   <div style="text-align:left">:octicons-x-16:</div> | <div style="text-align:left">:octicons-x-16:</div> | <div style="text-align:left">:octicons-check-16:</div>
| Update      |   <div style="text-align:left">:octicons-x-16:</div> | <div style="text-align:left">:octicons-x-16:</div> | <div style="text-align:left">:octicons-check-16:</div>
| Delete      |   <div style="text-align:left">:octicons-x-16:</div> | <div style="text-align:left">:octicons-x-16:</div> | <div style="text-align:left">:octicons-check-16:</div>

#### User

| Action       | Read  | Write | Admin  |
|--------------|-------|-------|--------|
| Listing      |   <div style="text-align:left">:octicons-x-16:</div> | <div style="text-align:left">:octicons-x-16:</div> | <div style="text-align:left">:octicons-check-16:</div>
| Update      |   <div style="text-align:left">:octicons-x-16:</div> | <div style="text-align:left">:octicons-x-16:</div> | <div style="text-align:left">:octicons-check-16:</div>
| Delete      |   <div style="text-align:left">:octicons-x-16:</div> | <div style="text-align:left">:octicons-x-16:</div> | <div style="text-align:left">:octicons-check-16:</div>

#### Team

| Action       | Read  | Write | Admin  |
|--------------|-------|-------|--------|
| Listing      |   <div style="text-align:left">:octicons-x-16:</div> | <div style="text-align:left">:octicons-x-16:</div> | <div style="text-align:left">:octicons-check-16:</div>
| Update      |   <div style="text-align:left">:octicons-x-16:</div> | <div style="text-align:left">:octicons-x-16:</div> | <div style="text-align:left">:octicons-check-16:</div>
| Delete      |   <div style="text-align:left">:octicons-x-16:</div> | <div style="text-align:left">:octicons-x-16:</div> | <div style="text-align:left">:octicons-check-16:</div>


#### Health

| Action       | Read  | Write | Admin  |
|--------------|-------|-------|--------|
| Listing      |   <div style="text-align:left">:octicons-x-16:</div> | <div style="text-align:left">:octicons-x-16:</div> | <div style="text-align:left">:octicons-check-16:</div>