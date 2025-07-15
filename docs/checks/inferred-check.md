# Inferred Check

Qualytics automatically generates inferred checks during a Profile operation. These checks typically cover 80-90% of the rules needed by users. They are created and maintained through profiling, which involves statistical analysis and machine learning methods.

Let's get started 🚀

## Navigation

**Step 1:** Log in to your Qualytics account and select the datastore from the left menu.

![datastore](../assets/checks/inferred-checks/datastore-light.png#only-light)
![datastore](../assets/checks/inferred-checks/datastore-dark.png#only-dark)

**Step 2:** Click on the **"Checks"** from the Navigation Tab.

![checks](../assets/checks/inferred-checks/checks-light.png#only-light)
![checks](../assets/checks/inferred-checks/checks-dark.png#only-dark)

**Step 3:** In the top-right corner, click on the "**Run**" button, then select "**Profile**" from the dropdown menu. This action will initiate the profiling process that generates inferred checks.

![run](../assets/checks/inferred-checks/run-light.png#only-light)
![run](../assets/checks/inferred-checks/run-dark.png#only-dark)

!!! note
    Inferred checks will be automatically updated with the next Profiling run. Manually updating an inferred check will take it out of the automatic update workflow.

To understand how to Inferred checks, you can follow the steps from the documentation [**Profile Operation.**](../source-datastore/profile.md)

After the profiling run is complete, inferred checks will be automatically created based on the analysis of your data.

![profiling](../assets/checks/inferred-checks/profiling-light.png#only-light)
![profiling](../assets/checks/inferred-checks/profiling-dark.png#only-dark)

**1. Check Summary**: Provides a summary of the schema validation check, including its unique identifier, type, status, and associated warnings or information. It serves as a quick reference for users to assess the check's current state and access relevant actions.

For demonstration purposes, the applied rule type is **Expected Schema**.

![check-summary](../assets/checks/inferred-checks/check-summary-light.png#only-light)
![check-summary](../assets/checks/inferred-checks/check-summary-dark.png#only-dark)

**Check ID**: A unique identifier assigned to this particular check.

![check-id](../assets/checks/inferred-checks/check-id-light.png#only-light)
![check-id](../assets/checks/inferred-checks/check-id-dark.png#only-dark)

**Check Type**: Indicates the nature of the validation being performed on the check.

![check-type](../assets/checks/inferred-checks/check-type-light.png#only-light)
![check-type](../assets/checks/inferred-checks/check-type-dark.png#only-dark)

**Warnings**: Indicates the presence of active anomalies detected in the dataset. Clicking on this icon opens a dropdown menu with the following options:

* **View**: Displays detailed information about the detected anomalies.

* **Acknowledge**: Marks the anomaly as reviewed or acknowledged.

* **Archive**: Moves the anomaly record to the archive for future reference.

![warnings](../assets/checks/inferred-checks/warnings-light.png#only-light)
![warnings](../assets/checks/inferred-checks/warnings-dark.png#only-dark)

**Open Details**: Provides additional details or guidance about the check. Clicking this icon typically displays more context or documentation related to schema validation.

![open-details](../assets/checks/inferred-checks/open-details-light.png#only-light)
![open-details](../assets/checks/inferred-checks/open-details-dark.png#only-dark)

**Check Actions**: Opens a dropdown menu with more actions related to managing or modifying the check.

![check-actions](../assets/checks/inferred-checks/check-actions-light.png#only-light)
![check-actions](../assets/checks/inferred-checks/check-actions-dark.png#only-dark)

**2. Target**: Specifies the dataset and file that the inferred check will be applied to. This section ensures that the validation rules are correctly assigned to the intended source datastore. Users can select a different file if needed by clicking the dropdown.

![target](../assets/checks/inferred-checks/target-light.png#only-light)
![target](../assets/checks/inferred-checks/target-dark.png#only-dark)

**3. Fields List**: Displays the fields that are expected to be present in the dataset.

![fields](../assets/checks/inferred-checks/fields-light.png#only-light)
![fields](../assets/checks/inferred-checks/fields-dark.png#only-dark)

| **No.** | **Fields**             | **Description**                                                                 |
|---------|---------------------------|------------------------------------------------------------------------------------|
| 1       | Date of Birth          |Stores date and time values, ensuring precise representation of birth dates.     |
| 2       | Created Date           | Holds the record’s creation date as a text value rather than a structured date format.                                           |                                       |

**4. Allow Other Fields (Checkbox)**:

* If **checked**, the validation process allows additional fields beyond those explicitly listed.
* If **unchecked**, any unexpected field in the dataset will trigger an error.

![allow-fields](../assets/checks/inferred-checks/allow-fields-light.png#only-light)
![allow-fields](../assets/checks/inferred-checks/allow-fields-dark.png#only-dark)

**5. Description**: Enter a detailed description of the check template, including its purpose, applicable data, and relevant information to ensure clarity for users. If you're unsure of what to include, click on the **"💡" lightbulb** icon to apply a suggested description based on the rule type.

![description](../assets/checks/inferred-checks/description-light.png#only-light)
![description](../assets/checks/inferred-checks/description-dark.png#only-dark)

**6. Tags**: Tags help categorize and manage checks efficiently. The tag **"test partition scan"** in this case suggests that this check is related to a specific test or partition scan process.

![tags](../assets/checks/inferred-checks/tags-light.png#only-light)
![tags](../assets/checks/inferred-checks/tags-dark.png#only-dark)

**7. Additional Metadata**: Add key-value pairs as additional metadata to enrich your check. Click the plus icon **(+)** next to this section to open the metadata input form, where you can add key-value pairs.

![additional-metadata](../assets/checks/inferred-checks/additional-metadata-light.png#only-light)
![additional-metadata](../assets/checks/inferred-checks/additional-metadata-dark.png#only-dark)

Enter the desired key-value pairs. After entering the necessary metadata, click **"Confirm"** to save the custom metadata.

![confirm-button](../assets/checks/inferred-checks/confirm-button-light.png#only-light)
![confirm-button](../assets/checks/inferred-checks/confirm-button-dark.png#only-dark)

!!! note
    The **Target** field is non-editable. It automatically reflects the selected dataset and cannot be modified manually.

**Step 4**: After completing all the check details, click on the **"Validate"** button. This will perform a validation operation on the check without saving it. The validation allows you to verify that the logic and parameters defined for the check are correct. It ensures that the check will work as expected by running it against the data without committing any changes.

![validate-button](../assets/checks/inferred-checks/validate-button-light.png#only-light)
![validate-button](../assets/checks/inferred-checks/validate-button-dark.png#only-dark)

If the validation is successful, a green message will appear saying **"Validation Successful"**.

![validation-successful](../assets/checks/inferred-checks/validation-successful-light.png#only-light)
![validation-successful](../assets/checks/inferred-checks/validation-successful-dark.png#only-dark)

**Step 5**: Once you have a successful validation, click the **"Update"** button.

![update-button](../assets/checks/inferred-checks/update-button-light.png#only-light)
![update-button](../assets/checks/inferred-checks/update-button-dark.png#only-dark)

After clicking on the **“Update”** button, your check is successfully updated and a success flash message will appear saying **“Check successfully updated”**.

![successfully-updated](../assets/checks/inferred-checks/successfully-updated-light.png#only-light)
![successfully-updated](../assets/checks/inferred-checks/successfully-updated-dark.png#only-dark)

## Inference Engine

1. After metadata is generated by a [**Profile Operation**](../source-datastore/profile.md), Inference Engine is initiated to kick off Inductive and Unsupervised learning methods.  
     
2. Available data is partitioned into a training set and a testing set.  
     
3. The engine applies numerous machine learning models & techniques to the training data in an effort to discover well-fitting data quality constraints.

4. Those inferred constraints are then filtered by testing them against the held out testing set & only those that assert true above a certain threshold are converted and exposed to users as Inferred Checks.