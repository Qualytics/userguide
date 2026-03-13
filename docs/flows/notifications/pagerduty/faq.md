# PagerDuty Notification FAQ

## Configuration

#### How do I send PagerDuty notifications from a Flow?

Add a **Notification** action to your Flow and select **PagerDuty** as the notification type. Configure the message, severity, and optionally add custom details or a Routing Key override.

#### Can I use variables in the notification message?

Yes. PagerDuty messages support variable interpolation using `{{ variable_name }}` syntax. Available variables include `{{ flow_name }}`, `{{ operation_type }}`, `{{ datastore_name }}`, `{{ container_name }}`, `{{ anomaly_message }}`, and more. The autocomplete feature in the message editor will suggest available variables as you type.

#### What severity levels are available?

Four levels: **Info**, **Warning**, **Error**, and **Critical**. The default is **Info**. Each level maps directly to PagerDuty's severity classification, which controls urgency and notification behavior based on your service's configuration.

---

## Routing & Delivery

#### Can I send different events to different PagerDuty services?

Yes. Each PagerDuty notification action in a Flow supports a **Routing Key Override** property. When set, the override key routes that specific action's events to a different PagerDuty service than the default integration key.

#### What happens if the PagerDuty integration is disconnected but a Flow still references it?

The Flow action will fail to deliver the notification. The Flow itself will continue to execute, but the PagerDuty notification step will be skipped with an error. Other actions in the same Flow (e.g., Slack notifications, HTTP actions) are not affected.

---

## Incident Details

#### What information is included in the PagerDuty incident?

Each incident includes:

- **Summary**: The rendered notification message from your Flow action
- **Severity**: The configured severity level (Info, Warning, Error, Critical)
- **Source**: Your Qualytics instance URL
- **Component**: The affected container name
- **Class**: The event type (anomaly, operation, partition scan, etc.)
- **Custom Details**: System-generated metadata plus any custom key-value pairs you configured
- **Links**: A direct link back to the relevant resource in the Qualytics UI

---

## Testing & History

#### Can I test a PagerDuty notification before publishing the Flow?

Yes. Click the **Test notification** button in the PagerDuty notification action configuration. This sends a test event to PagerDuty using the configured settings. Note that test events **will create an incident** in your PagerDuty service (unlike connection validation, which uses Change Events).

#### Can I see a history of PagerDuty events sent by Qualytics?

PagerDuty events are sent as part of Flow executions. You can review Flow execution history in the Qualytics UI to see which notifications were triggered and their status.
