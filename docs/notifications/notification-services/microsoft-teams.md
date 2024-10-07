#  Microsoft Teams Notification

Integrating Microsoft Teams notifications allows users to receive timely updates or alerts directly in their Teams channel. By setting up Microsoft Teams notifications with specific trigger conditions, you can ensure that you are instantly informed about critical events, such as operation completions or anomalies detected. This approach allows you to take immediate action when necessary, helping to address issues quickly and maintain the smooth and efficient operation of your processes.

## Navigation to Notifications

**Step 1:** Log in to your Qualytics account and click the **“Notification Rules”** button on the left side panel of the interface. 

![settings](../../assets/notifications/services/microsoft-teams/notification-rule-light-1.png#only-light)
![settings](../../assets/notifications/services/microsoft-teams/notification-rule-dark-1.png#only-dark)

## **Add Microsoft Teams Notification**

**Step 1:** Click on the **“Add Notifications”** button located in the top right corner.

![add-notification](../../assets/notifications/services/microsoft-teams/add-notification-light-3.png#only-light)
![add-notification](../../assets/notifications/services/microsoft-teams/add-notification-dark-3.png#only-dark)

A modal window **“Add Notification Rule”** will appear providing you with options to set notification rules. 

![notification-rule](../../assets/notifications/services/microsoft-teams/notification-rule-light-4.png#only-light)
![notification-rule](../../assets/notifications/services/microsoft-teams/notification-rule-dark-4.png#only-dark)

**Step 2:** Enter the following details to add the notification rule.

**1. Name:** Enter a specific and descriptive title to your notification rule to easily identify its purpose.

**2. Description:** Provide a brief description of what the notification rule does or when it should trigger.

![notification-rule](../../assets/notifications/services/microsoft-teams/notification-rule-light-44.png#only-light)
![notification-rule](../../assets/notifications/services/microsoft-teams/notification-rule-dark-44.png#only-dark)

**3. Trigger When**: Select the event or condition from the dropdown menu that will trigger the notification. Below is the list of available events you can choose from:

- **Operation Completion:** This type of notification is triggered whenever an operation, such as a catalog, profile, or scan, is completed on a source datastore. Upon completion, teams are promptly notified through in-app notifications and, the Microsoft Teams channel. For example, the team is notified whenever the catalog operation is completed, helping them proceed with the profile operation on the datastore. 

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

![triggered-condition](../../assets/notifications/services/microsoft-teams/triggered-condition-light-5.png#only-light)
![triggered-condition](../../assets/notifications/services/microsoft-teams/triggered-condition-dark-5.png#only-dark)

**4.** **Message:** Enter your custom message using variables in the **Message** field, where you can specify the content of the notification that will be sent out. 

!!! tip
    You can write your custom notification message by utilizing the autocomplete feature. This feature allows you to easily insert internal variables such as **{{rule_name}}**, **{{container_name}}**, and **{{datastore_name}}**. As you start typing, the autocomplete will suggest and recommend relevant variables in the dropdown.

![message](../../assets/notifications/services/microsoft-teams/message-light-6.png#only-light)
![message](../../assets/notifications/services/microsoft-teams/message-dark-6.png#only-dark)

**5.** **Datastore Tags:** Use the drop-down menu to **select the datastore tags**. Notifications will be generated for only those source datastores that have the datastore tags you select in this step. For example, if you select **“critical”** datastore tag from the dropdown menu, notifications will be generated only for source datastores having the "critical" tag applied to them. 

!!! note
    If you choose **"An Anomaly is Detected"** as the trigger condition, you must define the Anomaly Tag, set a minimum anomaly weight, and select the check rule types. This ensures that only anomalies with a weight equal to or greater than the specified value and matching the selected check rule types will trigger a notification. If no weight or check rule types are specified, these filters will be ignored.
    
![tags](../../assets/notifications/services/microsoft-teams/tags-light-7.png#only-light)
![tags](../../assets/notifications/services/microsoft-teams/tags-dark-7.png#only-dark)

**6. Notification Channel:** Select **“Microsoft Teams”** as your notification channel and enter the **“Webhook URL”** where you want the notification to be sent.

![microsoft-team](../../assets/notifications/services/microsoft-teams/microsoft-team-light-8.png#only-light)
![microsoft-team](../../assets/notifications/services/microsoft-teams/microsoft-team-dark-8.png#only-dark)

## Test Microsoft Teams Notification

**Step 1.** Click the **"Test Notification"** button to send a test message to the provided **“Webhook URL”**. If the message is successfully sent, you will receive a confirmation notification indicating **"Notification successfully sent".**

![test](../../assets/notifications/services/microsoft-teams/test-light-9.png#only-light)
![test](../../assets/notifications/services/microsoft-teams/test-dark-9.png#only-dark)

**Step 2:** The **test notification** will be sent to the Webhook URL address you have provided. This verifies that the address provided is correct.

![test-notification](../../assets/notifications/services/microsoft-teams/test-notification-10.png#only-light)
![test-notification](../../assets/notifications/services/microsoft-teams/test-notification-10.png#only-dark)

## **Save Microsoft Teams Notification**

**Step 1:** Once you have entered all the values and selected **“Microsoft Teams”** as notification channels, then click on the **“Save”** button.

![save](../../assets/notifications/services/microsoft-teams/save-light-11.png#only-light)
![save](../../assets/notifications/services/microsoft-teams/save-dark-11.png#only-dark)

After clicking the Save button, a message will appear on the screen saying **"Notification Successfully Created".**

![notification-created](../../assets/notifications/services/microsoft-teams/notification-created-light-12.png#only-light)
![notification-created](../../assets/notifications/services/microsoft-teams/notification-created-dark-12.png#only-dark)

## Post Results

Once you’ve saved your notification rules settings, all real-time notifications will be sent to the Webhook URL address you specified, ensuring you receive them directly in your Microsoft Teams channel.

For example when an operation is completed, or if any anomalies are detected in a table or file, a notification will be sent to the Microsoft Teams channel as configured. This ensures you are promptly alerted to critical events or irregularities, enabling immediate action when necessary. By providing real-time updates, it helps maintain the integrity and smooth operation of your processes.

![post-result](../../assets/notifications/services/microsoft-teams/post-result-13.png#only-light)
![post-result](../../assets/notifications/services/microsoft-teams/post-result-13.png#only-dark)
