# Quick start

Setup your Qualytics Deployment, create a datastore, generate a profile, infer data quality rules, scan for anomalies and monitor data freshness.

---

# Prepare

* Each Qualytics deployment is a single-tenant, dedicated cloud instance configured per requirements discussed with your organization. 
* As such, the `URL` for the front-end for ACME would be:
    1. `https://acme.qualytics.io`

* The API is available at:
    1. `https://acme.qualytics.io/api/docs`

* Your credentials will be provided to you automatically from your instance:

    !!!warning
        Please check your spam folder if you don’t see the invite. 

* Quickly get started by connecting your Qualytics deployment to a first:
    1. [Data Store](/datastores/what-is-datastore)
    2. Generating a [profile](/operations/profile) for it, 
    3. Automatically [inferring](/glossary#inference) a set of data quality rules from it
    4. Asserting those rules through a [scan](/operations/scan) to detect data [anomalies](/glossary#anomaly).

## Connect a `Data Store`

* The first step of configuring a Qualytics instance is to `Add New Data Store`

* To add a Data Store via Qualytics, the user must first select the specific Data Store `Type` such that the appropriate form for collecting connection details can be rendered.

* As the applicable connection details are collected, the UI will verify network connectivity from the Qualytics Deployment to the user specified Host/Port or URI and indicate whether the combination is accessible. This is to assist in diagnosing any network routing restrictions.

* The Add Data Store flow will then prompt the user for an Enrichment Location with two options:

    1. `External` - the enrichment data will be written to a separate Data Store.
    2. `None` - no enrichment data will be recorded for this Data Store. This severely limits functionality for Qualytics to detect anomalies and is not recommended.

    !!! info
        * If `External` option is selected, then the User should be presented with a dropdown list of all configured Enrichment Data Stores along with the ability to configure a new Enrichment Data Store to serve as this new Data Store’s enrichment location. 
        * The flow to configure an Enrichment Data Store only differs from the non-Enrichment Data Store in that the user-specified connection details should be verified for the ability to _write_ enrichment data.

* When the Data Store connection details are submitted:
    1. A `synchronous` ConnectionVerification operation will be initiated to verify that the indicated Data Store can be accessed appropriately from Firewall. 
    2. The result of that operation will either return an error message to the user on the new Data Store form view on failure, or mark the new Data Store as `connected` and initiate an asynchronous Catalog operation on success.  
    3. If any future Operation is unable to establish a connection to the Data Store:
        1. The connected property of the Data Store will be set `false`.  
        2. The UI will `warn`/`prompt` users to address any such Data Store connectivity issues.


## Generate a `Profile`

* 80% of the job of today’s Data Scientist is the upfront curation of a set of data, including steps taken to determine what type of ML modeling might prove useful for that data.

* In the same way that a Data Scientist might begin a new modeling effort, our Data Firewall `profiles` customer data using systematic computational analysis in a fully `automated`/`scalable` manner.

* In addition to standard Field metadata, we track other metadata such as:
    1. `type`.
    2. `min`/`max`.
    3. `min_length`/`max_length`.
    4. `completeness`/`sparsity`.
    5. `histograms` (ratios of values)
        1. Firewall calculates more sophisticated statistical measures like: skewness, kurtosis, pearson correlation coefficients.

* While these numerical analysis techniques are not strictly `Machine Learning`, the statistical analysis and prep work is necessary to facilitate Machine Learning in order to generate appropriate, statistically relevant data quality rules at scale.

* An important part of profiling is identification of column data types, which is typically a tedious task in large tables. A machine learning model trained to infer the data types and properties can help accelerate this task by automatically identifying key phrases and linking them to commonly associated attributes.

* After initial profiling generates metadata, the Qualytics Inference Engine carries out ML via various learning methods such as `inductive` and `unsupervised learning`. The engine applies numerous machine learning models & techniques to the training data in an effort to discover well-fitting data quality constraints. The inferred constraints are then filtered by testing them against the held out testing set & only those that assert true are converted to data quality Checks.

* Two concrete examples of sophisticated ruletypes automatically inferred at this stage are:
    1. A sophisticated normality test is applied to each numeric field to discover whether certain types of anomaly checks are applicable & bases its quality check recommendations upon that learning
    2. Linear regression models are automatically generated to fit any highly correlated fields in the same table. 
    !!!info 
        If a good fit model is identified, it is recorded as a predicting model for those correlated fields and used to identify future anomalies.

## `Scan` for anomalies

* Upon completion of the initial Profile Operation the user is able to initiate a `Scan Operation`.

* Qualytics will initiate a “`Full`” `Scan` for the initial Scan by default.  

    !!!info
        * This will produce a baseline from which Quality Scores will be generated and will help validate all defined Checks. 
        * The user should be able to monitor the progress of the Scan Operation and be alerted to its completion. 
        * If the user signed out before completion, the user should be alerted to the completion upon next sign in.

### Presenting Scan Operation Results

* Upon completion of the Scan operation, the user will be able to review the following data points:

    1. `Start time` and `Finish Time` of the Scan Operation.
    2. A `listing of all the named Containers` included in the Scan.
        1. The `number of records scanned` in each listed Container.
        2. The `number of anomalies detected` in each listed Container.
        3. The `total record count in each listed Container` at the time of scanning.
        4. The `total record count in each listed Container` at the time of scanning.
    3. `Total counts` (sum of all Container counts) of:
        1. `Records scanned`.
        2. `Anomalies detected`.
        3. `Total Records`.

    !!!info
        The user should be alerted to any failure to scan any Container of the Data Store with some indication of how to address the issue (assign an identifier, set a record limit, etc..).


## Monitor `data freshness`
