# Quick Start Guide

Want to get started immediately with a high-level overview and typical defaults? This section is for you.

---

## Steps

#### Step 1: [**Connect a Datastore**](/userguide/datastores/what-is-datastore)

Use the intuitive web app or API provided by Qualytics to connect your datastores. This allows the platform to connect and work with your data seamlessly. We recommend adding at least one [Enrichment Datastore](userguide/enrichment/what-is-enrichment/), which helps in identifying and addressing anomalous data more easily.

![Add a Datastore](assets/datastores/what-is/listing-datastores-light.png#only-light){: style="width:450px"}
![Add a Datastore](assets/datastores/what-is/listing-datastores-dark.png#only-dark){: style="width:450px"}

<br>

#### Step 2: [**Generate a Profile**](/userguide/operations/profile)

Perform a Profile Operation on your chosen datastore. This operation generates valuable metadata insights for all the data assets within the store. It also automatically infers customized data quality checks based on the profiled data.

![Generate a Profile](assets/operations/operation-profile-light.png#only-light)
![Generate a Profile](assets/operations/operation-profile-dark.png#only-dark)

<br>

#### Step 3: [**Scan and Assert Data Quality Checks**](/userguide/operations/scan)

Initiate a scan of your datastore to assert the automatically inferred checks (as well as any additional checks you create) against both historical and new data within the store. This step ensures that your data is thoroughly evaluated for any anomalies.

![Run a Scan](assets/operations/operation-scan-light.png#only-light)
![Run a Scan](assets/operations/operation-scan-dark.png#only-dark)

<br>

#### Step 4: [**Review and Flag Anomalies**](/userguide/anomalies/what-is-an-anomaly)

After the scan, review the identified anomalies and flag them with the appropriate status. Qualytics learns from your business and preferences during this process, adapting its future operations to better suit your needs.

![Anonamlies](assets/anomalies/anomaly-table-light.png#only-light)
![Anomalies](assets/anomalies/anomaly-table-dark.png#only-dark)

<!-- moved body of Concepts to index -->
<!-- created technical-iomplementation-guide.md and moved all content below to new page-->
