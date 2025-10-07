# FAQs

### 1. What’s the difference between a Flow and a Trigger?

A **Flow** is the overall automation pipeline, while a **Trigger** determines *when* the flow starts — such as on operation completion, anomaly detection, or manually.

### 2. Can I have multiple actions under a single flow?

Yes. You can chain multiple actions (like **notifications** or **operations**) under a single flow to perform sequential or parallel tasks.

### 3. What happens if I deactivate a flow?

Once deactivated, the flow’s triggers stop executing until you **reactivate** it. Existing executions won’t be affected.

### 4. Can I test notifications before publishing?

Yes. Each notification channel (**Email**, **Slack**, **Teams**, **PagerDuty**, **HTTP**) includes a **Test**
