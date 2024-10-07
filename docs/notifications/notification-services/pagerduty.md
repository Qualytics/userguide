#  PagerDuty Notification

Integrating PagerDuty with Qualytics ensures that your team gets instant alerts for critical data events and system issues. With this connection, you can automatically receive real-time notifications about anomalies, operation completions and other important events directly in your PagerDuty account. By categorizing alerts based on severity, it ensures the right people are notified at the right time, speeding up decision-making and resolving incidents efficiently. This helps your team respond quickly to issues, reducing downtime and keeping data operations on track. 

## Navigation to Notifications

**Step 1:** Log in to your Qualytics account and click the **Notification Rules** button on the left side panel of the interface.

![setting](../../../assets/notifications/services/pagerduty/notification-rule-light-1.png#only-light)
![setting](../../../assets/notifications/services/pagerduty/notification-rule-dark-1.png#only-dark)

## Add PagerDuty Notification

**Step 1:** Click on the **Add Notifications** button located in the top right corner.

![add-notifications](../../../assets/notifications/services/pagerduty/add-notifications-light-3.png#only-light)
![add-notifications](../../../assets/notifications/services/pagerduty/add-notifications-dark-3.png#only-dark)

A modal window **Add Notification Rule** will appear providing you with fields to set notification rules.

![notification-rule](../../../assets/notifications/services/pagerduty/notification-rule-light-4.png#only-light)
![notification-rule](../../../assets/notifications/services/pagerduty/notification-rule-dark-4.png#only-dark)

**Step 2:** Enter the following details to add the notification rule.

**1. Name:** Enter a specific and descriptive title to your notification rule to easily identify its purpose.

**2. Description:** Provide a brief description of what the notification rule does or when it should trigger.

![notification-rule](../../../assets/notifications/services/pagerduty/name-description-light.png#only-light)
![notification-rule](../../../assets/notifications/services/pagerduty/name-description-dark.png#only-dark)

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

![conditions](../../../assets/notifications/services/pagerduty/conditions-light-5.png#only-light)
![conditions](../../../assets/notifications/services/pagerduty/conditions-dark-5.png#only-dark)

**4.** **Message:** Enter your custom message using variables in the Message field, where you can specify the content of the notification that will be sent out. 

!!! tip
    You can write your custom notification message by utilizing the autocomplete feature. This feature allows you to easily insert internal variables such as **{{rule_name}}**, **{{container_name}}**, and **{{datastore_name}}**. As you start typing, the autocomplete will suggest and recommend relevant variables in the dropdown.

![message](../../../assets/notifications/services/pagerduty/message-light-6.png#only-light)
![message](../../../assets/notifications/services/pagerduty/message-dark-6.png#only-dark)

**5. Datastore Tags:** Use the drop-down menu to **select the datastore tags**. Notifications will be generated for only those source datastores that have the datastore tags you select in this step. For example, if you select the **“critical”** datastore tag from the dropdown menu, notifications will be generated only for source datastores having the "critical" tag applied to them. 

!!! note
    If you choose **"An Anomaly is Detected"** as the trigger condition, you must define the Anomaly Tag, set a minimum anomaly weight, and select the check rule types. This ensures that only anomalies with a weight equal to or greater than the specified value and matching the selected check rule types will trigger a notification. If no weight or check rule types are specified, these filters will be ignored.

![tag](../../../assets/notifications/services/pagerduty/tags-light-7.png#only-light)
![tag](../../../assets/notifications/services/pagerduty/tags-dark-7.png#only-dark) 

**6. Notification Channel:** Select **PagerDuty** as your notification channel and enter the **Integration Key** where you want the notification to be sent.

!!! info 
    For detailed instructions on creating or configuring the PagerDuty integration, please refer to the PagerDuty documentation available [here](https://support.pagerduty.com/docs/services-and-integrations).

![channel](../../../assets/notifications/services/pagerduty/channel-light-8.png#only-light)
![channel](../../../assets/notifications/services/pagerduty/channel-dark-8.png#only-dark)

**7. Severity:** Select the appropriate PagerDuty severity level to categorize incidents based on their urgency and impact. The available severity levels are:

- **Info:** For informational messages that don't require immediate action but provide helpful context.

- **Warning:** For potential issues that may need attention but aren't immediately critical.

- **Error:** For significant problems that require prompt resolution to prevent disruption.

- **Critical:** For urgent issues that demand immediate attention due to their severe impact on system operations.

![severity](../../../assets/notifications/services/pagerduty/severity-light-9.png#only-light)
![severity](../../../assets/notifications/services/pagerduty/severity-dark-9.png#only-dark)

## Test PagerDuty Notification

Click on the **Test notification** button to check if the integration key is functioning correctly. Once the test notification is sent, you will see a success message, **"Notification successfully sent."** 

This confirms that the integration is properly configured and that the PagerDuty account will receive notifications as expected.

![test](../../../assets/notifications/services/pagerduty/test-light-10.png#only-light)
![test](../../../assets/notifications/services/pagerduty/test-dark-10.png#only-dark)

## Save PagerDuty Notification

**Step 1:** Once you have entered all the values and selected **PagerDuty** as notification channels, then click on the **Save** button.

![save](../../../assets/notifications/services/pagerduty/save-light-11.png#only-light)
![save](../../../assets/notifications/services/pagerduty/save-dark-11.png#only-dark)

After clicking the **Save** button, a success flash message will be displayed saying **"Notification Successfully Created".**

![success](../../../assets/notifications/services/pagerduty/success-light-12.png#only-light)
![success](../../../assets/notifications/services/pagerduty/success-dark-12.png#only-dark)

## Post Results

Once you’ve saved the PagerDuty notification rule, all real-time notifications will be sent to the integration key you specified,

For example, when an operation is completed or an anomaly is detected in a table or file, a notification will be sent to the integration key you provided. This keeps you informed of critical events in real-time, allowing you to take quick action to maintain smooth operations.

![pagerduty](../../../assets/notifications/services/pagerduty/pagerduty-13.png#only-light)
![pagerduty](../../../assets/notifications/services/pagerduty/pagerduty-13.png#only-dark)
