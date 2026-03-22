# Add Computed Fields

**Step 1:** Log in to Your Qualytics Account, navigate to the side menu, and select the **source datastore** where you want to create a computed field.

![datastore](../../assets/fields/computed-fields/add-computed-fields/select-datastore.png)

**Step 2:** Select the **Container** within the chosen datastore where you want to create the computed field. This container holds the data to which the new computed field will be applied, enabling you to enhance your data analysis within that specific datastore.

For demonstration purposes, we have selected the **S3 TPCH** source datastore and the **orders/ORDERS-*.csv** container within it to create a computed field.

![container](../../assets/fields/computed-fields/add-computed-fields/select-container.png)

**Step 3:** After selecting the container, click on the **Add** button and select **Computed Field** from the dropdown menu to create a new computed field. 

![computed-field](../../assets/fields/computed-fields/add-computed-fields/computed-field-option.png)

A modal window will appear, allowing you to enter the details for your computed field. 

![add-field](../../assets/fields/computed-fields/add-computed-fields/add-field-form.png)

**Step 4:** Enter the **Name** for the computed field, select **Transformation Type** from the dropdown menu, and optionally add **Additional Metadata**.

| REF. | FIELDS | ACTION |
|------|--------|--------|
| 1 | Field Name (Required) | Add a unique name for your computed field. |
| 2 | Transformation Type (Required) | The type of transformation you want to apply from the available options. |
| 3 | Additional Metadata (Optional) | Enhance the computed field definition by setting custom metadata. Click the plus icon **(+)** to open the metadata input form and add key-value pairs. |

![fields](../../assets/fields/computed-fields/add-computed-fields/select-source-fields.png)

!!! info
    Transformations are changes made to data, like converting formats, doing calculations, or cleaning up fields. In Qualytics, you can use transformations to meet specific needs, such as cleaning entity names, converting formatted numbers, or applying custom expressions. With various transformation types available, Qualytics enables you to customize your data directly within the platform, ensuring it’s accurate and ready for analysis.

| Transformation Types | Purpose | Reference |
|------|--------|---------|
| Cast | Converts an existing field to a different data type (such as number, date, timestamp, or boolean) so it can be used correctly in checks, aggregations, and calculations. | For more information, please refer to the guide [cast section.](../computed-fields/transformation-types.md#cast){target="_blank"} |
| Cleaned Entity Name | Removes business signifiers (such as 'Inc.' or 'Corp') from an entity name. | For more information, please refer to the guide [cleaned entity name section.](../computed-fields/transformation-types.md#cleaned-entity-name){target="_blank"} |
| Convert Formatted Numeric | Removes formatting (such as parentheses for denoting negatives or commas as delimiters) from values that represent numeric data, converting them into a numerically typed field. | For more information, please refer to the guide [convert formatted numeric section.](../computed-fields/transformation-types.md#convert-formatted-numeric){target="_blank"} |
| Custom Expression | Allows you to create a new field by applying any valid Spark SQL expression to one or more existing fields. | For more information, please refer to the guide [custom expression section.](../computed-fields/transformation-types.md#custom-expression){target="_blank"} |

![transformation-type](../../assets/fields/computed-fields/add-computed-fields/select-transformation-type.png)

**Step 5:** After selecting the appropriate **Transformation Type**, click the **Save** button.

![save](../../assets/fields/computed-fields/add-computed-fields/save-computed-field.png)

**Step 6:** After clicking on the **Save** button, your computed field is created and a success flash message will display saying **The computed field has been successfully created**.

![success](../../assets/fields/computed-fields/add-computed-fields/creation-success.png)

You can find your computed field by clicking on the dropdown arrow next to the container you selected when creating the computed field.

![field-created](../../assets/fields/computed-fields/add-computed-fields/field-created.png)