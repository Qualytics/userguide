# Anomaly Types

Anomalies in Qualytics are classified into two primary types, **Record Anomalies** and **Shape Anomalies**, each targeting different aspects of data integrity. Record anomalies flag individual rows that fail specific quality checks, such as missing or invalid values. Shape anomalies, on the other hand, detect structural issues in the dataset, like missing columns or schema mismatches. Together, these types provide a comprehensive approach to identifying both value-level and schema-level data quality issues.

Let’s get started 🚀

## Record Anomaly

A record anomaly identifies a single record (row) as anomalous and provides specific details regarding why it is considered anomalous. The simplest form of a record anomaly is a row that lacks an expected value for a field.

## Example Use Case

**Scenario**

We have an **Employee dataset** used for payroll.

**Rules:**

- Every employee must have a **Salary greater than 40,000**.  
- The dataset must contain these **four columns**: `id`, `name`, `age`, `salary`.  
- The `name` must follow the `"First Last"` format.

**Rule Checked:** Salary > 40,000

### Input Table

| id | name        | age | salary  |
|----|------------|-----|---------|
| 1  | John Doe    | 28  | 50,000 |
| 2  | Jane Smith  | 35  | 75,000 |
| 3  | Bob Johnson | 22  | 30,000 |

## Detection Result (Record Anomaly)

| id | name        | age | salary  | anomaly_reason                              |
|----|------------|-----|---------|--------------------------------------------|
| 3  | Bob Johnson | 22  | 30,000 | Salary is less than the required 40,000    |

#### Why this is a Record Anomaly:

The table structure is correct. **Only one row’s value violates the rule**.

## Shape Anomaly

A shape anomaly identifies an anomalous structure within the analyzed data. The simplest shape anomaly is a dataset that doesn't match the expected schema because it lacks one or more fields. Some shape anomalies only apply to a subset of the data being analyzed and can therefore produce a count of the number of rows that reflect the anomalous concern. Where that is possible, the shape anomaly's anomalous_record_count is populated.

!!! note
    Sometimes, shape anomalies only affect a subset of the dataset. This means that only certain rows exhibit the structural issue, rather than the entire dataset.

## Example Use Case

**Scenario**

We have a **Sales Orders dataset**.

**Rules:**
- Required columns: `order_id`, `customer_id`, `order_date`, `total_amount`.  
- `order_date` must be in **YYYY-MM-DD** format.

## Shape Anomaly Example (Strong)

## Input Table (Faulty)

| order_id | customer_id | order_date  |
|----------|-------------|------------|
| 101      | C001        | 2025-08-10 |
| 102      | C002        | 08/11/2025 |
| 103      | C003        | 2025-08-12 |

## Detection Result (Shape Anomalies)

| order_id | customer_id | order_date  | total_amount | anomaly_reason                                    |
|----------|-------------|------------|-------------|--------------------------------------------------|
| 101      | C001        | 2025-08-10 | –           | Missing total_amount column                       |
| 102      | C002        | 08/11/2025 | –           | Missing total_amount column; Date format incorrect |
| 103      | C003        | 2025-08-12 | –           | Missing total_amount column                       |

### Why this is a Shape Anomaly:

- A **required column** (`total_amount`) is completely missing from the structure.  
- A **field format** (`order_date` in row 102) does not match the required **YYYY-MM-DD** pattern.  
- The problem is with the **shape/structure** of the dataset, not just a wrong value.

!!! note
    When a shape anomaly affects only a portion of the dataset, Qualytics can count the number of rows that have the structural problem. This count is stored in the anomalous_record_count field, providing a clear measure of how widespread the issue is within the dataset. Example: Imagine a dataset that is supposed to have columns for id, name, age, and salary. If some rows are missing the salary column, this would be flagged as a shape anomaly. If this issue only affects 50 out of 1,000 rows, the anomalous_record_count would be 50, indicating that 50 rows have a structural issue. 