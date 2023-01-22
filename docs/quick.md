# Quick start

Want to get started immediately with a high-level overview and typical defaults? This section is for you.

---

# Concepts
Qualytics is the Active Data Quality Platform that enables teams to manage data quality at scale through advanced automation. Qualytics analyzes your historic data for its shapes and patterns in order to infer contextual data quality rules that are then asserted against new data (often in incremental loads) to identify anomalies. When an anomaly is identified, Qualytics provides your team with everything needed to take corrective actions using their existing data tooling & prefered monitoring solutions.

<iframe width="100%" height="460" src="https://www.youtube.com/embed/Dxzt4LRibIE" title="YouTube video player" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture; web-share" allowfullscreen></iframe>

## Accessing your Qualytics deployment

* Each Qualytics deployment is a single-tenant, dedicated cloud instance configured per requirements discussed with your organization. As such, you deployment will be accessible from a custom `URL` specific to your organization.

* For example, ACME's Qualytics deployment might be published here:
    1. `https://acme.qualytics.io`

* The corresponding API documnetation would then be available here:
    1. `https://acme.qualytics.io/api/docs`

* Your specific credentials and `URL` will be provided to you automatically by email.

    !!!tip
        Please check your spam folder if you don’t see the invite.

After you've obtained access to your deployment, you'll want to:

1. [Connect a Datastore](/datastores/what-is-datastore)
2. Generate a [profile](/glossary#profile) for the datastore by running a Profile Operation.
    - This step will automatically infer a set of data quality checks from your data
4. Assert those checks to detect data [anomalies](/glossary#anomaly).


## Connect a `Datastore`

* The first step of configuring a Qualytics instance is to `Add New Datastore`

* To add a Datastore via Qualytics, the user must first select the specific Datastore `Type` such that the appropriate form for collecting connection details can be rendered.

* As the applicable connection details are collected, the UI will verify network connectivity from the Qualytics Deployment to the user specified Host/Port or URI and indicate whether the combination is accessible. This is to assist in diagnosing any network routing restrictions.

* The Add Datastore flow will then prompt the user for an Enrichment Location with two options:

    1. `External` - the enrichment data will be written to a separate Datastore.
    2. `None` - no enrichment data will be recorded for this Datastore. This severely limits functionality for Qualytics to detect anomalies and is not recommended.

    !!! info
        * If `External` option is selected, then the User should be presented with a dropdown list of all configured Enrichment Datastores along with the ability to configure a new Enrichment Datastore to serve as this new Datastore’s enrichment location. 
        * The flow to configure an Enrichment Datastore only differs from the non-Enrichment Datastore in that the user-specified connection details should be verified for the ability to _write_ enrichment data.

* When the Datastore connection details are submitted:
    1. A `synchronous` ConnectionVerification operation will be initiated to verify that the indicated Datastore can be accessed appropriately from Firewall. 
    2. The result of that operation will either return an error message to the user on the new Datastore form view on failure, or mark the new Datastore as `connected` and initiate an asynchronous Catalog operation on success.  
    3. If any future Operation is unable to establish a connection to the Datastore:
        1. The connected property of the Datastore will be set `false`.  
        2. The UI will `warn`/`prompt` users to address any such Datastore connectivity issues.


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

* Two concrete examples of sophisticated rule types automatically inferred at this stage are:
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
        The user should be alerted to any failure to scan any Container of the Datastore with some indication of how to address the issue (assign an identifier, set a record limit, etc..).


## Monitor `data freshness`
