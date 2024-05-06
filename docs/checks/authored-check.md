# Authored Check

`Authored` checks are manually authored by a user from scratch via UI or API. There are many types of checks that can be authored through templates for common checks as well as more complex rules through `SQL` and `UDF` (in `Scala`).

## Authoring Checks

1.  After going to `Checks` tab

    ![Screenshot](../assets/checks/checks-tab-light.png#only-light){: style="width:300px"}
    ![Screenshot](../assets/checks/checks-tab-dark.png#only-dark){: style="width:300px"}

2.  On the right top menu, click on `Add`

    ![Screenshot](../assets/checks/add-light.png#only-light){: style="width:300px"}
    ![Screenshot](../assets/checks/add-dark.png#only-dark){: style="width:300px"}

3.  Click on `Check`

    ![Screenshot](../assets/checks/check-light.png#only-light){: style="width:300px"}
    ![Screenshot](../assets/checks/check-dark.png#only-dark){: style="width:300px"}

4. You are going to see the `Authored Checks Details` modal:

    ![Screenshot](../assets/checks/authored-check-details-light.png#only-light)
    ![Screenshot](../assets/checks/authored-check-details-dark.png#only-dark)

* Through this modal, a user can create an `Authored Quality Check` based on the desired field and input specific details of a rule.

!!! note
    * The UI will automatically adapt to a specific Check's input parameters.

## Authoring Checks via API

* Users are able to author and interact with Checks through the API by passing JSON Payloads. Please refer to the API documentation on details: `acme.qualytics.io/api/docs`

    ![Screenshot](../assets/checks/quality-checks-doc.png)

