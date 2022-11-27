# Webhook

## Steps to setup Webhook

---

![Screenshot](../../assets/notifications/services/webhook-notification.png){: style="width:550px;"}

### `Name` <spam id='required'>`required`</spam>

* The notification name to be created in Qualytics App.

### `When` <spam id='required'>`required`</spam>

* Is `When` the notification will be triggered:
    * `An Operation Completes`.
    * `Anomalies are Detected in a Table or File`.
    * `An Anomaly is Detected`.
    * `Freshness SLA Violation`.

### `With the Tags` 
* Is the tag that will be show during the notification.   
!!! info
    You can create any tags if necessary to be shown during the notification.

### `Deliver a notification by`
* You can select multiple services for the same `Notification` category.

### `Webhook` 
* Is the Webhook URL that links directly to your channel.

!!! info
    You can check the official documentation of your Service Message to find on how to create or how to find the webhook URL.

### `Description`
* You can add a detailed description of why this notification is being created or some additional information.
