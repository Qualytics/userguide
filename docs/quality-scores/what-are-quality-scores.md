# What are Quality Scores?

Quality Scores are measures of data quality calculated at the field, [container](/userguide/glossary#container), and [datastore](/userguide/glossary#datastore) level and recorded as time-series enabling you to track movement over time. A quality score ranges from 0-100 with higher scores indicating higher quality. We'll look at how quality scores are measured for each of those data assets in turn:

## Quality Scoring a Field

Contributions to field scores decay over time so that only relatively recent inputs directly influence a field's score. The following inputs contribute to a field's quality score:

- its ratio of valid record anomalies to records
- whether it is checked for expected completeness
- the number other checks defined for it
- its consistency

## Quality Scoring a Container

Contributions to container scores decay over time so that only relatively recent inputs directly influence a container's score. The following inputs contribute to a container's quality score:

- the mean of all its fields' scores
- its ratio of valid shape anomalies to records
- whether it is checked for expected volumetrics
- the frequency with which it is scanned
- whether it has a Freshness SLA defined
- the duration of any Freshness SLA violations

## Quality Scoring a Datastore

Contributions to datastore scores decay over time so that only relatively recent inputs directly influence a datastore's score. A datastore's quality score is the simple mean of its containers' scores.
