# Between Times

Use the `betweenTimes` rule when you need to validate that date or timestamp values fall within an expected time window. This check is ideal for catching early, late, or invalid records caused by ingestion delays, timezone issues, or system errors.

## What is Between Times?

Think of Between Times as a **time window guardrail for your data ⏱️**.

Just like a store that only accepts deliveries between **9 AM and 6 PM**, this check makes sure your data shows up **when it’s supposed to**—not before, not after.

If a record arrives too early, too late, or completely outside the allowed window, Between Times flags it immediately.

**In simple terms:** Between Times makes sure your data arrives on time—and only on time.

## Add Between Times Check

Use the Between Times check to validate timestamps, enforce business hours, and detect out-of-range records before they impact reporting or downstream systems.

<!--ARCADE EMBED START--><div style="position: relative; padding-bottom: calc(48.0208% + 41px); height: 0px; width: 100%;"><iframe src="https://demo.arcade.software/hSgyntZZ7yLMwpQpvsB1?embed&embed_mobile=tab&embed_desktop=inline&show_copy_link=true" title="Add a Between Times Check" frameborder="0" loading="lazy" webkitallowfullscreen mozallowfullscreen allowfullscreen allow="clipboard-write" style="position: absolute; top: 0; left: 0; width: 100%; height: 100%; color-scheme: light;" ></iframe></div><!--ARCADE EMBED END-->

## What Does Between Times Do?

Between Times helps you answer questions like:

- “Did these records arrive during valid business hours?”
- “Are any timestamps outside the expected date range?”
- “Did old or future-dated records sneak into my dataset?”

**In simple terms:** It ensures every date or timestamp stays within an allowed start and end time.

## How Does Between Times Work?

### Step 1: Choose the Time Field

Select the date or timestamp field you want to validate (for example, `created_at` or `event_time`).

### Step 2: Define the Allowed Time Window

Set:

- **Start Time**
- **End Time**

This could be a date range, business hours, or a strict ingestion window.

### Step 3: The Validation Happens

Between Times checks every record:

- Inside the window → ✅ Pass  

- Outside the window → ❌ Flagged as anomalous

### Step 4: Review the Results

If violations exist, you’ll see exactly:

- Which records failed
- By how much they were early or late
- Which field caused the anomaly

## Why Should You Use Between Times?

### 1. Catch Timing Issues Early 

Late or early data can silently corrupt reports. This check surfaces issues immediately.

### 2. Prevent Invalid Historical or Future Data  

Old test records or future-dated entries won’t sneak into production analytics.

### 3. Improve Trust in Time-Based Reports  

Dashboards, SLAs, and audits depend on correct timestamps. Between Times keeps them reliable.

### 4. Reduce Downstream Failures  

Many pipelines break when timestamps are out of range. This check stops bad data upstream.

## Real-Life Example: City Infrastructure Dataset

### The Situation

A city data team manages a **building permits dataset**. Each permit record includes a `CREATED_DATE` field that should fall between:

- **January 1, 1995**
- **June 2, 2019**

This dataset feeds:

- Urban planning reports
- Historical trend analysis
- Compliance dashboards

### The Problem They Faced

Over time, the team noticed strange trends in reports:

- Some permits appeared **decades too early**
- Others showed dates **far in the future**
- KPIs based on yearly counts were off

They suspected bad timestamps but had no automated way to catch them.

### The Solution: Between Times

They configured a **Between Times** check on the `CREATED_DATE` field with the allowed date range.

<!--ARCADE EMBED START--><div style="position: relative; padding-bottom: calc(48.0208% + 41px); height: 0px; width: 100%;"><iframe src="https://demo.arcade.software/WQfRRRrwVp8Lqt13SzvS?embed&embed_mobile=tab&embed_desktop=inline&show_copy_link=true" title="Solution" frameborder="0" loading="lazy" webkitallowfullscreen mozallowfullscreen allowfullscreen allow="clipboard-write" style="position: absolute; top: 0; left: 0; width: 100%; height: 100%; color-scheme: light;" ></iframe></div><!--ARCADE EMBED END-->

**Rule Setup:**

- Field: `CREATED_DATE`
- Start Time: `1995-01-01`
- End Time: `2019-06-02`

### What Between Times Discovered

!!! warning "VIOLATION DETECTED"
    - Field: `CREATED_DATE`
    - Rule Applied: Between Times
    - 21.98% of records were outside the allowed time window

**Example of Flagged Records:**

