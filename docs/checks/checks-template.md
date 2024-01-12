# Checks Template

The `Checks Template` empowers users to create, manage, and apply standardized checks across different datastores efficiently.

## Overview of Checks Template

Checks Template is a powerful feature that allows users to create standardized checks independently of specific data assets such as datastores, containers, or fields. 

Templates serve as blueprints for creating checks and can be applied across different datastores.

## Creating a Checks Template

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

## Applying a Template to Create Checks

1. Access the "`Library`" and select the desired template.
2. Choose the target datastore for the check.
3. Create a new check instance based on the selected template.
4. Customize the check instance as needed for the specific datastore.
4. Save the check instance.

    !!! info
        Once a check is saved, **Table** and **Rule Type** are locked and can't be changed

    ![Screenshot](../assets/checks/checks-template/creating-check-based-on-template-dark.png#only-dark)
    ![Screenshot](../assets/checks/checks-template/creating-check-based-on-template-light.png#only-light)


## Template States: Locked and Unlocked Instances

| Template State   | Description                                                                   |
|-------------------|-------------------------------------------------------------------------------|
| Unlocked Instances| Instances can evolve independently of the template. Subsequent template updates do not affect unlocked instances.|
| Locked Instances  | Instances created as locked inherit changes made to the template. They remain synchronized with the template.|

=== "Template State"

    ``` mermaid
    graph TD
    A[Start] -->|Is `Template Locked` enabled?| B{Yes/No}
    B -->|No| E[Subsequent template updates do not affect unlocked instances]
    B -->|Yes| C[Instances created as locked inherit changes]
    C --> D[They remain synchronized with the template]
    E --> F[Instances can evolve independently]
    F --> G[End]
    D --> G[End]
    ```

## Use Case: Standardizing Validation Checks for Customer Data

Imagine you are a data quality analyst working for a retail company that collects customer data from various sources, including online and in-store transactions. Ensuring the accuracy and consistency of customer data is crucial for business operations and decision-making.


### Scenario & Challenge 

You need to perform regular data validation checks on customer data across different databases and environments (dev, staging, production).

### Solution with Checks Template

#### Step 1: Template Creation

1. Navigate to the "Library" in Qualytics.
2. Create a Checks Template named "Customer Data Validation."
3. Define standard checks for customer data, such as verifying email formats, checking for missing addresses, and validating phone numbers.

#### Step 2: Applying Template to Datastores

1. Access the "Library" and select the "Customer Data Validation" template.
2. Based on your choice for "Template Locked":
    - If "Template Locked" is enabled:
        - Apply the template to multiple datastores, ensuring consistency across environments.
    - If "Template Locked" is disabled:
        - Apply the template to a sandbox or select datastores for initial testing.

#### Step 3: Instance Customization

1. Create quality checks of the template for dev, staging, and production datastores.
2. Based on your choice for "Template Locked":
    - If "Template Locked" is enabled:
        - Customize instances based on specific requirements of each environment.
    - If "Template Locked" is disabled:
        - Allow instances to evolve independently to adapt checks to unique requirements.

#### Step 4: Monitoring and Reporting

1. Regularly run scans on all instances to identify anomalies in customer data.
2. Easily track anomalies and updates in the "Library" for comprehensive reporting.

### Benefits

#### Consistency Across Environments

- If "Template Locked" is enabled: Standardized checks ensure that customer data is consistently validated, regardless of the database or environment.

- If "Template Locked" is disabled: Flexibility to adapt checks based on unique requirements.

#### Efficiency in Validation

By creating a template, analysts save time by avoiding the need to recreate checks for each datastore.

#### Customization for Specific Environments

Instances allow customization:
    - If "Template Locked" is enabled: Adapt checks to the unique requirements of dev, staging, and production environments.
    - If "Template Locked" is disabled: Instances can evolve independently to meet specific needs.

#### Centralized Monitoring

The "Library" provides a centralized location for monitoring anomalies, updates, and the status of all instances, regardless of "Template Locked" status.

=== "Use Case"
    ``` mermaid
    graph TD
    A[Start] -->|Create Checks Template| B[Navigate to 'Library' in Qualytics]
    B --> C[Create a Checks Template named 'Customer Data Validation']
    C --> D[Define standard checks for customer data]
    D --> E[Access the 'Library' and select the 'Customer Data Validation' template]
    E -->|Is 'Template Locked' enabled?| F{Yes/No}
    F -->|Yes| G[Apply the template to multiple datastores for consistency]
    G --> H[Create instances of the template for dev, staging, and production datastores]
    H --> I[Customize instances based on specific requirements of each environment]
    F -->|No| J[Apply the template to a sandbox or select datastores for initial testing]
    J --> H
    I --> K[Regularly run scans on all instances to identify anomalies]
    K --> L[Easily track anomalies and updates in the 'Library' for comprehensive reporting]
    L --> M[End]
    ```
