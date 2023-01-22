# Anomaly Details

* The `Anomaly Details` modal provides specific details about the Anomaly, including source record and checks that failed assertions, along with ability to take `Notes` and provide feedback to ML methods through updating `Status` of the anomaly.

![Screenshot](../assets/anomalies/anomaly-details-light.png#only-light)
![Screenshot](../assets/anomalies/anomaly-details-dark.png#only-dark)

* Users have the ability to provide feedback to the ML methods through Supervised Learning. Specifically, the user can `Acknowledge`, `Resolve` or `Invalidate` an anomaly. 
    *Each of these actions will change the tolerances of the data quality checks behind the anomaly.*

* Datastore details:
    ![Screenshot](../assets/anomalies/anomaly-details-tab-1-light.png#only-light)
    ![Screenshot](../assets/anomalies/anomaly-details-tab-1-dark.png#only-dark)
    1. The `Datastore` name
    2. The `Location` where this data is stored.
    3. The `Record Type` of the anomaly.
    4. The `Date Time` of the anomaly creation.

* Failed Check details:
    <!-- ![Screenshot](../assets/anomalies/anomaly-details-tab-2.png) -->
    ![Screenshot](../assets/anomalies/anomaly-details-tab-2-light.png#only-light)
    ![Screenshot](../assets/anomalies/anomaly-details-tab-2-dark.png#only-dark)

    * `Status` of the selected Anomaly   
        *Users can edit the status to `Acknowledged`, `Resolved` or `Invalid`.*

    * `Tags`: labels that serve the purpose of grouping anomalies and driving downstream workflows. For more details, see TODO hyperlink the tag   
        *Users can create new or apply existing tags*

    * `Field`: all the fields of that specific anomaly found   
        *Users can filter by Field in this view*   

    * `File`/`Table`: datastore in which anomaly was found

    * `Rule`: rule type that failed the assertion(s)  
        *You can check all the Rule types [here.](/checks/what-is#the-definitive-list-of-rule-types)*
    
    * `Violation`: details of how the anomaly failed the assertion(s) of rule(s)   

    * `Coverage` ![Screenshot](../assets/anomalies/coverage-dark.png){: style="width:25px;height:25px;margin-bottom:-5px"}: the expected tolerance of the rule

    * `Type`  ![Screenshot](../assets/anomalies/quality-check-type.png){: style="width:20px;height:20px;margin-bottom:-5px"}: `Infered` or `Authored`

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