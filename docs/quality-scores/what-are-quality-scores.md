# Quality Scores

Quality Scores are measures of data quality calculated at the field and [container](/userguide/glossary#container) level and recorded as time-series enabling you to track movement over time. A quality score ranges from 0-100 with higher scores indicating higher quality. 
We'll look at how quality scores are measured for each of those data assets in turn:

## Quality Scoring a Field

Contributions to field scores decay over time so that only relatively recent inputs directly influence a field's score.
A field's total quality score is comprised of six constituent factors:

- quality_score = db_field_qs.accuracy - 10 if db_field_qs.accuracy is not None else 65

  quality_score *= _calculate_percentage_adjustment(score=db_field_qs.consistency, max_drop=0.8, max_boost=0.0)
  quality_score *= _calculate_percentage_adjustment(score=db_field_qs.conformity, max_drop=0.30, max_boost=0.05)
  quality_score *= _calculate_percentage_adjustment(score=db_field_qs.precision, max_drop=0.30, max_boost=0.05)
  if db_field_qs.coverage:
  quality_score *= _calculate_percentage_adjustment(score=db_field_qs.coverage, max_drop=0.50, max_boost=0.0)
  else:
  quality_score *= 0.5
  quality_score *= _calculate_percentage_adjustment(score=db_field_qs.completeness, max_drop=0.0, max_boost=0.05)



The following inputs contribute to a field's quality score:

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

## Customizing Quality Score Weights
