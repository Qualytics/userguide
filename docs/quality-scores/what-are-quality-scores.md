# Quality Scores

Quality Scores are measures of data quality calculated at the field and [container](/userguide/glossary#container) level 
and recorded as time-series, enabling you to track movement over time. A quality score ranges from 0-100, with higher 
scores indicating higher quality. Total quality scores are comprised of eight distinct factors in support of a more 
understanding of the underlying quality aspects of your data.

## Quality Scoring a Field

A field's total quality score is comprised of eight constituent factors, each quantified on a 0-100 scale. 
The total score is then calculated from these individual factors based on their relevance and impact as well as any
configured custom weighting:

- **Completeness**: A measure of the average completeness.
- **Coverage**: Assesses whether sufficient data quality checks exist for the given field.
- **Conformity**: Checks alignment of the content to the required standards.
- **Consistency**: Ensures values are the same for all copies and representations.
- **Precision**: Verifies that the data is of the expected defined resolution.
- **Timeliness**: Evaluates if data is available when and where it is expected.
- **Volumetrics**: Analyzes if data maintains the same size and shape across similar cycles.
- **Accuracy**: Determines if the data accurately represents the real-world values.

## Quality Scoring a Container

Container quality scoring also considers these eight factors, calculated as a weighted average from all the fields 
within the container. Additionally, the following measures contribute to a container's quality score:

- **Weighted average of all its fields' factor scores**
- **Shape anomaly adjustments**
- **Volumetric checks**
- **Scanning frequency**
- **Timeliness assessments through Freshness SLA**
- **Duration and impact of Freshness SLA violations**

## Customizing Quality Score Weights

You can customize how each factor influences the total quality score by adjusting their weights according to their 
significance in your data quality framework. This customization allows you to tailor the quality scoring to better 
fit your organization’s data governance standards and operational needs.
