# Security

Every user in Qualytics has one of two roles:

- `Admin` - user has full access to everything in the system and can manage datastores, teams, and users. This means that an `Admin` has the ability to access everything in the application, as well as manage user accounts and team permissions.
- `Member` a normal user with only explicitly granted access to the system inherited from any `Teams` the user is assigned to.

Visible only to users with the Admin role, the `Security` area gives administrators the ability to grant and revoke 
permissions to `Member` users.

In Qualytics, access controls are assigned at the datastore level. A non-administrator user (`Member`) will have one of three 
levels of access (`Permission`) to any datastore connected to Qualytics:

1. `Write` - the ability to perform operations on and manage the metadata for a datastore 
2. `Read` - the ability to view and report on the datastore
3.  None - the datastore will not be visible or accessible to the user

These permissions are not granted directly to users but instead are granted to `Teams` and a user will inherit the
permissions of any team to which she is assigned.

* All users are assigned to the default `Public` team and have access to all `Public` Datastores
* Admins can create & manage other teams and assign both users and datastores to them
* When a datastore is assigned to a team, the team is granted either `Read` or `Write` access and all team members inherit this permission

!!! note
    - Only users with the `Admin` role have the ability to add new datastores and manage global platform `Settings` such as those in the `Security` area 

---
## Managing Teams & Permissions

* Find the `Security` section by clicking on `Settings` in the menu bar:

  ![Screenshot](../../assets/notifications/settings-tab-light.png#only-light){: style="width:300px;"}
  ![Screenshot](../../assets/notifications/settings-tab-dark.png#only-dark){: style="width:300px;"}

* In `Settings` find the `Security` tab:

  ![Screenshot](../../assets/security/security-tab-light.png#only-light)
  ![Screenshot](../../assets/security/security-tab-dark.png#only-dark)

As an `Admin` user, you can manage the `Users` & `Teams` listed or create new ones:

  ![Screenshot](../../assets/security/security-overview-light.png#only-light)
  ![Screenshot](../../assets/security/security-overview-dark.png#only-dark)

### Creating Teams
  You can create a new team clicking in the `Add New Team` buttom:

  - ![Screenshot](../../assets/security/create-team.png){: style="height:50px;"}

  - A modal will open with the fields you can add:
      * `Name`
      * `Description`
      * `Permission` [`Read` or `Write`]
      * `Users`
      * `Datastores`
      * `Enrichment Datastores`

      ![Screenshot](../../assets/security/add-team-light.png#only-light){: style="height:400px;"}
      ![Screenshot](../../assets/security/add-team-dark.png#only-dark){: style="height:400px;"}


A team can be granted two types of permissions to a datastore: 

1. `Write` - the ability to perform operations on and manage the metadata for a datastore
2. `Read` - the ability to view and report on the datastore


### Editing Teams

* In the `Teams` section you can see all the `teams` 

  ![Screenshot](../../assets/security/security-team-overview-light.png#only-light)
  ![Screenshot](../../assets/security/security-team-overview-dark.png#only-dark)

* and also edit a specific one:

  ![Screenshot](../../assets/security/edit-team-light.png#only-light){: style="height:400px;"}
  ![Screenshot](../../assets/security/edit-team-dark.png#only-dark){: style="height:400px;"}


### Managing Users

#### Editing a User's Role
* In the `Users` section, an admin can change a user's role:
    
  ![Screenshot](../../assets/security/edit-user-permission-light.png#only-light){: style="height:300px;"}
  ![Screenshot](../../assets/security/edit-user-permission-dark.png#only-dark){: style="height:300px;"}

#### Adding or Removing a User to teams
* You can add/remove a `User` to a team:

  ![Screenshot](../../assets/security/edit-user-team-light.png#only-light){: style="height:400px;"}
  ![Screenshot](../../assets/security/edit-user-team-dark.png#only-dark){: style="height:400px;"}

!!! note
    - All users are inside the `Public` team by default and that can't be changed. If users should have no default access to any datastore, then no datastores should be assigned to the `Public` team.
