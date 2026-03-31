# Datastore Quality Score API

The Data Quality Score API allows you to retrieve and update quality score settings for a datastore, as well as access historical quality score data.

!!! tip
    For complete API documentation, including request/response schemas, visit the [API docs](https://demo.qualytics.io/api/docs){:target="_blank"}.

## Get Quality Score Settings

Retrieve the current quality score settings (decay period and dimension weights) for a datastore.

### Request

```bash
GET /api/datastores/{datastore_id}/score-settings
```

### Example

```bash
curl -X GET "https://your-instance.qualytics.io/api/datastores/42/score-settings" \
  -H "Authorization: Bearer YOUR_API_TOKEN"
```

### Response

```json
{
  "decay_period_days": 180,
  "completeness_weight": 1.0,
  "coverage_weight": 1.0,
  "conformity_weight": 1.0,
  "consistency_weight": 1.0,
  "precision_weight": 1.0,
  "timeliness_weight": 1.0,
  "volumetrics_weight": 1.0,
  "accuracy_weight": 1.0
}
```

## Update Quality Score Settings

Update the decay period and/or dimension weights for a datastore. You only need to include the fields you want to change — omitted fields remain unchanged.

### Request

```bash
PUT /api/datastores/{datastore_id}/score-settings
```

### Request Schema

| Field | Type | Default | Range | Description |
| :--- | :--- | :---: | :---: | :--- |
| `decay_period_days` | `integer` | `180` | 7–180 | The time frame in days over which historical data is evaluated for scoring. |
| `completeness_weight` | `float` | `null` | 0.0–2.0 | Weight for the Completeness dimension. |
| `coverage_weight` | `float` | `null` | 0.0–2.0 | Weight for the Coverage dimension. |
| `conformity_weight` | `float` | `null` | 0.0–2.0 | Weight for the Conformity dimension. |
| `consistency_weight` | `float` | `null` | 0.0–2.0 | Weight for the Consistency dimension. |
| `precision_weight` | `float` | `null` | 0.0–2.0 | Weight for the Precision dimension. |
| `timeliness_weight` | `float` | `null` | 0.0–2.0 | Weight for the Timeliness dimension. |
| `volumetrics_weight` | `float` | `null` | 0.0–2.0 | Weight for the Volumetrics dimension. |
| `accuracy_weight` | `float` | `null` | 0.0–2.0 | Weight for the Accuracy dimension. |

!!! note
    A weight of `null` uses the system default (1.0). A weight of `0.0` effectively disables the dimension — it will not negatively impact the score.

### Example: Change Decay Period

Shorten the decay period to 30 days for a more real-time quality view:

```bash
curl -X PUT "https://your-instance.qualytics.io/api/datastores/42/score-settings" \
  -H "Authorization: Bearer YOUR_API_TOKEN" \
  -H "Content-Type: application/json" \
  -d '{
    "decay_period_days": 30
  }'
```

### Example: Prioritize Accuracy and Completeness

Increase the weight of Accuracy and Completeness while reducing Volumetrics:

```bash
curl -X PUT "https://your-instance.qualytics.io/api/datastores/42/score-settings" \
  -H "Authorization: Bearer YOUR_API_TOKEN" \
  -H "Content-Type: application/json" \
  -d '{
    "accuracy_weight": 2.0,
    "completeness_weight": 1.5,
    "volumetrics_weight": 0.3
  }'
```

### Example: Disable Timeliness and Volumetrics

If timeliness and volumetrics are not relevant for your use case:

```bash
curl -X PUT "https://your-instance.qualytics.io/api/datastores/42/score-settings" \
  -H "Authorization: Bearer YOUR_API_TOKEN" \
  -H "Content-Type: application/json" \
  -d '{
    "timeliness_weight": 0.0,
    "volumetrics_weight": 0.0
  }'
```

### Example: Reset All Weights to Default

Set all weights to `null` to restore system defaults:

```bash
curl -X PUT "https://your-instance.qualytics.io/api/datastores/42/score-settings" \
  -H "Authorization: Bearer YOUR_API_TOKEN" \
  -H "Content-Type: application/json" \
  -d '{
    "decay_period_days": 180,
    "completeness_weight": null,
    "coverage_weight": null,
    "conformity_weight": null,
    "consistency_weight": null,
    "precision_weight": null,
    "timeliness_weight": null,
    "volumetrics_weight": null,
    "accuracy_weight": null
  }'
```

### Response

Returns the updated settings:

```json
{
  "decay_period_days": 180,
  "completeness_weight": null,
  "coverage_weight": null,
  "conformity_weight": null,
  "consistency_weight": null,
  "precision_weight": null,
  "timeliness_weight": null,
  "volumetrics_weight": null,
  "accuracy_weight": null
}
```

## Get Historical Quality Scores

Retrieve the last 10 quality score snapshots for a datastore, recorded as daily metrics.

### Request

```bash
GET /api/datastores/{datastore_id}/quality-scores
```

### Example

```bash
curl -X GET "https://your-instance.qualytics.io/api/datastores/42/quality-scores" \
  -H "Authorization: Bearer YOUR_API_TOKEN"
```

### Response

```json
[
  {
    "date": "2026-03-30",
    "total": 87.4,
    "completeness": 95.2,
    "coverage": 72.0,
    "conformity": 91.3,
    "consistency": 88.7,
    "precision": 94.1,
    "timeliness": 82.5,
    "volumetrics": 90.0,
    "accuracy": 85.6
  },
  {
    "date": "2026-03-29",
    "total": 85.1,
    "completeness": 94.8,
    "coverage": 70.0,
    "conformity": 89.2,
    "consistency": 87.3,
    "precision": 93.5,
    "timeliness": 80.0,
    "volumetrics": 88.5,
    "accuracy": 84.2
  }
]
```

### Response Schema

| Field | Type | Description |
| :--- | :--- | :--- |
| `date` | `date` | The date of the quality score snapshot. |
| `total` | `float` | The overall quality score (0–100). |
| `completeness` | `float` | Completeness dimension score (0–100). |
| `coverage` | `float` | Coverage dimension score (0–100). |
| `conformity` | `float` | Conformity dimension score (0–100). |
| `consistency` | `float` | Consistency dimension score (0–100). |
| `precision` | `float` | Precision dimension score (0–100). |
| `timeliness` | `float` | Timeliness dimension score (0–100). |
| `volumetrics` | `float` | Volumetrics dimension score (0–100). |
| `accuracy` | `float` | Accuracy dimension score (0–100). |

## Important Notes

!!! note "Automatic Recalculation"
    After updating quality score settings, scores are automatically recalculated for all containers and fields in the datastore. There is no manual recalculation endpoint.

!!! note "Permissions"
    Retrieving settings requires at least **Member** role. Updating settings requires **Editor** team permission on the datastore. Retrieving historical scores requires **Reporter** team permission.
