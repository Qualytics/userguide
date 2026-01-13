# After Date Time

Use the `afterDateTime` rule when you need to ensure that a timestamp value occurs **strictly after a defined cutoff date and time**.

This rule is commonly used for **data freshness validation**, **cutover enforcement**, and **post-migration correctness**.

## What is After Date Time?

Think of **After Date Time** as a **gatekeeper for time-based data**.

Just like a security guard checks that people enter a building **after opening time**, this rule ensures that every value in a timestamp field occurs **after a specific date and time**.

If any record shows up **before or exactly at the cutoff**, it gets flagged as an anomaly.

## Add After Date Time Check

Use the After Date Time Check to validate timestamp fields against a fixed cutoff and detect records that violate expected time boundaries.

<!--ARCADE EMBED START--><div style="position: relative; padding-bottom: calc(48.0208% + 41px); height: 0px; width: 100%;"><iframe src="https://demo.arcade.software/5xoq4jojtCHHXZ83n6tS?embed&embed_mobile=tab&embed_desktop=inline&show_copy_link=true" title="Add a After Date Time" frameborder="0" loading="lazy" webkitallowfullscreen mozallowfullscreen allowfullscreen allow="clipboard-write" style="position: absolute; top: 0; left: 0; width: 100%; height: 100%; color-scheme: light;" ></iframe></div><!--ARCADE EMBED END-->

## What Does After Date Time Do?

After Date Time helps you answer questions like:

- “Are all records created **after the system go-live time**?”
- “Did any old data sneak in after migration?”
- “Are late or backdated records affecting reports?”
- “Is this dataset truly fresh and recent?”

**In simple terms:** It guarantees that your data is **newer than a specific moment in time**.

## How Does After Date Time Work?

### Step 1: Select the Timestamp Field

You choose a **single date or timestamp field**, such as:

- `created_at`
- `order_date`
- `event_time`
- `processed_at`

### Step 2: Define the Cutoff Date & Time

You specify the **exact date and time** that acts as the lower boundary.

**Example:** 2025-12-01 06:15:00 

Only records **after this moment** are valid.

### Step 3: Rule Evaluation

For each record, Qualytics checks:

- Is the field value **greater than** the cutoff timestamp?

### Step 4: Get Your Results

- **Pass** – All timestamps are after the cutoff  
- **Anomalies Found** – One or more records violate the rule and are flagged

## Why Should You Use After Date Time?

### 1. Enforce System Cutovers

During migrations or system upgrades, old timestamps can corrupt reports.  
This rule ensures **only post-cutover data exists**.

### 2. Validate Data Freshness

Helps confirm that pipelines are producing **new data**, not reprocessing old records.

### 3. Prevent Reporting Errors

Backdated entries can:

- Inflate historical metrics
- Break daily dashboards
- Trigger incorrect alerts

After Date Time stops this at the source.

### 4. Strengthen Compliance & Audits

Regulated environments often require strict timestamp validation.  
This rule provides a **clear, auditable boundary**.

## Real-Life Example: Enforcing a Login Cutover After System Migration

### The Situation

**BrightCart**, an e-commerce company, migrated its **user authentication system** to a new identity provider on **December 1, 2025 at 06:15 UTC**.

From this point onward:

- All user login activity must be recorded by the new system
- Any login timestamp before this cutoff is considered invalid
- Old timestamps indicate legacy data, cache issues, or failed sync jobs

This login data is critical because it feeds:

- Account security audits
- User activity tracking
- Fraud detection
- Session-based personalization

### The Problem They Faced

A few days after the migration, the security team noticed something unusual:

- Some users appeared inactive for years
- Fraud detection rules started misfiring
- Recently active customers were flagged as **“dormant”**

On investigation, they found that:

- The `LAST_LOGIN_TS` field still contained old timestamps
- Many records had values like `2022-03-01`
- These values should not exist after a **2025 cutover**

Manual checking wasn’t scalable — the table contained **millions of rows**.

### The Solution: After Date Time

The data team configured an **After Date Time** check to enforce a hard time boundary.

<!--ARCADE EMBED START--><div style="position: relative; padding-bottom: calc(48.0208% + 41px); height: 0px; width: 100%;"><iframe src="https://demo.arcade.software/wPHCSd6kjDoxuzBWplsv?embed&embed_mobile=tab&embed_desktop=inline&show_copy_link=true" title="Solution" frameborder="0" loading="lazy" webkitallowfullscreen mozallowfullscreen allowfullscreen allow="clipboard-write" style="position: absolute; top: 0; left: 0; width: 100%; height: 100%; color-scheme: light;" ></iframe></div><!--ARCADE EMBED END-->

#### What they configured:

- **Table:** `ECOMMERCE_ORDERS`
- **Field:** `LAST_LOGIN_TS`
- **Cutoff:** `2025-12-01 06:15 UTC`
- **Coverage:** 100% (every record must comply)

**Rule intent:**  
Every user record must have a `LAST_LOGIN_TS` that occurred **after** the authentication system migration.

### Sample Records (What the Data Looked Like)

| LAST_LOGIN_TS | CUSTOMER_EMAIL | CUSTOMER_ID |
|--------------|----------------|-------------|
| 2025-12-03 09:42 | customer043@example.com | C013 |
| <span class="text-negative">2022-03-01 10:00</span> | customer041@example.com | C011 |
| <span class="text-negative">2022-03-01 10:00</span> | customer040@example.com | C010 |
| 2025-12-05 18:21 | customer031@example.com | C001 |

### What After Date Time Discovered

When the check ran, Qualytics flagged **110 anomalous records**.

All failed records shared the same issue:

- Their `LAST_LOGIN_TS` occurred **before the cutover**
- Some timestamps were copied from legacy systems
- Others were default or cached values

