#  Email Notification

Adding email notifications allows users to receive timely updates or alerts directly in their inbox.  By setting up notifications with specific triggers and channels, you can ensure that you are promptly informed about critical events, such as operation completions or detected anomalies. This proactive approach allows you to take immediate action when necessary, helping to address issues quickly and maintain the smooth and efficient operation of your processes.

Let’s get started 🚀

## Navigation to Notifications

Log in to your Qualytics account and click the **"Notification Rules** button on the left side panel of the interface. 

![notification-rule](../../assets/notifications/services/email/notification-rule-light-1.png#only-light)
![notification-rule](../../assets/notifications/services/email/notification-rule-dark-1.png#only-dark)

## Add Email Notification

**Step 1:** Click on the **Add Notifications** button located in the top right corner.

![add-notification](../../assets/notifications/services/email/add-notification-light-3.png#only-light)
![add-notification](../../assets/notifications/services/email/add-notification-dark-3.png#only-dark)

A modal window **Add Notification Rule** will appear providing you with fields to set notification rules.  

![modal-window](../../assets/notifications/services/email/modal-window-light-4.png#only-light)
![modal-window](../../assets/notifications/services/email/modal-window-dark-4.png#only-dark)

**Step 2:** Enter the following details to add the notification rule.

**1. Name:** Enter a specific and descriptive title to your notification rule to easily identify its purpose.

**2. Description:** Provide a brief description of what the notification rule does or when it should trigger.

![name-description](../../assets/notifications/services/email/name-description-light.png#only-light)
![name-description](../../assets/notifications/services/email/name-description-dark.png#only-dark)

**3. Trigger When**: Select the event or condition from the dropdown menu that will trigger the notification. Below is the list of available events you can choose from:

- **Operation Completion:** This type of notification is triggered whenever an operation, such as a catalog, profile, or scan, is completed on a source datastore. Upon completion, teams are promptly notified through in-app messages and, if configured, via external notification channels such as email, Slack, Microsoft Teams, and others. For example, the team is notified whenever the catalog operation is completed, helping them proceed with the profile operation on the datastore. 

- **An Anomaly is Identified:** This type of notification is triggered when any single anomaly is identified in the data. The notification message typically includes the type of anomaly detected and the datastore where it was found. It provides specific information about the anomaly type, which helps quickly understand the issue's nature.

!!! tip 
    Users can specify a minimum anomaly weight for this trigger condition. This threshold ensures that only anomalies with a weight equal to or greater than the specified value will trigger a notification. If no value is set, all detected anomalies, regardless of their weight, will generate notifications. This feature helps prioritize alerts based on the importance of the anomalies, allowing users to focus on more critical issues. 

!!! tip
    Users can specify check rule types for this trigger condition. This selection ensures that only anomalies identified by the chosen rule types will trigger a notification. If no check rule types are selected, this filter will be ignored, resulting in all anomalies generating notifications. This feature enables users to prioritize alerts based on specific criteria, allowing them to focus on the most relevant issues.

- **Anomalies are Detected in a Table or File:** This notification is triggered when multiple anomalies are detected within a specific table, file and check rule types. It includes information about the number of anomalies found and the specific scan target within the datastore. This is useful for assessing the overall health of a particular datastore. No concept of weights.  

| Factors | An Anomaly is Identified | Anomalies are Detected in a Table or File |
|--------|--------|-------|
| Trigger Event | Notifies for individual anomaly detection | Notifies for multiple anomalies within a specific table or file |
| Notification Content | Focuses on the type of anomaly and the affected datastore. | Provide a count of anomalies and specifies the scan target within the datastore. |
| Notification Targeting  | Tags, Weight and Check Rule Types  | Tags, Check Rule Types or both  |

![trigger-condition](../../assets/notifications/services/email/trigger-condition-light-5.png#only-light)
![trigger-condition](../../assets/notifications/services/email/trigger-condition-dark-5.png#only-dark)

**4.** **Message:** Enter your custom message using variables in the Message field, where you can specify the content of the notification that will be sent out. 

!!! tip 
    You can write your custom notification message by utilizing the autocomplete feature. This feature allows you to easily insert internal variables such as **{{rule_name}}**, **{{container_name}}**, and **{{datastore_name}}**. As you start typing, the autocomplete will suggest and recommend relevant variables in the dropdown. 

![message](../../assets/notifications/services/email/message-light-6.png#only-light)
![message](../../assets/notifications/services/email/message-dark-6.png#only-dark)

**5.** **Datastore Tags:** Use the drop-down menu to **select the datastore tags**. Notifications will be generated for only those source datastores that have the datastore tags you select in this step. For example, if you select **critical** datastore tag from the dropdown menu, notifications will be generated only for source datastores having the "critical" tag applied to them. 

!!! note 
    If you choose **"An Anomaly is Detected"** as the trigger condition, you must define the Anomaly Tag, set a minimum anomaly weight, and select the check rule types. This ensures that only anomalies with a weight equal to or greater than the specified value and matching the selected check rule types will trigger a notification. If no weight or check rule types are specified, these filters will be ignored. 

![tags](../../assets/notifications/services/email/tags-light-7.png#only-light)
![tags](../../assets/notifications/services/email/tags-dark-7.png#only-dark)

**6. Notification Channel:** Select **Email** as your notification channel and enter the **Email Address** where you want the notification to be sent.  

![email-channel](../../assets/notifications/services/email/email-channel-light-8.png#only-light)
![email-channel](../../assets/notifications/services/email/email-channel-dark-8.png#only-dark)

## Test Email Notification

**Step 1.** Click the **Test Notification** button to send a test email to the provided address. If the email is successfully sent, you will receive a confirmation message indicating **Notification successfully sent**

![test-notification](../../assets/notifications/services/email/test-notification-light-9.png#only-light)
![test-notification](../../assets/notifications/services/email/test-notification-dark-9.png#only-dark)

**Step 2:** The test email will be sent to the address you have provided. This verifies that the address provided is correct.

![recieve-notification](../../assets/notifications/services/email/recieve-notification-light-10.png#only-light)
![recieve-notification](../../assets/notifications/services/email/recieve-notification-light-10.png#only-dark)

## Save Email Notification

**Step 1:** Once you have entered all the values and selected **Email** as notification channels, then click on the **Save** button.

![save-button](../../assets/notifications/services/email/save-button-light-11.png#only-light)
![save-button](../../assets/notifications/services/email/save-button-dark-11.png#only-dark)

After clicking the Save button, a success message will be displayed saying **Notification Successfully Created.**

![created-notification](../../assets/notifications/services/email/created-notification-light-12.png#only-light)
![created-notification](../../assets/notifications/services/email/created-notification-dark-12.png#only-dark)

## Post Results

Once you’ve saved your notification rules settings, all real-time notifications will be sent to the email address you specified, ensuring you receive them directly in your inbox.  

For example when an operation is completed, or if any anomalies are detected in a table or file, a notification will be sent to the email address you provided.This ensures you are promptly alerted to critical events or irregularities, enabling immediate action when necessary. By providing real-time updates, it helps maintain the integrity and smooth operation of your processes.

![live-notification](../../assets/notifications/services/email/live-notification-light-13.png#only-light)
![live-notification](../../assets/notifications/services/email/live-notification-light-13.png#only-dark)

