# Computed Fields Overview

In the Qualytics Data Quality platform, you can enhance your data analysis by creating computed fields. These fields allow you to apply transformations and custom transformations to your data dynamically.

## How to Create a Computed Field

**Step 1**: Access the specific Container from your Datastore. Click on `Add` and `Computed Field` to create a new computed field.
    
![Screenshot](../assets/container/computed-field/add-computed-field-light.png#only-light){: style="width:640px"}
![Screenshot](../assets/container/computed-field/add-computed-field-dark.png#only-dark){: style="width:640px"}

**Step 2**: Specify the information of the computed field:

![Screenshot](../assets/container/computed-field/transformation-type-options-light.png#only-light)
![Screenshot](../assets/container/computed-field/transformation-type-options-dark.png#only-dark)

| REF. | FIELDS | ACTIONS |
|------|--------|---------|
| 1.   | Field Name (Required) | Add a unique name for your computed field. |
| 2.   | Transformation Type (Required) |The type of transformation you want to apply from the available options. |

### Types of Transformations

#### Cleaned Entity Name

This transformation removes common business signifiers from entity names, making your data cleaner and more uniform.

##### Options for Cleaned Entity Name

| REF. | FIELDS | ACTIONS |
|------|--------|---------|
| 1.   | **Drop from Suffix** | Add a unique name for your computed field. |
| 2.   | **Drop from Prefix** | Removes specified terms from the beginning of the entity name. |
| 3.   | **Drop from Interior** | Removes specified terms from the beginning of the entity name. |
| 4.   | **Additional Terms to Drop** (Custom) | Allows you to specify additional terms that should be dropped from the entity name. |
| 5.   | **Terms to Ignore** (Custom) | Designate terms that should be ignored during the cleaning process. |

##### Example for Cleaned Entity Name

| **Example** | **Input**                  | **Transformation**             | **Output**               |
|-------------|----------------------------|--------------------------------|--------------------------|
| 1           | "TechCorp, Inc."           | **Drop from Suffix**: "Inc."   | "TechCorp"               |
| 2           | "Global Services Ltd."     | **Drop from Prefix**: "Global" | "Services Ltd."          |
| 3           | "Central LTD & Finance Co."      | **Drop from Interior**: "LTD"    | "Central & Finance Co."     |
| 4           | "Eat & Drink LLC"          | **Additional Terms to Drop**: "LLC", "&" | "Eat Drink" |
| 5           | "ProNet Solutions Ltd."    | **Terms to Ignore**: "Ltd."    | "ProNet Solutions"       |

#### Convert Formatted Numeric

This transformation converts formatted numeric values into a plain numeric format, stripping out any characters like commas or parentheses that are not numerically significant.


##### Example for Convert Formatted Numeric

| **Example** | **Input**                  | **Transformation**                              | **Output**               |
|-------------|----------------------------|-------------------------------------------------|--------------------------|
| 1           | "$1,234.56"                | **Remove non-numeric characters**: ",", "$"     | "1234.56"                |
| 2           | "(2020)"                   | **Remove non-numeric characters**: "(", ")"     | "-2020"                   |
| 3           | "100%"                     | **Remove non-numeric characters**: "%"          | "100"      


#### Custom Expression

Enables the creation of a field based on a custom computation using Spark SQL. This is useful for applying complex logic or transformations that are not covered by other types.

##### Using Custom Expression:
   You can combine multiple fields, apply conditional logic, or use any valid Spark SQL functions to derive your new computed field.
   
   Example: To create a field that sums two existing fields, you could use the expression `SUM(field1, field2)`.

##### Example for Custom Expression

| **Example** | **Input Fields**           | **Custom Expression**                           | **Output**               |
|-------------|----------------------------|-------------------------------------------------|--------------------------|
| 1           | `field1 = 10`, `field2 = 20` | `SUM(field1, field2)`                          | `30`                     |
| 2           | `salary = 50000`, `bonus = 5000` | `salary + bonus`                              | `55000`                  |
| 3           | `hours = 8`, `rate = 15.50` | `hours * rate`                                  | `124`                    |
| 4           | `status = 'active'`, `score = 85` | `CASE WHEN status = 'active' THEN score ELSE 0 END` | `85` |
