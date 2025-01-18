# Flows Actions

Flow can allow users to add **Actions** in your pipeline by chaining nodes and configurates what action this pipeline will do.
Actions can be **Notifications** or **Operations**, allowing users to inform varios notification channel or execute tasts based on specific operation.
This will execute a defined action sequence. The user can select what he wants the application to do when the trigger activates.

!!! info
    Previously, sending notifications required configuring notification rules. This process was replaced and improved through flows.

## Operations

The user can run all operations when the trigger activates. He can select Catalog, Profile, or Scan operations. After choosing one of the options, he must set the operations.
The form is same to run a [Catalog](../source-datastore/catalog.md), [Profile](../source-datastore/profile.md) or [Scan](../source-datastore/scan.md) operations.

![flows-operations](../assets/flows/actions/flows-operations-light.png#only-light)
![flows-operations](../assets/flows/actions/flows-operations-dark.png#only-dark)

| Operation | Description |
|-------|--------|
| **Catalog** | A Catalog Operation imports named data collections like tables, views, and files into a Source Datastore |
| **Profile** | The Profile Operation is a comprehensive analysis conducted on every record within all available containers in a datastore |
| **Scan** | The Scan Operation in Qualytics is performed on a datastore to enforce data quality checks for various data collections such as tables, views, and files |

## Notifications

The user can send a notification by choosing one of the options that the app has.

![flows-notifications](../assets/flows/actions/flows-notifications-light.png#only-light)
![flows-notifications](../assets/flows/actions/flows-notifications-dark.png#only-dark)

| Notification | Description |
|-------|--------|
| [**In-App**](#in-app) | This will send an app notification to all users that use Qualytics|
| [**Email**](#email) | This will send an email notification|
| [**Slack**](#slack) | This will send a Slack notification|
| [**Microsoft Teams**](#microsoft-teams) | This will send a Microsoft Teams notification|
| [**Pager Duty**](#page-duty) | This will send a Pager Duty notification|

### In-App

In-App notifications allow users to managing your notifications, you ensure that critical updates reach you at the right time, while unnecessary alerts are minimized, allowing you to stay focused on what matters most.

**Step 1:** Select In-App notification

![flows-option-1](../assets/flows/actions/flows-option-1-light.png#only-light)
![flows-option-1](../assets/flows/actions/flows-option-1-dark.png#only-dark)

**Step 2:** Add a message

![flows-in-app-1](../assets/flows/actions/flows-in-app-1-light.png#only-light)
![flows-in-app-1](../assets/flows/actions/flows-in-app-1-dark.png#only-dark)

**Step 3:** Click on "**Save**" button.

![flows-in-app-2](../assets/flows/actions/flows-in-app-2-light.png#only-light)
![flows-in-app-2](../assets/flows/actions/flows-in-app-2-dark.png#only-dark)

### Email

Adding email notifications allows users to receive timely updates or alerts directly in their inbox.  By setting up notifications with specific triggers and channels, you can ensure that you are promptly informed about critical events, such as operation completions or detected anomalies. This proactive approach allows you to take immediate action when necessary, helping to address issues quickly and maintain the smooth and efficient operation of your processes.

**Step 1:** Select Email notification

![flows-option-2](../assets/flows/actions/flows-option-2-light.png#only-light)
![flows-option-2](../assets/flows/actions/flows-option-2-dark.png#only-dark)

**Step 2:** Enter the Email Addresses where you want the notification to be sent.

![flows-in-app-1](../assets/flows/actions/flows-in-app-1-light.png#only-light)
![flows-in-app-1](../assets/flows/actions/flows-in-app-1-dark.png#only-dark)

!!! info
    Use "," (comma) to add more emails

**Step 3:** Add a message

![flows-in-app-2](../assets/flows/actions/flows-email-2-light.png#only-light)
![flows-in-app-2](../assets/flows/actions/flows-email-2-dark.png#only-dark)

!!! info
    You can click on "Test Notification" button to send a test email to the provided address. If the email is successfully sent, you will receive a confirmation message indicating Notification successfully sent

**Step 4:** Click on "**Save**" button.

![flows-email-3](../assets/flows/actions/flows-email-3-light.png#only-light)
![flows-email-3](../assets/flows/actions/flows-email-3-dark.png#only-dark)

### Slack

To set up Slack notifications, start by naming your notification and selecting the triggers, such as operation completion or anomaly detection. Next, add relevant tags and configure the Slack Webhook URL to connect directly to your Slack channel.

**Step 1:** Select Slack notification

![flows-option-3](../assets/flows/actions/flows-option-3-light.png#only-light)
![flows-option-3](../assets/flows/actions/flows-option-3-dark.png#only-dark)

**Step 2:** Add a Weebhook URL

![flows-slack-1](../assets/flows/actions/flows-slack-1-light.png#only-light)
![flows-slack-1](../assets/flows/actions/flows-slack-1-dark.png#only-dark)

!!! info
    You can only add one URL per Node

**Step 3:** Add a message

![flows-slack-2](../assets/flows/actions/flows-slack-2-light.png#only-light)
![flows-slack-2](../assets/flows/actions/flows-slack-2-dark.png#only-dark)

!!! info
    You can click on "Test Notification" button  to send a test message to the provided Webhook URL. If the message is successfully sent, you will receive a confirmation notification indicating "Notification successfully sent".

**Step 4:** Click on "**Save**" button.

![flows-slack-3](../assets/flows/actions/flows-slack-3-light.png#only-light)
![flows-slack-3](../assets/flows/actions/flows-slack-3-dark.png#only-dark)

### Microsoft Teams

Integrating Microsoft Teams notifications allows users to receive timely updates or alerts directly in their Teams channel. By setting up Microsoft Teams notifications with specific trigger conditions, you can ensure that you are instantly informed about critical events, such as operation completions or anomalies detected. This approach allows you to take immediate action when necessary, helping to address issues quickly and maintain the smooth and efficient operation of your processes.

To set up Slack notifications, start by naming your notification and selecting the triggers, such as operation completion or anomaly detection. Next, add relevant tags and configure the Slack Webhook URL to connect directly to your Slack channel.

**Step 1:** Select Microsoft Teams notification

![flows-option-4](../assets/flows/actions/flows-option-4-light.png#only-light)
![flows-option-4](../assets/flows/actions/flows-option-4-dark.png#only-dark)

**Step 2:** Add a Weebhook URL

![flows-microsoft-teams-1](../assets/flows/actions/flows-microsoft-teams-1-light.png#only-light)
![flows-microsoft-teams-1](../assets/flows/actions/flows-microsoft-teams-1-dark.png#only-dark)

!!! info
    You can only add one URL per Node

**Step 3:** Add a message

![flows-microsoft-teams-2](../assets/flows/actions/flows-microsoft-teams-2-light.png#only-light)
![flows-microsoft-teams-2](../assets/flows/actions/flows-microsoft-teams-2-dark.png#only-dark)

!!! info
    You can click on "Test Notification" button to send to the Webhook URL address you have provided. This verifies that the address provided is correct.

**Step 4:** Click on "**Save**" button.

![flows-microsoft-teams-3](../assets/flows/actions/flows-microsoft-teams-3-light.png#only-light)
![flows-microsoft-teams-3](../assets/flows/actions/flows-microsoft-teams-3-dark.png#only-dark)

### Page Duty

Integrating PagerDuty with Qualytics ensures that your team gets instant alerts for critical data events and system issues. With this connection, you can automatically receive real-time notifications about anomalies, operation completions and other important events directly in your PagerDuty account. By categorizing alerts based on severity, it ensures the right people are notified at the right time, speeding up decision-making and resolving incidents efficiently. This helps your team respond quickly to issues, reducing downtime and keeping data operations on track.

**Step 1:** Select Pager Duty notification

![flows-option-5](../assets/flows/actions/flows-option-5-light.png#only-light)
![flows-option-5](../assets/flows/actions/flows-option-5-dark.png#only-dark)

**Step 2:** Add an Integration Key

![flows-pager-duty-1](../assets/flows/actions/flows-pager-duty-1-light.png#only-light)
![flows-pager-duty-1](../assets/flows/actions/flows-pager-duty-1-dark.png#only-dark)

**Step 3:** Select a Severity. The table below will show all Severity available.

![flows-pager-duty-2](../assets/flows/actions/flows-pager-duty-2-light.png#only-light)
![flows-pager-duty-2](../assets/flows/actions/flows-pager-duty-2-dark.png#only-dark)

| Severity |
|-------|
| info |
| warning |
| error |
| critical |

**Step 3:** Add a message

![flows-pager-duty-3](../assets/flows/actions/flows-pager-duty-3-light.png#only-light)
![flows-pager-duty-3](../assets/flows/actions/flows-pager-duty-3-dark.png#only-dark)

!!! info
    You can click on "Test Notification" button to check if the integration key is functioning correctly. Once the test notification is sent, you will see a success message, "Notification successfully sent."

**Step 4:** Click on "**Save**" button.

![flows-pager-duty-4](../assets/flows/actions/flows-pager-duty-4-light.png#only-light)
![flows-pager-duty-4](../assets/flows/actions/flows-pager-duty-4-dark.png#only-dark)

## HTTP

![flows-http](../assets/flows/actions/flows-http-light.png#only-light)
![flows-http](../assets/flows/actions/flows-http-dark.png#only-dark)

| Notification | Description |
|-------|--------|
| [**Webhook**](#weebhook) | This will send notifications using webhooks, making it easy to stay updated in real time |
| [**HTTP Action**](#http-action) | This will send updates or alerts directly to a specified server endpoint |

### Weebhook

Qualytics allows you to connect external apps for notifications using webhooks, making it easy to stay updated in real time. When you set up a webhook, it sends an instant alert to the connected app whenever a specific event or condition occurs. This means you can quickly notify about important events as they happen and respond right away. By using webhook notifications, you can keep your system running smoothly, keep everyone informed, and manage your operations more efficiently.

**Step 1:** Select Weebhook notification

![flows-option-6](../assets/flows/actions/flows-option-6-light.png#only-light)
![flows-option-6](../assets/flows/actions/flows-option-6-dark.png#only-dark)

**Step 2:** Add a Weebhook URL

![flows-weebhook-1](../assets/flows/actions/flows-weebhook-1-light.png#only-light)
![flows-weebhook-1](../assets/flows/actions/flows-weebhook-1-dark.png#only-dark)

!!! info
    You can only add one URL per Node

**Step 3:** Add a message

![flows-weebhook-2](../assets/flows/actions/flows-weebhook-2-light.png#only-light)
![flows-weebhook-2](../assets/flows/actions/flows-weebhook-2-dark.png#only-dark)

!!! info
    You can click on "Test HTTP" button to send a test notification to the webhook URL you provided. If the webhook URL is correct, you will receive a confirmation message saying "Notification successfully sent." This indicates that the webhook is functioning correctly.

**Step 4:** Click on "**Save**" button.

![flows-weebhook-3](../assets/flows/actions/flows-weebhook-3-light.png#only-light)
![flows-weebhook-3](../assets/flows/actions/flows-weebhook-3-dark.png#only-dark)

### HTTP Action

Integrating HTTP Action notifications allows users to receive timely updates or alerts directly to a specified server endpoint. By setting up HTTP Action notifications with specific trigger conditions, you can ensure that you are instantly informed about critical events, such as operation completions or anomalies detected. This approach enables you to take immediate action when necessary, helping to address issues quickly and maintain the smooth and efficient operation of your processes.

**Step 1:** Select HTTP Action notification

![flows-option-7](../assets/flows/actions/flows-option-7-light.png#only-light)
![flows-option-7](../assets/flows/actions/flows-option-7-dark.png#only-dark)

**Step 2:** Add an Action URL

![flows-http-action-1](../assets/flows/actions/flows-weebhook-1-light.png#only-light)
![flows-http-action-1](../assets/flows/actions/flows-weebhook-1-dark.png#only-dark)

!!! info
    You can only add one URL per Node

**Step 3:** Add HTTP Verb

![flows-http-action-2](../assets/flows/actions/flows-http-action-2-light.png#only-light)
![flows-http-action-2](../assets/flows/actions/flows-http-action-2-dark.png#only-dark)

**Step 4:** Add User Name

![flows-http-action-3](../assets/flows/actions/flows-http-action-3-light.png#only-light)
![flows-http-action-3](../assets/flows/actions/flows-http-action-3-dark.png#only-dark)

**Step 5:** Select an Auth Type. The table below will show all auth available.

![flows-http-action-4](../assets/flows/actions/flows-http-action-4-light.png#only-light)
![flows-http-action-](../assets/flows/actions/flows-http-action-4-dark.png#only-dark)

| Auth Type |
|-------|
| bearer |
| basic |
| digest |

**Step 6:** Add Secreat

![flows-http-action-5](../assets/flows/actions/flows-http-action-5-light.png#only-light)
![flows-http-action-5](../assets/flows/actions/flows-http-action-5-dark.png#only-dark)

**Step 7:** Add a message

![flows-http-action-6](../assets/flows/actions/flows-http-action-6-light.png#only-light)
![flows-http-action-6](../assets/flows/actions/flows-http-action-6-dark.png#only-dark)

!!! info
    You can click on "Test HTTP" button to verify the correctness of the Action URL. If the URL is correct, a confirmation message saying "Notification successfully sent" will appear, confirming that the HTTP action is set up and functioning properly.

**Step 8:** Click on "**Save**" button.

![flows-http-action-7](../assets/flows/actions/flows-http-action-7-light.png#only-light)
![flows-http-action-7](../assets/flows/actions/flows-http-action-7-dark.png#only-dark)