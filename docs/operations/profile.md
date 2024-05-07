# Profile Operation

A Profile Operation will analyze every available record in all available Containers in a datastore. Full Profiles provide the benefit of generating metadata with 100% fidelity at the cost of maximum compute time.

The Profile Operation is executed on a Datastore to analyze the named collections of data (tables, files, etc.) within it. The operation will:

* Identify the fields within the collection
* Gather statistical data about each field according to its declared or inferred type
* Submit that metadata to the Qualytics Inference Engine to produce appropriate data quality checks
* Test the inferred data quality checks against actual source data to tune with desired sensitivities


!!! note
    Profile Operations can be run at any time to update the inferred data quality checks automatically based on new data in the Datastore. It's recommended to run Profile operations periodically to update inferred rules.

## Configuration

![Screenshot](../assets/operations/operation-profile-light.png#only-light)
![Screenshot](../assets/operations/operation-profile-dark.png#only-dark)

A Profile Operation can be configured with the following options:

* **Record limit**: Profile only a subset of the available data
* **Disable Check Inference**: Update field metadata without adjusting or infering data quality checks
* **Target selection**
    - All tables/files
    - Subset of available named collections (tables, files, etc.)
    - Selection of collections based on tags

    ![Screenshot](../assets/operations/operation-profile-specific-tables-light.png#only-light)
    ![Screenshot](../assets/operations/operation-profile-specific-tables-dark.png#only-dark)

* **Schedule Options**: There's also an option to schedule the operation by:
    - **Hourly**
    - **Daily**
    - **Weekly**
    - **Monthly**
    - **Advanced**
        - Cron job expression

![Screenshot](../assets/operations/scheduling-a-profile-light.png#only-light)
![Screenshot](../assets/operations/scheduling-a-profile-dark.png#only-dark)
