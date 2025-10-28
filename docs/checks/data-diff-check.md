# Data Diff

!!! info "Recommended Check"
    Qualytics recommends using the `dataDiff` rule type instead of the `isReplicaOf`.
    
    The `isReplicaOf` check is being deprecated and will no longer be maintained, while `dataDiff` provides the same functionality with enhanced performance and additional capabilities.

## What is Data Diff?

Think of Data Diff as a **"spot the difference" game for your business data**. 

Just like when you compare two pictures side-by-side to find what's changed, Data Diff compares two sets of information to make sure they match perfectly. It's like having a super-careful assistant who checks that when you copy something important, nothing gets lost, changed, or added by mistake.

## Add Data Diff Check and Detect Anomalies

Use the Data Diff Check to compare two tables, detect anomalies, and run a scan to identify mismatched or missing records for accurate data validation.

<!--ARCADE EMBED START--><div style="position: relative; padding-bottom: calc(47.9861% + 41px); height: 0px; width: 100%;"><iframe src="https://demo.arcade.software/LhdAk8rN6egUFK8dmjfV?embed&embed_mobile=tab&embed_desktop=inline&show_copy_link=true" title="Configure and Run a Data Quality Check with Data Diff" frameborder="0" loading="lazy" webkitallowfullscreen mozallowfullscreen allowfullscreen allow="clipboard-write" style="position: absolute; top: 0; left: 0; width: 100%; height: 100%; color-scheme: light;" ></iframe></div><!--ARCADE EMBED END-->

## What Does Data Diff Do?

Data Diff helps you answer questions like:

- "Did all my customer orders copy correctly to the backup system?"
- "Is the sales report showing the same numbers as the original database?"
- "When we moved data from System A to System B, did everything transfer properly?"

**In simple terms:** It makes sure Data Set A is an exact match of Data Set B.

## How Does Data Diff Work?

Let's break it down into simple steps:

### Step 1: Choose What to Compare

You pick two sets of data:

- **The Original** (your main source of truth)
- **The Copy** (backup, report, or transferred data)

### Step 2: Pick What Matters
You decide which information is important to check. For example:

- Customer names
- Order amounts
- Product IDs
- Dates

### Step 3: The Comparison Happens

Data Diff automatically looks at both sets:

- Is everything from the original in the copy?
- Is there anything extra in the copy that shouldn't be there?
- Do all the values match exactly?

### Step 4: Get Your Results

The Data Diff report shows:

- **Pass** – Target and reference datasets match; no action needed.
- **Anomalies Found** – Differences detected; view the report to see which rows or fields differ.

## Why Should You Use Data Diff?

### 1. Catch Mistakes Before They Cause Problems

Imagine your finance team creates a quarterly report from last night's data backup. If some transactions didn't copy over, your report would be wrong. Data Diff catches this immediately.

### 2. Save Time and Reduce Stress

Instead of manually checking thousands of rows in spreadsheets, Data Diff does it automatically in seconds.

### 3. Build Trust in Your Data

When you present numbers to leadership or clients, you can confidently say, "This data has been verified."

### 4. Protect Your Business

Wrong data can lead to:

- Incorrect invoices
- Bad business decisions
- Compliance issues
- Customer complaints

Data Diff acts as your safety net.

## Real-Life Example: Online Retail Store

Let me walk you through a complete, real-world scenario:

### The Situation

**Sunshine Electronics** is an online store that sells gadgets. Every night at midnight, their system creates a backup copy of all the day's orders. This backup is used for:

  - Creating daily sales reports
  - Feeding data to their accounting system
  - Analyzing customer trends

### The Problem They Had

One morning, the Sales Manager noticed the daily report showed 1,247 orders, but the warehouse had shipped 1,250 packages. **Where did 3 orders go?**

After investigating, they discovered:

  - The backup system had a glitch
  - Some orders placed between 11:58 PM and midnight weren't copied over
  - This had been happening for weeks
  - They had been under-reporting revenue and had incorrect inventory counts

### The Solution: Data Diff

They set up Data Diff to automatically compare their main orders database with the backup every morning.

**Here's what they compared:**

**Original Orders Database:**

| Order ID | Customer Name | Product | Amount | Date |
| :--------- | :------------- | :-------- | :------- | :----------- |
| 10001 | Sarah Johnson | Laptop | $899 | Jan 15, 2025 |
| 10002 | Mike Chen | Headphones | $149 | Jan 15, 2025 |
| 10003 | Emily Davis | Tablet | $399 | Jan 15, 2025 |
| ... | ... | ... | ... | ... |
| 10248 | David Lee | Phone Case | $19 | Jan 15, 2025 |
| 10249 | Anna Brown | USB Cable | $12 | Jan 15, 2025 |
| 10250 | Tom Wilson | Mouse | $29 | Jan 15, 2025 |

