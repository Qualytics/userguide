# Datastore Quality Score API

The Data Quality Score API allows you to retrieve and update quality score settings for a datastore, as well as access historical quality score data.

!!! tip
    For complete API documentation, including request/response schemas, visit the [API docs](https://demo.qualytics.io/api/docs){:target="_blank"}.

All endpoints use the base URL of your Qualytics deployment (e.g., `https://your-instance.qualytics.io/api`).

---

## Get Quality Score Settings

Retrieve the current quality score settings (decay period and dimension weights) for a datastore.

**Endpoint**: `GET /api/datastores/{datastore_id}/score-settings`

**Permission**: Member user role (no team permission required)

??? example "Example request and response"

    **Request**:

    ```bash
    curl -X GET "https://your-instance.qualytics.io/api/datastores/42/score-settings" \
      -H "Authorization: Bearer YOUR_TOKEN"
    ```

    **Response**:

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

!!! note "null vs 1.0"
    When a datastore has never had its settings explicitly configured, the GET endpoint returns `null` for all weight fields. A `null` weight means the system default (`1.0`) is used. Once you update any setting, subsequent GET calls return the explicitly set values.

---

## Update Quality Score Settings

Update the decay period and/or dimension weights for a datastore. This endpoint uses **partial update semantics** — you only need to include the fields you want to change. Omitted fields remain unchanged.

**Endpoint**: `PUT /api/datastores/{datastore_id}/score-settings`

**Permission**: Member user role + Editor team permission on the datastore

**Request Body**:

| Field | Type | Default | Range | Description |
| :--- | :--- | :---: | :---: | :--- |
| `decay_period_days` | `integer` | `180` | 7–180 | The time frame in days over which historical data is evaluated for scoring. |
| `completeness_weight` | `float` | `null` (1.0) | 0.0–2.0 | Weight for the Completeness dimension. |
| `coverage_weight` | `float` | `null` (1.0) | 0.0–2.0 | Weight for the Coverage dimension. |
| `conformity_weight` | `float` | `null` (1.0) | 0.0–2.0 | Weight for the Conformity dimension. |
| `consistency_weight` | `float` | `null` (1.0) | 0.0–2.0 | Weight for the Consistency dimension. |
| `precision_weight` | `float` | `null` (1.0) | 0.0–2.0 | Weight for the Precision dimension. |
| `timeliness_weight` | `float` | `null` (1.0) | 0.0–2.0 | Weight for the Timeliness dimension. |
| `volumetrics_weight` | `float` | `null` (1.0) | 0.0–2.0 | Weight for the Volumetrics dimension. |
| `accuracy_weight` | `float` | `null` (1.0) | 0.0–2.0 | Weight for the Accuracy dimension. |

!!! note
    A weight of `null` uses the system default (1.0). A weight of `0.0` effectively disables the dimension — it will not negatively impact the score.

??? example "Change decay period"

    Shorten the decay period to 30 days for a more real-time quality view:

    **Request**:

    ```bash
    curl -X PUT "https://your-instance.qualytics.io/api/datastores/42/score-settings" \
      -H "Authorization: Bearer YOUR_TOKEN" \
      -H "Content-Type: application/json" \
      -d '{
        "decay_period_days": 30
      }'
    ```

    **Response**:

    ```json
    {
      "decay_period_days": 30,
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

??? example "Prioritize Accuracy and Completeness"

    Increase Accuracy and Completeness while reducing Volumetrics:

    **Request**:

    ```bash
    curl -X PUT "https://your-instance.qualytics.io/api/datastores/42/score-settings" \
      -H "Authorization: Bearer YOUR_TOKEN" \
      -H "Content-Type: application/json" \
      -d '{
        "accuracy_weight": 2.0,
        "completeness_weight": 1.5,
        "volumetrics_weight": 0.3
      }'
    ```

    **Response**:

    ```json
    {
      "decay_period_days": 30,
      "completeness_weight": 1.5,
      "coverage_weight": 1.0,
      "conformity_weight": 1.0,
      "consistency_weight": 1.0,
      "precision_weight": 1.0,
      "timeliness_weight": 1.0,
      "volumetrics_weight": 0.3,
      "accuracy_weight": 2.0
    }
    ```

??? example "Disable Timeliness and Volumetrics"

    **Request**:

    ```bash
    curl -X PUT "https://your-instance.qualytics.io/api/datastores/42/score-settings" \
      -H "Authorization: Bearer YOUR_TOKEN" \
      -H "Content-Type: application/json" \
      -d '{
        "timeliness_weight": 0.0,
        "volumetrics_weight": 0.0
      }'
    ```

    **Response**:

    ```json
    {
      "decay_period_days": 30,
      "completeness_weight": 1.5,
      "coverage_weight": 1.0,
      "conformity_weight": 1.0,
      "consistency_weight": 1.0,
      "precision_weight": 1.0,
      "timeliness_weight": 0.0,
      "volumetrics_weight": 0.0,
      "accuracy_weight": 2.0
    }
    ```

??? example "Reset all weights to default"

    Set all weights to `null` to restore system defaults:

    **Request**:

    ```bash
    curl -X PUT "https://your-instance.qualytics.io/api/datastores/42/score-settings" \
      -H "Authorization: Bearer YOUR_TOKEN" \
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

    **Response**:

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

For the UI equivalent, see [Quality Score Settings](../managing-datastores/quality-score-settings.md){:target="_blank"}.

---

## Get Historical Quality Scores

Retrieve the last 10 quality score snapshots for a datastore, recorded as daily metrics.

**Endpoint**: `GET /api/datastores/{datastore_id}/quality-scores`

**Permission**: Member user role + Reporter team permission on the datastore

!!! note "Limitation"
    This endpoint returns a **fixed maximum of 10 snapshots**. There is no pagination or date range parameter — the response always contains the most recent 10 daily scores available.

??? example "Example request and response"

    **Request**:

    ```bash
    curl -X GET "https://your-instance.qualytics.io/api/datastores/42/quality-scores" \
      -H "Authorization: Bearer YOUR_TOKEN"
    ```

    **Response**:

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

---

## Error Responses

| Status Code | Description |
| :--- | :--- |
| `401 Unauthorized` | Missing or invalid API token. |
| `403 Forbidden` | User does not have the required role or team permission. |
| `404 Not Found` | Datastore with the specified ID does not exist, or no settings have been configured yet. |
| `422 Unprocessable Entity` | Invalid request body (e.g., decay_period_days outside 7–180 range, weight outside 0–2.0). |

??? example "Error response examples"

    **403 Forbidden**:

    ```json
    { "detail": "You must have editor permission in at least one of these teams: ['Data Platform']" }
    ```

    **404 Not Found**:

    ```json
    { "detail": "No quality score settings found for datastore id: 999" }
    ```

    **422 Unprocessable Entity**:

    ```json
    { "detail": [{ "loc": ["body", "decay_period_days"], "msg": "ensure this value is greater than or equal to 7", "type": "value_error.number.not_ge" }] }
    ```

---

## Permission Summary

| Operation | Minimum Permission |
| :--- | :--- |
| Get quality score settings | Member user role |
| Update quality score settings | Member user role + Editor team permission |
| Get historical quality scores | Member user role + Reporter team permission |

!!! note "Automatic Recalculation"
    After updating quality score settings, scores are automatically recalculated for all containers and fields in the datastore. There is no manual recalculation endpoint.
