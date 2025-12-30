# Between

The **Between** rule is used to ensure that numeric values stay within an expected and acceptable range.  
It is commonly used to catch outliers, invalid measurements, and data entry or pipeline errors before they impact reports or downstream systems.

## What is Between?

Think of **Between** as a **“safety fence” for numeric values** in your data.

Just like speed limits on a road prevent unsafe driving, the Between check ensures that numbers stay within boundaries that make sense for your business.  
If a value goes below the minimum or above the maximum, it gets flagged immediately.

**In simple terms:** This number must fall within this range.

## Add Between Check

Use the Between check when you want to validate that a numeric field stays within an expected minimum and maximum value.

<!--ARCADE EMBED START--><div style="position: relative; padding-bottom: calc(40.6806% + 41px); height: 0px; width: 100%;"><iframe src="https://demo.arcade.software/oLKe4W3dZvKtOZybnLsL?embed&embed_mobile=tab&embed_desktop=inline&show_copy_link=true" title="Add a Between Check" frameborder="0" loading="lazy" webkitallowfullscreen mozallowfullscreen allowfullscreen allow="clipboard-write" style="position: absolute; top: 0; left: 0; width: 100%; height: 100%; color-scheme: light;" ></iframe></div><!--ARCADE EMBED END-->

This helps you detect:

- Unexpected spikes or drops  
- Data entry mistakes  
- Sensor or system malfunctions  
- Broken transformations or unit conversion issues  

## What Does Between Do?

Between helps you answer questions like:

- “Is this quantity unreasonably low or high?”  
- “Did a system send an invalid numeric value?”  
- “Are measurements staying within realistic limits?”  
- “Did a unit conversion break and inflate values?”  

**In short:** It ensures your numbers stay realistic and trustworthy.

## How Does Between Work?

Let’s break it down step by step.

### Step 1: Choose a Numeric Field

You select a single numeric field, such as:

- Quantity  
- Price  
- Temperature  
- Duration  
- Weight  
- Usage count  

### Step 2: Define the Acceptable Range

You specify:

- Minimum value  
- Maximum value  
- Whether each boundary is inclusive or exclusive  

**Example:**

- Min = 5 (inclusive)  
- Max = 20 (inclusive)  

This means:  
👉 **5 ≤ value ≤ 20**

### Step 3: Validation Happens Automatically

For each record, the Between check evaluates:

- Is the value less than the minimum?  
- Is the value greater than the maximum?  

If **yes** → **Anomaly detected**

### Step 4: Review the Results

The output shows:

- **Pass** – Value is within the allowed range  
- **Anomaly Found** – Value falls outside the range  

## Why Should You Use Between?

### 1. Catch Invalid Values Early

A quantity of `-3`, `0`, or `10,000` may technically be a number—but it may not make sense for your business.

Between catches these issues before they reach dashboards or customers.

### 2. Prevent Bad Decisions

Out-of-range values can:

- Skew averages  
- Break charts  
- Trigger false alerts  
- Lead to wrong operational decisions  

Between protects your analytics from bad inputs.

### 3. Save Manual Validation Time

Instead of scanning reports for suspicious numbers, Between continuously validates every new record automatically.

### 4. Increase Confidence in Data Quality

When stakeholders see numbers within expected bounds, trust in your data increases.

## Real-Life Example: Insurance Location Risk Validation (Between Check)

### The Situation

An insurance company maintains a **property insurance portfolio** in the `FL_INSURANCE` table.  
This data is used by actuarial and catastrophe-risk models to calculate premiums and exposure.

One critical numeric field is **`POINT_GRANULARITY`**, which defines the resolution used for location-based risk calculations.

Based on business and modeling requirements:

- **Minimum allowed value:** `1.000`  
- **Maximum allowed value:** `5.000`  

Any value outside this range makes the risk calculation unreliable.

### The Problem

During a routine data quality scan on the **Insurance Portfolio – Staging** datastore, analysts noticed unexpected behavior in downstream risk models.

There were:

- No missing records  
- No schema mismatches  
- No pipeline failures  

However, some policies showed **unexpected risk scores**, even though the data appeared complete.

### The Solution: Between Check

To validate numeric correctness, the data team configured a **Between check** on the `POINT_GRANULARITY` field with the following rules:

<!--ARCADE EMBED START--><div style="position: relative; padding-bottom: calc(40.6806% + 41px); height: 0px; width: 100%;"><iframe src="https://demo.arcade.software/xS3XhQ4HikNTQI1hTirW?embed&embed_mobile=tab&embed_desktop=inline&show_copy_link=true" title="Solution" frameborder="0" loading="lazy" webkitallowfullscreen mozallowfullscreen allowfullscreen allow="clipboard-write" style="position: absolute; top: 0; left: 0; width: 100%; height: 100%; color-scheme: light;" ></iframe></div><!--ARCADE EMBED END-->

- **Min:** `1.000` (inclusive)  
- **Max:** `5.000` (inclusive)

This ensured that every insurance record used a valid granularity level for risk computation.

### What the Between Check Discovered

!!! warning "OUT-OF-RANGE VALUES DETECTED"
    - Field: `POINT_GRANULARITY`
    - Rule Applied: Between
    - Violation: **0.049%** of filtered records (36,645 total)
    - Allowed Range: **1.000 to 5.000**

### Source Records (Anomalous Values)

