# PagerDuty FAQ

## Setup & Configuration

#### What is a Routing Key and where do I find it?

A Routing Key (also called an Integration Key) is a unique identifier that routes events to a specific PagerDuty service. You can find it in your PagerDuty account by navigating to **Services > [Your Service] > Integrations > Events API v2**. Each service can have its own Routing Key.

#### Do I need admin access to PagerDuty to set up the integration?

You need sufficient permissions in PagerDuty to create or manage a service and add an Events API v2 integration. Typically, a PagerDuty Admin or Manager role is required for these actions.

#### What PagerDuty plan do I need?

The Events API v2 is available on all PagerDuty plans, including the free tier. No specific paid plan is required for the Qualytics integration.

#### Can I connect multiple PagerDuty services?

Qualytics supports one PagerDuty integration (one default Routing Key) at the platform level. However, you can route events to **different PagerDuty services** by using the **Routing Key Override** property in individual Flow actions. This gives you multi-service routing without needing multiple integrations.

#### Does the integration require OAuth?

No. PagerDuty integration uses a simple **Routing Key** (Integration Key) instead of OAuth tokens. There is no authorization flow or token refresh required.

---

## Connection & Validation

#### What happens when I create the integration?

Qualytics validates your Routing Key by sending a **Change Event** to PagerDuty. Change Events are informational and **do not create incidents**, so your on-call team will not be alerted during setup.

#### What if my Routing Key is invalid?

The integration creation will fail with an error message indicating that the key could not be validated. Double-check that you copied the correct Integration Key from your PagerDuty service's Events API v2 integration.

#### How do I rotate my Routing Key?

Edit the PagerDuty integration in Qualytics (Settings > Integrations > PagerDuty > Edit) and update the Routing Key with the new value. Qualytics will validate the new key before saving.

#### Can Qualytics reach PagerDuty if I'm behind a firewall?

Qualytics communicates with PagerDuty's public Events API (`https://events.pagerduty.com`). Ensure that outbound HTTPS traffic to this domain is allowed from your Qualytics deployment.

---

## Managing the Integration

#### Can I edit the Routing Key after the integration is created?

Yes. Go to **Settings > Integrations**, click the vertical ellipses (⋮) next to PagerDuty, and select **Edit**. Update the Routing Key and click **Update**. The new key is validated before saving.

#### What happens when I disconnect the PagerDuty integration?

Disconnecting removes the integration configuration. Any Flow actions that reference PagerDuty will no longer be able to deliver notifications, but the Flow actions themselves are not deleted. You can re-create the integration at any time.

#### Can I manage the integration via API?

Yes. All integration operations — create, read, update, and delete — are available through the Qualytics API. See the [PagerDuty API](pagerduty-api.md) documentation for endpoints and examples.

---

## Troubleshooting

#### My PagerDuty events are not creating incidents. What should I check?

1. Verify the Routing Key is correct and not expired
2. Check that the PagerDuty service associated with the key is not disabled
3. Ensure the severity level matches your service's urgency settings — some services may suppress low-severity events
4. Verify that your Qualytics deployment can reach `https://events.pagerduty.com` over HTTPS

#### The test notification succeeded but I don't see an incident in PagerDuty.

Check the following:

- The PagerDuty service may have **event rules** that suppress or route certain events
- The incident may have been auto-resolved by PagerDuty's event intelligence
- The severity may be set to **Info**, which some services treat as low urgency and may not surface prominently
