# Microsoft Teams Notification FAQ

## Setup & Prerequisites

#### Do I need to set up the Teams integration before using Teams notifications in Flows?

Yes. You must first connect the Microsoft Teams integration in **Settings > Integrations > Microsoft Teams** before you can select Teams channels in Flow notification actions. See the [Microsoft Teams Integration guide](../../../settings/integrations/alerting/msft_teams.md) for setup instructions.

---

## Channel & Configuration

#### How do I choose which Teams channel to send notifications to?

The **Channel** dropdown in the Microsoft Teams notification configuration shows all available channels from your connected Teams workspace. Select the channel where you want notifications to appear.

#### Can I send notifications to multiple Teams channels from the same Flow?

Yes. Add multiple Microsoft Teams notification actions to your Flow, each configured with a different channel.

---

## Message & Customization

#### What format are Teams notifications?

Microsoft Teams notifications are sent as Adaptive Cards, which provide a rich, structured format with sections, facts, and action buttons. The card format varies based on the trigger type.

#### Can I customize the notification message?

Yes. You can write a custom message using dynamic variables (tokens). The message content is rendered within the Adaptive Card format specific to Microsoft Teams.

#### What is the `operation_result_color__msft_teams` token?

This is a Teams-specific token that returns a color code compatible with Microsoft Teams Adaptive Cards. It is used to color-code notifications based on the operation result (e.g., green for success, red for failure).
