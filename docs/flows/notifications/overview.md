# Notifications

Users can configure the application to send notifications through various channels as part of Flow actions. When a Flow trigger fires — such as an anomaly detection, operation completion, or scheduled event — Qualytics delivers notifications to the configured channels.

![notification](../../assets/flows/notifications/notification-44.png)

## Available Channels

| Channel | Description |
| :--- | :--- |
| [In App](in-app/overview.md) | Send notifications directly within the Qualytics platform to all users. |
| [Email](email/overview.md) | Deliver notifications to specified email addresses with customizable subject and message. |
| [Slack](slack/overview.md) | Send rich, interactive notifications to Slack channels with actionable buttons. |
| [Microsoft Teams](microsoft-teams/overview.md) | Deliver notifications to Microsoft Teams channels. |
| [PagerDuty](pagerduty/overview.md) | Trigger PagerDuty incidents with configurable severity, custom details, and routing. |

## Notification Message Variables

All notification channels support dynamic message variables (tokens) that are automatically replaced with real values when a Flow is triggered. The available tokens depend on the **Flow trigger type** (Anomaly, Operation, Partition Scan, etc.), not on the notification channel.

For the complete reference of all available tokens organized by trigger type, see the [Message Variables](message-variables.md) documentation.
