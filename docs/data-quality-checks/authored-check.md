# Authored Check

Authored checks are manually created by users within the Qualytics platform or API. You can author many types of checks, ranging from simple templates for common checks to complex rules using Spark SQL and User-Defined Functions (UDF) in Scala.

Let's get started 🚀

## Navigation

**Step 1:** Log in to your Qualytics account and select the datastore from the left menu.

![datastore](../assets/data-quality-checks/authored-check/datastore.png)

**Step 2:** Click on the **"Checks"** from the Navigation Tab.

![checks](../assets/data-quality-checks/authored-check/checks-tab.png)

**Step 3:** In the top-right corner, click on the **"Add"** button, then select **"Check"** from the dropdown menu.

![add](../assets/data-quality-checks/authored-check/add-btn.png)

A modal window titled **“Authored Check Details”** will appear, providing you the options to add the authored check details.

![window](../assets/data-quality-checks/authored-check/window.png)

**Step 4:** Enter the following details to add the authored check:

**1. Associate with a Check Template:**

* If you toggle **ON** the **"Associate with a Check Template"** option, the check will be linked to a specific template.

* If you toggle **OFF** the **"Associate with a Check Template"** option, the check will not be linked to any template, which allows you full control to modify the properties independently.

![check-temp](../assets/data-quality-checks/authored-check/checks-temp.png)

**2. Rule Type (Required)**: Select a Rule from the dropdown menu, such as checking for non-null values, matching patterns, comparing numerical values, or verifying date-time constraints. Each rule type defines the specific validation logic to be applied.

For demonstration purposes we have selected the **After Date Time** rule type.

![rule](../assets/data-quality-checks/authored-check/rule-type.png)

For more details about the available rule types, refer to the [**Rule Types Overview**](../data-quality-checks/rule-types-overview.md){target="blank"} documentation.

!!! note
    Different rule types have different sets of fields and options appearing when selected. 

**3. File (Required)**: Select a file from the dropdown menu on which the check will be performed.

![file](../assets/data-quality-checks/authored-check/file.png)

**4. Field (Required)**: Select a field from the dropdown menu on which the check will be performed.

![field](../assets/data-quality-checks/authored-check/field.png)

**5. Filter Clause**: Specify a valid [Spark SQL](https://spark.apache.org/docs/latest/sql-ref.html) **WHERE** expression to filter the data on which the check will be applied.

The filter clause defines the conditions under which the check will be applied. It typically includes a **WHERE** statement that specifies which rows or data points should be included in the check.

![filter](../assets/data-quality-checks/authored-check/filter-clause.png)

**6. Custom Anomaly Messages**: Enable this option to use a source record field as the anomaly message instead of the default system-generated message.

Select a source field from the dropdown. The value in that field will be displayed as the anomaly description for failed records.

!!! note
    If the selected field is empty for a failed record, the default system-generated message will be used.

![custom](../assets/data-quality-checks/authored-check/custom.png)

**7. Date (Required)**: Enter the reference date for the rule. For the **After Date Time** rule, records in the selected field must have a timestamp later than this specified date.

![date](../assets/data-quality-checks/authored-check/date.png)

!!! note
    Spark SQL expressions used in calculated fields are editable, enabling greater flexibility in configuration.

**8. Coverage**: Adjust the **Coverage setting** to specify the percentage of records that must comply with the check.

!!! note
    The Coverage setting applies to most rule types and allows you to specify the percentage of records that must meet the validation criteria.

![coverage](../assets/data-quality-checks/authored-check/coverage.png)

**9. Description (Required)**: Enter a detailed description of the check template, including its purpose, applicable data, and relevant information to ensure clarity for users. If you're unsure of what to include, click on the **"💡" lightbulb** icon to apply a suggested description based on the rule type.

**Example:** The **Date of Birth** must be a timestamp later than **< date_time >**.

This description specifies that the **Date of Birth** field must have a timestamp later than the specified **< date_time >**.

![description](../assets/data-quality-checks/authored-check/description.png)

**10. Tag**: Assign relevant tags to your check to facilitate easier searching and filtering based on categories like **"data quality," "financial reports,"** or **"critical checks."**

![tag](../assets/data-quality-checks/authored-check/tag.png)

**11. Additional Metadata**: Add key-value pairs as additional metadata to enrich your check. Click the plus icon **(+)** next to this section to open the metadata input form, where you can add key-value pairs.

![metadata](../assets/data-quality-checks/authored-check/metadata.png)

Enter the desired key-value pairs (e.g., **DataSourceType: SQL Database** and **PriorityLevel: High**). After entering the necessary metadata, click **"Confirm"** to save the custom metadata.

![confirm](../assets/data-quality-checks/authored-check/confirm.png)

**Step 4:** After completing all the check details, click on the **"Validate"** button. This will perform a validation operation on the check without saving it. The validation allows you to verify that the logic and parameters defined for the check are correct. It ensures that the check will work as expected by running it against the data without committing any changes.

![validate](../assets/data-quality-checks/authored-check/validate.png)

If the validation is successful, a green message will appear saying **"Validation Successful"**.

![msg](../assets/data-quality-checks/authored-check/validate-msg.png)

If the validation fails, a red message will appear saying **"Failed Validation"**. This typically occurs when the check logic or parameters do not match the data properly.

![failed](../assets/data-quality-checks/authored-check/failed.png)

**Step 5:** Once you have a successful validation, click the **"Save"** button.

![Save](../assets/data-quality-checks/authored-check/save-btn.png)

After clicking on the **“Save”** button your check is successfully created and a success flash message will appear saying **“Check successfully created”**.

![msg](../assets/data-quality-checks/authored-check/msg-btn.png)

## Author a Check via API

Users are able to author and interact with Checks through the API by passing JSON Payloads. Please refer to the API documentation on details: `qualytics.io/api/docs`

![Screenshot](../assets/data-quality-checks/quality-checks-doc.png)