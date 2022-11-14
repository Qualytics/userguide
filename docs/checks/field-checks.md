# What is?

---
Adding a Check means authoring a new data quality check from scratch. 

There are multiple types of checks that can be authored through the UI, which includes SQL and UDF (in Scala) as well.

--- 
## Checks Tab

1.  Select a `Data Store`.
2.  Click on `Checks` tab  <br><br>
    ![Screenshot](../assets/checks/checks-tab.png)
3. You are going to see all checks related to your `Data Store` <br><br>
    ![Screenshot](../assets/checks/all-quality-checks.png)

---

## Add a new Data Quality `Check`

1.  After going to `Checks` tab
2.  On your right top menu, click in `Add`
    ![Screenshot](../assets/checks/add-checks.png)
3. Click in `Check`
4. You are going to see the `Authored Checks Details` menu
    ![Screenshot](../assets/checks/authored-check-details.png)

* In this menu you can create an `Authored Quality Check` based on your specific column/columns you want.

---
## Quality Checks Doc

* The same can be achieved through the API with passing JSON Payloads. Please refer to the API documentation on details: `acme.qualytics.io/api/docs`

    ![Screenshot](../assets/checks/quality-checks-doc.png)