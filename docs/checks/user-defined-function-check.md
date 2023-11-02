# User Defined Function

### Definition

*Asserts that the given user-defined function (as scala script) evaluates to true over the field's value.*

### In-Depth Overview

The `User Defined Function` rule enables the application of a custom Scala function on a specified field, allowing for highly customizable and flexible validation based on user-defined logic.

### Field Scope

**Single:** The rule evaluates a single specified field.

**Accepted Types**

| Type        |                          |
|-------------|--------------------------|
| `String`    | <div style="text-align:center">:octicons-check-16:</div> |

### General Properties {#general-properties}

{%
    include-markdown "components/general-props/index.md"
    start='<!-- all-props--start -->'
    end='<!-- all-props--end -->'
%}

### Specific Properties

Implements a user-defined scala script.

| Name                 | Description                              |
|----------------------|------------------------------------------|
| <div class="text-primary">Scala Script</div> | The custom scala script to evaluate each record. |

???+ note
    The Scala script must contain a function that should return a boolean value, determining the validity of the record based on the field's value.

    Below is a scaffold to guide the creation of the Scala function:

    ```scala
    (field: String) => {
      // Your custom logic goes here
    }
    ```

### Anomaly Types

{%
    include-markdown "components/anomaly-support/index.md"
    start='<!-- all-types--start -->'
    end='<!-- all-types--end -->'
%}

### Example

**Objective**: *Validate that each record in the LINEITEM table has a well-structured JSON in the L_ATTRIBUTES column by ensuring the presence of essential keys: "color", "weight", and "dimensions".*

**Sample Data**

| L_ORDERKEY | L_LINENUMBER | L_ATTRIBUTES |
|------------|--------------|--------------|
| 1          | 1            | {"color": "red", "weight": 15, "dimensions": "10x20x15"} |
| 2          | 2            | <span class="text-negative">{"color": "blue", "weight": 20}</span> |
| 3          | 1            | <span class="text-negative">{"color": "green", "dimensions": "5x5x5"}</span> |
| 4          | 3            | <span class="text-negative">{"weight": 10, "dimensions": "20x20x20"}</span> |

??? example "Inputs"
    **Scala Script**

    ```scala
    (lAttributes: String) => {
      import play.api.libs.json._

      try {
        val json = Json.parse(lAttributes)
        
        // Define the keys we expect to find in the JSON
        val expectedKeys = List("color", "weight", "dimensions")
        
        // Check if the expected keys are present in the JSON
        expectedKeys.forall(key => (json \ key).toOption.isDefined)
      } catch {
        case e: Exception => false // Return false if parsing fails
      }
    }
    ```

**Anomaly Explanation**

In the sample data above, the entries with `L_ORDERKEY` **2**, **3**, and **4** do not satisfy the rule because they lack at least one of the essential keys ("color", "weight", "dimensions") in the L_ATTRIBUTES column.

=== "Flowchart"
    ```mermaid
    graph TD
    A[Start] --> B[Retrieve L_ATTRIBUTES]
    B --> C{Does L_ATTRIBUTES contain all essential keys?}
    C -->|Yes| D[Move to Next Record/End]
    C -->|No| E[Mark as Anomalous]
    E --> D
    ```

**Potential Violation Messages**

!!! example "Record Anomaly"
    The `L_ATTRIBUTES` value of `{"color": "blue", "weight": 20}` does not evaluate true as a parameter to the given UDF.

!!! example "Shape Anomaly"
    In `L_ATTRIBUTES`, 75.000% of 4 filtered records (3) do not evaluate true as a parameter to the given UDF.
