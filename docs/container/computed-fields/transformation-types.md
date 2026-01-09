# Types of Transformations

## Cast

The **Cast** transformation converts field values to a specified target data type using Spark SQL casting rules. This is commonly used when a field is ingested as a string but must behave as a numeric, date, timestamp, or boolean value for profiling, checks, or downstream computations.

### When to Use Cast

Use **Cast** when:

- A numeric field is ingested as a string (for example, `"1000"` instead of `1000`)
- Dates or timestamps need explicit typing
- Boolean logic is required on string values
- Quality checks or aggregations require strict data types

### Options for Cast

| REF. | FIELD | WHAT IT MEANS |
|-----|------|----------------|
| 1 | **Name** | A clear, descriptive name for the new computed field you are creating. |
| 2 | **Transformation Type** | Choose **Cast** to convert the data type of an existing field. |
| 3 | **Field** | The existing column whose values you want to convert into another data type. |
| 4 | **Target Type** | The data type you want the field to become (for example: number, date, timestamp, decimal, or boolean). |
| 5 | **Format** | Optional, Used only when converting text into dates or timestamps, so the system knows how to read the date format correctly. |
| 6 | **Additional Metadata** | Optional information you can attach to the field to provide extra context or documentation. |

### Target Type Examples

| **Input Value** | **Target Type** | **Result** |
|----------------|---------------|------------|
| `"1000"` | `int` | `1000` |
| `"1234.56"` | `decimal(10,2)` | `1234.56` |
| `"true"` | `boolean` | `true` |
| `"2023-12-31"` | `date` | `2023-12-31` |

### Format Examples (Date / Timestamp Casting)

The **Format** field is only required when casting string values into `date` or `timestamp`.

Common examples:

| **Format Pattern** | **Example Input** |
|-------------------|------------------|
| `MM/dd/yyyy` | `12/31/2023` |
| `dd/MM/yyyy` | `31/12/2023` |
| `yyyy-MM-dd HH:mm:ss` | `2023-12-31 14:30:00` |

### Practical Use Case

A field such as **BUSINESS_ID** or **Transaction_Amount** is ingested as a string due to upstream system constraints. By applying a **Cast** transformation, the field becomes properly typed—enabling accurate aggregations, anomaly detection, and quality checks.

## Cleaned Entity Name

This transformation removes common business signifiers from entity names, making your data cleaner and more uniform.

### Options for Cleaned Entity Name

| REF. | FIELDS | ACTIONS |
|------|--------|---------|
| 1   | **Drop from Suffix** | Add a unique name for your computed field. |
| 2   | **Drop from Prefix** | Removes specified terms from the beginning of the entity name. |
| 3   | **Drop from Interior** | Removes specified terms from the beginning of the entity name. |
| 4   | **Additional Terms to Drop** (Custom) | Allows you to specify additional terms that should be dropped from the entity name. |
| 5   | **Terms to Ignore** (Custom) | Designate terms that should be ignored during the cleaning process. |

### Example for Cleaned Entity Name

| **Example** | **Input**                  | **Transformation**             | **Output**               |
|-------------|----------------------------|--------------------------------|--------------------------|
| 1           | "TechCorp, Inc."           | **Drop from Suffix**: "Inc."   | "TechCorp"               |
| 2           | "Global Services Ltd."     | **Drop from Prefix**: "Global" | "Services Ltd."          |
| 3           | "Central LTD & Finance Co."      | **Drop from Interior**: "LTD"    | "Central & Finance Co."     |
| 4           | "Eat & Drink LLC"          | **Additional Terms to Drop**: "LLC", "&" | "Eat Drink" |
| 5           | "ProNet Solutions Ltd."    | **Terms to Ignore**: "Ltd."    | "ProNet Solutions"       |

## Convert Formatted Numeric

This transformation converts formatted numeric values into a plain numeric format, stripping out any characters like commas or parentheses that are not numerically significant.

### Example for Convert Formatted Numeric

| **Example** | **Input**   | **Transformation** | **Output** |
|-------------|-------------|--------------------|------------|
| 1           | "$1,234.56" | **Remove non-numeric characters**: ",", "$" | "1234.56"  |
| 2           | "(2020)"    | **Remove non-numeric characters**: "(", ")" | "-2020"    |
| 3           | "100%"      | **Remove non-numeric characters**: "%"      | "100"      

## Custom Expression

Enables the creation of a field based on a custom computation using Spark SQL. This is useful for applying complex logic or transformations that are not covered by other types.

### Using Custom Expression:
   You can combine multiple fields, apply conditional logic, or use any valid Spark SQL functions to derive your new computed field.
   
   **Example**: To create a field that sums two existing fields, you could use the expression `SUM(field1, field2)`.

   **Advanced Example**: You need to ensure that a log of leases has no overlapping dates for an asset, but your data only captures a single lease's details like: 
   
| **LeaseID** |  **AssetID** | **Lease_Start** | **Lease_End** |
|-------------|-------------|--------------------|------------|
| 1           | 42          | 1/1/2025         |   2/1/2026    |
| 2           | 43          | 1/1/2025         |   2/1/2026    |
| 3           | 42          | 1/1/2026         |   2/1/2026    |
| 4           | 43          | 2/2/2026         |   2/1/2027    |

You can see in this example that **Lease 1** has overlapping dates with **Lease 3** for the same Asset. This can be difficult to detect without a full transformation of the data. However, we can accomplish our goal easily with a Computed Field.
We'll simply add a Computed Field to our table named **"Next_Lease_Start"** and define it with the following custom expression so that our table will now hold the new field and render it as shown below.

`LEAD(Lease_Start, 1) OVER (PARTITION BY AssetID ORDER BY Lease_Start)` 

 | **LeaseID** |  **AssetID** | **Lease_Start** | **Lease_End** | **Next_Lease_Start** |
|-------------|-------------|--------------------|------------|------------|
| 1           | 42          | 1/1/2025         |   2/1/2026    | 1/1/2026    |
| 2           | 43          | 1/1/2025         |   2/1/2026    | 2/2/2026    |
| 3           | 42          | 1/1/2026         |   2/1/2026    |             |
| 4           | 43          | 2/2/2026         |   2/1/2027    |             |

Now you can author a Quality Check stating that **Lease_End** should always be less than **"Next_Lease_Start"** to catch any errors of this type. In fact, Qualytics will automatically infer that check for you at [Level 3 Inference](../../source-datastore/profile.md#level-3-time-series-and-comparative-relationship-checks){target="_blank"}!

### More Examples for Custom Expression

| **Example** | **Input Fields**  | **Custom Expression**  | **Output**   |
|-------------|--------------|-----------------|---------------------|
| 1   | `field1 = 10`, `field2 = 20` | `SUM(field1, field2)` | `30`  |
| 2   | `salary = 50000`, `bonus = 5000` | `salary + bonus`  | `55000` |
| 3   | `hours = 8`, `rate = 15.50` | `hours * rate`         | `124`   |
| 4   | `status = 'active'`, `score = 85` | `CASE WHEN status = 'active' THEN score ELSE 0 END` | `85` |