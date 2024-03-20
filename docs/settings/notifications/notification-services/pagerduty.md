# PagerDuty

## Steps to setup PagerDuty Notifications

---

![Screenshot](../../../assets/notifications/services/pagerduty-notification-light.png#only-light)
![Screenshot](../../../assets/notifications/services/pagerduty-notification-dark.png#only-dark)

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

### `PagerDuty Config` 
* The PagerDuty configuration for connection to user's PagerDuty instance:

    #### PagerDuty integration key <spam id='required'>`required`</spam>
    #### PagerDuty Severity <spam id='required'>`required`</spam>

!!! info
    Check [here](https://support.pagerduty.com/docs/services-and-integrations) for the official documentation from PagerDuty on how to create or configure the PagerDuty integration.
 
### `Description` <spam id='required'>`optional`</spam>
* Payload / description of the notification
