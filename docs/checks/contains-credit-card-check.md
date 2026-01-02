# Contains Credit Card

Use the `containsCreditCard` rule when you need to ensure that sensitive payment fields actually contain valid credit card numbers.  

## What is Contains Credit Card?

Think of **Contains Credit Card** as a sanity check for payment data .

Just like a cashier won’t accept a payment without a card number, this rule ensures that a selected field contains a valid credit card number — not empty values, placeholders, or incorrect data.

**In simple terms:** It verifies that credit card fields truly contain credit card numbers.

## Add Contains Credit Card Check

Use the Contains Credit Card check to validate payment-related fields and detect records where the credit card number is missing or invalid.

<!--ARCADE EMBED START--><div style="position: relative; padding-bottom: calc(48.0208% + 41px); height: 0px; width: 100%;"><iframe src="https://demo.arcade.software/xnCOenSHiMohh0ughx4N?embed&embed_mobile=tab&embed_desktop=inline&show_copy_link=true" title="Add a Contains Credit Card" frameborder="0" loading="lazy" webkitallowfullscreen mozallowfullscreen allowfullscreen allow="clipboard-write" style="position: absolute; top: 0; left: 0; width: 100%; height: 100%; color-scheme: light;" ></iframe></div><!--ARCADE EMBED END-->

## What Does Contains Credit Card Do?

It helps you answer questions like:

- “Do all completed orders actually have a credit card number?”
- “Are payment records missing sensitive fields?”
- “Did upstream systems send incomplete payment data?”

**In short:** It flags records where a credit card number is expected but missing or invalid.

## How Does Contains Credit Card Work?

### Step 1: Select the Field

Choose a single field that should contain a credit card number (e.g., `CARD_NUMBER`).

### Step 2: Pattern Validation

Qualytics checks whether each value matches known credit card formats (continuous digits or hyphen-separated patterns).

### Step 3: Anomaly Detection

If a record does not contain a valid credit card number, it is marked anomalous.

### Step 4: Review Results

You can review exactly which records failed and why.

## Real-Life Example: E-commerce Orders

### The Situation

An e-commerce company stores order data in the `ECOMMERCE_ORDERS` table.

Each successful order is expected to include a credit card number in the `CARD_NUMBER` field.

This data is critical for:

- Payment reconciliation
- Fraud investigation
- Compliance audits

### The Problem

Before this check was configured, the data team had to **manually review order records** to verify whether credit card numbers were present.

This manual process:

- Took significant time during each review
- Did not scale as order volume increased
- Still risked missing incomplete or invalid payment records

### The Solution

The team implemented the **Contains Credit Card** check on the `CARD_NUMBER` field.

<!--ARCADE EMBED START--><div style="position: relative; padding-bottom: calc(40.6806% + 41px); height: 0px; width: 100%;"><iframe src="https://demo.arcade.software/6qAg3lwWl57Ud3zTVBDt?embed&embed_mobile=tab&embed_desktop=inline&show_copy_link=true" title="Solution" frameborder="0" loading="lazy" webkitallowfullscreen mozallowfullscreen allowfullscreen allow="clipboard-write" style="position: absolute; top: 0; left: 0; width: 100%; height: 100%; color-scheme: light;" ></iframe></div><!--ARCADE EMBED END-->

With this check in place, Qualytics automatically validates every record during each scan and flags any order where the credit card number is missing or invalid—removing the need for manual review.

### What the Check Detected

During the scan, Qualytics identified **26 anomalous records** where the `CARD_NUMBER` field did not contain a valid credit card number, even though the orders were marked as completed.

### Output

| CARD_NUMBER | CUSTOMER_EMAIL          | PRODUCT_ID | QUANTITY | ORDER_DATE |
|------------|-------------------------|------------|----------|------------|
| <span class="text-negative">Missing</span> | customer056@example.com | P115 | 1  | 2022-02-01 |
| <span class="text-negative">Missing</span> | customer052@example.com | P111 | -1 | 2022-02-01 |
| <span class="text-negative">Missing</span> | customer048@example.com | P107 | 3  | 2022-01-01 |
| <span class="text-negative">Missing</span> | customer036@example.com | P115 | 1  | 2022-02-01 |
| <span class="text-negative">Missing</span> | customer028@example.com | P107 | 3  | 2022-02-01 |
| <span class="text-negative">Missing</span> | customer020@example.com | P119 | 5  | 2022-02-01 |
| <span class="text-negative">Missing</span> | customer016@example.com | P115 | 1  | 2022-02-01 |
| <span class="text-negative">Missing</span> | customer012@example.com | P111 | 2  | 2022-02-01 |
| <span class="text-negative">Missing</span> | customer008@example.com | P107 | 3  | 2022-02-01 |
| <span class="text-negative">Missing</span> | customer004@example.com | P103 | 4  | 2022-02-01 |

![output](../assets/checks/contains-credit-card/anomaly-detail.png)

!!! warning "Anomaly Detected"
    - **Rule Applied:** Contains Credit Card  
    - **Field:** CARD_NUMBER  
    - **Anomalous Records:** 26  
    - **Violation:** Credit card number not found  

**Violation Message Example:** In `CARD_NUMBER`, 26.00% of filtered records (26) do not contain credit card numbers.

### Why This Matters

Without this check:

- Payments cannot be reliably audited
- Fraud investigations lack critical data
- Compliance requirements may fail
- Downstream billing systems may break

### The Outcome

After enabling the Contains Credit Card check:

- The team identified faulty upstream ingestion logic
- Missing card numbers were traced to a failed payment gateway response
- Incomplete payment records were blocked
- Data quality and compliance confidence improved

## When Should You Use Contains Credit Card?

Use this rule when you:

- Validate payment or transaction tables
- Enforce PCI or financial compliance
- Monitor upstream payment integrations
- Prevent incomplete payment records

## Key Takeaway

Contains Credit Card acts as a guardrail for payment data. If a system says *“payment received”*, this rule ensures the data proves it.

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
