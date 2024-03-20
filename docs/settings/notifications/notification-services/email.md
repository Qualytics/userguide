# Email

## Steps to setup Email

---

![Screenshot](../../../assets/notifications/services/email-notification-light.png#only-light)
![Screenshot](../../../assets/notifications/services/email-notification-dark.png#only-dark)

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

### `Email Addresses` <spam id='required'>`required`</spam>
* The `email` of the group or a person who will receive the email notification. Separate by commas for multiple:

```text
boss@corporation.com, vice-president@corporation.com, dataengineering@corporation.com
```

### `Description` <spam id='required'>`optional`</spam>
* Payload / description of the notification
