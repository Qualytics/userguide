# Metadata Analysis

* The `Anomaly Details` modal provides specific details about the Anomaly, including source record and checks that failed assertions, along with ability to take `Notes` and provide feedback to ML methods through updating `Status` of the anomaly.

![Screenshot](../assets/anomalies/anomaly-details-light.png#only-light)
![Screenshot](../assets/anomalies/anomaly-details-dark.png#only-dark)

* Users have the ability to provide feedback to the ML methods through Supervised Learning. Specifically, the user can `Acknowledge`, `Resolve` or `Invalidate` an anomaly.
    *Each of these actions will change the tolerances of the data quality checks behind the anomaly.*

* Datastore details:
    ![Screenshot](../assets/anomalies/anomaly-details-tab-1-light.png#only-light)
    ![Screenshot](../assets/anomalies/anomaly-details-tab-1-dark.png#only-dark)
    1. The `# ID` of the anomaly: *__69962__*
    1. The `Datastore` name: *__AzureSQL - Consolidated Balance__*
    2. The `Location` where this data is stored: *__qualytics.consolidated_balance.bank__*
    3. The `Record Type` of the anomaly: *__Shape__*
    4. The `Tags` are labels that serve the purpose of grouping anomalies and driving downstream workflows:
        *__High__*
    5. The `Status` of the selected Anomaly: *Users can edit the status to `Acknowledged`, `Resolved` or `Invalid`.*
    6. The `Detected at` of the anomaly creation time: *__02/21/23 5:40 PM__*

* Failed Fields details:
    ![Screenshot](../assets/anomalies/anomaly-details-tab-2-light.png#only-light)
    ![Screenshot](../assets/anomalies/anomaly-details-tab-2-dark.png#only-dark)

    * `Field`: all the fields of that specific anomaly found: *__currency__*

    * `Rule`: rule type that failed the assertion(s)
        *You can check all the Rule types [here.](/userguide/checks/what-is)*

    * `Violation`: details of how the anomaly failed the assertion(s) of rule(s)

    * `Coverage` ![Screenshot](../assets/anomalies/coverage-dark.png){: style="width:25px;height:25px;margin-bottom:-5px"}: the expected tolerance of the rule

    * `Type`  ![Screenshot](../assets/anomalies/quality-check-type.png){: style="width:20px;height:20px;margin-bottom:-5px"}: `Infered` or `Authored`

     4. The rule type `Tag`

* Source Records:

    Show in a tabular view all the records and fields and highlight records with anomaly data based on the rule type

    ![Screenshot](../assets/anomalies/anomaly-details-tab-3-light.png#only-light)
    ![Screenshot](../assets/anomalies/anomaly-details-tab-3-dark.png#only-dark)
        *Users can filter by Field in this view*


# Infered check details

* Clicking into a `Rule` will highlight its details and enables users to edit the rule as well:

![Screenshot](../assets/anomalies/infered-check-details-section-light.png#only-light)
![Screenshot](../assets/anomalies/infered-check-details-section-dark.png#only-dark)

* An anomaly can be archived via the ![Screenshot](../assets/anomalies/archive.png){: style="width:20px;height:20px;margin-bottom:-5px"} button.

* If you expand the section `Advanced Options` you can add a `Filter` clause and also change the `Coverage` percentage for that anomaly.

!!! note
    The `Filter` clause is a `WHERE` statement against your table. For example:
    `price != 33` or `price > discount + 20`

!!! info
    You can create a computed table and use multiple fields from different tables in a filter clause

# Suggested remediation

Qualytics can also provide you a suggested value

![Screenshot](../assets/anomalies/suggested-remediation-value-light.png#only-light)
![Screenshot](../assets/anomalies/suggested-remediation-value-dark.png#only-dark)

![Screenshot](../assets/anomalies/suggested-value-light.png#only-light)
![Screenshot](../assets/anomalies/suggested-value-dark.png#only-dark)