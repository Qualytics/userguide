# API Payload Examples

### Retrieving Anomaly by UUID or Id

**Endpoint (Get)**

```/api/anomalies/{id} (get)```

**Example Result Response**

```json
{
  "id": 0,
  "created": "2024-06-10T21:29:42.695Z",
  "uuid": "3fa85f64-5717-4562-b3fc-2c963f66afa6",
  "type": "shape",
  "is_new": true,
  "archived": true,
  "status": "Active",
  "source_enriched": true,
  "datastore": {
    "id": 0,
    "name": "string",
    "store_type": "jdbc",
    "type": "athena",
    "enrich_only": true,
    "enrich_container_prefix": "string",
    "favorite": true
  },
  "container": {
    "id": 0,
    "name": "string",
    "container_type": "table",
    "table_type": "table"
  },
  "partition": {
    "name": "string",
    "location": "string"
  },
  "weight": 0,
  "global_tags": [
    {
      "type": "external",
      "name": "string",
      "color": "string",
      "description": "string",
      "weight_modifier": 0,
      "integration": {
        "id": 0,
        "created": "2024-06-10T21:29:42.696Z",
        "name": "string",
        "type": "atlan",
        "api_url": "string",
        "overwrite": true,
        "last_synced": "2024-06-10T21:29:42.696Z",
        "status": "syncing"
      }
    },
    {
      "type": "external",
      "name": "string",
      "color": "string",
      "description": "string",
      "weight_modifier": 0,
      "integration": {
        "id": 0,
        "created": "2024-06-10T21:29:42.696Z",
        "name": "string",
        "type": "atlan",
        "api_url": "string",
        "overwrite": true,
        "last_synced": "2024-06-10T21:29:42.696Z",
        "status": "syncing"
      }
    }
  ],
  "anomalous_records_count": 0,
  "comments": [
    {
      "id": 0,
      "created": "2024-06-10T21:29:42.696Z",
      "message": "string",
      "user": {
        "id": 0,
        "created": "2024-06-10T21:29:42.696Z",
        "user_id": "string",
        "email": "string",
        "name": "string",
        "picture": "string",
        "role": "Member",
        "deleted_at": "2024-06-10T21:29:42.696Z",
        "teams": [
          {
            "id": 0,
            "name": "string",
            "permission": "Read"
          }
        ]
      }
    }
  ],
  "failed_checks": [
    {
      "quality_check": {
        "id": 0,
        "created": "2024-06-10T21:29:42.696Z",
        "fields": [
          {
            "id": 0,
            "created": "2024-06-10T21:29:42.696Z",
            "name": "string",
            "type": "Unknown",
            "completeness": 0,
            "weight": 0,
            "global_tags": [
              {
                "type": "global",
                "name": "string",
                "color": "string",
                "description": "string",
                "weight_modifier": 0
              },
              {
                "type": "external",
                "name": "string",
                "color": "string",
                "description": "string",
                "weight_modifier": 0,
                "integration": {
                  "id": 0,
                  "created": "2024-06-10T21:29:42.697Z",
                  "name": "string",
                  "type": "atlan",
                  "api_url": "string",
                  "overwrite": true,
                  "last_synced": "2024-06-10T21:29:42.697Z",
                  "status": "syncing"
                }
              }
            ],
            "latest_profile_id": 0,
            "quality_score": {
              "total": 0,
              "completeness": 0,
              "coverage": 0,
              "conformity": 0,
              "consistency": 0,
              "precision": 0,
              "timeliness": 0,
              "volumetrics": 0,
              "accuracy": 0
            }
          }
        ],
        "description": "string",
        "rule_type": "afterDateTime",
        "coverage": 0,
        "inferred": true,
        "template_locked": true,
        "is_new": true,
        "num_container_scans": 0,
        "filter": "string",
        "properties": {
          "allow_other_fields": true,
          "assertion": "string",
          "comparison": "string",
          "datetime": "2024-06-10T21:29:42.697Z",
          "expression": "string",
          "field_name": "string",
          "field_type": "Unknown",
          "id_field_names": [
            "string"
          ],
          "inclusive": true,
          "inclusive_max": true,
          "inclusive_min": true,
          "interval_name": "Yearly",
          "last_value": 0,
          "list": [
            "string"
          ],
          "max": 0,
          "max_size": 0,
          "max_time": "2024-06-10T21:29:42.697Z",
          "min": 0,
          "min_size": 0,
          "min_time": "2024-06-10T21:29:42.697Z",
          "pattern": "string",
          "ref_container_id": 0,
          "ref_datastore_id": 0,
          "tolerance": 0,
          "value": 0,
          "ref_expression": "string",
          "ref_filter": "string",
          "required_labels": [
            "road"
          ],
          "numeric_comparator": {
            "epsilon": 0,
            "as_absolute": true
          },
          "duration_comparator": {
            "millis": 0
          },
          "string_comparator": {
            "ignore_whitespace": false
          },
          "distinct_field_name": "string",
          "pair_substrings": true,
          "pair_homophones": true,
          "spelling_similarity_threshold": 0
        },
        "template_checks_count": 0,
        "anomaly_count": 0,
        "type": "global",
        "name": "string",
        "color": "string",
        "description": "string",
        "weight_modifier": 0
      },
      {
        "type": "external",
        "name": "string",
        "color": "string",
        "description": "string",
        "weight_modifier": 0,
        "integration": {
          "id": 0,
          "created": "2024-06-10T21:29:42.697Z",
          "name": "string",
          "type": "atlan",
          "api_url": "string",
          "overwrite": true,
          "last_synced": "2024-06-10T21:29:42.697Z",
          "status": "syncing"
        }
      }
    ],
    "latest_profile_id": 0,
    "quality_score": {
      "total": 0,
      "completeness": 0,
      "coverage": 0,
      "conformity": 0,
      "consistency": 0,
      "precision": 0,
      "timeliness": 0,
      "volumetrics": 0,
      "accuracy": 0
    }
  }
],
  "description": "string",
  "rule_type": "afterDateTime",
  "coverage": 0,
  "inferred": true,
  "template_locked": true,
  "is_new": true,
  "num_container_scans": 0,
  "filter": "string",
  "properties": {
    "allow_other_fields": true,
    "assertion": "string",
    "comparison": "string",
    "datetime": "2024-06-10T21:29:42.697Z",
    "expression": "string",
    "field_name": "string",
    "field_type": "Unknown",
    "id_field_names": [
      "string"
    ],
    "inclusive": true,
    "inclusive_max": true,
    "inclusive_min": true,
    "interval_name": "Yearly",
    "last_value": 0,
    "list": [
      "string"
    ],
    "max": 0,
    "max_size": 0,
    "max_time": "2024-06-10T21:29:42.697Z",
    "min": 0,
    "min_size": 0,
    "min_time": "2024-06-10T21:29
}
```

### Retrieving Anomaly Source Records

**Endpoint (Get)**
```/api/anomalies/{id}/source-record (get)```

**Example Result Response**

```json
{
  "source_record":"[{\"_qualytics_entity_id\":0,\"COLUMN_1\": VALUE 1,\"COLUMN_2\":\" VALUE 1\"},{\"_qualytics_entity_id\":1234,\"COLUMN_1\": VALUE 2,\"COLUMN 2\":\"VALUE 2\"},{\"_qualytics_entity_id\":5678}]",
  "created":"2024-06-10T21:24:34.617296Z"
}
```