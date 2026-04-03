# Datastore Quality Score FAQ

Answers to common questions about data quality scores on source datastores in Qualytics.

## General

### What is a Data Quality Score?

A Data Quality Score is a quantified measure (0–100) that reflects the health of your data. Higher scores indicate superior quality. Scores are calculated at the field, container, and datastore levels, and recorded as time series so you can track changes over time.

### How is the datastore-level quality score calculated?

The datastore score is the **weighted average** of all container scores within the datastore. Only containers that have been scanned are included. Container weights can be influenced by tag weight modifiers.

### How is the container-level quality score calculated?

Each container score is calculated using a **multiplicative baseline model** starting from a baseline of 70. The 8 quality dimensions each contribute a multiplicative adjustment factor proportional to their configured weight, resulting in a final score between 0 and 100.

### Why does the model start from a baseline of 70?

The baseline of 70 represents a "neutral starting point" — a container with no anomalies and default profiles receives a score around 70. Each dimension can then pull the score down (if issues exist) or push it slightly up (if the dimension is exceptionally clean). This baseline is **not configurable** — it is a fixed constant in the scoring algorithm.

### What are the 8 quality dimensions?

Completeness, Coverage, Conformity, Consistency, Precision, Timeliness, Volumetrics, and Accuracy. Each measures a different aspect of data quality and is scored independently on a 0–100 scale. See the [Introduction](introduction.md){:target="_blank"} page for details on each dimension.

### What does a score of 0 mean?

A score of 0 indicates severe data quality issues — for example, a container where every quality check fails or where critical dimensions like accuracy or consistency have major problems.

### What does a score of 100 mean?

A score of 100 indicates perfect data quality across all enabled dimensions — no anomalies detected, all checks passing, complete data with consistent types and volumes.

### My datastore has no quality score — is this normal?

Yes. A datastore will not have a quality score until at least one of its containers has been **scanned**. The recommended order is **Sync → Profile → Scan**. Containers that have been synced and profiled but never scanned are excluded from the datastore-level score. See the [Introduction](introduction.md){:target="_blank"} for more details.

### Why is my datastore score different from the average of my container scores?

The datastore score is a **weighted** average, not a simple average. Containers with higher tag weight modifiers contribute more to the datastore score. Also, only scanned containers are included — unscanned containers are excluded from the calculation.

## Settings

### If I change settings on the datastore, does it affect my containers?

