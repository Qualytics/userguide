# External Scan Operation

External Scan is a specialized Scan Operation that enables you to assert data quality checks against data residing outside the platform. 

It empowers you to assess the quality of external datasets while leveraging the defined checks and anomaly detection capabilities within the platform.

## Key Characteristics:

 - External Data Sources: Accepts CSV, XLSX, and XLS files as data sources.
 - Schema Requirement: Requires an existing schema or structure within the platform that aligns with the external data's format. This schema can be based on a view, computed table, file, or other compatible object.
 - Check Assertion: Uses the same data quality checks defined for the corresponding schema to identify anomalies within the external data.
 - Anomaly Recording: Records any detected anomalies in the associated Enrichment Datastore, similar to standard Scan Operations.


!!! info
    To perform data quality checks on an External Scan operation, users need to have a pre-existing structure.

---

## External Scan Configuration

1. Begin by selecting the existing profile that matches the external data's format.
2. File Upload: Upload the external data file (CSV, XLSX, or XLS).
3. Scan: External Scans always perform full scans of the uploaded data.

![Screenshot](../assets/operations/external-scan-light.png#only-light)
![Screenshot](../assets/operations/external-scan-dark.png#only-dark)

An External Scan Operation can be configured with the following file formats:

| File Extension | .csv                                             | .xls                                            | .xlsx                                          |
|-----------------|--------------------------------------------------|-------------------------------------------------|------------------------------------------------|
| File Format     | Comma-separated values                            | Microsoft Excel 97-2003 Workbook                | Microsoft Excel 2007+ Workbook                   |
| Header Row      | Required for optimal reading. It should contain column names. | Recommended, but not strictly required.     | Recommended, but not strictly required.        |
| Empty Cells     | Represented as empty strings.                     | Allowed.                                        | Allowed.                                       |
| Data Types      | Typically inferred by Spark.                      | May require explicit specification for complex types. | May require explicit specification for complex types. |
| Nested Data     | Not directly supported. Consider flattening or using alternative file formats. | Not directly supported. Consider flattening or using alternative file formats. | Not directly supported. Consider flattening or using alternative file formats. |
| Additional Considerations | - Ensure consistent delimiter usage (usually commas). - Avoid special characters or line breaks within fields. - Enclose text fields containing commas or delimiters in double quotes. | - Use a plain XLS format without macros or formatting. - Consider converting to CSV for simpler handling. | - Use a plain XLSX format without macros or formatting. - Consider converting to CSV for simpler handling. |

## Scenario

A company maintains a large sales database containing information about various transactions, customers, and products. 
The organization wants to ensure data quality and identify any anomalies in the sales data. 

An External Scan is initiated to validate the integrity of the sales table.


### Specific Checks:

| Check                   | Description                                               |
|-------------------------|-----------------------------------------------------------|
| `Expected Schema`       | Verify that all columns have the same data type as the selected profile structure. |
| `Exists in`       | Verify that all transactions have valid customer and product references. |
| `Between Times`    | Ensure that transaction dates fall within an expected range. |
| `Satisfies Expression`      | Validate that the calculated revenue aligns with the unit price and quantity sold. The formula is: `R=Quantity×Unit Price` |


### Potential Anomalies:

| Anomaly                | Description                                               |
|------------------------|-----------------------------------------------------------|
| Data type issue     | The external resource does not follow the data type schema. |
| Missing References     | Transactions without valid customer or product references. |
| Out-of-Range Dates      | Transactions with dates outside the expected range.        |
| Inconsistent Revenue    | Mismatch between calculated revenue and unit price times quantity. |


### Benefits of External Scan:

| Benefit                   | Description                                               |
|---------------------------|-----------------------------------------------------------|
| Quality Assurance         | Identify and rectify data inconsistencies before downstream processes. |
| Data Integrity            | Ensure that all records adhere to defined schema and constraints. |
| Anomaly Detection         | Uncover potential issues that might impact business analytics and reporting. |


### CSV Table (Sales Data):
| Transaction_ID | Customer_ID | Product_ID | Transaction_Date | Quantity | Unit_Price |
|-----------------|-------------|------------|-------------------|----------|------------|
| 1               | 101         | 201        | 2023-01-15        | 5        | 20.00      |
| 2               | 102         | 202        | 2023-02-20        | 3        | 15.50      |
| 3               | 103         | 201        | 2023-03-10        | 2        | 25.00      |
| 4               | 104         | 203        | 2023-04-05        | 1        | 30.00      |
| ...             | ...         | ...        | ...               | ...      | ...        |


=== "Flowchart"
  ```mermaid
  graph TB
  subgraph Init
    A[Start] --> B[Load Sales Data]
  end

  subgraph Checks
    B --> C1[Expected schema]
    B --> C2[Exists in]
    B --> C3[Between times]
    B --> C4[Satisfies expression]

    C1 -->|Invalid| E1[Expected schema anomaly]
    C2 -->|Invalid| E2[Exists in anomaly]
    C3 -->|Invalid| E3[Between times anomaly]
    C4 -->|Invalid| E4[Satisfies expression anomaly]
  end

  subgraph End

    E1 --> J[Finish]
    E2 --> J[Finish]
    E3 --> J[Finish]
    E4 --> J[Finish]
  end

  ```

