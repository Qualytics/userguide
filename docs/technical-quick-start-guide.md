# Technical Quick Start Guide

## Accessing your Qualytics Deployment

Each Qualytics deployment is a single-tenant, dedicated cloud instance, configured per requirements discussed with your organization. Therefore, your deployment will be accessible from a custom `URL` specific to your organization.

For example, ACME's Qualytics deployment might be published at `https://acme.qualytics.io`, and the corresponding API documentation would be available at `https://acme.qualytics.io/api/docs`. Note that your specific credentials and `URL` will be provided to you automatically by email.

!!!tip
    Please check your spam folder if you don’t see the invite.

After you've obtained access to your deployment, you'll want to:

1. Connect a [Datastore](https://userguide.qualytics.io/glossary/#datastore)
2. Initiate a [profiling](https://userguide.qualytics.io/glossary/#profiling) on the source datastore by running a Profile Operation. This step will automatically infer a set of data quality checks from your data.
3. Assert those checks to detect data [anomalies](https://userguide.qualytics.io/glossary/#anomaly)

## Connecting a [Datastore](./glossary.md)

The first step of configuring a Qualytics instance is to `Add Source Datastore`. In order to add a Source Datastore via Qualytics, you need to select the specific `Connector`. This is necessary so that the appropriate form for collecting connection details can be rendered.

As you provide the required connection details, the UI verifies network connectivity and indicates whether the combination is accessible. This feature assists in diagnosing any network routing restrictions.

While configuring the connection, you'll also come across an option to automatically trigger an asynchronous [Catalog operation](https://userguide.qualytics.io/glossary/#catalog-operation) upon successful Datastore creation.

Once the connection details are confirmed, the "Add Datastore" process moves to a second optional but **strongly recommended step: the configuration of an Enrichment Datastore**. 

The Enrichment Datastore serves as a location to record enrichment data (anomalies and metadata for a Source Datastore). This is a crucial step as it significantly enhances Qualytics's ability to detect anomalies.

!!!warning
    While it is optional, not setting an Enrichment Datastore may limit the Qualytics's features.

In this step, you'll have two options:

1. Configure a new Enrichment Datastore
2. Use the dropdown list to select an existing Enrichment Datastore that was previously configured

The process of configuring a new Enrichment Datastore is similar to that of a Source Datastore, with one key difference: the connection details you provide must have the ability to **write** enrichment data.

!!!note
    If you don't have a specific location to store these results, you can request the **QFS (Qualytics File System)** connector provided by Qualytics for this purpose.

During the Source Datastore and Enrichment Datastore configuration steps, you'll find an option to `Test Connection`. This initiates a synchronous operation that verifies whether the indicated Datastore can be appropriately accessed from the [Compute Daemon](https://userguide.qualytics.io/glossary/#compute-daemon):

- If the operation is successful, you can proceed with the configuration. Any issues during this `Test Connection` process will result in an error message being displayed on the current step of the form, be it the Source Datastore or Enrichment Datastore step.

!!!note
    If any future operation fails to establish a connection with the Datastore, the UI will provide warnings to guide you in resolving the connectivity issues.

## Generate a [Profile](https://userguide.qualytics.io/glossary/#profile-operation)

The majority of a data scientist's work revolves around upfront curation of data, which involves taking steps to determine which type of ML modeling might be beneficial for the given data. Our Data Compute Daemon begins this process much like a data scientist initiating a new modeling effort. It profiles customer data through systematic computational analysis, executed in a fully **automated** and **scalable** manner.

We track a wide range of metadata in addition to standard field metadata, which includes:

1. `type`
2. `min` / `max`
3. `min_length` / `max_length`
4. `completeness` / `sparsity`
5. `histograms` (ratios of values)
    - Our Compute Daemon also calculates more sophisticated statistical measures such as `skewness`, `kurtosis`, and `pearson correlation coefficients`.

While these numerical analysis techniques do not strictly fall under `Machine Learning`, their role in statistical analysis and preparatory work is indispensable. They facilitate ML by generating appropriate and statistically relevant data quality rules at scale.

One crucial part of profiling is identifying column data types, which is typically a tedious task in large tables. A machine learning model trained to infer the data types and properties can help accelerate this task by automatically identifying key phrases and linking them to commonly associated attributes.

Upon completing the initial profiling and metadata generation, the Qualytics Inference Engine carries out ML via various learning methods such as `inductive` and `unsupervised learning`. The engine applies numerous machine learning models & techniques to the training data in an effort to discover well-fitting data quality constraints. The inferred constraints are then filtered by testing them against the held out testing set & only those that assert true are converted to data quality Checks.

Two concrete examples of sophisticated rule types automatically inferred at this stage are:

1. **the application of a robust normality test:** this is applied to each numeric field to discover whether certain types of anomaly checks are applicable & bases its quality check recommendations upon that learning.
2. **the generation of linear regression models:** this is automatically generated to fit any highly correlated fields in the same table. If a good fit model is identified, it's recorded as a predicting model for those correlated fields and used to identify future anomalies.

Now that you have a deeper understanding of how our profiling operation works, you're ready to take action. To initiate a Profile Operation, navigate to the details of the specific source datastore you've created. There, you'll find a step to start the Profile Operation.

## Initiating and Reviewing a [Scan](https://userguide.qualytics.io/glossary/#incremental-scan-operation) for [Anomalies](https://userguide.qualytics.io/glossary/#anomaly)

After the initial Profile Operation is complete, you can start a Scan Operation. By default, Qualytics initiates a `Full` Scan for the first operation. This comprehensive scan establishes a baseline for generating Quality Scores and facilitates the validation of all defined checks.

As the Scan Operation progresses, you can monitor its status in real-time. If you choose, you can set up in-app [notifications](./settings/notifications/overview-of-a-notification.md) to alert you when the operation is complete, whether you're currently signed in or you log back in later.

Upon completion of the Scan operation, you can review the following data points:

- `Start time` and `Finish Time` of operation
- `Total counts` for all scanned Containers, including:
    - Records scanned
    - Anomalies detected
    - Total Records

!!!info
    Any issues, such as the failure to scan any Container of the source datastore, will be indicated, along with suggestions on how to address the issue, such as assigning an identifier or setting a record limit.

<!-- ## Monitor `data freshness` -->