!!! warning "ANOMALIES DETECTED"
    - Rule Applied: After Date Time  
    - Field Checked: LAST_LOGIN_TS  
    - Cutoff: 2025-12-01 06:15 UTC  
    - Anomalous Records: 110  

### Anomaly Output (Source Records View)

| LAST_LOGIN_TS                          | CUSTOMER_EMAIL              | CUSTOMER_ID |
|---------------------------------------|-----------------------------|-------------|
| <span class="text-negative">2022-03-01T10:00:00.000Z</span> | customer043@example.com | C013 |
| <span class="text-negative">2022-03-01T10:00:00.000Z</span> | customer041@example.com | C011 |
| <span class="text-negative">2022-03-01T10:00:00.000Z</span> | customer040@example.com | C010 |
| <span class="text-negative">2022-03-01T10:00:00.000Z</span> | customer031@example.com | C001 |
| <span class="text-negative">2022-03-01T10:00:00.000Z</span> | customer028@example.com | C028 |
| <span class="text-negative">2022-03-01T10:00:00.000Z</span> | customer026@example.com | C026 |
| <span class="text-negative">2022-03-01T10:00:00.000Z</span> | customer021@example.com |      |
| <span class="text-negative">2022-03-01T10:00:00.000Z</span> | customer014@example.com | C014 |
| <span class="text-negative">2022-03-01T10:00:00.000Z</span> | customer012@example.com | C012 |
| <span class="text-negative">2022-03-01T10:00:00.000Z</span> | customer009@example.com | C009 |

![anomaly-result](../assets/checks/after-date-time/anomaly-result.png)

**Why they failed:**

- The rule requires timestamps to be **strictly later than** the cutoff
- Any value before or equal to the cutoff violates post-migration expectations

### Why This Was a Serious Issue

Without this check:

- Active users looked inactive
- Security reports were inaccurate
- Fraud systems operated on false signals
- Business decisions were based on stale behavior data

### The Outcome

#### Immediate Fix

- Identified the service populating `LAST_LOGIN_TS`
- Corrected the data pipeline to read from the new auth system
- Backfilled affected records with correct timestamps

#### Long-Term Protection

- Any future regression is detected automatically
- Cutover boundaries are continuously enforced
- Teams trust that login activity reflects real user behavior

## Key Takeaways

- After Date Time enforces strict time boundaries
- It guarantees post-cutover data correctness
- It prevents legacy or backdated records from polluting datasets
- It runs automatically once configured

## When Should You Use After Date Time?

Use After Date Time whenever you need to:

- Enforce system go-live or migration cutoffs
- Validate ingestion or processing timestamps
- Detect stale or replayed data
- Protect dashboards from historical pollution

### Field Scope

**Single:** The rule evaluates a single specified field.

**Accepted Types**

| Type    |                          |
|---------|--------------------------|
| `Date`      | <div style="text-align:center">:octicons-check-16:</div>  |
| `Timestamp` | <div style="text-align:center">:octicons-check-16:</div>  |

### General Properties

{%
    include-markdown "components/general-props/index.md"
    start='<!-- all-props--start -->'
    end='<!-- all-props--end -->'
%}

### Specific Properties

Specify a particular date and time to act as the threshold for the rule.

| Name           | Description                                                   |
|----------------|---------------------------------------------------------------|
| <div class="text-primary">Date</div>  | The timestamp used as the lower boundary. Values in the selected field should be after this timestamp. |

### Anomaly Types

{%
    include-markdown "components/anomaly-support/index.md"
    start='<!-- all-types--start -->'
    end='<!-- all-types--end -->'
%}

### Example

**Objective**: *Ensure that all O_ORDERDATE entries in the ORDERS table are later than 10:30 AM on December 31st, 1991.*

**Sample Data**

| O_ORDERKEY | O_ORDERDATE |
|------------|-------------|
| 1  | <span class="text-negative">1991-12-31 10:30:00</span> |
| 2  | 1992-01-02 09:15:00 |
| 3  | <span class="text-negative">1991-12-14 10:25:00</span> |

=== "Payload example"
    ``` json
    {
        "description": "Ensure that all O_ORDERDATE entries in the ORDERS table are later than 10:30 AM on December 31st, 1991.",
        "coverage": 1,
        "properties":  {
            "datetime": "1991-12-31 10:30:00"
        },
        "tags": [],
        "fields": ["O_ORDERDATE"],
        "additional_metadata": {"key 1": "value 1", "key 2": "value 2"},
        "rule": "afterDateTime",
        "container_id": {container_id},
        "template_id": {template_id},
        "filter": "1=1"
    }
    ```

**Anomaly Explanation**

In the sample data above, the entries with `O_ORDERKEY` **1** and **3** do not satisfy the rule because their `O_ORDERDATE` values are not after **1991-12-31 10:30:00**.

=== "Flowchart"
    ``` mermaid
    graph TD
    A[Start] --> B[Retrieve O_ORDERDATE]
    B --> C{Is O_ORDERDATE > '1991-12-31 10:30:00'?}
    C -->|Yes| D[Move to Next Record/End]
    C -->|No| E[Mark as Anomalous]
    E --> D
    ```
=== "SQL"
    ```sql
    -- An illustrative SQL query demonstrating the rule applied to example dataset(s)
    select
        o_orderkey
        , o_orderdate
    from orders 
    where
        o_orderdate <= '1991-12-31 10:30:00'
    ```

**Potential Violation Messages**

!!! example "Record Anomaly"
    The `O_ORDERDATE` value of `1991-12-14 10:30:00` is not later than **1991-12-31 10:30:00**

!!! example "Shape Anomaly"
    In `O_ORDERDATE`, 66.667% of 3 filtered records (2) are not later than **1991-12-31 10:30:00**
