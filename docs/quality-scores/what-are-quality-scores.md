# Quality Scores

Quality Scores are quantified measures of data quality calculated at the field
and [container](https://userguide.qualytics.io/glossary/#container) levels recorded as time-series to enable tracking of changes over time.
Scores range from 0-100 with higher values indicating superior quality. These scores integrate eight distinct factors
providing a granular analysis of the attributes that impact the overall data quality.

## Quality Scoring a Field

Each field receives a total quality score based on eight key factors each evaluated on a 0-100 scale. The overall score
is a composite reflecting the relative importance and configured weights of these factors:

- **Completeness**: Measures the average completeness of a field across all profiles.
- **Coverage**: Assesses the adequacy of data quality checks for the field.
- **Conformity**: Checks alignment with standards defined by quality checks.
- **Consistency**: Ensures uniformity in type and scale across all data representations.
- **Precision**: Evaluates the resolution of field values against defined quality checks.
- **Timeliness**: Gauges data availability according to schedule inheriting the container's timeliness.
- **Volumetrics**: Analyzes consistency in data size and shape over time inheriting the container's volumetrics.
- **Accuracy**: Determines the fidelity of field values to their real-world counterparts.

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
