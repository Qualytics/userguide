# Checks Overview

Checks in Qualytics are rules applied to data that ensure quality by validating accuracy, consistency, and integrity. Each check includes a data quality rule, along with filters, tags, tolerances, and notifications, allowing efficient management of data across tables and fields.

Let’s get started 🚀

## Checks Types

In Qualytics, you will come across two types of checks:

### Inferred Checks

Qualytics automatically generates inferred checks during a Profile operation. These checks typically cover 80-90% of the rules needed by users. They are created and maintained through profiling, which involves statistical analysis and machine learning methods.

For more details on Inferred Checks, please refer to the [**Inferrred Check**](../checks/inferred-check.md) documentation.

### Authored Checks

Authored checks are manually created by users within the Qualytics platform or API. You can author many types of checks, ranging from simple templates for common checks to complex rules using Spark SQL and User-Defined Functions (UDF) in Scala.

For more details on Authored Checks, please refer to the [**Authored Checks**](../checks/inferred-check.md) documentation.

## View & Manage Checks

**Checks** tab in Qualytics provides users with an interface to view and manage various checks associated with their data. These checks are accessible through two different methods, as discussed below. 

### Method 1: Datastore-Specific Checks

**Step 1:** Log in to your Qualytics account and select the Datastore from the left menu.

![datastore](../assets/checks/checks-overview/datastores-light-1.png#only-light)
![datastore](../assets/checks/checks-overview/datastores-dark-1.png#only-dark)

**Step 2:** Click on the "Checks" from the Navigation Tab.

![tab](../assets/checks/checks-overview/tab-light-2.png#only-light)
![tab](../assets/checks/checks-overview/tab-dark-2.png#only-dark)

You will see a list of all the checks that have been applied to the selected datastore

![selected-datastore](../assets/checks/checks-overview/selected-datastore-light-3.png#only-light)
![selected-datastore](../assets/checks/checks-overview/selected-datastore-dark-3.png#only-dark)

You can switch between different types of checks to view them categorically (such as All, Active, Draft, and  Archived).

![categorically](../assets/checks/checks-overview/categorically-light-4.png#only-light)
![categorically](../assets/checks/checks-overview/categorically-dark-4.png#only-dark)

### Method 2: Explore Section

**Step 1:** Log in to your Qualytics account and click the **Explore** button on the left side panel of the interface.

![explore-tab](../assets/checks/checks-overview/explore-light-5.png#only-light)
![explore-tab](../assets/checks/checks-overview/explore-dark-5.png#only-dark)

**Step 2:** Click on the **"Checks"** from the Navigation Tab.

![checks](../assets/checks/checks-overview/checks-light-6.png#only-light)
![checks](../assets/checks/checks-overview/checks-dark-6.png#only-dark)

You'll see a list of all the checks that have been applied to various tables and fields across different source datastores.

![list](../assets/checks/checks-overview/list-light-7.png#only-light)
![list](../assets/checks/checks-overview/list-dark-7.png#only-dark)

## Check Templates

Check Templates empower users to efficiently create, manage, and apply standardized checks across various datastores, acting as blueprints that ensure consistency and data integrity across different datasets and processes.

Check templates streamline the validation process by enabling check management independently of specific data assets such as datastores, containers, or fields. These templates reduce manual intervention, minimize errors, and provide a reusable framework that can be applied across multiple datasets, ensuring all relevant data adheres to defined criteria. This not only saves time but also enhances the reliability of data quality checks within an organization.

For more details about check templates, please refer to the [**Check Templates**](../checks/checks-template.md) documentation.

## Apply Check Template for Quality Checks

You can export check templates to make quality checks easier and more consistent. Using a set template lets you quickly verify that your data meets specific standards, reducing mistakes and improving data quality. Exporting these templates simplifies the process, making finding and fixing errors more efficient, and ensuring your quality checks are applied across different projects or systems without starting from scratch.

For more details how to apply checks template for quality check, please refer to the [**Apply Checks Template for Quality Check**](../checks/apply-check-template-for-quality-checks.md) documentation.

## Export Check Templates

You can export check templates to easily share or reuse your quality check settings across different systems or projects. This saves time by eliminating the need to recreate the same checks repeatedly and ensures that your quality standards are consistently applied. Exporting templates helps maintain accuracy and efficiency in managing data quality across various environments.

For more details about export checks template, please refer to the [**Export Check Templates**](../checks/export-check-templates.md) documentation.

## Manage Checks in Datastore

Managing your checks within a datastore is important to maintain data integrity and ensure quality. You can categorize, create, update, archive, restore, delete, and clone checks, making it easier to apply validation rules across the datastores. The system allows for checks to be set as active, draft, or archived based on their current state of use. You can also define reusable templates for quality checks to streamline the creation of multiple checks with similar criteria. With options for important and favorite, users have full flexibility to manage data quality efficiently.

For more details how to manage checks in datastore, please refer to the [**Manage Checks in Datastore**](../checks/manage-checks.md) documentation.

## Check Rule Types

In Qualytics, a variety of check rule types are provided to maintain data quality and integrity.These rules define specific criteria that data must meet, and checks apply these rules during the validation process.

For more details about check rule types, please refer to the (**Rule Types Overview**) documentation.
