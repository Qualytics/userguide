# Contains Email

Think of **Contains Email** as a **basic hygiene check for contact data**.

Any time your system stores customer or user information, email addresses are often the **primary identifier**—used for communication, login, billing, and notifications. This check ensures that the field you expect to contain an email address **actually does**.

## Add Contains Email Check

Use the **Contains Email** check to validate that a specific field includes an email address in the expected format and to detect records where email data is missing, broken, or malformed.

<!--ARCADE EMBED START--><div style="position: relative; padding-bottom: calc(48.0208% + 41px); height: 0px; width: 100%;"><iframe src="https://demo.arcade.software/twbxUZA3Y8reonlkOjfy?embed&embed_mobile=tab&embed_desktop=inline&show_copy_link=true" title="Add a Contains Email Check " frameborder="0" loading="lazy" webkitallowfullscreen mozallowfullscreen allowfullscreen allow="clipboard-write" style="position: absolute; top: 0; left: 0; width: 100%; height: 100%; color-scheme: light;" ></iframe></div><!--ARCADE EMBED END-->

## What Does Contains Email Do?

Contains Email helps you catch issues like:

- Missing `@` or domain name  
- Truncated or partially stored email values  
- Corrupted email data during ingestion or transformation  
- Non-email text accidentally stored in an email field  

**In simple terms:** It makes sure your email fields actually contain emails.

## How Does Contains Email Work?

### Step 1: Choose the Field

You select **one field** that is expected to contain an email address (for example: `email`, `contact_details`, or a JSON column containing email data).

### Step 2: The Validation Happens

Qualytics scans each record and checks whether the field value matches a valid email pattern.

### Step 3: Get Your Results

- **Pass** – The field contains a valid email address  
- **Anomaly Found** – The value does not contain a valid email  

## Why Should You Use Contains Email?

### 1. Prevent Broken Communication

If emails are malformed, automated emails fail silently—customers never receive confirmations, alerts, or updates.

### 2. Improve Data Quality Upstream

Catching bad emails early prevents downstream issues in CRM systems, marketing tools, and analytics.

### 3. Avoid Operational Errors

Invalid email data can cause:

- Failed notifications
- Login issues
- Customer support escalations
- Compliance gaps

Contains Email acts as a **first-line validation check**.

## Real-Life Example: Customer Contact Data Review

Let me walk you through a complete, real-world scenario:

### The Situation

**BrightCart** is an online retail platform that collects customer contact details during account creation and checkout. Email addresses are critical because they are used for:

- Order confirmations  
- Shipping notifications  
- Password resets  
- Customer support communication  

Before sharing this data with marketing and support teams, the data team reviews it to ensure email information is correct.

### The Problem They Had

Initially, the team relied on **manual review** to validate email data.

One week, customer support noticed an increase in complaints like:

- “I didn’t receive my order confirmation”
- “Password reset email never arrived”

When the data team investigated, they found that **some customer records did not contain valid email addresses**—but these issues had gone unnoticed during manual review.

After digging deeper, they discovered:

- The dataset had grown to tens of thousands of records  
- Analysts were reviewing only a small sample due to time constraints  
- Subtle issues (like missing domains or incomplete emails) were easy to miss  
- Manual checks were inconsistent and error-prone  

### The Solution: Contains Email

To avoid relying on visual inspection, the team introduced the **Contains Email** check to automatically validate email-related fields during every scan.

Instead of checking a few records by hand, the rule evaluated **every record consistently**.

<!--ARCADE EMBED START--><div style="position: relative; padding-bottom: calc(48.0208% + 41px); height: 0px; width: 100%;"><iframe src="https://demo.arcade.software/WTlyBM9ezszi133CMJ35?embed&embed_mobile=tab&embed_desktop=inline&show_copy_link=true" title="Solution" frameborder="0" loading="lazy" webkitallowfullscreen mozallowfullscreen allowfullscreen allow="clipboard-write" style="position: absolute; top: 0; left: 0; width: 100%; height: 100%; color-scheme: light;" ></iframe></div><!--ARCADE EMBED END-->

### What the System Discovered

**ALERT GENERATED:**

!!! warning "EMAIL VALIDATION FAILED"
    - Rule Applied: Contains Email  
    - Anomalous Records: 100% of evaluated records  

**Technical Output (from Qualytics):**

When reviewing the flagged records, the team noticed values like:

