# In App Notification FAQ

## Delivery & Targeting

#### Who receives In App notifications?

All users with access to the Qualytics platform will receive In App notifications when a Flow triggers this action.

#### Can I target specific users with In App notifications?

No. In App notifications are delivered to all users in the platform. If you need to notify specific individuals, consider using Email or Slack notifications instead.

#### Where do In App notifications appear?

In App notifications appear in the notification bell icon in the Qualytics navigation bar. Users can view and manage their notifications from there.

---

## Configuration & Customization

#### Can I customize the notification message?

Yes. You can write a custom message using dynamic variables (tokens) like `{{ flow_name }}`, `{{ datastore_name }}`, and `{{ anomaly_message }}`. The autocomplete feature will suggest available tokens as you type.

#### Do In App notifications support all trigger types?

Yes. In App notifications support all Flow trigger types: Anomaly, Operation, Partition Scan, Schedule, and Manual.