**Backup Orders Database:**

| Order ID | Customer Name | Product | Amount | Date |
| :--------| :-------------| :-------| :------| :-----|
| 10001 | Sarah Johnson | Laptop | $899 | Jan 15, 2025 |
| 10002 | Mike Chen | Headphones | $149 | Jan 15, 2025 |
| 10003 | Emily Davis | Tablet | $399 | Jan 15, 2025 |
| ...   | ...     | ...     | ... | ...     |
| <span class="text-negative">10248</span>  | <span class="text-negative">Missing</span> | <span class="text-negative">Missing</span> | <span class="text-negative">Missing</span> | <span class="text-negative">Missing</span> | 
| <span class="text-negative">10249</span> | <span class="text-negative">Missing</span> | <span class="text-negative">Missing</span> | <span class="text-negative">Missing</span> | <span class="text-negative">Missing</span> | 
| <span class="text-negative">10250</span> | <span class="text-negative">Missing</span> | <span class="text-negative">Missing</span> | <span class="text-negative">Missing</span> | <span class="text-negative">Missing</span> |

### What Data Diff Discovered

**ALERT GENERATED:**

!!! warning "DIFFERENCE DETECTED!"
    - Fields Affected: amount, order_id, product, order_date, customer_name
    - Rule Applied: Data Diff
    - Anomalous Records: 3

**Technical Anomaly Output:**

!!! info
    - Anomaly Type: Shape
    - Source Records: 1,250
    - Target Records: 1,247
    - Missing Records: 3 (order_ids: 10248, 10249, 10250)

### The Outcome

**Immediate Benefits:**

- They fixed the backup system timing issue
- They recovered the missing orders data
- They corrected their sales reports

**Long-term Benefits:**

- Now they get an automatic email every morning confirming data matches
- If there's ever a mismatch, they know within hours instead of weeks
- They prevented thousands of dollars in unreported revenue
- Their inventory tracking became accurate again

## Another Quick Example: Healthcare Clinic

**City Health Clinic** transfers patient appointment data from their scheduling system to their billing system every hour.

**They use Data Diff to check:**

- Patient Name
- Appointment Date
- Doctor Assigned
- Service Type
- Insurance Information

### 📋 Before Correction (Data Diff Caught This)

| **Field**      | **Scheduling System** | **Billing System** |
|----------------|----------------------|--------------------|
| Patient        | Robert Martinez       | Robert Martinez    |
| Doctor         | Dr. Smith             | Dr. Smith          |
| Insurance Plan | BlueCross Plan **A**  | <span style="color:red">BlueCross Plan **B** </span> |

The **Insurance Plan** code changed during transfer. Without Data Diff, the clinic would have billed the wrong insurer.

### ✅ After Correction (Fixed Data)

| **Field**      | **Scheduling System** | **Billing System** |
|----------------|----------------------|--------------------|
| Patient        | Robert Martinez       | Robert Martinez    |
| Doctor         | Dr. Smith             | Dr. Smith          |
| Insurance Plan | BlueCross Plan **A**  | BlueCross Plan **A** |

!!! info
    Data Diff caught the mismatch and the billing team corrected it before submitting the claim — avoiding claim rejection, payment delays, and extra work.

## Key Takeaways

**Data Diff is like having a careful proofreader** who checks that when you copy important information, nothing goes wrong.

**It works automatically**- you set it up once, and it keeps watching your data 24/7.

**It catches problems early**- before they affect your reports, decisions, or customers.

**It gives you peace of mind**- you can trust that your backup, reports, and transferred data are accurate.

## When Should You Use Data Diff?

Use Data Diff whenever you:

- Copy data from one place to another
- Create backups of important information
- Generate reports from multiple sources
- Transfer data between different systems
- Move data to the cloud
- Export data to partners or vendors

### Field Scope

**Multi:** The rule evaluates multiple specified fields.

**Accepted Types**

| Type        |                          |
|-------------|--------------------------|
| `Date`      | <div style="text-align:center">:octicons-check-16:</div>      |
| `Timestamp` | <div style="text-align:center">:octicons-check-16:</div>      |
| `Integral`  | <div style="text-align:center">:octicons-check-16:</div>      |
| `Fractional`| <div style="text-align:center">:octicons-check-16:</div>      |
| `String`    | <div style="text-align:center">:octicons-check-16:</div>      |
| `Boolean`   | <div style="text-align:center">:octicons-check-16:</div>      |

### General Properties

