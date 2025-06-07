# Quality Scores

Quality Scores are quantified measures of data quality calculated at the field
and [container](https://userguide.qualytics.io/glossary/#container) levels recorded as time-series to enable tracking of changes over time.
Scores range from 0-100 with higher values indicating superior quality. These scores integrate eight distinct factors
providing a granular analysis of the attributes that impact the overall data quality.

## Quality Scoring a Field

Each field receives a total quality score based on eight key factors each evaluated on a 0-100 scale. The overall score
is a composite reflecting the relative importance and configured weights of these factors:

- **Completeness**: Measures the percentage of non-null values in a field across all records. For example, if a "phone_number" field has values present in 90 out of 100 records, its completeness score would be 90%.
- **Coverage**: Evaluates whether appropriate quality rules and checks are in place to monitor the field's quality. By default, Qualytics expects at least three checks for each field.
- **Conformity**: Measures how well the data adheres to specified formats, patterns, and business rules. For example, checking if dates follow the required format (YYYY-MM-DD) or if phone numbers match the expected pattern. The rule types that measure conformity are listed below.
- **Consistency**: Ensures uniformity in type and scale across all data representations. Verifies that data maintains the same type and representation over time. For example, ensuring that a typed numeric column does not change over time to a string.
- **Precision**: Evaluates the resolution of field values against defined quality checks. The rule types that measure precision are listed below.
- **Timeliness**: Gauges data availability according to schedule inheriting the container's timeliness. This is explicitly measured as the percentage of time that a table does not adhere to its defined volumetric checks.
- **Volumetrics**: Analyzes consistency in data size and shape over time inheriting the container's volumetrics. This is measured as the ratio of records scanned to volumetric anomalies. The rule types that measure volumetrics are listed below.
- **Accuracy**: Determines the fidelity of field values to their real-world counterparts. This is the ratio of records scanned to anomalies detected on the field for any check (regardless of rule type).

## Quality Scoring a Container

A container is any structured data entity such as a table or dataframe that comprises multiple fields. Containers are
scored using the same eight factors with each factor's score derived from a weighted average across its fields.
Additional container-specific metrics also influence the total quality score:

- **Shape anomaly adjustments**
- **Volumetric checks**
- **Scanning frequency**
- **Profiling frequency**
- **Timeliness assessments through Freshness SLA**
- **Impact of Freshness SLA violations**

## Customizing Quality Score Weights and Decay Time

You can tailor the impact of each quality factor on the total score by adjusting their weights allowing the scoring
system to align with your organization’s data governance priorities. Additionally the decay period for considering past
data events defaults to 180 days but can be customized to fit your operational needs ensuring the scores reflect the
most relevant data quality insights.

### Most Impactful Factors
While the specific weights can be configured based on your use case, in general the factors that most heavily influence quality scores are:

Coverage - Applying frequent, comprehensive quality checks is critical.
Accuracy - Large volumes of anomalies or pattern violations severely impact scores.
Completeness - Significant null rates are a major detractor, especially for key fields.
Consistency - Erratic or unstable data characteristics over time reduce confidence.
Timeliness - Stale or temporally skewed data can undermine many use cases.

## Factor Impacting Rule Types

Specific check rule types are considered for factor score calculations at the field level for the following factors.

### Conformity Rule Types

```
RuleType.matchesPattern
RuleType.minLength
RuleType.maxLength
RuleType.isReplicaOf
RuleType.isType
RuleType.entityResolution
RuleType.expectedSchema
RuleType.fieldCount
RuleType.isCreditCard
RuleType.isAddress
RuleType.containsCreditCard
RuleType.containsUrl
RuleType.containsEmail
RuleType.containsSocialSecurityNumber
RuleType.minPartitionSize
RuleType.maxPartitionSize
```

### Precision Rule Types

```
RuleType.afterDateTime
RuleType.beforeDateTime
RuleType.between
RuleType.betweenTimes
RuleType.equalTo
RuleType.equalToField
RuleType.greaterThan
RuleType.greaterThanField
RuleType.lessThan
RuleType.lessThanField
RuleType.maxValue
RuleType.minValue
RuleType.notFuture
RuleType.notNegative
RuleType.positive
RuleType.predictedBy
RuleType.sum
```

### Volumetric Rule Types

```
RuleType.timeDistributionSize 
RuleType.minPartitionSize 
RuleType.maxPartitionSize
```
