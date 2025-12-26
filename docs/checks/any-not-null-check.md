# Any Not Null

Use the **Any Not Null** rule when business logic requires **at least one** field in a group to contain a value.
This rule is ideal for optional-but-required data scenarios where multiple fields exist, but at least one must be populated.

## What is Any Not Null?

Think of **Any Not Null** as a **“minimum information required”** check for your data.

It makes sure that **at least one important field in a record is filled**.  
If all selected fields are empty, that record is considered invalid and gets flagged.

**In simple terms:** At least one of these fields must have a value.

This rule is especially useful when multiple optional fields exist, but having none of them makes the record unusable.

## Add Any Not Null Check

Use the **Any Not Null** check when you want to ensure that records are not completely blank across a group of related fields.

<!--ARCADE EMBED START--><div style="position: relative; padding-bottom: calc(78.2692% + 41px); height: 0px; width: 100%;"><iframe src="https://demo.arcade.software/YRIqJifrb6cYQeXp6mUK?embed&embed_mobile=tab&embed_desktop=inline&show_copy_link=true" title="Untitled (Wed Dec 24 2025)" frameborder="0" loading="lazy" webkitallowfullscreen mozallowfullscreen allowfullscreen allow="clipboard-write" style="position: absolute; top: 0; left: 0; width: 100%; height: 100%; color-scheme: light;" ></iframe></div><!--ARCADE EMBED END-->

This helps detect:

- Incomplete records  
- Broken data ingestion pipelines  
- UI or API issues where optional fields are skipped entirely  

## What Does Any Not Null Do?

It answers questions like:

- “Did this record capture any meaningful information at all?”
- “Are users submitting forms without filling any contact details?”
- “Is my system creating placeholder rows with no real data?”

**In short:** It prevents empty or useless records from silently entering your system.

## How Does Any Not Null Work?

### Step 1: Select Multiple Fields

You choose a set of related fields, such as:

- Email  
- Phone number  
- Username  

### Step 2: Rule Evaluation

For each record:

- If **at least one field has a value** → ✅ Pass  
- If **all selected fields are NULL** → 🚨 Anomaly  

### Step 3: Anomaly Reporting

Any record that fails the rule is flagged and appears in the anomaly results.

## Why Should You Use Any Not Null?

### 1. Stop Empty Records Early

Empty rows can:

- Break downstream analytics  
- Inflate row counts  
- Cause confusion during audits  

This rule blocks them immediately.

### 2. Improve Data Quality at the Source

If data is missing here, it’s usually a **form, API, or ingestion issue**.  
Any Not Null helps you catch it where it starts.

### 3. Protect Reporting & Automation

Automations, alerts, and reports rely on **at least one usable field**.  
This check ensures records are worth processing.

## Real-Life Example: Orders Missing Required Context After System Update

### The Situation

**SunriseMart** is an online retail company that processes thousands of customer orders every day.  
Each order is stored in the `ORDERS` table and is used by multiple teams:

- Order fulfillment
- Customer support
- Sales and revenue reporting

For every order, SunriseMart expects **at least one of the following fields to be present**:

- `O_COMMENT` – customer or system notes
- `O_ORDERSTATUS` – order state such as *Pending*, *Shipped*, or *Cancelled*

Individually, these fields are optional — but **having both missing makes the order unusable**.

### The Problem They Faced

After deploying a backend update, the operations team noticed something unusual:

- Some orders were appearing in reports
- But fulfillment teams could not process them
- Customer support could not identify their status

On investigation, they discovered that:

- A background job was creating order records
- The job populated technical fields like `O_ORDERKEY`, timestamps, and metadata
- But **failed to populate both `O_COMMENT` and `O_ORDERSTATUS`**

This issue went unnoticed at first because:

- The table contained millions of rows
- The problematic records were mixed with valid ones
- Manually checking each record was not feasible

### Why Manual Checking Didn’t Work

Without an automated rule, the team had to:

- Write manual SQL queries
- Scan large result sets
- Re-run checks repeatedly as new data arrived

This approach was:

- Time-consuming
- Easy to miss edge cases
- Not scalable as data volume increased

By the time an issue was found, downstream systems had already consumed the bad data.

### The Solution: Any Not Null

<!--ARCADE EMBED START--><div style="position: relative; padding-bottom: calc(49.1909% + 41px); height: 0px; width: 100%;"><iframe src="https://demo.arcade.software/ikJs6JRwTz8xr8KsDfJ1?embed&embed_mobile=tab&embed_desktop=inline&show_copy_link=true" title="Untitled (Wed Dec 24 2025)" frameborder="0" loading="lazy" webkitallowfullscreen mozallowfullscreen allowfullscreen allow="clipboard-write" style="position: absolute; top: 0; left: 0; width: 100%; height: 100%; color-scheme: light;" ></iframe></div><!--ARCADE EMBED END-->

