# Computed Fields Details

Computed Field Details provides a quick overview of the metrics generated from a computed field. The **Totals** section summarizes the results produced by this computed field and displays a report that reflects only the data output of this specific computed field.

### Totals

**1 Quality Score**: This provides a comprehensive assessment of the overall health of the data, factoring in multiple checks for accuracy, consistency, and completeness. A higher score, closer to 100, indicates optimal data quality with minimal issues or errors detected. A lower score may highlight areas that require attention and improvement.

**2 Sampling**: This shows the percentage of data that was evaluated during profiling. A sampling rate of 100% indicates that the entire dataset was analyzed, ensuring a complete and accurate representation of the data’s quality across all records, rather than just a partial sample.  
   
**3 Completeness**: This metric measures how fully the data is populated without missing or null values. A higher completeness percentage means that most fields contain the necessary information, while a lower percentage indicates data gaps that could negatively impact downstream processes or analysis.

**4 Active Checks**: This refers to the number of ongoing quality checks being applied to the dataset. These checks monitor aspects such as format consistency, uniqueness, and logical correctness. Active checks help maintain data integrity and provide real-time alerts about potential issues that may arise.

**5 Active Anomalies**: This tracks the number of anomalies or irregularities detected in the data. These could include outliers, duplicates, or inconsistencies that deviate from expected patterns. A count of zero indicates no anomalies, while a higher count suggests that further investigation is needed to resolve potential data quality issues.

![Totals](../../assets/container/computed-fields/computed-fields-details/totals-light-9.png)

### Profile

This provides detailed insights into the characteristics of the field, including its type, distinct values, and length. You can use this information to evaluate the data's uniqueness, length consistency, and complexity.

| **No** | **Profile**           | **Description**                                                                 |
|--------|-----------------------|---------------------------------------------------------------------------------|
| 1      | Declared Type          | Indicates whether the type is declared by the source or inferred.               |
| 2      | Distinct Values        | Count of distinct values observed in the dataset.                               |
| 3      | Min Length             | Shortest length of the observed string values or lowest value for numerics.      |
| 4      | Max Length             | Greatest length of the observed string values or highest value for numerics.     |
| 5      | Mean                   | Mathematical average of the observed numeric values.                            |
| 6      | Median                 | The median of the observed numeric values.                                      |
| 7      | Standard Deviation     | Measure of the amount of variation in observed numeric values.                  |
| 8      | Kurtosis               | Measure of the ‘tailedness’ of the distribution of observed numeric values.     |
| 9      | Skewness               | Measure of the asymmetry of the distribution of observed numeric values.        |
| 10     | Q1                     | The first quartile; the central point between the minimum and the median.       |
| 11     | Q3                     | The third quartile; the central point between the median and the maximum.       |
| 12     | Sum                    | Total sum of all observed numeric values.                                       |

![Profile](../../assets/container/computed-fields/computed-fields-details/profile-light-10.png)

You can hover over the **(i)** button to view the native field properties, which provide detailed information such as the field's type (numeric), size, decimal digits, and whether it allows null values.

![Hover](../../assets/container/computed-fields/computed-fields-details/hover-light-11.png)

#### Last Profile

The **Last Profile** timestamp helps users understand how up to date the field is. When you hover over the time indicator shown on the right side of the Last Profile label (e.g., "8 months ago"), a tooltip displays the complete date and time the field was last profiled.

![last-profile](../../assets/container/computed-fields/computed-fields-details/last-profile-light.png)

This visibility ensures better context for interpreting profile metrics like mean, completeness, and anomalies.