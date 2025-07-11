# Authored Check

Authored checks are manually created by users within the Qualytics platform or API. You can author many types of checks, ranging from simple templates for common checks to complex rules using Spark SQL and User-Defined Functions (UDF) in Scala.

Let's get started 🚀

## Navigation

**Step 1:** Log in to your Qualytics account and select the datastore from the left menu.

![datastore](../assets/checks/authored-checks/datastore-light.png#only-light)
![datastore](../assets/checks/authored-checks/datastore-dark.png#only-dark)

**Step 2:** Click on the **"Checks"** from the Navigation Tab.

![checks](../assets/checks/authored-checks/checks-tab-light.png#only-light)
![checks](../assets/checks/authored-checks/checks-tab-dark.png#only-dark)

**Step 3:** In the top-right corner, click on the **"Add"** button, then select **"Check"** from the dropdown menu.

![add](../assets/checks/authored-checks/add-btn-light.png#only-light)
![add](../assets/checks/authored-checks/add-btn-dark.png#only-dark)

A modal window titled **“Authored Check Details”** will appear, providing you the options to add the authored check details.

![window](../assets/checks/authored-checks/window-light.png#only-light)
![window](../assets/checks/authored-checks/window-dark.png#only-dark)

**Step 4:** Enter the following details to add the authored check:

**1. Associate with a Check Template:**

* If you toggle **ON** the **"Associate with a Check Template"** option, the check will be linked to a specific template.

* If you toggle **OFF** the **"Associate with a Check Template"** option, the check will not be linked to any template, which allows you full control to modify the properties independently.

![check-temp](../assets/checks/authored-checks/checks-temp-light.png#only-light)
![check-temp](../assets/checks/authored-checks/checks-temp-dark.png#only-dark)

**2. Rule Type (Required)**: Select a Rule from the dropdown menu, such as checking for non-null values, matching patterns, comparing numerical values, or verifying date-time constraints. Each rule type defines the specific validation logic to be applied.

For demonstration purposes we have selected the **After Date Time** rule type.

![rule](../assets/checks/authored-checks/rule-type-light.png#only-light)
![rule](../assets/checks/authored-checks/rule-type-dark.png#only-dark)

For more details about the available rule types, refer to the "**Rule Types Overview**" documentation.

!!! note
    Different rule types have different sets of fields and options appearing when selected. 

**3. File (Required)**: Select a file from the dropdown menu on which the check will be performed.

![file](../assets/checks/authored-checks/file-light.png#only-light)
![file](../assets/checks/authored-checks/file-dark.png#only-dark)

**4. Field (Required)**: Select a field from the dropdown menu on which the check will be performed.

![field](../assets/checks/authored-checks/field-light.png#only-light)
![field](../assets/checks/authored-checks/field-dark.png#only-dark)

**5. Filter Clause**: Specify a valid [Spark SQL](https://spark.apache.org/docs/latest/sql-ref.html) **WHERE** expression to filter the data on which the check will be applied.

The filter clause defines the conditions under which the check will be applied. It typically includes a **WHERE** statement that specifies which rows or data points should be included in the check.

![filter](../assets/checks/authored-checks/filter-clause-light.png#only-light)
![filter](../assets/checks/authored-checks/filter-clause-dark.png#only-dark)

**6. Date (Required)**: Enter the reference date for the rule. For the **After Date Time** rule, records in the selected field must have a timestamp later than this specified date.

![date](../assets/checks/authored-checks/date-light.png#only-light)
![date](../assets/checks/authored-checks/date-dark.png#only-dark)

!!! note
    Spark SQL expressions used in calculated fields are editable, enabling greater flexibility in configuration.

**7. Coverage**: Adjust the **Coverage setting** to specify the percentage of records that must comply with the check.

!!! note
    The Coverage setting applies to most rule types and allows you to specify the percentage of records that must meet the validation criteria.

![coverage](../assets/checks/authored-checks/coverage-light.png#only-light)
![coverage](../assets/checks/authored-checks/coverage-dark.png#only-dark)

**8. Description (Required)**: Enter a detailed description of the check template, including its purpose, applicable data, and relevant information to ensure clarity for users. If you're unsure of what to include, click on the **"💡" lightbulb** icon to apply a suggested description based on the rule type.

**Example:** The **Date of Birth** must be a timestamp later than **< date_time >**.

This description specifies that the **Date of Birth** field must have a timestamp later than the specified **< date_time >**.

![description](../assets/checks/authored-checks/description-light.png#only-light)
![description](../assets/checks/authored-checks/description-dark.png#only-dark)

**9. Tag**: Assign relevant tags to your check to facilitate easier searching and filtering based on categories like **"data quality," "financial reports,"** or **"critical checks."**

![tag](../assets/checks/authored-checks/tag-light.png#only-light)
![tag](../assets/checks/authored-checks/tag-dark.png#only-dark)

**10. Additional Metadata**: Add key-value pairs as additional metadata to enrich your check. Click the plus icon **(+)** next to this section to open the metadata input form, where you can add key-value pairs.

![metadata](../assets/checks/authored-checks/metadata-light.png#only-light)
![metadata](../assets/checks/authored-checks/metadata-dark.png#only-dark)

Enter the desired key-value pairs (e.g., **DataSourceType: SQL Database** and **PriorityLevel: High**). After entering the necessary metadata, click **"Confirm"** to save the custom metadata.

![confirm](../assets/checks/authored-checks/confirm-light.png#only-light)
![confirm](../assets/checks/authored-checks/confirm-dark.png#only-dark)

**Step 4:** After completing all the check details, click on the **"Validate"** button. This will perform a validation operation on the check without saving it. The validation allows you to verify that the logic and parameters defined for the check are correct. It ensures that the check will work as expected by running it against the data without committing any changes.

![validate](../assets/checks/authored-checks/validate-light.png#only-light)
![validate](../assets/checks/authored-checks/validate-dark.png#only-dark)

If the validation is successful, a green message will appear saying **"Validation Successful"**.

![msg](../assets/checks/authored-checks/validate-msg-light.png#only-light)
![msg](../assets/checks/authored-checks/validate-msg-dark.png#only-dark)

If the validation fails, a red message will appear saying **"Failed Validation"**. This typically occurs when the check logic or parameters do not match the data properly.

![failed](../assets/checks/authored-checks/failed-light.png#only-light)
![failed](../assets/checks/authored-checks/failed-dark.png#only-dark)

**Step 5:** Once you have a successful validation, click the **"Save"** button.

![Save](../assets/checks/authored-checks/save-btn-light.png#only-light)
![Save](../assets/checks/authored-checks/save-btn-dark.png#only-dark)

After clicking on the **“Save”** button your check is successfully created and a success flash message will appear saying **“Check successfully created”**.

![msg](../assets/checks/authored-checks/msg-btn-light.png#only-light)
![msg](../assets/checks/authored-checks/msg-btn-dark.png#only-dark)

## Author a Check via API

Users are able to author and interact with Checks through the API by passing JSON Payloads. Please refer to the API documentation on details: `qualytics.io/api/docs`

![Screenshot](../assets/checks/quality-checks-doc.png)