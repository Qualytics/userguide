# Is Address

### Definition

*Asserts that the values contain the specified required elements of an address.*

### In-Depth Overview

This check leverages machine learning powered by the [libpostal library](https://github.com/openvenues/libpostal) to support multilingual street address parsing/normalization that can handle addresses all over the world. The underlying statistical NLP model was trained using data from OpenAddress and OpenStreetMap, a total of about 1.2 billion records of data from over 230 countries, in 100+ languages. The international address parser uses Conditional Random Fields, which can infer a globally optimal tag sequence instead of making local decisions at each word, and it achieves 99.45% full-parse accuracy on held-out addresses (i.e. addresses from the training set that were purposefully removed so we could evaluate the parser on addresses it hasn’t seen before).

### Field Scope

**Single:** The rule evaluates a single specified field.

**Accepted Types**

| Type        |                          |
|-------------|--------------------------|
| `String`    | <div style="text-align:center">:octicons-check-16:</div>  |

### General Properties

{%
    include-markdown "components/general-props/index.md"
    start='<!-- all-props--start -->'
    end='<!-- all-props--end -->'
%}

### Specific Properties


| Name                           | Description                                               |
|--------------------------------|-----------------------------------------------------------|
| <div class="text-primary">Required Labels</div> | The labels that must be identifiable in the value of each record |


!!! info

    The address parser can technically use any string labels that are defined in the training data, but these are the ones currently supported:

- road: Street name(s)
- city: Any human settlement including cities, towns, villages, hamlets, localities, etc
- state: First-level administrative division. Scotland, Northern Ireland, Wales, and England in the UK are mapped to "state" as well (convention used in OSM, GeoPlanet, etc.)
- country: Sovereign nations and their dependent territories, anything with an ISO-3166 code
- postcode: Postal codes used for mail sorting

This check allows the user to define any combination of these labels as required elements of the value held in each record. Any value these does not contain every required element will be identified as anomalous.


### Anomaly Types

{%
    include-markdown "components/anomaly-support/index.md"
    start='<!-- all-types--start -->'
    end='<!-- all-types--end -->'
%}


### Example

**Objective**: *Ensure that all values in O_MAILING_ADDRESS include the labels "road", "city", "state", and "postcode"*

**Sample Data**


| O_ORDERKEY | O_MAILING_ADDRESS          |
|------------|--------------------|
| 1          | One-hundred twenty E 96th St, new york NY 14925 |
| 2          | <div class="text-negative">Quatre vingt douze R. de l'Église, 75196 cedex 04</div> |
| 3          | 781 Franklin Ave Crown Heights Brooklyn NYC NY 11216 USA |

=== "Payload example"
    ``` json
    {
        "description": "Ensure that all values in O_MAILING_ADDRESS include the labels "road", "city", "state", and "postcode"",
        "coverage": 1,
        "properties": {
            "required_labels": ["road","city","state","country","postcode"]
            },
        "tags": [],
        "fields": ["O_MAILING_ADDRESS"],
        "additional_metadata": {"key 1": "value 1", "key 2": "value 2"},
        "rule": "isAddress",
        "container_id": {container_id},
        "template_id": {template_id},
        "filter": "1=1"
    }
    ```

**Anomaly Explanation**

In the sample data above, the entry with `O_ORDERKEY` **2** does not satisfy the rule because the `O_MAILING_ADDRESS` value includes only a road and postcode which violates the business logic that city and state also be present.

=== "Flowchart"
    ``` mermaid
    graph TD
    A[Start] --> B[Retrieve O_MAILING_ADDRESS]
    B --> C[Infer address labels using ML]
    C --> D{Are all required labels present?}
    D -->|Yes| E[Move to Next Record/End]
    D -->|No| F[Mark as Anomalous]
    F --> E
    ```


**Potential Violation Messages**

!!! example "Record Anomaly"
    The `O_MAILING_ADDRESS` value of `Quatre vingt douze R. de l'Église, 75196 cedex 04` does not adhere to the required format.

!!! example "Shape Anomaly"
    In `O_MAILING_ADDRESS`, 33.33% of 3 filtered records (1) do not adhere to the required format.

