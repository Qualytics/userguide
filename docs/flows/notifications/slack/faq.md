# Slack Notification FAQ

## Setup & Prerequisites

#### Do I need to set up the Slack integration before using Slack notifications in Flows?

Yes. You must first connect the Slack integration in **Settings > Integrations > Slack** before you can select Slack channels in Flow notification actions. See the [Slack Integration guide](../../../settings/integrations/alerting/slack.md) for setup instructions.

---

## Channel & Configuration

#### How do I choose which Slack channel to send notifications to?

The **Channel** dropdown in the Slack notification configuration shows all available channels from your connected Slack workspace. Select the channel where you want notifications to appear.

#### Can I send notifications to multiple Slack channels from the same Flow?

Yes. Add multiple Slack notification actions to your Flow, each configured with a different channel.

---

## Message & Customization

#### Do different trigger types generate different Slack messages?

Yes. Each trigger generates a unique Slack notification format. Operation completions include status and result details, anomaly detections include container and check information, and partition scans include partition-specific data.

#### Is the Slack notification message customizable?

Slack notifications use a rich format (Block Kit) with structured content. The message template is pre-configured based on the trigger type, but you can customize the content using message variables. The Preview section in the configuration shows how the notification will appear.

#### What is the `operation_result_color` token?

This is a Slack-specific token that returns a hex color code based on the operation result (e.g., green for success, red for failure). It is used internally by the Slack Block Kit template to color-code notifications.

---

## Actions & Interactivity

#### What actions can I take on Slack notifications?

Slack notifications from Qualytics include interactive buttons depending on the trigger type:

- **View Operation** — Open operation details in Qualytics
- **View Results** — Examine scan results
- **View Anomaly** — Investigate anomaly details
- **Acknowledge** — Mark an anomaly as reviewed
- **Comment** — Add a comment for team collaboration
- **Archive** — Archive the anomaly if no further action is needed
