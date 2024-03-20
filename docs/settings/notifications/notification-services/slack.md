# Slack

## Steps to setup Slack Notifications

---

![Screenshot](../../../assets/notifications/services/slack-notification-light.png#only-light)
![Screenshot](../../../assets/notifications/services/slack-notification-dark.png#only-dark)

### `Name` <spam id='required'>`required`</spam>

* freetext name of the Notification

### `When` <spam id='required'>`required`</spam>

* when the notification will be triggered:
    * `An Operation Completes`.
    * `Anomalies are Detected in a Table or File`.
    * `An Anomaly is Detected`.
    * `Freshness SLA Violation`.

### `With the Tags` <spam id='required'>`required`</spam>
* tags that will drive the notification from an anomaly   
!!! info
    Refer to the tags page to add / edit tags and checks page for association of tags to checks / anomalies.

### `Deliver a notification by` <spam id='required'>`required`</spam>
* Service to be utilized for the notification

### `Slack Webhook Config` <spam id='required'>`required`</spam>
* Slack Webhook URL config that links directly to user's channel

!!! info
    Check [here](https://api.slack.com/messaging/webhooks) for the official Slack documentation how to create or configure the Slack webhook URL.

### `Description` <spam id='required'>`optional`</spam>
* Payload / description of the notification
