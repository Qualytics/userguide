# Qualytics Security page

* The `Security` section allows users with `administrator` role to manage `Users`, `Teams`, `Datastores` and `API` credentials.

---

* Find the `Security` section by clicking on `Settings` in the menu bar:

  ![Screenshot](../assets/notifications/settings-tab-light.png#only-light)
  ![Screenshot](../assets/notifications/settings-tab-dark.png#only-dark)

* In `Settings` find the `Security` tab:

  ![Screenshot](../assets/security/security-tab-light.png#only-light)
  ![Screenshot](../assets/security/security-tab-dark.png#only-dark)

## Qualytics Supported roles

* The Qualytics Application supports 2 types of roles: `Admin` and `Member`.
    * An `Admin` user has full access to everything in the system and can manage datastores, teams, and users. This means that an `Admin` has the ability to access everything in the application, as well as manage user accounts and team permissions.

    * On the other hand, a `Member` user has limited access to the system depending on the `Team` the user belongs to. 
    
## Qualytics Supported permissions

  * A team can have two types of permissions - `Read` and `Write`. 
  * A `Read` permission allows the user to only view the app and add/update comments 
  * while a `Write` permission allows the user to view and manage limited functionalities of the system.

## Security Page: Teams, Users and Datastores

As an `Admin` user, you can see the security page and navigate through the `Users`, `Teams` or `API Keys` tab:

  ![Screenshot](../assets/security/security-overview-light.png#only-light)
  ![Screenshot](../assets/security/security-overview-dark.png#only-dark)

### Creating Teams
  You can create a new team clicking in the `Add New Team` buttom:

  - ![Screenshot](../assets/security/create-team.png){: style="height:50px;"}

  - A modal will open with the fields you can add:
      * `Name`
      * `Description`
      * `Permission` [`Read` or `Write`]
      * `Users`
      * `Datastores`
      * `Enrichment Datastores`

      ![Screenshot](../assets/security/add-team-light.png#only-light){: style="height:400px;"}
      ![Screenshot](../assets/security/add-team-dark.png#only-dark){: style="height:400px;"}


### Managing Teams

* In the `Teams` section you can see all the `teams` and also edit a specific one:

  ![Screenshot](../assets/security/security-team-overview-light.png#only-light)
  ![Screenshot](../assets/security/security-team-overview-dark.png#only-dark)

### Managing Users

* In the `Users` section you can change the `Permission` to:
    - Admin
    - Member

  ![Screenshot](../assets/security/edit-user-permission-light.png#only-light){: style="height:300px;"}
  ![Screenshot](../assets/security/edit-user-permission-dark.png#only-dark){: style="height:300px;"}

* And also, you can assign a `Team` to the `User`:

  ![Screenshot](../assets/security/edit-user-team-light.png#only-light){: style="height:400px;"}
  ![Screenshot](../assets/security/edit-user-team-dark.png#only-dark){: style="height:400px;"}


### Retreiving API Keys

- In the `API Keys` section, you can get the:
  * `Domain`
  * `Client ID`
  * `Client Secret`
  * `Audience`

  ![Screenshot](../assets/security/qualytics-api-keys-light.png#only-light)
  ![Screenshot](../assets/security/qualytics-api-keys-dark.png#only-dark)




!!! note
    - All users are inside the `Public` team by default and can't be changed. 
    - If you want to change the visibility of the `User` of a specific `Datastore`, you can update the default `Public` team of the `Datastore`.


