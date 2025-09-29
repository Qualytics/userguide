# Quality Scores

Quality Scores are quantified measures of data quality calculated at the field and [container](https://userguide.qualytics.io/glossary/#container) levels, recorded as time-series to enable tracking of changes over time.
Scores range from 0-100 with higher values indicating superior quality for the intended purpose. These scores integrate eight distinct dimensions,
providing a granular analysis of the attributes that impact the overall data quality. The overall score
is a composite reflecting the relative importance and [configured weights](#most-impactful-factors) of these factors:

- **Completeness**: Measures the average percentage of non-null values in a field throughout the measurement period. For example, if a "phone_number" field has values present in 90 out of 100 records, its completeness score for the measurement would be 90%.
- **Coverage**: Measures the number of quality checks defined for monitoring the field's quality. 
- **Conformity**: Measures how well the data adheres to specified formats, patterns, and business rules. For example, checking if dates follow the required format (YYYY-MM-DD) or if phone numbers match the expected pattern.<br>_<span class="text-sm">See [Appendix: Dimension Rule Types](#conformity-rule-types) for the full Conformity rule type list.</span>_
- **Consistency**: Measures uniformity in type and scale across all data representations. Verifies that data maintains the same type and representation over time. For example, ensuring that a typed numeric column does not change over time to a string.
- **Precision**: Evaluates the resolution of field values against defined quality checks.<br>_<span class="text-sm">See [Appendix: Dimension Rule Types](#precision-rule-types) for the full Precision rule type list.</span>_
- **Timeliness**: Gauges data availability according to schedule.<br><span class="text-sm">_See [Appendix: Dimension Rule Types](#timeliness-rule-types) for the full Timeliness rule type list._</span>
- **Volumetrics**: Analyzes consistency in data size and shape over time.<br><span class="text-sm">_See [Appendix: Dimension Rule Types](#volumetric-rule-types) for the full Volumetrics rule type list._</span>
- **Accuracy**: Determines the fidelity of field values to their real-world counterparts or expected values. 

### How Completeness, Precision, and Accuracy Differ

| Dimension    | Focus | Example Question It Answers                                                     |
|--------------|-------|---------------------------------------------------------------------------------|
| **Completeness** | Are values present? | What % of rows in `phone_number` are non-null?                                  |
| **Precision**    | Are values within the expected level of detail or granularity? | Are all `age` values between 0–120? Do decimals have required 2-digit precision? |
| **Accuracy**     | Are values correct compared to real-world truth or integrity checks? | Is the relationship between `square_footage` and `price` maintained?            |

!!! Important
    A data asset's quality score is **a measure of its fitness for the intended use case**. It is not a simple measure of error, but instead a holistic confidence measure that considers the eight fundamental dimensions of data quality as described below.  Quality scores are dynamic and will evolve as your data and business needs change over time.

## Field-Level Quality Scoring

Each field receives individual scores for eight quality dimensions, each evaluated on a 0-100 scale.

### Completeness Dimension

The **Completeness** score measures the average percentage of non-null values in a field over the measurement period.

**How Completeness is Calculated**

- **Scale**: 0 to 100, representing the average completeness percentage
- **Measurement period**: Defined by the configured decay time (default 180 days)
- **Formula**: Average of `(non-null values / total records) × 100` across all measurements in the period
- **Example**: If a "phone_number" field averages 90% completeness over the measurement period, its completeness score would be 90

### Coverage Dimension

The **Coverage** score measures how many distinct quality checks have been applied to a field. It is designed to reward the first few checks heavily, then taper off as more checks are added, following a curve of diminishing returns.

**How Coverage is Calculated**

- **Scale**: The score ranges continuously from 0 to 100
- **Anchor points**:
    - **0 checks** → score of **0**
    - **1 check** → score of approximately **60**
- **Diminishing returns**: Each additional check contributes less than the previous one. As the number of checks grows, the score approaches 100 but never exceeds it

Mathematically, the scoring curve follows an exponential growth model:
```
score(n) = 100 × (1 - e^(-k × n))
```
where n is the number of checks and k is tuned so that 1 check = 60.

**Why This Model?**

- **Strong early reward**: The first check dramatically increases confidence in field coverage
- **Fair balance**: More checks always improve the score, but the improvement diminishes as coverage becomes robust, preventing runaway inflation

!!! note "Field vs. Container Coverage"
    At the **field level**, Coverage reflects the **number of distinct quality checks** defined for that field.  
    At the **container level**, Coverage is an **aggregate of field-level coverage scores**, further adjusted by **scan frequency** (more frequent scans → greater confidence).

### Conformity Dimension

The **Conformity** score measures how well the data adheres to specified formats, patterns, and business rules.

**How Conformity is Calculated**

- **Scale**: 0 to 100 based on the ratio of conforming values
- **Formula**: `(1 - (rows with anomalous values as specified by conformity checks / min(scanned rows, container rows))) × 100`
- **Denominator**: Uses the smaller of scanned row count or container row count to prevent score inflation
- **Applicable rule types**: Pattern matching, length constraints, type validation, schema expectations, and format-specific validations (_See [Appendix: Dimension Rule Types](#appendix-dimension-rule-types) for the full Conformity rule type list._)

**Examples**

- Email field where 95% of scanned/total rows match valid email pattern → **Score ~95**
- Date field with consistent YYYY-MM-DD format → **Score ~100**
- Phone field with mixed formats and invalid entries → **Score ~60**

### Consistency Dimension

The **Consistency** score measures how stable a field's values remain over time compared to their expected statistical profile. This highlights fields that are "drifting" (changing shape, format, or density).

**How Consistency is Calculated**

1. **Check for type changes**
    - If a field flips between types (e.g., sometimes a number, sometimes a string), score is set to **0**

2. **Collect summary statistics** per field type:
    - **Numeric fields**: median and interquartile range (IQR)
    - **String fields**: distinct count, min/max length, Shannon entropy
    - **Datetime fields**: earliest timestamp, distinct timestamp count

3. **Measure stability**
    - Track variation of each statistic across the analysis window
    - Normalize changes for fair comparison across different scales

4. **Apply thresholds and weights**
    - Each change type has an expected tolerance (e.g., ±10% for numeric medians)
    - Variations within tolerance incur little/no penalty
    - Larger variations reduce the score proportionally

5. **Combine into final score**
    - **100**: Field stayed fully consistent
    - **60-90**: Mild to moderate changes worth monitoring
    - **Below 60**: Meaningful shift requiring investigation
    - **0**: Type change detected

!!! important "Consistency vs. Accuracy"
    **Consistency** checks whether a field’s **statistical shape and distribution remain stable over time** (e.g., numeric medians, string entropy).
    
    **Accuracy**, by contrast, evaluates whether values are **correct and aligned to real-world truths or integrity rules**.

    Together, they capture different aspects of trustworthiness.

    **Examples**

    - Numeric "Price" field with stable median and IQR → **Score ~100**
    - String "Country" field where distinct values double unexpectedly → **Score ~75**
    - Datetime field with sudden two-year backfill → **Score ~60**
    - ID field alternating between numeric and string types → **Score = 0**

### Precision Dimension

The **Precision** score evaluates the resolution and granularity of field values against defined quality checks.

**How Precision is Calculated**

- **Scale**: 0 to 100 based on the ratio of values meeting precision requirements
- **Formula**: `(1 - (rows with anomalous values as specified by precision checks / min(scanned rows, container rows))) × 100`
- **Denominator**: Uses the smaller of scanned row count or container row count to prevent score inflation
- **Applicable rule types**: Range validations, comparisons, mathematical constraints, and temporal boundaries (_See [Appendix: Dimension Rule Types](#appendix-dimension-rule-types) for the full Conformity rule type list._)

**Examples**

- Decimal field maintaining required 2-digit precision → **Score ~100**
- Timestamp field with appropriate granularity (no future dates) → **Score ~95**
- Age field with values outside valid range (0-120) → **Score ~85**

### Accuracy Dimension

The **Accuracy** score determines the fidelity of field values to their real-world counterparts or expected values.

**How Accuracy is Calculated**

- **Scale**: 0 to 100 based on the overall anomaly rate across all data integrity (excludes metadata checks like schema, volume, freshness, etc..) check types
- **Formula**: `(1 - (rows with anomalous values as specified by accuracy checks / min(scanned rows, container rows))) × 100`
- **Denominator**: Uses the smaller of scanned row count or container row count to prevent score inflation
- **Comprehensive**: Considers anomalies from all data integrity rule types
- **Represents**: Overall correctness and trustworthiness of the field data

**Interpretation**

- **95-100**: Highly accurate data suitable for critical decisions
- **80-94**: Generally reliable with some known issues
- **60-79**: Moderate accuracy requiring validation for important uses
- **Below 60**: Significant accuracy concerns requiring remediation

### Timeliness & Volumetrics Dimensions

Both the **Timeliness** and **Volumetrics** dimensions are measured at the container level as described below. Field-level scores are inherited from their container-level scores.


## Container-Level Quality Scoring

A container (table, view, file, or other structured data asset or any aggregation of data assets such as assets that share a common tag) receives an overall quality score derived from its constituent fields and additional container-specific metrics.

### How Container Scores Are Calculated

Your container's total Quality Score starts at a **baseline of 70**. Each of the eight data quality dimensions then adjusts this baseline:

- **Dimension aggregation**:
    - **Completeness**: Weighted average of all field completeness scores
    - **Coverage**: Weighted average of field coverage scores, adjusted for scan frequency
    - **Conformity**: Weighted average of field conformity scores, adjusted for schema-level conformity checks
    - **Consistency**: Weighted average of field consistency scores, adjusted for profiling frequency
    - **Precision**: Weighted average of field precision scores
    - **Accuracy**: Weighted average of field accuracy scores
    - **Timeliness**: Calculated using process described below
    - **Volumetrics**: Calculated using process described below
- **Proportional adjustment**: Each dimension adjusts the score proportionally to its 0–100 rating
- **Influence capping**: Every dimension has maximum positive and negative impact limits
- **Weight controls**: Higher weights make dimensions more influential; zero weight removes effect entirely
- **Missing value handling**: Documented defaults substitute for unmeasurable dimensions
- **Special case**: If only one dimension is weighted, the Quality Score mirrors that dimension's rating
- **Final clipping**: Result is always constrained between 0 and 100

!!! note "Why a 70-Point Baseline?"
    The **70-point baseline** represents a **neutral confidence starting point**.

    - Dimensions then adjust the baseline **downward** when issues are found or **upward** when strong quality signals exist.
    - This calibration ensures that new containers without extensive checks or history begin from a reasonable midpoint rather than 0.

### Timeliness Dimension

The **Timeliness** score gauges whether data is available according to its expected schedule.

**How Timeliness is Calculated**

- **Scale**: 0 to 100 based on adherence to freshness requirements
- **Field level**: Directly inherited from the container's timeliness score
- **Anomaly counting**: Counts distinct anomalies from the relevant check types within the measurement period (cutoff date)
- **Formula (container)**: Scores start at 100 and decrease based on anomaly count
    - First anomaly causes a 40-point drop (score becomes 60)
    - Each additional anomaly has diminishing impact
    - Formula: `Score = 100 - min(100 × (1 - e^(-k × anomaly_count)), 100)`
    - Where k is calibrated so one anomaly = 40% score reduction
- **Applicable rule types**: Time distribution size, freshness constraints (_See [Appendix: Dimension Rule Types](#appendix-dimension-rule-types) for the full Conformity rule type list._)

**Score Interpretation**

- **100**: No timeliness anomalies detected
- **60**: One anomaly detected (40-point penalty)
- **40-60**: Multiple anomalies with diminishing penalties
- **0-40**: Significant anomaly counts indicating serious issues
- **None/Null**: No checks of this type configured (unmeasured)

### Volumetrics Dimension

The **Volumetrics** score analyzes consistency in data size and shape over time.

!!! note "Shared Scoring Formula"
    Timeliness and Volumetrics both use the **same exponential penalty formula** for anomaly counts.  
    This consistency ensures comparable scoring behavior across dimensions, even though the anomalies being measured differ.

**How Volumetrics is Calculated**

- **Scale**: 0 to 100 based on volumetric stability
- **Field level**: Directly inherited from the container's volumetrics score
- **Anomaly counting**: Counts distinct anomalies from the relevant check types within the measurement period (cutoff date)
- **Formula (container)**: Scores start at 100 and decrease based on anomaly count
    - First anomaly causes a 40-point drop (score becomes 60)
    - Each additional anomaly has diminishing impact
    - Formula: `Score = 100 - min(100 × (1 - e^(-k × anomaly_count)), 100)`
    - Where k is calibrated so one anomaly = 40% score reduction
- **Applicable rule types**: Row count size, partition size constraints (_See [Appendix: Dimension Rule Types](#appendix-dimension-rule-types) for the full Conformity rule type list._)

**Examples**

- Container with consistent record counts per partition → **Score ~100**
- Container showing unexpected spikes or drops in volume → **Score ~75**
- Container with erratic or missing time distributions → **Score ~50**


### Additional Container-Level Factors

Beyond the eight dimensions, containers incorporate:

- **Scanning frequency**: More frequent scanning improves confidence and boosts coverage scores
- **Profiling frequency**: Regular profiling ensures statistics remain current and boosts consistency scores
- **Field tag weights**: Field weights are used when calculated weighted averages for container-level dimensions

### Most Impactful Dimensions

While specific scoring weights [can be customized](#customizing-quality-score-weights-and-decay-time), dimensions that typically most influence quality scores are:

- **Coverage**: Asserting frequent, comprehensive quality checks is critical
- **Accuracy**: Large volumes of anomalies severely impact scores
- **Consistency**: Erratic or unstable data characteristics reduce confidence

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

!!! note "Fitness for Purpose in Practice"
    Remember: Quality Scores are not absolute “grades.”  
    They reflect **how well your data is suited for its intended business use**, influenced by weighting, tagging, and anomaly detection.  
    Two datasets may have different scores but still both be "fit for purpose" depending on use case.

## Customizing Quality Score Weights and Decay Time

The default quality score weightings and decay time represent best practice considerations as codified by the data quality experts at Qualytics and our work with enterprises of all shapes, sizes, and sectors.
We recommend that both be left in their default state for all customers and use cases.

That said, we recognize that customers may desire to alter our default scoring algorithms for a variety of reasons, and we support that optionality by allowing administrators to tailor the impact of each quality dimension on the total score by adjusting their weights.
This alters the scoring algorithm to align with customized governance priorities. Additionally, the decay period for considering past
data events defaults to 180 days but can be customized to fit your operational needs, ensuring the scores reflect the most relevant data quality insights for your organization.

!!! warning "Use Caution When Customizing Weights"
    We strongly recommend retaining default weights unless governance priorities **clearly justify changes**.

    - Adjusting weights can significantly alter how anomalies impact overall scores.
    - Misaligned weights may cause misleading signals about data quality.  
    
    Proceed carefully, and document any custom weighting rationale.


## Appendix: Dimension Rule Types

The following lists summarize which rule types contribute to each dimension’s quality score.  

---

### Conformity Rule Types

| No. | Rule Type |
| :---- | :---- |
| 1. | Matches Pattern |
| 2. | Min Length |
| 3. | Max Length |
| 4. | Data Diff |
| 5. | Is Type |
| 6. | Entity Resolution |
| 7. | Expected Schema |
| 8. | Field Count |
| 9. | Is Credit Card |
| 10. | Is Address |
| 11. | Contains Credit Card |
| 12. | Contains URL |
| 13. | Contains Email |
| 14. | Contains Social Security Number |

### Precision Rule Types

| No. | Rule Type |
| :---- | :---- |
| 1. | After Date Time |
| 2. | Before Date Time |
| 3. | Between |
| 4. | Between Times |
| 5. | Equal To |
| 6. | Equal To Field |
| 7. | Greater Than |
| 8. | Greater Than Field |
| 9. | Less Than |
| 10. | Less Than Field |
| 11. | Max Value |
| 12. | Min Value |
| 13. | Not Future |
| 14. | Not Negative |
| 15. | Positive |
| 16. | Predicted By |
| 17. | Sum |

### Volumetric Rule Types

| No. | Rule Type |
| :---- | :---- |
| 1. | Volumetric |
| 2. | Min Partition Size |
| 3. | Max Partition Size |

### Timeliness Rule Types

| No. | Rule Type |
| :---- | :---- |
| 1. | Freshness |
| 2. | Time Distribution Size |
