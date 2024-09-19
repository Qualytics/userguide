# Check Templates

Check Templates empower users to efficiently create, manage, and apply standardized checks across various datastores, acting as blueprints that ensure consistency and data integrity across different datasets and processes. 

Check templates streamline the validation process by enabling check management independently of specific data assets such as datastores, containers, or fields. These templates reduce manual intervention, minimize errors, and provide a reusable framework that can be applied across multiple datasets, ensuring all relevant data adheres to defined criteria. This not only saves time but also enhances the reliability of data quality checks within an organization.

Let's get started 🚀

**Step 1:** Log in to your Qualytics account and click the **“Library”** button on the left side panel of the interface.

![library](../assets/checks/add-check-template/library-light-1.png#only-light)
![library](../assets/checks/add-check-template/library-dark-1.png#only-dark)

**Step 2:** Click on the **“Add Check Template”** button located in the top right corner.

![add-check](../assets/checks/add-check-template/add-check-light-2.png#only-light)
![add-check](../assets/checks/add-check-template/add-check-dark-2.png#only-dark)

A modal window titled **“Check Template Details”** will appear, providing you the options to add the check template details.

![template-detail](../assets/checks/add-check-template/template-detail-light-3.png#only-light)
![template-detail](../assets/checks/add-check-template/template-detail-dark-3.png#only-dark)

**Step 3:** Enter the following details to add the check template:

- **Rule Type (Required)**  
- **Filter Clause**  
- **Description (Required)**  
- **Tag**  
- **Additional Metadata**  
- **Template Locked**

**1. Rule Type (Required):** Select a [Rule type](https://userguide.qualytics.io/checks/overview-of-a-check/\#checks-tab:\~:text=to%20your%20Datastore-,Check%20Rule%20Types,-Rule%20Type) from the dropdown menu for data validation, such as checking for non-null values, matching patterns, comparing numerical values, or verifying date-time constraints. Each rule type defines the specific validation logic to be applied.

For more details about the available rule types, refer to the "[Check Rule Types](https://userguide.qualytics.io/checks/overview-of-a-check/\#checks-tab:\~:text=to%20your%20Datastore-,Check%20Rule%20Types,-Rule%20Type)" section.

!!! note 
    Different rule types have different sets of fields and options appearing when selected.

![rule-type](../assets/checks/add-check-template/rule-type-light-4.png#only-light)
![rule-type](../assets/checks/add-check-template/rule-type-dark-4.png#only-dark)

**2. Filter Clause:** Specify a valid [Spark SQL](https://spark.apache.org/docs/latest/sql-ref.html) `WHERE` expression to filter the data on which the check will be applied.

The filter clause defines the conditions under which the check will be applied. It typically includes a `WHERE` statement that specifies which rows or data points should be included in the check.

**Example:** A filter clause might be used to apply the check only to rows where a certain column meets a specific condition, such as `WHERE status \= 'active'`.

![filter-clause](../assets/checks/add-check-template/filter-clause-light-5.png#only-light)
![filter-clause](../assets/checks/add-check-template/filter-clause-dark-5.png#only-dark)

Adjust the **Coverage setting** to specify the percentage of records that must comply with the check.

!!! note 
    The Coverage setting applies to most rule types and allows you to specify the percentage of records that must meet the validation criteria. 

![coverage-setting](../assets/checks/add-check-template/coverage-setting-light-6.png#only-light)
![coverage-setting](../assets/checks/add-check-template/coverage-setting-dark-6.png#only-dark)

**3. Description (Required):** Enter a detailed description of the check template, including its purpose, applicable data, and relevant information to ensure clarity for users. If you're unsure of what to include, click on the **"💡"** **lightbulb** icon to apply a suggested description based on the rule type.

**Example**: **"The < field > must exist in `bank_transactions_*.csv.Total_Transaction_Amount` (Bank Dataset - Staging)"**.

This description clarifies that the specified field must be present in a particular file (`bank_transactions_*.csv`) and column (`Total_Transaction_Amount`) within the Bank Dataset. 

![description](../assets/checks/add-check-template/description-light-7.png#only-light)
![description](../assets/checks/add-check-template/description-dark-7.png#only-dark)

**4. Tag**: Assign relevant tags to your check template to facilitate easier searching and filtering based on categories like **"data quality,"** **"financial reports,"** or **"critical checks."**

![tag](../assets/checks/add-check-template/tag-light-8.png#only-light)
![tag](../assets/checks/add-check-template/tag-dark-8.png#only-dark)

**5. Additional Metadata:** Add key-value pairs as additional metadata to enrich your check. Click the plus icon **(+)** next to this section to open the metadata input form, where you can add key-value pairs.

![metadata](../assets/checks/add-check-template/metadata-light-8.png#only-light)
![metadata](../assets/checks/add-check-template/metadata-dark-8.png#only-dark)

Enter the desired key-value pairs (e.g., **DataSourceType: SQL Database** and **PriorityLevel: High**). After entering the necessary metadata, click **"Confirm"** to save the custom metadata.  

![key-value](../assets/checks/add-check-template/key-value-light-9.png#only-light)
![key-value](../assets/checks/add-check-template/key-value-dark-9.png#only-dark)

**6. Template Locked:** Check or uncheck the **"Template Locked"** option to determine whether all checks created from this template will have their properties automatically synced to any changes made to the template.

For more information about the template state, jump to the "[**Template State**](#template-state)section below.  

![template](../assets/checks/add-check-template/template-light-10.png#only-light)
![template](../assets/checks/add-check-template/template-dark-10.png#only-dark)

**Step 4:** Once you have entered all the required fields, click the **“Save”** button to finalize the template.

!!! warning
    Once a template is saved, the selected rule type becomes locked and cannot be changed. 

![save-button](../assets/checks/add-check-template/save-button-light-11.png#only-light)
![save-button](../assets/checks/add-check-template/save-button-dark-11.png#only-dark)

After clicking the **"Save"** button, your check template is created, and a success flash message will appear stating, **"Check Template successfully created."**

![message](../assets/checks/add-check-template/message-light-12.png#only-light)
![message](../assets/checks/add-check-template/message-dark-12.png#only-dark)

After saving the check template, you can now **Apply a Check Template to create Quality Checks**, which will enforce the validation rules defined in the template across your datastores. This ensures consistent data quality and compliance with the criteria you’ve established.

## Template State

Any changes to a template may or may not impact its related checks, depending on whether the template state is locked or unlocked. Managing the template state allows you to control if updates automatically apply to all related checks or let them function independently.

**Unlocked**

- Quality Checks can evolve independently of the template. Subsequent updates to an unlocked Check Template do not affect its related quality checks

**Locked**

- Quality Checks from a locked Check Template will inherit changes made to the template. Subsequent updates to a locked Check Template do affect its related quality checks


!!! info 
    Tags will be synced independently of unlocked and locked Check Templates, while Description and Additional Metadata will not be synced. This behavior is general for Check Templates. 

=== "Template State"

    ``` mermaid
    graph TD
    A[Start] -->|Is `Template Locked` enabled?| B{Yes/No}
    B -->|No| E[The quality check can evolve independently]
    B -->|Yes| C[They remain synchronized with the template]
    C --> D[End]
    E --> D[End]
    ```