| <span class="text-negative">POINT_GRANULARITY</span> | EQ_SITE_DEDUCTIBLE | TIV_2011 | HU_SITE_LIMIT |
|-------------------|-------------------|----------|---------------|
| <span class="text-negative">6</span>  | 26405             | 191651   | 369075        |
| <span class="text-negative">6</span>  | 72628             | 580170   | -80130        |
| <span class="text-negative">9</span>  | 92381             | 165469   | 753709        |
| <span class="text-negative">6</span>  | 17849             | 939037   | 365831        |
| <span class="text-negative">7</span>  | 17753             | 196937   | 676446        |
| <span class="text-negative">6</span>  | 35655             | 957449   | -75944        |
| <span class="text-negative">8</span>  | 57319             | 856692   | 923312        |
| <span class="text-negative">7</span>  | 56104             | 78318    | 770455        |
| <span class="text-negative">6</span>  | 21986             | 152933   | -19570        |
| <span class="text-negative">10</span> | 71621             | -12793   | -32706        |

![between-check-anomaly-result](../assets/checks/between-check/anomaly-result.png)

These records were structurally valid but **numerically invalid** according to business rules.

### Anomaly Interpretation

- The records existed in the table and passed schema validation  
- Only the **numeric constraint** was violated  
- Because a range rule failed, the anomaly was classified as a **Shape anomaly**  
- This indicated a **data quality issue**, not missing or duplicate data  

### Root Cause Identified

Further investigation showed:

- An upstream ingestion change defaulted `POINT_GRANULARITY` to higher values
- No validation existed at the source system
- The issue silently propagated into staging analytics

### The Outcome

**Immediate Results**
- Invalid values were corrected
- Risk models were recalculated using valid granularity levels

**Long-Term Protection**
- The Between check now runs automatically on each scan
- Any future out-of-range values are flagged immediately
- Incorrect risk calculations are prevented before reporting or pricing

### 🔍 Key Takeaway

**Between checks protect numeric fields that must stay within strict business limits.**

In this case, the Between check caught values that were technically valid numbers—but **business-invalid**, preventing incorrect insurance risk assessments and downstream decisions.

### Field Scope

**Single:** The rule evaluates a single specified field.

**Accepted Types**

| Type          |                          |
|---------------|--------------------------|
| `Integral`    | <div style="text-align:center">:octicons-check-16:</div>  |
| `Fractional`  | <div style="text-align:center">:octicons-check-16:</div>  |

### General Properties

{%
    include-markdown "components/general-props/index.md"
    start='<!-- all-props--start -->'
    end='<!-- all-props--end -->'
%}

### Specific Properties

Specify both minimum and maximum boundaries, and determine if these boundaries should be inclusive.

| Name                   | Explanation                                                                                                 |
|------------------------|-------------------------------------------------------------------------------------------------------------|
| <div class="text-primary">Max</div>                | The upper boundary of the range.                                                                             |
| <div class="text-primary">Inclusive (Max)</div>    | If true, the upper boundary is considered a valid value within the range. Otherwise, it's exclusive.     |
| <div class="text-primary">Min</div>                | The lower boundary of the range.                                                                             |
| <div class="text-primary">Inclusive (Min)</div>    | If true, the lower boundary is considered a valid value within the range. Otherwise, it's exclusive.     |

### Anomaly Types

{%
    include-markdown "components/anomaly-support/index.md"
    start='<!-- all-types--start -->'
    end='<!-- all-types--end -->'
%}

### Example

**Objective**: *Ensure that all L_QUANTITY entries in the LINEITEM table are between 5 and 20 (inclusive).*

**Sample Data**

| L_ORDERKEY | L_QUANTITY |
|------------|------------|
| 1          | <span class="text-negative">4</span>          |
| 2          | 15         |
| 3          | <span class="text-negative">21</span>         |

=== "Payload example"
    ``` json
    {
        "description": "Ensure that all L_QUANTITY entries in the LINEITEM table are between 5 and 20 (inclusive)",
        "coverage": 1,
        "properties": {
            "min":5,
            "inclusive_min":true
            "max":20,
            "inclusive_max":true
        },
        "tags": [],
        "fields": ["L_QUANTITY"],
        "additional_metadata": {"key 1": "value 1", "key 2": "value 2"},
        "rule": "between",
        "container_id": {container_id},
        "template_id": {template_id},
        "filter": "1=1"
    }
    ```

**Anomaly Explanation**

In the sample data above, the entries with `L_ORDERKEY` **1** and **3** do not satisfy the rule because their `L_QUANTITY` values are not between **5** and **20** inclusive.

=== "Flowcharts"
    ``` mermaid
    graph TD
    A[Start] --> B[Retrieve L_QUANTITY]
    B --> C{Is 5 <= L_QUANTITY <= 20?}
    C -->|Yes| D[Move to Next Record/End]
    C -->|No| E[Mark as Anomalous]
    E --> D
    ```

=== "SQL"
    ```sql
    -- An illustrative SQL query demonstrating the rule applied to example dataset(s).
    select
        l_orderkey
        , l_quantity
    from lineitem 
    where
        l_quantity < 5
        or l_quantity > 20
    ```

**Potential Violation Messages**

!!! example "Record Anomaly"
    The value for `L_QUANTITY` of 4 is not between **5.000** and **20.000**.
        
!!! example "Shape Anomaly"
    In `L_QUANTITY`, 66.67% of 3 filtered records (2) are not between **5.000** and **20.000**.

