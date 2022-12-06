# What is a Notification?

* `Notifications` allow users to send alerts / notifications through a myriad of supported systems. Notifications can drive downstream workflows as well as alerts, and are utilized via `Tags`.

---

* `Notifications` section can be found under `Settings` > `Notifications`:

 ![Screenshot](../assets/notifications/settings-tab.png){: style="height:450px"}

 ![Screenshot](../assets/notifications/notification-tab.png){: style="width:230px"}

* All active `notifications` are highlighted with the ability to `add` new:
 ![Screenshot](../assets/notifications/all-notifications.png){: style="width:530px"}

---

# Create a Notification

* In the right top of the `Notification` screen, navigate to `Add`.

 ![Screenshot](../assets/notifications/add-notification.png){: style="width:130px"}

 ![Screenshot](../assets/notifications/notification-screen.png)

* Details:
     - `Name`: freetext name of the notification
     - `When`: when the notification should be triggered
        * `An Operation Completes`
        * `Anomalies are Detected in a Table or File`
        * `An Anomaly is Detected`
        * `Freshness SLA Violation`
    - `With the Tags`: tags that will initiate the notification
    - `Deliver a notification by`: how notification should be delivered:
        * `Email`.
        * `Http Action`.
        * `Microsoft Teams`.
        * `PagerDuty`.
        * `Slack`.
        * `Webhook`.

 * TODO - add details of custom messaging       