No. Datastore and container quality score settings are **completely independent**. Changing the decay period or dimension weights on a datastore does not propagate to its containers, and vice versa. Each level must be configured separately. See the [Independent Settings per Level](introduction.md#independent-settings-per-level){:target="_blank"} section for details.

### Can different datastores have different weights?

Yes. Quality score settings are configured **per datastore**. Each datastore can have its own decay period and dimension weights tailored to its specific governance priorities.

## Decay Period

### What is the decay period?

The decay period controls how far back in time Qualytics looks when calculating scores. Only anomalies, profiles, and scans within the decay window are included.

### What is the default decay period?

**180 days**. This means only data quality events from the last 6 months affect the score.

### Can I change the decay period?

Yes. You can set it to any value between **7 and 180 days** (in 7-day increments) through the [Quality Score Settings](../managing-datastores/quality-score-settings.md){:target="_blank"} or via the [API](api.md){:target="_blank"}.

### What happens when anomalies age out of the decay window?

They are excluded from the score calculation. This means if an anomaly was detected 7 months ago and the decay period is 180 days, it no longer impacts the score — even if it was never resolved. The score naturally improves as old issues age out.

### Does changing the decay period trigger a recalculation?

Yes. When you save new quality score settings, all container and field scores in the datastore are automatically recalculated.

## Dimension Weights

### What are dimension weights?

Each of the 8 quality dimensions has a configurable weight (0.0–2.0) that controls its impact on the total container score. Higher weights increase the dimension's influence.

### What is the default weight?

The system default is **1.0** for all dimensions. A `null` value in the API also resolves to 1.0.

### What happens if I set a weight to 0?

The dimension is effectively **disabled** — it turns grey in the settings UI and will not negatively impact the score. It receives the maximum possible boost factor, meaning it has no downward pull on the total score.

### Can I set a weight higher than 1?

Yes. Weights range from **0.0 to 2.0** (in 0.1 increments). A weight of 2.0 doubles the dimension's impact compared to the default, making the total score more sensitive to that dimension.

## Score Changes

### When are scores recalculated?

Quality scores are automatically recalculated when:

- A [**Scan operation**](../operations/scan.md){:target="_blank"} completes (anomalies detected or clean scan).
- A [**Profile operation**](../operations/profile.md){:target="_blank"} completes (new field statistics).
- An **anomaly status changes** (acknowledged, resolved, etc.).
- A **quality check is deleted**.
- An **anomaly is deleted**.
- **Quality score settings are updated** (decay period or weights changed).

### Are recalculations immediate?

Recalculations happen automatically after qualifying events. When multiple events occur in rapid succession (e.g., bulk anomaly resolution), they are batched to prevent redundant calculations.

### Can I manually trigger a recalculation?

No. There is no manual recalculation endpoint. Scores are always recalculated automatically based on the events listed above.

### Why did my score change without running a new scan?

Several things can trigger a recalculation without a new scan:

- Resolving or acknowledging anomalies changes the anomaly count.
- Deleting quality checks removes their anomalies from the calculation.
- Anomalies aging out of the decay window naturally improves the score.
- Changing dimension weights or decay period recalculates all scores.

## Troubleshooting

### Why isn't my score improving after fixing issues?

There are several possible reasons:

- **Decay period** — If you fixed the data but haven't re-scanned, the old anomalies are still within the decay window. Run a new Scan to detect that the issues are resolved.
- **Re-scan needed** — Qualytics doesn't know the data is fixed until a Scan confirms it. After fixing the source data, run a Scan to update the anomaly status.
- **Other dimensions** — You may have fixed one dimension (e.g., Accuracy) but another dimension (e.g., Coverage or Completeness) is dragging the score down. Check the per-dimension breakdown on the container detail page.
- **Weight configuration** — A dimension with a high weight that still has issues will dominate the score. Review your [dimension weights](../managing-datastores/quality-score-settings.md){:target="_blank"}.

## Tags and Weights

### How do tags affect quality scores?

Tags assigned to datastores can have a **weight modifier** (-10 to 10) that influences how individual containers contribute to the datastore-level quality score. Containers with higher tag weights have more impact on the overall score. See the [Tags Introduction](../tags/introduction.md#quality-score-impact){:target="_blank"} for details.

### What happens when I add or remove a tag with a weight modifier?

Container weights are recalculated immediately. The weight modifiers of all tags on each container are summed and normalized relative to each other. This changes the relative contribution of each container to the datastore score.

## Operations

### Do I need to run all three operations (Sync, Profile, Scan) to get a quality score?

You need at least a **Scan** for a container to be included in the datastore score. However, running a **Profile** first enables additional dimensions (Completeness, Consistency) and allows automatic check inference, which improves Coverage scores.

### Does syncing affect the quality score?

Not directly. Sync discovers containers and fields but does not produce quality scores. However, new containers discovered by Sync will appear with no score until they are profiled and scanned.

### What happens to the score when I add new containers?

New containers (discovered via Sync) are excluded from the datastore score until they are scanned. Once scanned, they are included in the weighted average.

## Permissions

### Who can view quality scores?

Any user with at least **Member** user role and **Reporter** team permission can view quality scores. See the [Permissions](permissions.md){:target="_blank"} page for the full matrix.

### Who can change quality score settings?

Users with **Member** user role and **Editor** team permission on the datastore. See the [Permissions](permissions.md){:target="_blank"} page for the full matrix.

## API

### Is there an API to update quality score settings?

Yes. Use `PUT /api/datastores/{id}/score-settings` to update the decay period and dimension weights. See the [API](api.md){:target="_blank"} page for examples.

### Can I retrieve historical quality scores via the API?

Yes. Use `GET /api/datastores/{id}/quality-scores` to retrieve the last 10 daily quality score snapshots. There is no pagination or date range parameter — the endpoint always returns the most recent 10. See the [API](api.md#get-historical-quality-scores){:target="_blank"} page for details.
