# Notifications FAQ

## General

#### What are notifications in Qualytics?

Notifications are actions within Flows that send alerts through configured channels (In App, Email, Slack, Microsoft Teams, PagerDuty) when a trigger event occurs, such as an anomaly detection, operation completion, or partition scan.

#### How many notification channels can I use in a single Flow?

There is no limit. You can add multiple notification actions to a Flow, each configured with a different channel. For example, a single Flow can send an In App notification, an Email, and a Slack message simultaneously.

#### Do all notification channels receive the same information?

All channels have access to the same set of message variables (tokens) based on the Flow trigger type. However, the format and presentation may differ — for example, Slack uses Block Kit for rich formatting, while PagerDuty creates structured incidents with severity levels.

---

## Triggers & Behavior

#### Which Flow trigger types support notifications?

Notifications are supported on all trigger types: **Anomaly**, **Operation**, **Partition Scan**, **Anomaly Archive**, **Anomaly Delete**, **Schedule**, and **Manual**. However, Schedule and Manual triggers do not support message variables — only static text.

#### What happens if a notification fails to send?

If a notification action fails (e.g., due to a disconnected integration or invalid configuration), the Flow continues to execute. Other actions in the same Flow — including other notification channels — are not affected.

#### Are notifications sent in real time?

Yes. Notifications are dispatched immediately when the Flow trigger fires. Delivery time depends on the external channel (e.g., Slack, Email, PagerDuty).

---

## Message Variables

#### What are message variables?

Message variables (also called tokens) are dynamic placeholders like `{{ flow_name }}` or `{{ datastore_name }}` that are automatically replaced with real values when a notification is sent. They allow you to create reusable, context-aware messages.

#### Are the same variables available across all channels?

Yes. The available variables depend on the **Flow trigger type**, not on the notification channel. All channels share the same set of tokens for a given trigger. The only exceptions are channel-specific color tokens for Slack (`{{ operation_result_color }}`) and Microsoft Teams (`{{ operation_result_color__msft_teams }}`).

#### What happens if I use a variable that is not supported by the trigger type?

The variable will not be replaced and will appear as raw text in the notification message. Use the autocomplete feature in the message editor — it only suggests variables valid for the selected trigger type.

---

## Testing & Permissions

#### Can I test notifications before publishing the Flow?

Yes. Each notification channel includes a **Test Notification** button that sends a sample message before the Flow is published. This allows you to verify the configuration and message formatting.

#### What permissions are needed to configure and test notifications?

A **Member** role is required to configure notification actions. A **Manager** role is required to send test notifications.

#### Does testing a notification affect external systems?

It depends on the channel. For most channels (In App, Email, Slack, Microsoft Teams), a test message is sent to the configured destination. For PagerDuty, test notifications **will create an actual incident** in your PagerDuty service.
