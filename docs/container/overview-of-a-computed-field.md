# Computed Fields

Computed Fields allow you to enhance data analysis by applying dynamic transformations directly to your data. These fields let you create new data points, perform calculations, and customize data views based on your specific needs, ensuring your data is both accurate and actionable.

Let's get started 🚀

## Add Computed Fields

**Step 1:** Log in to Your Qualytics Account, navigate to the side menu, and select the **source datastore** where you want to create a computed field.

![datastore](../assets/container/computed-field/datastore-light-1.png#only-light)
![datastore](../assets/container/computed-field/datastore-dark-1.png#only-dark)

**Step 2:** Select the **Container** within the chosen datastore where you want to create the computed field. This container holds the data to which the new computed field will be applied, enabling you to enhance your data analysis within that specific datastore.

For demonstration purposes, we have selected the **`Bank Dataset-Staging`** source datastore and the **`bank_transactions_.csv`** container within it to create a computed field.

![container](../assets/container/computed-field/container-light-2.png#only-light)
![container](../assets/container/computed-field/container-dark-2.png#only-dark)

**Step 3:** After selecting the container, click on the **Add** button and select **Computed Field** from the dropdown menu to create a new computed field. 

![computed-field](../assets/container/computed-field/computed-field-light-3.png#only-light)
![computed-field](../assets/container/computed-field/computed-field-dark-3.png#only-dark)

A modal window will appear, allowing you to enter the details for your computed field. 

![add-field](../assets/container/computed-field/add-field-light-4.png#only-light)
![add-field](../assets/container/computed-field/add-field-dark-4.png#only-dark)

**Step 4:** Enter the **Name** for the computed field and select **Transformation Type** from the dropdown menu. 

| REF. | FIELDS | ACTION |
|------|--------|--------|
| 1. | Field Name (Required) | Add a unique name for your computed field. |
| 2. | Transformation Type (Required) | The type of transformation you want to apply from the available options. |

!!! info
    Transformations are changes made to data, like converting formats, doing calculations, or cleaning up fields. In Qualytics, you can use transformations to meet specific needs, such as cleaning entity names, converting formatted numbers, or applying custom expressions. With various transformation types available, Qualytics enables you to customize your data directly within the platform, ensuring it’s accurate and ready for analysis. 


| Transformation Types | Purpose | Reference |
|------|--------|---------|
| Cleaned Entity Name | Removes business signifiers (such as 'Inc.' or 'Corp') from an entity name. | [See here](#cleaned-entity-name) |
| Convert Formatted Numeric | Removes formatting (such as parentheses for denoting negatives or commas as delimiters) from values that represent numeric data, converting them into a numerically typed field. | [See here](#convert-formatted-numeric) |
| Custom Expression | Allows you to create a new field by applying any valid Spark SQL expression to one or more existing fields. | [See here](#custom-expression) |

![transformation-type](../assets/container/computed-field/transformation-type-light-5.png#only-light)
![transformation-type](../assets/container/computed-field/transformation-type-dark-5.png#only-dark)

**Step 5:** After selecting the appropriate **Transformation Type**, click the **Save** button.

![save](../assets/container/computed-field/save-light-6.png#only-light)
![save](../assets/container/computed-field/save-dark-6.png#only-dark)

**Step 6:** After clicking on the **Save** button, your computed field is created and a success flash message will display saying **A computed field has been created successfully**.

![success](../assets/container/computed-field/success-light-7.png#only-light)
![success](../assets/container/computed-field/success-dark-7.png#only-dark)

You can find your computed field by clicking on the dropdown arrow next to the container you selected when creating the computed field.

![field-created](../assets/container/computed-field/field-created-light-8.png#only-light)
![field-created](../assets/container/computed-field/field-created-dark-8.png#only-dark)

## Types of Transformations

### Cleaned Entity Name

This transformation removes common business signifiers from entity names, making your data cleaner and more uniform.

#### Options for Cleaned Entity Name

| REF. | FIELDS | ACTIONS |
|------|--------|---------|
| 1.   | **Drop from Suffix** | Add a unique name for your computed field. |
| 2.   | **Drop from Prefix** | Removes specified terms from the beginning of the entity name. |
| 3.   | **Drop from Interior** | Removes specified terms from the beginning of the entity name. |
| 4.   | **Additional Terms to Drop** (Custom) | Allows you to specify additional terms that should be dropped from the entity name. |
| 5.   | **Terms to Ignore** (Custom) | Designate terms that should be ignored during the cleaning process. |

#### Example for Cleaned Entity Name

| **Example** | **Input**                  | **Transformation**             | **Output**               |
|-------------|----------------------------|--------------------------------|--------------------------|
| 1           | "TechCorp, Inc."           | **Drop from Suffix**: "Inc."   | "TechCorp"               |
| 2           | "Global Services Ltd."     | **Drop from Prefix**: "Global" | "Services Ltd."          |
| 3           | "Central LTD & Finance Co."      | **Drop from Interior**: "LTD"    | "Central & Finance Co."     |
| 4           | "Eat & Drink LLC"          | **Additional Terms to Drop**: "LLC", "&" | "Eat Drink" |
| 5           | "ProNet Solutions Ltd."    | **Terms to Ignore**: "Ltd."    | "ProNet Solutions"       |

### Convert Formatted Numeric

This transformation converts formatted numeric values into a plain numeric format, stripping out any characters like commas or parentheses that are not numerically significant.


#### Example for Convert Formatted Numeric

| **Example** | **Input**   | **Transformation** | **Output** |
|-------------|-------------|--------------------|------------|
| 1           | "$1,234.56" | **Remove non-numeric characters**: ",", "$" | "1234.56"  |
| 2           | "(2020)"    | **Remove non-numeric characters**: "(", ")" | "-2020"    |
| 3           | "100%"      | **Remove non-numeric characters**: "%"      | "100"      

### Custom Expression

Enables the creation of a field based on a custom computation using Spark SQL. This is useful for applying complex logic or transformations that are not covered by other types.

#### Using Custom Expression:
   You can combine multiple fields, apply conditional logic, or use any valid Spark SQL functions to derive your new computed field.
   
   Example: To create a field that sums two existing fields, you could use the expression `SUM(field1, field2)`.

#### Example for Custom Expression

| **Example** | **Input Fields**  | **Custom Expression**  | **Output**   |
|-------------|--------------|-----------------|---------------------|
| 1   | `field1 = 10`, `field2 = 20` | `SUM(field1, field2)` | `30`  |
| 2   | `salary = 50000`, `bonus = 5000` | `salary + bonus`  | `55000` |
| 3   | `hours = 8`, `rate = 15.50` | `hours * rate`         | `124`   |
| 4           | `status = 'active'`, `score = 85` | `CASE WHEN status = 'active' THEN score ELSE 0 END` | `85` |