| C_NAME | C_MKTSEGMENT | C_PHONE | cp_custkey |
|------|--------------|---------|-----------|
| <span class="text-negative">Customer#000000002</span> | AUTOMOBILE | 23-768-687-3665 | 2 |
| <span class="text-negative">Customer#000000002</span> | AUTOMOBILE | 23-768-687-3665 | 2 |
| <span class="text-negative">Customer#000000002</span> | AUTOMOBILE | 23-768-687-3665 | 2 |
| <span class="text-negative">Customer#000000002</span> | AUTOMOBILE | 23-768-687-3665 | 2 |
| <span class="text-negative">Customer#000000002</span> | AUTOMOBILE | 23-768-687-3665 | 2 |
| <span class="text-negative">Customer#000000002</span> | AUTOMOBILE | 23-768-687-3665 | 2 |
| <span class="text-negative">Customer#000000002</span> | AUTOMOBILE | 23-768-687-3665 | 2 |
| <span class="text-negative">Customer#000000002</span> | AUTOMOBILE | 23-768-687-3665 | 2 |
| <span class="text-negative">Customer#000000002</span> | AUTOMOBILE | 23-768-687-3665 | 2 |
| <span class="text-negative">Customer#000000002</span> | AUTOMOBILE | 23-768-687-3665 | 2 |

![anomaly-result](../assets/checks/contains-email/anomaly-result.png)

### Summary

- Manual review did not scale as data volume increased  
- Incorrect values slipped through unnoticed  
- The automated check immediately surfaced the issue across the entire dataset  
- The problem was identified in minutes instead of days  

### The Outcome

**Immediate Benefits:**

- The team corrected the rule configuration  
- Email validation was applied to the correct data  
- False assumptions from manual review were eliminated  

**Long-Term Benefits:**

- No more time-consuming manual inspections  
- Consistent validation across all records  
- Fewer customer communication failures  
- Greater trust in data shared across teams  

### Key Takeaway

Manual data review works only at small scale. Automated checks like **Contains Email** ensure that **every record is validated**, every time—without relying on human attention or sampling.

### Field Scope

**Single:** The rule evaluates a single specified field.

**Accepted Types**

| Type     |                          |
|----------|--------------------------|
| `String` | <div style="text-align:center">:octicons-check-16:</div> |

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

**Objective**: *Ensure that the `C_CONTACT_DETAILS` field contains at least one valid email address for every record in the CUSTOMER dataset.*

**Sample Data**

| C_CUSTKEY | C_CONTACT_DETAILS                          |
|-----------|----------------------------------|
| 1         | {"name": "John Doe", "email": "john.doe@example.com"}             |
| 2         | <span class="text-negative">{"name": "Amy Lu", "email": "amy.lu@"}</span> |
| 3         | {"name": "Jane Smith", "email": "jane.smith@domain.org"}            |

=== "Payload example"
    ``` json
    {
        "description": "Ensure that all C_CONTACT_DETAILS entries in the CUSTOMER table contain valid email addresses",
        "coverage": 1,
        "properties": {},
        "tags": [],
        "fields": ["C_CONTACT_DETAILS"],
        "additional_metadata": {"key 1": "value 1", "key 2": "value 2"},
        "rule": "containsEmail",
        "container_id": {container_id},
        "template_id": {template_id},
        "filter": "1=1"
    }
    ```

**Anomaly Explanation**

In the sample data above, the entry with `C_CUSTKEY` **2** does not satisfy the rule because its `C_CONTACT_DETAILS` value does not follow a typical email format.

=== "Flowchart"
    ``` mermaid
    graph TD
    A[Start] --> B[Retrieve C_CONTACT_DETAILS]
    B --> C{Does C_CONTACT_DETAILS contain an email address?}
    C -->|Yes| D[Move to Next Record/End]
    C -->|No| E[Mark as Anomalous]
    E --> D
    ```

=== "SQL"
    ```sql
    -- An illustrative SQL query demonstrating the rule applied to example dataset(s).
    select
        c_custkey,
        c_contact_details
    from customer 
    where
        not regexp_like(c_contact_details, '^[a-zA-Z0-9._%-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,4}$')
    ```

**Potential Violation Messages**

!!! example "Record Anomaly"
    The `C_CONTACT_DETAILS` value of `{"name": "Amy Lu", "email": "amy.lu@"}` does not contain an email address.

!!! example "Shape Anomaly"
    In `C_CONTACT_DETAILS`, 33.333% of 3 filtered records (1) do not contain email addresses.