| CREATED_DATE | CT2010 | XCoord | CB2010 |
|-------------|--------|--------|--------|
| <span class="text-negative">1990-03-05T16:36:27.448Z</span> | 112 | 959857 | 2034 |
| <span class="text-negative">1993-03-28T09:24:21.483Z</span> | 112 | 959604 | 1020 |
| <span class="text-negative">1993-08-19T01:27:27.406Z</span> | 70  | 959403 | 2009 |
| <span class="text-negative">2020-04-08T13:08:12.275Z</span> | 239 | 942672 | 1006 |
| <span class="text-negative">1992-06-28T02:11:50.123Z</span> | 207 | 947120 | 3000 |
| <span class="text-negative">2020-11-04T16:30:36.819Z</span> | 177 | null   | null |
| <span class="text-negative">2020-06-04T14:36:40.406Z</span> | 177 | 958051 | 2002 |
| <span class="text-negative">1991-03-20T21:22:40.939Z</span> | 187 | 948974 | 1015 |
| <span class="text-negative">1992-09-20T18:47:49.845Z</span> | 169 | 951372 | 1012 |
| <span class="text-negative">2019-10-16T12:39:31.870Z</span> | 169 | 953637 | 1002 |

![anomaly-result](../assets/checks/between-time/anomaly-result.png)

### 🔍 Summary

- These records fall **outside the valid historical window**
- They likely came from:
  - Legacy system imports
  - Incorrect timezone conversions
  - Manual data entry errors
- Without this check, they were silently skewing reports

### The Outcome

**Immediate Benefits:**
- Invalid records were identified in minutes
- Analysts excluded bad data from reports
- Data quality issues were traced to the source system

**Long-Term Benefits:**
- Automated monitoring for timestamp validity
- Accurate historical reporting
- Increased trust in time-based analytics
- Fewer surprises during audits

## Key Takeaways

**Between Times acts like a time gate for your data.**

- It ensures records arrive **only within expected time windows**
- It catches early, late, and impossible timestamps
- It runs automatically once configured
- It protects reports, dashboards, and downstream systems

## When Should You Use Between Times?

Use Between Times whenever you need to validate **when** data occurs:

- Event ingestion timestamps
- Record creation dates
- Business hours enforcement
- Historical data boundaries
- SLA and compliance monitoring

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

Specify the range of dates or times that values in the selected field should fall between.

| Name           | Description                                                   |
|----------------|---------------------------------------------------------------|
| <div class="text-primary">Min</div>  | The timestamp used as the lower boundary. Values in the selected field should be after this timestamp. |
| <div class="text-primary">Max</div>  | The timestamp used as the upper boundary. Values in the selected field should be before this timestamp. |

### Anomaly Types

{%
    include-markdown "components/anomaly-support/index.md"
    start='<!-- all-types--start -->'
    end='<!-- all-types--end -->'
%}

### Example

**Objective**: *Ensure that all O_ORDERDATE entries in the ORDERS table are between 10:30 AM on January 1st, 1991 and 3:00 PM on December 31st, 1991.*

**Sample Data**

| O_ORDERKEY | O_ORDERDATE |
|------------|-------------|
| 1  | <span class="text-negative">1990-12-31 10:30:00</span> |
| 2  | 1991-06-02 09:15:00 |
| 3  | <span class="text-negative">1992-01-01 01:25:00</span> |


=== "Payload example"
    ``` json
    {
        "description": "Ensure that all O_ORDERDATE entries in the ORDERS table are between 10:30 AM on January 1st, 1991 and 3:00 PM on December 31st, 1991",
        "coverage": 1,
        "properties": {
            "min_time":"1991-01-01T10:30:00Z",
            "max_time":"1991-12-31T15:00:00Z"
        },
        "tags": [],
        "fields": ["O_ORDERDATE"],
        "additional_metadata": {"key 1": "value 1", "key 2": "value 2"},
        "rule": "betweenTimes",
        "container_id": {container_id},
        "template_id": {template_id},
        "filter": "_PARITY = 'odd'"
    }
    ```

**Anomaly Explanation**

In the sample data above, the entries with `O_ORDERKEY` **1** and **3** do not satisfy the rule because their `O_ORDERDATE` values are not between **1991-01-01 10:30:00** and **1991-12-31 15:00:00**.

=== "Flowchart"
    ``` mermaid
    graph TD
    A[Start] --> B[Retrieve O_ORDERDATE]
    B --> C{Is '1991-01-01 10:30:00' <= O_ORDERDATE <= '1991-12-31 15:00:00'?}
    C -->|Yes| D[Move to Next Record/End]
    C -->|No| E[Mark as Anomalous]
    E --> D
    ```

=== "SQL"
    ```sql
    -- An illustrative SQL query demonstrating the rule applied to example dataset(s).
    select
        o_orderkey
        , o_orderdate
    from orders 
    where
        o_orderdate < '1991-01-01 10:30:00'
        or o_orderdate > '1991-12-31 15:00:00'
    ```

**Potential Violation Messages**

!!! example "Record Anomaly"
    The value for `O_ORDERDATE` of `1990-12-31 10:30:00` is not between **1991-01-01 10:30:00** and **1991-12-31 15:00:00**.

!!! example "Shape Anomaly"
    In `O_ORDERDATE`, 66.667% of 3 filtered records (2) are not between **1991-01-01 10:30:00** and **1991-12-31 15:00:00**.

