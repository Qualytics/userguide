# Check Templates

The `Check Templates` empowers users to create, manage, and apply standardized checks across different datastores efficiently, enabling check management independently of specific data assets such as datastores, containers, or fields, serving as check blueprints.

## Adding a Check Template

1. Navigate to the "`Library`" in the menu bar.

    ![Screenshot](../assets/checks/checks-template/library-dark.png#only-dark)
    ![Screenshot](../assets/checks/checks-template/library-light.png#only-light)

2. Click on "`Add Check Template`" to initiate a new template.

    ![Screenshot](../assets/checks/checks-template/add-check-template-dark.png#only-dark)
    ![Screenshot](../assets/checks/checks-template/add-check-template-light.png#only-light)

3. Define the template's characteristics, rules, and parameters.

    ![Screenshot](../assets/checks/checks-template/check-template-page-dark.png#only-dark)
    ![Screenshot](../assets/checks/checks-template/check-template-page-light.png#only-light)

4. Save the template for future use.

## Applying a Check Template to create Quality Checks

1. Access the `Library` and select the desired template.
2. Select the `Check` tab from the template and click in `Add`
2. Choose the target datastore, table and fields for the check.
3. Create a new Quality Check based on the selected template.
4. Customize the Quality Check as needed for the specific datastore. If the Check Template is `unlocked`.
4. Save the Quality Check.

    !!! info
        Once a check is saved, **Table** and **Rule Type** are locked and can't be changed

    ![Screenshot](../assets/checks/checks-template/creating-check-based-on-template-dark.png#only-dark)
    ![Screenshot](../assets/checks/checks-template/creating-check-based-on-template-light.png#only-light)


## Template State

The changes on a template can impact or not its related checks by managing the template state, which can be of the following:

| Template State   | Description                                                                   |
|-------------------|-------------------------------------------------------------------------------|
| Unlocked| `Quality Checks` can evolve independently of the template. Subsequent updates to an unlocked Check Template do not affect its related quality checks|
| Locked  | `Quality Checks` from a locked `Check Template` will inherit changes made to the template. Subsequent updates to a locked Check Template do affect its related quality checks|

!!! info
    Tags will be synced independently of unlocked and locked Check Templates, while `Description` and `Additional Metadata` will not be synced. 
    
    This behavior is general for Check Templates.


=== "Template State"

    ``` mermaid
    graph TD
    A[Start] -->|Is `Template Locked` enabled?| B{Yes/No}
    B -->|No| E[The quality check can evolve independently]
    B -->|Yes| C[They remain synchronized with the template]
    C --> D[End]
    E --> D[End]
    ```

## Use Case: Standardizing Validation Checks for Customer Data

Imagine you are a data quality analyst working for a retail company that collects customer data from various sources, including online and in-store transactions. Ensuring the accuracy and consistency of customer data is crucial for business operations and decision-making.

### Scenario

You need to perform regular data validation checks on customer data across different databases and environments (dev, staging, production).

#### Solution with Check Template

##### Step 1: Quality Check Template Creation

1. Navigate to the "`Library`" in Qualytics.
2. Create a Checks Template named "`Customer Data Validation`".
3. Define the common properties of the template for customer data, such as verifying email formats, checking for missing addresses, and validating phone numbers.

##### Step 2: Creating Quality Checks from the Template

1. Access the "Library" and select the "`Customer Data Validation`" template.
2. In `Checks` tab of the template, click in `Add` to create a Quality Check based on this template
3. The form will bring you all the information of the "`Customer Data Validation`" Quality Check Template .
4. If the `Template` is locked, you can only update specific fields, such as Datastore and Profile and Fields, and it will be maintaned in synchronization
5. Confirm if the values are good. Click in `Validate` and then `Save`

!!! info
    You can create as many Quality Check as you want for a specific template

#### Benefits

##### Consistency Across Environments

Standardized checks ensure that customer data is consistently validated, regardless of the database or environment.

##### Efficiency in Validation

By creating a template, analysts save time by avoiding the need to recreate checks for each datastore or environment.

##### Customization for Specific Environments

Quality Checks can be customized to adapt checks to the unique requirements of `dev`, `staging`, and `production` environments. 

You can define multiple customizations to a specific Quality Check if the template is `Unlocked`

##### Centralized Monitoring

The "`Library`" provides a centralized location for monitoring anomalies abnd updates, and the status of all Quality Checks.
