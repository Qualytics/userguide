# Microsoft Teams

## Steps to setup Microsoft Teams

---

![Screenshot](../../assets/notifications/services/microsoft-teams-notification.png){: style="width:550px;"}

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

### `Microsoft Teams Webhook Config` <spam id='required'>`required`</spam>
* Is the Microsoft Teams Webhook URL that links directly to your channel.

!!! info
    You can check [here](https://learn.microsoft.com/en-us/microsoftteams/platform/webhooks-and-connectors/how-to/add-incoming-webhook) in the official documentation how to create or how to find the URL.

### `Description`
* You can add a detailed description of why this notification is being created or some additional information.
