# Webhook Notifications

Qualytics allows you to connect external apps for notifications using webhooks, making it easy to stay updated in real time. When you set up a webhook, it sends an instant alert to the connected app whenever a specific event or condition occurs. This means you can quickly notify about important events as they happen and respond right away. By using webhook notifications, you can keep your system running smoothly, keep everyone informed, and manage your operations more efficiently.

Let’s get started 🚀

## Navigation to Notifications

**Step 1:** Log in to your Qualytics account and click the **Settings** button on the left side panel of the interface. 

![setting](../../assets/notifications/services/webhook/setting-light-1.png#only-light)
![setting](../../assets/notifications/services/webhook/setting-dark-1.png#only-dark)

## Add Webhook Notification

By adding a webhook of any external application where you want to send your notifications, you'll receive real-time alerts whenever specific conditions or events occur like an operation is complete or an anomaly is detected within a table or file.

**Step 1:** Click on the **Add Notifications** button located in the top right corner.

![add-notification](../../assets/notifications/services/webhook/add-notification-light-3.png#only-light)
![add-notification](../../assets/notifications/services/webhook/add-notification-dark-3.png#only-dark)

A modal window **Add Notification Rule** will appear providing you with fields to set notification rules.

![notification-rule](../../assets/notifications/services/webhook/notification-rule-light-4.png#only-light)
![notification-rule](../../assets/notifications/services/webhook/notification-rule-dark-4.png#only-dark)

**Step 2:** Enter the following details to add the notification rule.

**1. Name:** Enter a specific and descriptive title to your notification rule to easily identify its purpose.

**2. Description:** Provide a brief description of what the rule does or when it should trigger.

![name](../../assets/notifications/services/webhook/name-light-5.png#only-light)
![name](../../assets/notifications/services/webhook/name-dark-5.png#only-dark)

**3. Trigger When**: Select the event or condition from the dropdown menu that will trigger the notification. Below is the list of available events you can choose from:

- **Operation Completion:** This type of notification is triggered whenever an operation, such as a catalog, profile, or scan, is completed on a source datastore. Upon completion, teams are promptly notified through in-app messages, and a webhook is triggered to send notifications to external systems or applications. For example, when a catalog operation is completed, a webhook notification is sent, allowing the team to proceed with the profile operation on the datastore efficiently.

- **An Anomaly is Identified:** This type of notification is triggered when any single anomaly is identified in the data. The notification message typically includes the type of anomaly detected and the datastore where it was found. It provides specific information about the anomaly type, which helps quickly understand the issue's nature.

!!! tip
    Users can specify a minimum anomaly weight for this trigger condition. This threshold ensures that only anomalies with a weight equal to or greater than the specified value will trigger a notification. If no value is set, all detected anomalies, regardless of their weight, will generate notifications. This feature helps prioritize alerts based on the importance of the anomalies, allowing users to focus on more critical issues.

!!! tip
    Users can specify check rule types for this trigger condition. This selection ensures that only anomalies identified by the chosen rule types will trigger a notification. If no check rule types are selected, this filter will be ignored, resulting in all anomalies generating notifications. This feature enables users to prioritize alerts based on specific criteria, allowing them to focus on the most relevant issues.

- **Anomalies are Detected in a Table or File:** This notification is triggered when multiple anomalies are detected within a specific table, file and check rule types. It includes information about the number of anomalies found and the specific scan target within the datastore. This is useful for assessing the overall health of a particular datastore. No concept of weights. 

| Factors | An Anomaly is Identified | Anomalies are Detected in a Table or File |
|--------|--------|--------|
| Trigger Event | Notifies for individual anomaly detection | Notifies for multiple anomalies within a specific table or file |
| Notification Content | Focuses on the type of anomaly and the affected datastore. | Provide a count of anomalies and specifies the scan target within the datastore. |
| Notification Targeting  | Tags, Weight and Check Rule Types  | Tags, Check Rule Types or both  |

![conditions](../../assets/notifications/services/webhook/conditions-light-6.png#only-light)
![conditions](../../assets/notifications/services/webhook/conditions-dark-6.png#only-dark)

**4.** **Message:** Enter your custom message using variables in the **Message** field, where you can specify the content of the notification that will be sent out. 

!!! tip 
    You can write your custom notification message by utilizing the autocomplete feature. This feature allows you to easily insert internal variables such as **{{rule_name}}**, **{{container_name}}**, and **{{datastore_name}}**. As you start typing, the autocomplete will suggest and recommend relevant variables in the dropdown.

![message](../../assets/notifications/services/webhook/message-light-7.png#only-light)
![message](../../assets/notifications/services/webhook/message-dark-7.png#only-dark)

**5.** **Datastore Tags:** Use the drop-down menu to **select the datastore tags**. Notifications will be generated for only those source datastores that have the datastore tags you select in this step. For example, if you select the **"critical"** datastore tag from the dropdown menu, notifications will be generated only for source datastores having the "critical" tag applied to them. 

!!! note 
    If you choose "An Anomaly is Detected" as the trigger condition, you must define the Anomaly Tag, set a minimum anomaly weight, and select the check rule types. This ensures that only anomalies with a weight equal to or greater than the specified value and matching the selected check rule types will trigger a notification. If no weight or check rule types are specified, these filters will be ignored.

![tag](../../assets/notifications/services/webhook/tag-light-8.png#only-light)
![tag](../../assets/notifications/services/webhook/tag-dark-8.png#only-dark)

**Step 6:** Select **"Webhook"** as the notification channel and enter the desired **"Webhook URL"** of the target system where you want to receive notifications.

!!! info 
    Please refer to the official documentation of the target system for detailed instructions on how to create or configure the webhook URL.

![channel](../../assets/notifications/services/webhook/channel-light-9.png#only-light)
![channel](../../assets/notifications/services/webhook/channel-dark-9.png#only-dark)

## Test Webhook Notification

This feature lets you send a test message to your configured webhook URL to verify that it is correctly set up and receiving notifications. It helps ensure that your integration is working before real events trigger alerts.

**Step 1:** Click on the **"Test Notification"** button to send a test notification to the webhook URL you provided. If the webhook URL is correct, you will receive a confirmation message saying **"Notification successfully sent."** This indicates that the webhook is functioning correctly.

![test](../../assets/notifications/services/webhook/test-light-10.png#only-light)
![test](../../assets/notifications/services/webhook/test-dark-10.png#only-dark)

The test also triggers a payload and sends an HTTP POST request to the configured URL endpoint. It confirms that the webhook is correctly configured and that notifications will be sent to the intended endpoint when real events occur.

![test-notification](../../assets/notifications/services/webhook/test-notification-11.png#only-light)
![test-notification](../../assets/notifications/services/webhook/test-notification-11.png#only-dark)

## Save Webhook Notification

Once you have provided all the necessary values, set the trigger conditions for the notification, and test the notification, click the **"Save"** button.

![save](../../assets/notifications/services/webhook/save-light-12.png#only-light)
![save](../../assets/notifications/services/webhook/save-dark-12.png#only-dark)

After clicking the **“Save”** button, a success message will be displayed saying "Notification Successfully Created".

![success](../../assets/notifications/services/webhook/success-light-13.png#only-light)
![success](../../assets/notifications/services/webhook/success-dark-13.png#only-dark)

## Post Results

After setting up a notification in Qualytics to be sent via webhook, the system watches for the specific events or conditions you've defined. When one of these events happens, the webhook is triggered, and Qualytics sends an HTTP POST request to the external application's URL. This request contains detailed information about the event, enabling the external application to take action. 

As a result, the external application can update dashboards, trigger alerts, or integrate the data into workflows in real-time. This ensures you can quickly respond to important events or data changes in Qualytics.

![notification-send](../../assets/notifications/services/webhook/notification-send-14.png#only-light)
![notification-send](../../assets/notifications/services/webhook/notification-send-14.png#only-dark)
