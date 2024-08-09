# Notifications: Overview

Notifications in Qualytics offer a powerful system for delivering crucial alerts and updates across various communication channels. By setting up notification rules with specific triggers and channels, users can ensure timely awareness of critical events. This functionality enhances productivity, optimizes incident response, and promotes effective data management within the Qualytics platform.

Let’s get started 🚀

## Multiple Notification Channels

Qualytics emphasizes the configuration of multiple notification channels, which are crucial for ensuring that important alerts and updates reach users effectively through various platforms.

### In-App Notifications

In-app notifications in Qualytics are real-time alerts that keep users informed about various events related to their data operations and quality checks. These notifications are displayed within the Qualytics interface and cover a range of activities, including operation completions, anomaly detections, and service level agreement (SLA) status updates. 

![notifications](../../assets/notifications/notifications-light-1.png#only-light)
![notifications](../../assets/notifications/notifications-light-1.png#only-dark)
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

## Automated Workflows

The notification system of Qualytics integrates with popular data management tools like **Airflow**, **Fivetran**, and **Airbyte**, significantly improving the efficiency of data quality management processes. This automation enables proactive detection and remediation of data anomalies, helping maintain high data quality, reducing manual effort, and supporting confident data-driven decision-making. 

Here is how automated workflow works: 

**1. Anomaly Detection:** Qualytics continuously monitors data quality and identifies anomalies that deviate from expected patterns or thresholds. These anomalies could be related to data completeness, consistency, accuracy, or any other dimension of data quality defined by the Qualytics 8 framework. 

**2. Notification Triggers:** When an anomaly is detected, Qualytics sends a notification to the relevant team members or stakeholders. These notifications can be delivered through various channels, including in-app messages, email, Slack, Microsoft Teams, or other preferred communication platforms.  

**Trigger Event:**

- **Detection:** An anomaly or specific event is detected in the source datastore.

- **Examples:** Data anomalies, operation completions, data quality checks.

**3. Automated Workflow Initiation:** The notifications from Qualytics can also trigger automated workflows in tools like **Airflow**, **Fivetran**, and **Airbyte**. These tools are commonly used for data orchestration, transformation, and integration tasks. 

**4. Tailored Actions:** Users can set up specific actions or remediation steps that should be executed when an anomaly triggers a workflow. For example, upon detecting an anomaly in a datasource, Qualytics can automatically trigger an Airflow workflow to:

- Investigate the root cause of the anomaly  
- Perform data cleansing or transformation tasks to fix the issue  
- Notify the appropriate team members or stakeholders  
- Update dashboards or reports with the corrected data

**5. Efficiency Gains:** By automating these workflows, Qualytics helps organizations streamline their data quality management processes. Teams can quickly address data issues without manual intervention, saving time and resources. This allows them to focus on more strategic initiatives while maintaining high data quality standards.

## Reducing Notification Fatigue

Users can customize their notification settings to define which alerts they wish to receive and how they want to be notified. This flexibility ensures that users are only informed about relevant events, reducing notification fatigue.

For example, **“assigning tags”** while adding the notifications generates alerts regarding only those source datastores having the tags as defined while adding the notification. If the tag **“critical”** is defined while adding the notification rule, then the notification will be generated only for source datastores having the “critical” tag. 

## **User Feedback Integration**

The system allows for feedback on detected anomalies, which helps refine the anomaly detection process and reduce alert fatigue. This ensures that users are only notified about the most relevant issues. Notifications are enhanced by incorporating user feedback on actions taken. 

## Navigation to Notifications

**Step 1:** Log in to your Qualytics account and click the **“Settings”** button on the left side panel of the interface.

![global-settings](../../assets/notifications/global-settings-light-2.png#only-light)
![global-settings](../../assets/notifications/global-settings-light-2.png#only-dark)

**Step 2:** By default, you will be navigated to the **“Tags”** section. Click on the **“Notifications”** tab.

![notifications](../../assets/notifications/notifications-light-3.png#only-light)
![notifications](../../assets/notifications/notifications-light-3.png#only-dark)

## **Add Notification Rule**

In Qualytics, notification rules send in-app messages by default and can also notify you via external applications like **Email**, **Slack**, **Microsoft Teams**, and many more. This helps you stay updated on important events, like when an operation completes, even if you're not using the app. You can customize these alerts by adding datastore tags and choosing your preferred notification channels, ensuring you get timely updates.

**Step 1:** Click on the **“Add Notifications”** button located in the top right corner.

![add-notifications](../../assets/notifications/add-notifications-light-4.png#only-light)
![add-notifications](../../assets/notifications/add-notifications-light-4.png#only-dark)

A modal window **“Add Notification Rule”** will appear providing you with fields to set notification rules.

![notification-window](../../assets/notifications/notification-window-light-5.png#only-light)
![notification-window](../../assets/notifications/notification-window-light-5.png#only-dark)

**Step 2:** Enter the details to add the notification rule.

| REF.  | FIELD | ACTION |
|-------- |-------- |------- |
| 1.  | Name  | Enter a specific and descriptive title to your notification rule to easily identify its purpose. |
| 2.  | Description | A short note about what the rule does. |
| 3.  | Trigger when | Select the event or condition from the dropdown menu that will trigger the notification. Below is the list of available events you can choose from:<br><br> - **An Operation Completes**: Get notified when any operation completes on a data asset with the specified tags. <br><br> - **An Anomaly is Detected**: Get notified when any anomaly is identified with the specified tags and weight threshold. <br><br> - **Anomalies are Detected in a Table or File**: Get notified when an anomaly is identified in any table or file with the specified tags.<br><br> - **A Freshness SLA Violation Occurs**: Get notified for each SLA violation of a data asset with the specified tags. |
| 4. | Message | Enter your custom message in the Message field, where you can specify the content of the notification that will be sent out.<br><br> You can write your custom notification message by utilizing the autocomplete feature. This feature allows you to easily [insert internal variables](#available-variables) such as **{{rule_name}}**, **{{container_name}}**, and **{{datastore_name}}**. As you start typing, the autocomplete will suggest and recommend relevant variables in the dropdown.  |

![add-details](../../assets/notifications/add-details-light-6.png#only-light)
![add-details](../../assets/notifications/add-details-light-6.png#only-dark)

**Step 3:** Use the drop-down menu to **select the datastore tags**. Notifications will be generated for only those source datastores that have the datastore tags you select in this step. For example, if you select **“critical”** datastore tag from the dropdown menu, notifications will be generated only for source datastores having the "critical" tag applied to them. 

![select-tag](../../assets/notifications/select-tag-light-7.png#only-light)
![select-tag](../../assets/notifications/select-tag-light-7.png#only-dark)

**Step 4:** Select the notification channel where you want your alerts to be sent. This ensures you get notified in the way you prefer. 

| Channels | Description | References |
|------ |------ |------ |
| Emails | Sends notifications directly to your specified email addresses. | See more. |
| HTTP Action | Triggers an HTTP action to notify a specific endpoint or service. | See more. |
| Microsoft Teams | Sends notifications to a specified Microsoft Teams channel. | See more. |
| Pager Duty | Integrates with Pager Duty to alert you through your Pager Duty setup. | See more. |
| Slack  | Sends notifications to a specified Slack channel. | See more. |
| Webhook | Sends notifications via webhooks to custom endpoints you configure. | See more. |

!!! note
	If you do not select any notification channel, you will receive notifications by default via in-app notifications. However, if you choose any notification channel, such as Email, you will receive notifications through both your selected channel and also in-app notifications.

!!! tip
	Qualytics provides you with multiple options for receiving notifications. You can select one or more notification channels to get notified.

![select-channel](../../assets/notifications/select-channel-light-8.png#only-light)
![select-channel](../../assets/notifications/select-channel-light-8.png#only-dark)

**Step 4:** Once you have selected your preferred notification channels, then click on the **“Save”** button.

![save](../../assets/notifications/save-light-9.png#only-light)
![save](../../assets/notifications/save-light-9.png#only-dark)

After clicking on the **“Save”** button then a confirmation message will display saying **“Notification successfully created”**

![successfully-created](../../assets/notifications/successfully-created-light-10.png#only-light)
![successfully-created](../../assets/notifications/successfully-created-light-10.png#only-dark)

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
| **When Anomalies Are Detected in a Table or File** | {{rule_name}} | The name of the rule associated with the anomaly detection. |
|  | {{target_link}} | A link to the relevant target or source. |
|  | {{datastore_name}} | The name of the datastore where the anomaly was detected. |
|  | {{anomaly_count}} | The number of anomalies detected. |
|  | {{scan_target_name}} | The name of the scan target (table or file). |
|  | {{anomaly_message}} | A custom message related to the detected anomalies. |
|  | {{check_description}} | A description of the check that detected the anomaly. |
|  |  |  |
| **When an Anomaly is Detected** | {{rule_name}} | The name of the rule associated with the detected anomaly. |
|  | {{target_link}}| A link to the relevant target or source. |
|  | {{datastore_name}} | The name of the datastore where the anomaly was detected. |
|  | {{anomaly_message}} | A custom message related to the anomaly. |
|  | {{anomaly_type}} | The type of anomaly detected. |
|  | {{check_description}} | A description of the check that detected the anomaly. |
|  |  |  |
| **When a Freshness SLA Violation Occurs** | {{rule_name}} | The name of the rule associated with the SLA violation. |
|  | {{target_link}} | A link to the relevant target or source. |
|  | {{datastore_name}} | The name of the datastore where the violation occurred. |
|  | {{container_name}} | The name of the container involved. |
|  | {{freshness_violation_started}} | The time when the freshness violation started. |
|  | {{container_last_modified_time}} | The last modified time of the container. |