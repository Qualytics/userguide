# Notifications: Overview

Notifications in Qualytics offer a powerful system for delivering crucial alerts and updates across various communication channels. By setting up notification rules with specific triggers and channels, users can ensure timely awareness of critical events. This functionality enhances productivity, optimizes incident response, and promotes effective data management within the Qualytics platform.

Let’s get started 🚀

## Multiple Notification Channels

Qualytics emphasizes the configuration of multiple notification channels, which are crucial for ensuring that important alerts and updates reach users effectively through various platforms.

### In-App Notifications

In-app notifications in Qualytics are real-time alerts that keep users informed about various events related to their data operations and quality checks. These notifications are displayed within the Qualytics interface and cover a range of activities, including operation completions, anomaly detections, and service level agreement (SLA) status updates. 

![notifications](../../assets/notifications/notifications-light-1.png#only-light){: style="height:350px;width:350px;"}
![notifications](../../assets/notifications/notifications-dark-1.png#only-dark){: style="height:350px;width:350px;"}

### External Platforms

Qualytics allows users to choose external platforms where they want to receive notifications, enhancing integration with their existing workflows. You can: 

* Add Email Notification  
* Add HTTP Notification  
* Add Microsoft Teams Notification  
* Add Pager Duty Notification  
* Add Slack Notification  
* Add Webhook Notification

This versatility ensures that notifications are delivered through the most convenient and effective channels for each team, allowing them to stay informed and respond to real-time data quality issues. 

!!! note
	If you do not select any notification channel, by default, you will receive notifications via in-app notifications. However, if you choose any notification channel, such as Email, you will receive notifications through both your selected channel and also in-app notifications. 

!!! tip
	Qualytics provides you with multiple options for receiving notifications. You can select one or more notification channels to receive your notifications. 

## Reducing Notification Fatigue

Users can customize their notification settings to define which alerts they wish to receive and how they want to be notified. This flexibility ensures that users are only informed about relevant events, reducing notification fatigue.

For example, **“assigning tags”** while adding the notifications generates alerts regarding only those source datastores having the tags as defined while adding the notification. If the tag **“critical”** is defined while adding the notification rule, then the notification will be generated only for source datastores having the “critical” tag. 

## **User Feedback Integration**

The system allows for feedback on detected anomalies, which helps refine the anomaly detection process and reduce alert fatigue. This ensures that users are only notified about the most relevant issues. Notifications are enhanced by incorporating user feedback on actions taken. 

## Navigation to Notifications

**Step 1:** Log in to your Qualytics account and click the **“Settings”** button on the left side panel of the interface.

![global-settings](../../assets/notifications/global-settings-light-2.png#only-light)
![global-settings](../../assets/notifications/global-settings-dark-2.png#only-dark)

**Step 2:** By default, you will be navigated to the **“Tags”** section. Click on the **“Notifications”** tab.

![notifications](../../assets/notifications/notifications-light-3.png#only-light)
![notifications](../../assets/notifications/notifications-dark-3.png#only-dark)

## **Add Notification Rule**

In Qualytics, notification rules send in-app messages by default and can also notify you via external applications like **Email**, **Slack**, **Microsoft Teams**, and many more. This helps you stay updated on important events, like when an operation completes, even if you're not using the app. You can customize these alerts by adding datastore tags and choosing your preferred notification channels, ensuring you get timely updates.

**Step 1:** Click on the **“Add Notifications”** button located in the top right corner.

![add-notifications](../../assets/notifications/add-notifications-light-4.png#only-light)
![add-notifications](../../assets/notifications/add-notifications-dark-4.png#only-dark)

A modal window **“Add Notification Rule”** will appear providing you with fields to set notification rules.

![notification-window](../../assets/notifications/notification-window-light-5.png#only-light)
![notification-window](../../assets/notifications/notification-window-dark-5.png#only-dark)

**Step 2:** Enter the following details to add the notification rule.

**1. Name:** Enter a specific and descriptive title to your notification rule to easily identify its purpose.

**2. Description:** Provide a brief description of what the notification rule does or when it should trigger.

![name-description](../../assets/notifications/name-description-light.png#only-light)
![name-description](../../assets/notifications/name-description-dark.png#only-dark)

**3. Trigger When**: Select the event or condition from the dropdown menu that will trigger the notification. Below is the list of available events you can choose from:

* **Operation Completion:** This type of notification is triggered whenever an operation, such as a catalog, profile, or scan, is completed on a source datastore. Upon completion, teams are promptly notified through in-app messages and, if configured, via external notification channels such as email, Slack, Microsoft Teams, and others. For example, the team is notified whenever the catalog operation is completed, helping them proceed with the profile operation on the datastore. 

* **An Anomaly is Identified:** This type of notification is triggered when any single anomaly is identified in the data. The notification message typically includes the type of anomaly detected and the datastore where it was found. It provides specific information about the anomaly type, which helps quickly understand the issue's nature.

!!! tip 
	Users can specify a minimum anomaly weight for this trigger condition. This threshold ensures that only anomalies with a weight equal to or greater than the specified value will trigger a notification. If no value is set, all detected anomalies, regardless of their weight, will generate notifications. This feature helps prioritize alerts based on the importance of the anomalies, allowing users to focus on more critical issues.  

* **Anomalies are Detected in a Table or File:** This notification is triggered when multiple anomalies are detected within a specific table or file. It includes information about the number of anomalies found and the specific scan target within the datastore. This is useful for assessing the overall health of a particular datastore. No concept of weights. 

| Factors | An Anomaly is Identified | Anomalies are Detected in a Table or File |
|--------|--------|--------|
| Trigger Event | Notifies for individual anomaly detection | Notifies for multiple anomalies within a specific table or file |
| Notification Content | Focuses on the type of anomaly and the affected datastore. | Provide a count of anomalies and specifies the scan target within the datastore. |
| Notification Targeting  | Tags, Weight or both  | Only Tags  |

* **A Freshness SLA Violation Occurs:** This type of notification is triggered when data within a datastore does not meet the defined freshness criteria, violating the Service Level Agreement (SLA). The notification message typically includes details about the extent of the violation, the specific datastore affected, and the freshness threshold that was breached. This helps the team take prompt corrective actions to ensure data timeliness and reliability.

![trigger-condition](../../assets/notifications/trigger-condition-light.png#only-light)
![trigger-condition](../../assets/notifications/trigger-condition-dark.png#only-dark)

**4.** **Message:** Enter your custom message using variables in the Message field, where you can specify the content of the notification that will be sent out. 

!!! tip
	You can write your custom notification message by utilizing the autocomplete feature. This feature allows you to easily [insert internal variables](#available-variables) such as **{{rule_name}}**, **{{container_name}}**, and **{{datastore_name}}**. As you start typing, the autocomplete will suggest and recommend relevant variables in the dropdown.

![message](../../assets/notifications/message-light.png#only-light)
![message](../../assets/notifications/message-dark.png#only-dark)

**5. Datastore Tags:** Use the drop-down menu to **select the datastore tags**. Notifications will be generated for only those source datastores that have the datastore tags you select in this step. For example, if you select **“critical”** datastore tag from the dropdown menu, notifications will be generated only for source datastores having the "critical" tag applied to them. 

!!! note 
	If you choose **"An Anomaly is Detected"** as the trigger condition, you'll need to define the Anomaly's Tag and set a minimum Anomaly weight. This means that only anomalies with a weight equal to or greater than the specified value will trigger a notification. If no value is set, the weight will be ignored.

![select-tag](../../assets/notifications/select-tag-light-7.png#only-light)
![select-tag](../../assets/notifications/select-tag-dark-7.png#only-dark)

**6. Notification channel:** Select the notification channel where you want your alerts to be sent. This ensures you get notified in the way you prefer. 

| Channels | Description | References |
|-------|--------|--------|
| Emails | Send notifications directly to your specified email addresses. | [See more](https://userguide.qualytics.io/settings/notifications/notification-services/email/). |
| HTTP Action | Triggers an HTTP action to notify a specific endpoint or service. | [See more](https://userguide.qualytics.io/settings/notifications/notification-services/http-action/). |
| Microsoft Teams | Sends notifications to a specified Microsoft Teams channel. | [See more](https://userguide.qualytics.io/settings/notifications/notification-services/microsoft-teams/). |
| PagerDuty | Integrates with Pager Duty to alert you through your PagerDuty setup. | [See more](https://userguide.qualytics.io/settings/notifications/notification-services/pagerduty/). |
| Slack  | Sends notifications to a specific Slack channel. | [See more](https://userguide.qualytics.io/settings/notifications/notification-services/slack/). |
| Webhook | Sends notifications via webhooks to custom endpoints you configure. | [See more](https://userguide.qualytics.io/settings/notifications/notification-services/webhook/). |

!!! note 
	If you do not select any notification channel, you will receive notifications by default via in-app notifications. However, if you choose any notification channel, such as Email, you will receive notifications through both your selected channel and also in-app notifications.

!!! tip 
	Qualytics provides you with multiple options for receiving notifications. You can select one or more notification channels to get notified.

![select-channel](../../assets/notifications/select-channel-light-8.png#only-light)
![select-channel](../../assets/notifications/select-channel-dark-8.png#only-dark)

**Step 3:** Once you have selected your preferred notification channels, then click on the **“Save”** button.

![save](../../assets/notifications/save-light-9.png#only-light)
![save](../../assets/notifications/save-dark-9.png#only-dark)

After clicking on the **“Save”** button then a confirmation message will display saying **“Notification successfully created”**

![successfully-created](../../assets/notifications/successfully-created-light-10.png#only-light)
![successfully-created](../../assets/notifications/successfully-created-dark-10.png#only-dark)

## Available Variables

Qualytics provides a set of internal variables that you can use to customize your notification messages. These variables dynamically insert specific information related to the triggered event, ensuring that your notifications are both relevant and informative. Below is a list of variables categorized by the type of operation:

| Event  | Variable  | Description |
|----------|--------|--------|
| **When an Operation Completes** | {{rule_name}} | The name of the rule associated with the operation. |
|  | {{target_link}} | A link related to the operation. |
|  | {{datastore_name}} | The name of the datastore involved. |
|  | {{operation_message}} | A custom message related to the operation. |
|  | {{operation_type}} | The type of operation performed. |
|  | {{operation_result}} | The result of the operation. |
|  |  |  |
| **When an Anomaly is Detected** | {{rule_name}} | The name of the rule associated with the detected anomaly. |
|  | {{target_link}}| A link to the relevant target or source. |
|  | {{datastore_name}} | The name of the datastore where the anomaly was detected. |
|  | {{anomaly_message}} | A custom message related to the anomaly. |
|  | {{anomaly_type}} | The type of anomaly detected. |
|  | {{check_description}} | A description of the check that detected the anomaly. |
|  |  |  |
| **When Anomalies Are Detected in a Table or File** | {{rule_name}} | The name of the rule associated with the anomaly detection. |
|  | {{target_link}} | A link to the relevant target or source. |
|  | {{datastore_name}} | The name of the datastore where the anomaly was detected. |
|  | {{anomaly_count}} | The number of anomalies detected. |
|  | {{scan_target_name}} | The name of the scan target (table or file). |
|  | {{anomaly_message}} | A custom message related to the detected anomalies. |
|  | {{check_description}} | A description of the check that detected the anomaly. |
|  |  |  |
| **When a Freshness SLA Violation Occurs** | {{rule_name}} | The name of the rule associated with the SLA violation. |
|  | {{target_link}} | A link to the relevant target or source. |
|  | {{datastore_name}} | The name of the datastore where the violation occurred. |
|  | {{container_name}} | The name of the container involved. |
|  | {{freshness_violation_started}} | The time when the freshness violation started. |
|  | {{container_last_modified_time}} | The last modified time of the container. |

## Notification Examples 

### I. When an Operation Completes

**Message Template:**

Operation `{{operation_type}}` completed for the rule `{{rule_name}}` on datastore `{{datastore_name}}`. The result of the operation is `{{operation_result}}`. You can review the details here: `{{target_link}}`. Additional information: `{{operation_message}}`.

**Custom Message Example:**

Operation `Scan Operation` completed for the rule `Max Partition Size` on datastore `CustomerDataStore`. The result of the operation is `Success`. 

You can review the details here: `https://<your-instance>.qualytics.io/datastores/<datastore-id>/activity?operation_id=<operation-id>`. 

Additional information: `The scan confirmed that all partitions are within the allowed maximum number of records, ensuring data consistency and performance efficiency.`

### II. When an Anomaly is Detected

**Message Template:**

Anomaly detected by rule `{{rule_name}}` in the datastore `{{datastore_name}}`. The anomaly type is `{{anomaly_type}}`. For more details, see here-  `{{target_link}}`. Additional info: `{{anomaly_message}}` and check description: `{{check_description}}`.

**Custom Message Example:**

Anomaly detected by rule `Required Values` in the datastore `SalesDataStore`. The anomaly type is `record`. For more details, see here - `https://<your-instance>.qualytics.io/anomaly-details`. 

Additional info: `A record was found in the CUSTOMER table that lacks a required value for the field 'Customer_Status` and check description: `This rule asserts that all defined values, such as 'Customer_Status', must be present at least once within a field to ensure data completeness and integrity.`

### III. When Anomalies Are Detected in a Table or File

**Message Template:**

Alert! `{{anomaly_count}}` anomalies were detected in `{{scan_target_name}}` within the datastore `{{datastore_name}}`. The rule `{{rule_name}}` triggered this detection. Anomaly details: `{{anomaly_message}}`. You can review the details here: `{{target_link}}`. Description of the check: `{{check_description}}`.

**Custom Message Example:**

Alert! `1` anomaly was detected in the `LINEITEM` table within the datastore `SalesDataStore`. The rule `MaxValue_Rule_L_QUANTITY` triggered this detection. 

Anomaly details: `The quantity of items (L_QUANTITY) exceeded the maximum allowed value of 50`. You can review the details here: `https://<your-instance>.qualytics.io/anomaly-details`

Description of the check: `This check asserts that the quantity of items (L_QUANTITY) in the LINEITEM table does not exceed a value of 50, ensuring data accuracy and preventing potential overflows.`

### IV. When a Freshness SLA Violation Occurs

**Message Template:**

Freshness SLA violation detected for `{{datastore_name}}` in container `{{container_name}}`. The rule `{{rule_name}}` flagged the violation which started at `{{freshness_violation_started}}`. The last modification to the container was at `{{container_last_modified_time}}`.

**Custom Message Example:**

Freshness SLA violation detected for `CustomerDataStore` in container `OrdersContainer`. The rule `Required Values` flagged the violation which started at `2024-08-11T03:07:26.343000+00:00`. The last modification to the container was at `2024-08-09T21:00:15.651000+00:00`. 