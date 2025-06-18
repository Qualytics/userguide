# Quality Scores

Quality Scores are quantified measures of data quality calculated at the field and [container](https://userguide.qualytics.io/glossary/#container) levels, recorded as time-series to enable tracking of changes over time.
Scores range from 0-100 with higher values indicating superior quality for the intended purpose. These scores integrate eight distinct factors,
providing a granular analysis of the attributes that impact the overall data quality.

!!! Important
    A data asset's quality score is **a measure of its fitness for the intended use case**. It is not a simple measure of error, but instead a holistic confidence measure that considers the eight fundamental factors of data quality as described below.  Quality scores are dynamic and will evolve as your data and business needs change over time.


## Quality Scoring a Field

Each field receives a total quality score based on eight key factors each evaluated on a 0-100 scale. The overall score
is a composite reflecting the relative importance and [configured weights](#most-impactful-factors) of these factors:

- **Completeness**: Measures the percentage of non-null values in a field across all records. For example, if a "phone_number" field has values present in 90 out of 100 records, its completeness score would be 90%.
- **Coverage**: Evaluates whether appropriate quality rules and checks are in place to monitor the field's quality. By default, Qualytics expects at least three checks for each field.
- **Conformity**: Measures how well the data adheres to specified formats, patterns, and business rules. For example, checking if dates follow the required format (YYYY-MM-DD) or if phone numbers match the expected pattern. The rule types that measure conformity are listed below.
- **Consistency**: Ensures uniformity in type and scale across all data representations. Verifies that data maintains the same type and representation over time. For example, ensuring that a typed numeric column does not change over time to a string.
- **Precision**: Evaluates the resolution of field values against defined quality checks. The rule types that measure precision are listed below.
- **Timeliness**: Gauges data availability according to schedule inheriting the container's timeliness. This is explicitly measured as the percentage of time that a table does not adhere to its defined volumetric checks.
- **Volumetrics**: Analyzes consistency in data size and shape over time inheriting the container's volumetrics. This is measured as the ratio of records scanned to volumetric anomalies. The rule types that measure volumetrics are listed below.
- **Accuracy**: Determines the fidelity of field values to their real-world counterparts. This is the ratio of records scanned to anomalies detected on the field for any check (regardless of rule type).

## Quality Scoring a Container

A container is any structured data entity such as a table or file that comprises multiple fields. Containers are
scored using the same eight factors with each factor's score derived from a weighted average across its fields.
Additional container-specific metrics also influence the total quality score:

- **Shape anomaly adjustments**
- **Volumetric checks**
- **Scanning frequency**
- **Profiling frequency**
- **Timeliness assessments through Freshness SLA**
- **Impact of Freshness SLA violations**
- **Tags & respective weight adjustments of each field**

### Most Impactful Factors
While the specific weights [can be configured](#customizing-quality-score-weights-and-decay-time) based on your use case, in general the factors that most heavily influence quality scores are:

- Coverage - Applying frequent, comprehensive quality checks is critical.
- Accuracy - Large volumes of anomalies or pattern violations severely impact scores.
- Completeness - Significant null rates are a major detractor, especially for key fields.
- Consistency - Erratic or unstable data characteristics over time reduce confidence.
- Timeliness - Stale or temporally skewed data can undermine many use cases.

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


## How to Interpret and Use Quality Scores

Quality scores are dynamic measures of confidence that reflect the intrinsic quality of your data. It's important to recognize that different types of data will have varying levels of inherent quality. To illustrate this point, let's consider a standard mailing address in the USA. A typical schema representing a mailing address includes fields such as:

- Addressee
- Street
- Street 2
- City
- State
- Postal Code

The "State" field, which is naturally constrained by a limited set of known values, will inherently have a higher level of quality compared to the "Street 2" field. "Street 2" typically holds free-form text ranging from secondary unit designations to "care of" instructions and may often be left blank. In contrast, "State" is a required field for any valid mailing address.

Consider the level of confidence you would have in making business decisions based on the values held in the "State" field versus the "Street 2" field. This thought exercise demonstrates how the Qualytics Quality Score (with default configuration) should be interpreted.

While there are steps you can take to improve the quality score of the "Street 2" field, it would be unrealistic to expect it to meet the same standards as the "State" field. Instead, your efforts should focus on the change in measured quality score over time, with the goal of raising scores to an acceptable level of quality that meets your specific business needs.

To further explore how to respond to Quality Scores, let's consider the business requirements for capturing "Street 2" and its downstream use:

- If the primary use case for this address is to support credit card payment processing, where "Street 2" is rarely, if ever, considered, there may be no business need to focus on improving the quality of this field over time. In this case, you can reduce the impact of this field on the overall measured quality of the Address by applying a Tag with a negative weight modifier.

- On the other hand, if the primary use case for this address is to reliably ship a physical product to an intended recipient, ensuring a higher level of quality for the "Street 2" field becomes necessary. In this scenario, you may take actions such as defining additional data quality checks for the field, increasing the frequency of profiling and scanning, establishing a completeness goal, and working with upstream systems to enforce it over time.

!!! Important
    The key to effectively adopting Qualytics's Quality Scores into your data quality management efforts is to understand that it reflects both the intrinsic quality of the data and the steps taken to improve confidence that the data is fit for your specific business needs.


## Customizing Quality Score Weights and Decay Time

The default quality score weightings and decay time represent best practice considerations as codified by the data quality experts at Qualytics and our work with enterprises of all shapes, sizes, and sectors.
We recommend that both be left in their default state for all customers and use cases.

That said, we recognize that customers may desire to alter our default scoring algorithms for a variety of reasons, and we support that optionality by allowing administrators to tailor the impact of each quality factor on the total score by adjusting their weights.
This alters the scoring algorithm to align with customized governance priorities. Additionally, the decay period for considering past
data events defaults to 180 days but can be customized to fit your operational needs, ensuring the scores reflect the most relevant data quality insights for your organization.
