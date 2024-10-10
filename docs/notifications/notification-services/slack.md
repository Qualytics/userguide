# Slack Notification

To set up Slack notifications, start by naming your notification and selecting the triggers, such as operation completion or anomaly detection. Next, add relevant tags and configure the Slack Webhook URL to connect directly to your Slack channel. 

## Navigation to Notifications

**Step 1:** Log in to your Qualytics account and click the **Settings** button on the left side panel of the interface. 

![settings](../../assets/notifications/services/slack/settings-light-1.png#only-light)
![settings](../../assets/notifications/services/slack/settings-dark-1.png#only-dark)

## Add Slack Notification

**Step 1:** Click on the **Add Notifications** button located in the top right corner.

![add-notification](../../assets/notifications/services/slack/add-notification-light-3.png#only-light)
![add-notification](../../assets/notifications/services/slack/add-notification-dark-3.png#only-dark)

A modal window **Add Notification Rule** will appear providing you with fields to set notification rules.

![modal-window](../../assets/notifications/services/slack/modal-window-light-4.png#only-light)
![modal-window](../../assets/notifications/services/slack/modal-window-dark-4.png#only-dark)

**Step 2:** Enter the following details to add the notification rule.

**1. Name:** Enter a specific and descriptive title to your notification rule to easily identify its purpose.

**2. Description:** Provide a brief description of what the notification rule does or when it should trigger.

![enter-details](../../assets/notifications/services/slack/enter-details-light-55.png#only-light)
![enter-details](../../assets/notifications/services/slack/enter-details-dark-55.png#only-dark)

**3. Trigger When**: Select the event or condition from the dropdown menu that will trigger the notification. Below is the list of available events you can choose from:

- **Operation Completion:** This type of notification is triggered whenever an operation, such as a catalog, profile, or scan, is completed on a source datastore. Upon completion, teams are promptly notified through in-app messages, and a slack is triggered to send notifications to external systems or applications. For example, when a catalog operation is completed, a slack notification is sent, allowing the team to proceed with the profile operation on the datastore efficiently. 

- **An Anomaly is Identified:** This type of notification is triggered when any single anomaly is identified in the data. The notification message typically includes the type of anomaly detected and the datastore where it was found. It provides specific information about the anomaly type, which helps quickly understand the issue's nature.

!!! tip
    Users can specify a minimum anomaly weight for this trigger condition. This threshold ensures that only anomalies with a weight equal to or greater than the specified value will trigger a notification. If no value is set, all detected anomalies, regardless of their weight, will generate notifications. This feature helps prioritize alerts based on the importance of the anomalies, allowing users to focus on more critical issues.

!!! tip
    Users can specify check rule types for this trigger condition. This selection ensures that only anomalies identified by the chosen rule types will trigger a notification. If no check rule types are selected, this filter will be ignored, resulting in all anomalies generating notifications. This feature enables users to prioritize alerts based on specific criteria, allowing them to focus on the most relevant issues.

- **Anomalies are Detected in a Table or File:** This notification is triggered when multiple anomalies are detected within a specific table, file and check rule types. It includes information about the number of anomalies found and the specific scan target within the datastore. This is useful for assessing the overall health of a particular datastore. No concept of weights. 

| Factors | An Anomaly is Identified | Anomalies are Detected in a Table or File |
|---------|--------|--------|
| Trigger Event | Notifies for individual anomaly detection | Notifies for multiple anomalies within a specific table or file |
| Notification Content | Focuses on the type of anomaly and the affected datastore. | Provide a count of anomalies and specifies the scan target within the datastore. |
| Notification Targeting  | Tags, Weight and Check Rule Types  | Tags,Check Rule Types or both  |

![enter-details](../../assets/notifications/services/slack/enter-details-light-5.png#only-light)
![enter-details](../../assets/notifications/services/slack/enter-details-dark-5.png#only-dark)

**4.** **Message:** Enter your custom message using variables in the Message field, where you can specify the content of the notification that will be sent out. 

!!! tip 
    You can write your custom notification message by utilizing the autocomplete feature. This feature allows you to easily insert internal variables such as **{{rule_name}}**, **{{container_name}}**, and **{{datastore_name}}**. As you start typing, the autocomplete will suggest and recommend relevant variables in the dropdown. 

![message](../../assets/notifications/services/slack/message-light-6.png#only-light)
![message](../../assets/notifications/services/slack/message-dark-6.png#only-dark)

**5.** **Datastore Tags:** Use the drop-down menu to **select the datastore tags**. Notifications will be generated for only those source datastores that have the datastore tags you select in this step. For example, if you select **critical** datastore tag from the dropdown menu, notifications will be generated only for source datastores having the "critical" tag applied to them. 

!!! note 
    If you choose "An Anomaly is Detected" as the trigger condition, you must define the Anomaly Tag, set a minimum anomaly weight, and select the check rule types. This ensures that only anomalies with a weight equal to or greater than the specified value and matching the selected check rule types will trigger a notification. If no weight or check rule types are specified, these filters will be ignored.

![tags](../../assets/notifications/services/slack/tags-light-7.png#only-light)
![tags](../../assets/notifications/services/slack/tags-dark-7.png#only-dark)

**6. Notification Channel:** Select **Slack** as your notification channel and enter the **Webhook URL** where you want the notification to be sent.

!!! info
    Check [here](https://api.slack.com/messaging/webhooks) for the official Slack documentation how to create or configure the Slack webhook URL.

![slack-channel](../../assets/notifications/services/slack/slack-channel-light-8.png#only-light)
![slack-channel](../../assets/notifications/services/slack/slack-channel-dark-8.png#only-dark)

## Test Slack Notification

**Step 1:** Click the **"Test Notification"** button to send a test message to the provided **Webhook URL**. If the message is successfully sent, you will receive a confirmation notification indicating **"Notification successfully sent".**

![test-notification](../../assets/notifications/services/slack/test-notification-light-9.png#only-light)
![test-notification](../../assets/notifications/services/slack/test-notification-dark-9.png#only-dark)

**Step 2:** The test email will be sent to the Webhook URL address you have provided.This verifies that the address provided is correct .

![recieve-notification](../../assets/notifications/services/slack/recieve-notification-light-10.png#only-light)
![recieve-notification](../../assets/notifications/services/slack/recieve-notification-light-10.png#only-dark)

## Save Slack Notification

**Step 1:** Once you have entered all the values and selected **Slack** as notification channels, then click on the **Save** button.

![save-button](../../assets/notifications/services/slack/save-button-light-11.png#only-light)
![save-button](../../assets/notifications/services/slack/save-button-dark-11.png#only-dark)

After clicking the Save button, a message will appear on the screen saying **"Notification Successfully Created".**

![created-notification](../../assets/notifications/services/slack/created-notification-light-12.png#only-light)
![created-notification](../../assets/notifications/services/slack/created-notification-dark-12.png#only-dark)

## Post Results

Once you’ve saved your notification rules settings, all real-time notifications will be sent to the Webhook URL address you specified, ensuring you receive them directly in your Slack Webhook.

For example when an operation is completed, or if any anomalies are detected in a table or file, a notification will be sent to the Slack Webhook you provided.This ensures you are promptly alerted to critical events or irregularities, enabling immediate action when necessary. By providing real-time updates, it helps maintain the integrity and smooth operation of your processes.

![live-notification](../../assets/notifications/services/slack/live-notification-light-13.png#only-light)
![live-notification](../../assets/notifications/services/slack/live-notification-light-13.png#only-dark)
