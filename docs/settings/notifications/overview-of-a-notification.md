# Overview

`Notifications` supports delivering messages in response to a specified event using any number of supported integrations. Notifications can drive downstream workflows as well as alert users in realtime to data quality concerns.

![Screenshot](../../assets/notifications/settings-tab-light.png#only-light){: style="width:300px;"}
![Screenshot](../../assets/notifications/settings-tab-dark.png#only-dark){: style="width:300px;"}

![Screenshot](../../assets/notifications/notification-tab-light.png#only-light){: style="width:400px;"}
![Screenshot](../../assets/notifications/notification-tab-dark.png#only-dark){: style="width:400px;"}

![Screenshot](../../assets/notifications/all-notifications-light.png#only-light)
![Screenshot](../../assets/notifications/all-notifications-dark.png#only-dark)

# Add a Notification

1. In the right top of the `Notification` screen, navigate to `Add Notification`.

  ![Screenshot](../../assets/notifications/add-notification-light.png#only-light)
  ![Screenshot](../../assets/notifications/add-notification-dark.png#only-dark)

  ![Screenshot](../../assets/notifications/notification-screen-light.png#only-light)
  ![Screenshot](../../assets/notifications/notification-screen-dark.png#only-dark)

* **Name**: name of the notification
* **Description**: description of the notification
* **Tags**: add Tags to be included
* **TriggerWhen**: when the notification should be triggered
	* **An Operation Completes**
	* **Anomalies are Detected in a Table or File**
	* **An Anomaly is Detected**
	* **Freshness SLA Violation**
* **Use custom message**: a custom message when the notification was triggered
	![Screenshot](../../assets/notifications/notification-custom-messaging-light.png#only-light)![Screenshot](../../assets/notifications/notification-custom-messaging-dark.png#only-dark)
	* Qualytics App will use the `variables` to customize your messages.
	* Variables available by `Operation` when:
	* An operation Completes:
		* `{{rule_name}}`
		* `{{target_link}}`
		* `{{datastore_name}}`
		* `{{operation_message}}`
		* `{{operation_type}}`
		* `{{operation_result}}`
	* Anomalies are detected in a Table or File:
		* `{{rule_name}}`
		* `{{target_link}}`
		* `{{datastore_name}}`
		* `{{anomaly_count}}`
		* `{{scan_target_name}}`
		* `{{anomaly_message}}`
		* `{{check_description}}`
	* An Anomaly is Detected:
		* `{{rule_name}}`
		* `{{target_link}}`
		* `{{datastore_name}}`
		* `{{anomaly_message}}`
		* `{{anomaly_type}}`
		* `{{check_description}}`
	* Freshness SLA Violation:
		* `{{rule_name}}`
		* `{{target_link}}`
		* `{{datastore_name}}`
		* `{{container_name}}`
		* `{{freshness_violation_started}}`
		* `{{container_last_modified_time}}`
* **Notification channel**: how notification should be delivered:
	* **Email**.
	* **Http Action**.
	* **Microsoft Teams**.
	* **PagerDuty**.
	* **Slack**.
	* **Webhook**.