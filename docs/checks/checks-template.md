# Checks Template

The `Checks Template` empowers users to create, manage, and apply standardized checks across different datastores efficiently.

## Overview of Checks Template

Checks Template is a powerful feature that allows users to create standardized checks independently of specific data assets such as datastores, containers, or fields. Templates serve as blueprints for creating checks and can be applied across different datastores.

## Creating a Checks Template

1. Navigate to the "`Library`" in the menu bar.
2. Click on "`Create Template`" to initiate a new template.
3. Define the template's characteristics, rules, and parameters.
4. Save the template for future use.

## Applying a Template to Create Checks

1. Access the "`Library`" and select the desired template.
2. Choose the target datastore for the check.
3. Create a new check instance based on the selected template.
4. Customize the check instance as needed for the specific datastore.
4. Save the check instance.

## Template States: Locked and Unlocked Instances

| Template State   | Description                                                                   |
|-------------------|-------------------------------------------------------------------------------|
| Unlocked Instances| Instances can evolve independently of the template. Subsequent template updates do not affect unlocked instances.|
| Locked Instances  | Instances created as locked inherit changes made to the template. They remain synchronized with the template.|


## Reviewing Inherited Instances

Easily track all instances created from a template, including anomalies and updates.
Access reports for a comprehensive overview of inherited instances.

## Use Case: Standardizing Validation Checks for Customer Data

Imagine you are a data quality analyst working for a retail company that collects customer data from various sources, including online and in-store transactions. Ensuring the accuracy and consistency of customer data is crucial for business operations and decision-making.

### Scenario

#### Challenge 

You need to perform regular data validation checks on customer data across different databases and environments (dev, staging, production).

#### Solution with Checks Template

##### Step 1: Template Creation

1. Navigate to the "Library" in Qualytics.
2. Create a Checks Template named "Customer Data Validation."
3. Define standard checks for customer data, such as verifying email formats, checking for missing addresses, and validating phone numbers.

##### Step 2: Applying Template to Datastores

1. Access the "Library" and select the "Customer Data Validation" template.
2. Apply the template to multiple datastores, including a sandbox for initial testing.

##### Step 3: Instance Customization

1. Create instances of the template for dev, staging, and production datastores.
2. Customize instances based on specific requirements of each environment.

##### Step 4: Monitoring and Reporting

1. Regularly run scans on all instances to identify anomalies in customer data.
2. Easily track anomalies and updates in the "Library" for comprehensive reporting.

#### Benefits

##### Consistency Across Environments

Standardized checks ensure that customer data is consistently validated, regardless of the database or environment.

##### Efficiency in Validation

By creating a template, analysts save time by avoiding the need to recreate checks for each datastore.

##### Customization for Specific Environments

Instances allow customization to adapt checks to the unique requirements of dev, staging, and production environments.

##### Centralized Monitoring

The "Library" provides a centralized location for monitoring anomalies, updates, and the status of all instances.