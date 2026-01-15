# Notification Tokens

Qualytics allows you to customize notification messages using dynamic variables (tokens). These tokens are automatically replaced with real values when a Flow is triggered.

!!! important 
    The available notification tokens depend on the **Flow trigger type**. Only the tokens listed for a specific trigger will work in notification messages.

### 🔔 Anomaly-Triggered Flow Tokens

The following tokens are available when a Flow is triggered by an anomaly.

| Token | Description |
|------|------------|
| `{{flow_name}}` | Name of the Flow |
| `{{datastore_name}}` | Datastore where the anomaly occurred |
| `{{datastore_link}}` | Link to the datastore |
| `{{container_name}}` | Container (table or file) where the anomaly was detected |
| `{{container_link}}` | Link to the container |
| `{{anomaly_type}}` | Type of anomaly detected |
| `{{anomaly_message}}` | System-generated message describing the anomaly |
| `{{check_description}}` | Description of the check that detected the anomaly |
| `{{target_link}}` | Direct link to view the anomaly details |

### 🔍 Partition Scan Trigger Tokens

The following tokens are available when a Flow is triggered by a partition scan.

| Token | Description |
|------|------------|
| `{{flow_name}}` | Name of the Flow |
| `{{datastore_name}}` | Datastore where the scan was executed |
| `{{datastore_link}}` | Link to the datastore |
| `{{container_name}}` | Container (table or file) that was scanned |
| `{{container_link}}` | Link to the container |
| `{{scan_target_name}}` | Partition name that was scanned (table/view for JDBC sources, file name for DFS sources) |
| `{{anomaly_count}}` | Number of anomalies detected during the scan |
| `{{anomaly_message}}` | Message describing the scan results |
| `{{check_description}}` | Description of the check |
| `{{target_link}}` | Direct link to view the scan results |

### ⚙️ Operation-Triggered Flow Tokens

The following tokens are available when a Flow is triggered by an operation.

| Token | Description |
|------|------------|
| `{{flow_name}}` | Name of the Flow |
| `{{datastore_name}}` | Datastore involved in the operation |
| `{{datastore_link}}` | Link to the datastore |
| `{{operation_type}}` | Type of operation executed (Catalog, Profile, Scan) |
| `{{operation_result}}` | Result of the operation (Success or Failure) |
| `{{operation_message}}` | Message describing the operation execution |
| `{{target_link}}` | Direct link to view operation details |

!!! note
    Notification tokens appear in the autocomplete menu only if they are valid for the selected Flow trigger type. If a token does not appear in the list, it is not supported for that trigger.