To solve this, the data team implemented an **Any Not Null** check on:

- `O_COMMENT`
- `O_ORDERSTATUS`

The rule enforces a simple requirement:

> At least one of these fields must contain a value for every order record.

### What the Check Detected

When the check ran, it immediately flagged anomalous records where:

- `O_COMMENT` = NULL  
- `O_ORDERSTATUS` = NULL  

Example anomalous record:

| <span class="text-negative">O_COMMENT</span> | <span class="text-negative">O_ORDERSTATUS</span> | O_ORDERKEY | 
|------|------|--------|
| <span class="text-negative">NULL</span> | <span class="text-negative">NULL</span> | 1034599 |

These records appeared under **Failed Checks** with a clear violation message:

> There is no value set for any of `O_COMMENT` and `O_ORDERSTATUS`

![deactivate-user](../assets/checks/any-not-null/anomaly-detail.png)

### What This Confirmed

The Any Not Null check confirmed that:

- Orders were being created without any meaningful context
- The issue originated from the ingestion layer
- The problem was systematic, not a one-off error

### The Outcome

**Immediate Benefits**

- Invalid order records were detected automatically
- No manual scanning or ad-hoc queries were required
- Engineers quickly identified and fixed the faulty job

**Long-Term Benefits**

- Every order now contains at least one usable field
- Fulfillment and support workflows work reliably
- Data quality issues are caught early instead of downstream
- Trust in reporting and analytics was restored

### Key Takeaway

Any Not Null acts as a safety net that prevents context-less records from silently entering the system, replacing slow and unreliable manual validation with automated enforcement.

### Field Scope

**Multiple:** The rule evaluates multiple specified fields.

**Accepted Types**

| Type          |                          |
|---------------|--------------------------|
| `Date`        | <div style="text-align:center">:octicons-check-16:</div>  |
| `Timestamp`   | <div style="text-align:center">:octicons-check-16:</div>  |
| `Integral`    | <div style="text-align:center">:octicons-check-16:</div>  |
| `Fractional`  | <div style="text-align:center">:octicons-check-16:</div>  |
| `String`      | <div style="text-align:center">:octicons-check-16:</div>  |
| `Boolean`     | <div style="text-align:center">:octicons-check-16:</div>  |

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

**Objective**: *Ensure that for every record in the ORDERS table, at least one of the fields (O_COMMENT, O_ORDERSTATUS) isn't null.*

**Sample Data**

| O_ORDERKEY | O_COMMENT          | O_ORDERSTATUS |
|------------|--------------------|---------------|
| 1          | <span class="text-negative">NULL</span> | <span class="text-negative">NULL</span> |
| 2          | Good product      | NULL          |
| 3          | NULL               | Shipped       |

=== "Payload example"
    ``` json
    {
        "description": "Ensure that for every record in the ORDERS table, at least one of the fields (O_COMMENT, O_ORDERSTATUS) isn't null",
        "coverage": 1,
        "properties": {},
        "tags": [],
        "fields": ["O_ORDERSTATUS","O_COMMENT"],
        "additional_metadata": {"key 1": "value 1", "key 2": "value 2"},
        "rule": "anyNotNull",
        "container_id": {container_id},
        "template_id": {template_id},
        "filter": "_PARITY = 'odd'"
    }
    ```

**Anomaly Explanation**

In the sample data above, the entry with `O_ORDERKEY` **1** does not satisfy the rule because both `O_COMMENT` and `O_ORDERSTATUS` does not hold a value.

=== "Flowchart"
    ``` mermaid
    graph TD
    A[Start] --> B[Retrieve O_COMMENT and O_ORDERSTATUS]
    B --> C{Is Either Field Not Null?}
    C -->|Yes| D[Move to Next Record/End]
    C -->|No| E[Mark as Anomalous]
    E --> D
    ```
=== "SQL"
    ```sql
    -- An illustrative SQL query demonstrating the rule applied to example dataset(s).
    select
        o_orderkey
        , o_comment
        , o_orderstatus
    from orders 
    where
        o_comment is null
        and o_orderstatus is null
    ```

**Potential Violation Messages**

!!! example "Record Anomaly"
    There is no value set for any of `O_COMMENT, O_ORDERSTATUS`

!!! example "Shape Anomaly"
    In `O_COMMENT, O_ORDERSTATUS`, 33.333% of 3 filtered records (1) have no value set for any of `O_COMMENT, O_ORDERSTATUS`
