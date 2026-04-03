# Email Notification FAQ

## Configuration & Recipients

#### Can I send notifications to multiple email addresses?

Yes. Enter multiple email addresses separated by commas in the **Email Address** field (e.g., `user1@example.com, user2@example.com`).

#### Is the email subject customizable?

Yes. You can enter a custom subject line in the **Email Subject** field. If left empty, the default subject `Qualytics Notification` will be used.

#### Can I use variables in the email subject?

No. Dynamic tokens (variables) are only supported in the **Message** body, not in the Email Subject field.

---

## Message & Format

#### What format is the email notification?

Email notifications are sent as formatted messages with the content you configured in the Message field. Dynamic tokens are replaced with their actual values when the Flow triggers.

---

## Testing & Troubleshooting

#### Can I test the email notification before publishing the Flow?

Yes. Click the **Test Notification** button to send a test email to the configured address. You will see a confirmation message if the email was sent successfully.

#### What happens if an email address is invalid?

The notification delivery may fail for that specific address. Other valid addresses in the list will still receive the notification. You can verify addresses by using the **Test Notification** feature.
