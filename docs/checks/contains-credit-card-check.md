# Contains Credit Card

### Definition

*Asserts that the values contain a credit card number.*

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

### Anomaly Types

{%
    include-markdown "components/anomaly-support/index.md"
    start='<!-- all-types--start -->'
    end='<!-- all-types--end -->'
%}

### Example

**Objective**: *Ensure that every O_PAYMENT_DETAILS in the ORDERS table contains a credit card number to confirm the payment method used for each order.*

**Sample Data**

| O_ORDERKEY | O_PAYMENT_DETAILS                                                                   |
|------------|----------------------------------------------------------------------------------|
| 1          | {"date": "2023-09-25", "amount": 250.50, "credit_card": "5105105105105100"}  |
| 2          | <span class="text-negative">{"date": "2023-09-25", "amount": 150.75, "credit_card": "ABC12345XYZ"}</span>      |
| 3          | {"date": "2023-09-25", "amount": 200.00, "credit_card": "4111-1111-1111-1111"}  |

=== "Payload example"
    ``` json
    {
        "description": "Ensure that every O_PAYMENT_DETAILS in the ORDERS table contains a credit card number to confirm the payment method used for each order",
        "coverage": 1,
        "properties": {},
        "tags": [],
        "fields": ["C_CCN_JSON"],
        "additional_metadata": {"key 1": "value 1", "key 2": "value 2"},
        "rule": "containsCreditCard",
        "container_id": {container_id},
        "template_id": {template_id},
        "filter": "1=1"
    }
    ```

**Anomaly Explanation**

In the sample data above, the entry with `O_ORDERKEY` **2** violates the rule as the `O_PAYMENT_DETAILS` does not contain a credit card number, indicating an incomplete order record.

=== "Flowchart"
    ```mermaid
    graph TD
    A[Start] --> B[Retrieve O_PAYMENT_DETAILS]
    B --> C{Contains Credit Card Number?}
    C -->|Yes| D[Move to Next Record/End]
    C -->|No| E[Mark as Anomalous]
    E --> D
    ```

=== "SQL"
    ```sql
    -- An illustrative SQL query to identify order records that don't contain a credit card number in the payment details.
    select
        o_orderkey,
        o_payment_details
    from orders
    where
        not (regexp_like(o_payment_details, '[0-9]{16}'))
        or not (regexp_like(o_payment_details, '\d{4}-\d{4}-\d{4}-\d{4}'))
    ```

**Potential Violation Messages**

!!! example "Record Anomaly"
    The `O_PAYMENT_DETAILS` value of `{"date": "2023-09-25", "amount": 150.75, "credit_card": "ABC12345XYZ"}` does not contains a credit card number.

!!! example "Shape Anomaly"
    In `O_PAYMENT_DETAILS`, 33.33% of 3 order records (1) do not contain a credit card number.