{%
include-markdown "components/general-props/index.md"
start='<!-- filter-only--start -->'
end='<!-- filter-only--end -->'
%}

### Specific Properties

Specify the datastore and table/file where the reference data for the targeted fields is located for comparison.

| Name       | Description                                                   |
|------------|---------------------------------------------------------------|
| <div class="text-primary">Row Identifiers</div>  | The list of fields defining the compound key to identify rows in the comparison analysis. |
| <div class="text-primary">Datastore</div>  | The source datastore where the reference data for the targeted field(s) is located. |
| <div class="text-primary">Table/file</div> | The table, view or file in the source datastore that should serve as the reference for comparison. |
| <div class="text-primary">Comparators</div> | {{ comparator_short_desc }} |

!!! info
    The `DataDiff` rule supports editing of `Row Identifiers` and `Passthrough Fields`, allowing for more tailored configuration.

!!! note "Details"
    <div style="margin-top: -12px;">
    ### Row Identifiers
    </div>

    This optional input allows row comparison analysis by defining a list of fields as row identifiers, it enables a more detailed comparison between tables/files, where each row compound key is used to identify its presence or absence in the reference table/file compared to the target table/file.  Qualytics can inform if the row exists or not and distinguish which field values differ in each row present in the reference table/file, helping to determine if it is a data diff.

    !!! info
        Anomalies produced by a `DataDiff` quality check making use of `Row Identifiers` have their source records presented in a different visualization. <br><br>
        See more at: *[Comparison Source Records](../anomalies/source-record.md/#comparison-source-records)*

    {%
        include-markdown "components/comparators/index.md"
    %}
    {%
        include-markdown "components/comparators/numeric.md"
    %}
    {%
        include-markdown "components/comparators/duration.md"
    %}
    {%
        include-markdown "components/comparators/string.md"
    %}

### Anomaly Types

{%
    include-markdown "components/anomaly-support/index.md"
    start='<!-- shape-only--start -->'
    end='<!-- shape-only--end -->'
%}

### Example

**Scenario**: *Consider that the fields N_NATIONKEY and N_NATIONNAME in the NATION table need to be compared with a backup database for data validation purposes. The data engineering team wants to ensure that both fields in the backup accurately match the original.*

**Objective**: *Ensure that N_NATIONKEY and N_NATIONNAME from the NATION table match the data in the NATION_BACKUP table.*

**Sample Data from NATION**

| N_NATIONKEY | N_NATIONNAME       |
|-------------|--------------------|
| 1           | Australia          |
| 2           | United States      |
| 3           | Uruguay            |

**Reference Sample Data from NATION_BACKUP**

| N_NATIONKEY | N_NATIONNAME       |
|-------------|--------------------|
| 1           | Australia          |
| 2           | USA                |
| 3           | Uruguay            |

=== "Payload example"
    ``` json
    {
        "description": "Ensure that N_NATIONKEY and N_NATIONNAME from the NATION table match the data in the NATION_BACKUP table",
        "coverage": 1,
        "properties": {
            "ref_container_id": {ref_container_id},
            "ref_datastore_id": {ref_datastore_id}
        },
        "tags": [],
        "fields": ["N_NATIONKEY", "N_NATIONNAME"],
        "additional_metadata": {"key 1": "value 1", "key 2": "value 2"},
        "rule": "dataDiff",
        "container_id": {container_id},
        "template_id": {template_id},
        "filter": "1=1"
    }
    ```

**Anomaly Explanation**

The datasets representing the fields `N_NATIONKEY` and `N_NATIONNAME` in the original and the reference data are not completely identical, indicating a possible discrepancy in the data or an unintended change.

=== "Flowchart"
    ```mermaid
    graph TD
    A[Start] --> B[Retrieve Original Data]
    B --> C[Retrieve Reference Data]
    C --> D{Do datasets match for both fields?}
    D -->|Yes| E[End]
    D -->|No| F[Mark as Anomalous]
    F --> E
    ```

=== "SQL"
    ```sql
    -- An illustrative SQL query comparing original to reference data for both fields.
    select
        orig.n_nationkey as original_key,
        orig.n_nationname as original_name,
        ref.n_nationkey as reference_key,
        ref.n_nationname as reference_name
    from nation as orig
    left join nation_backup as ref on orig.n_nationkey = ref.n_nationkey
    where
        orig.n_nationname <> ref.n_nationname
    or
        orig.n_nationkey <> ref.n_nationkey
    ```

**Potential Violation Messages**

!!! example "Shape Anomaly"
    There is 1 record that differs between `NATION_BACKUP` (3 records) and `NATION` (3 records) in `<datastore_name>`