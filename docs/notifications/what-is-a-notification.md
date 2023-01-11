# What is a Notification?

* `Notifications` allow users to send alerts / notifications through a myriad of supported systems. Notifications can drive downstream workflows as well as alerts, and are utilized via `Tags`.

---

* `Notifications` section can be found under `Settings` > `Notifications`:

 ![Screenshot](../assets/notifications/settings-tab-light.png#only-light)
 ![Screenshot](../assets/notifications/settings-tab-dark.png#only-dark)

 ![Screenshot](../assets/notifications/notification-tab-light.png#only-light)
 ![Screenshot](../assets/notifications/notification-tab-dark.png#only-dark)

* All active `notifications` are highlighted with the ability to `add` new:
 ![Screenshot](../assets/notifications/all-notifications-light.png#only-light)
 ![Screenshot](../assets/notifications/all-notifications-dark.png#only-dark)

---

# Create a Notification

* In the right top of the `Notification` screen, navigate to `Add`.

 ![Screenshot](../assets/notifications/add-notification-light.png#only-light)
 ![Screenshot](../assets/notifications/add-notification-dark.png#only-dark)

 ![Screenshot](../assets/notifications/notification-screen-light.png#only-light)
 ![Screenshot](../assets/notifications/notification-screen-dark.png#only-dark)

* Details:
     - `Name`: freetext name of the notification
     - `Description`: description of the notification
     - `TriggerWhen`: when the notification should be triggered
        * `An Operation Completes`
        * `Anomalies are Detected in a Table or File`
        * `An Anomaly is Detected`
        * `Freshness SLA Violation`
    - `Use custom message`: a custom message when the notification was triggered
        * ![Screenshot](../assets/notifications/notification-custom-messaging-light.png#only-light)![Screenshot](../assets/notifications/notification-custom-messaging-dark.png#only-dark)
    - `Notification channel`: how notification should be delivered:
        * `Email`.
        * `Http Action`.
        * `Microsoft Teams`.
        * `PagerDuty`.
        * `Slack`.
        * `Webhook`.