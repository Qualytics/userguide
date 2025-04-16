# Status

System status provides a real-time overview of your system's resources, essential for monitoring performance and diagnosing potential issues. It provides key indicators and status updates to help you maintain system health and quickly address potential issues.

## Navigation to Status

**Step 1:** Log in to your Qualytics account and click the **Settings** button on the left side panel of the interface. 

![global-settings](../../assets/health/global-settings-light-1.png#only-light)
![global-settings](../../assets/health/global-settings-dark-1.png#only-dark)

**Step 2:** You will be directed to the Settings page; then click on the **Status** section.

![health](../../assets/health/health-light-2.png#only-light)
![health](../../assets/health/health-dark-2.png#only-dark)

## Summary Section

The **Summary** section displays the current platform version, along with the database status and RabbitMQ state.

| REF. | FIELD | ACTION | EXAMPLE |
|----- |-------|--------|---------|
| 1 | Current Platform Version | Shows the current version of your platform's core software.  | 20240808-3019c60 |
| 2 | Cloud Platform | Indicates which cloud provider the platform is hosted on. | Amazon Web Services (AWS) |
| 3 | Deployment Size | Indicates the size of the deployment that the client has contracted. | Medium |
| 4 | Database | Verifies your database connection. An "OK" status means it’s connected. | Status:OK |
| 5 | RabbitMQ | Confirms RabbitMQ (a message broker software) is running correctly with an "OK" state. | State:OK |

![summary](../../assets/health/summary-light-3.png#only-light)
![summary](../../assets/health/summary-dark-3.png#only-dark)

## Status Indicator

The status indicator reflects the overall system resources health.For example, in the image below, a green checkmark indicates that our system resources are healthy.

!!! note
    Status indicators are simple: a green checkmark indicates "Healthy," and a red exclamation mark means "Critical."

![health-indicator](../../assets/health/health-indicator-light-4.png#only-light)
![health-indicator](../../assets/health/health-indicator-dark-4.png#only-dark)

## Analytics Engine

The **Analytics Engine** section provides advanced information about the analytics engine's configuration and current state for technical users and developers.

| REF | FIELD | ACTION | EXAMPLE |
|-----|-------|--------|---------|
| 1 | Build Date | This shows the date and time when the Analytics Engine was built. | Aug 8 2024,7:39 AM (GMT+5:30) |
| 2 | Implementation Version | The version of the analytics engine implementation being used.  | 2.0.0 |
| 3 | Max Executors | Maximum number of executors allocated for processing tasks. | 10 |
| 4 | Max Memory Per Executor | This shows the maximum amount of memory allocated to each executor. | 25000 MB |
| 5 | Spark Version | The version of Apache Spark that the Analytics Engine uses for processing. | 3.5.1 |
| 6 | Core Per Executor | This shows the number of CPU cores assigned to each executor. | 3 |
| 7 | Max Dataframe Size | The maximum size of dataframes that can be processed.  | 50000 MB |
| 8 | Thread Pool State | Indicates the current state of the thread pool used for executing tasks.  | \[Running, parallelism \= 3, size \= 0, active \= 0, running \= 0, steals \= 0, tasks \= 0, submissions \= 0\] supporting 0 running operation with 0 queued requests |

![analytics-engine](../../assets/health/analytics-engine-light-5.png#only-light)
![analytics-engine](../../assets/health/analytics-engine-dark-5.png#only-dark)

## Private Routes

Users can now utilize private routes to view their IP addresses along with relevant system messages in the Analytics Engine, ensuring greater transparency and visibility into network activity.

![private-routes](../../assets/health/private-light.png#only-light)
![private-routes](../../assets/health/private-dark.png#only-dark)

## Manage Status Summary

You can perform essential tasks such as copying the status summary, refreshing it, and restarting the analytics engine. These functionalities help maintain an up-to-date overview of system performance and ensure accurate analytics.

### Copy Status Summary

The **Copy Status Summary** feature lets you duplicate all data from the Health Section for easy sharing or saving.

**Step 1:** Click the **vertical ellipsis** from the right side of the summary section and choose **Copy Status Summary** from the drop-down menu.

![copy-health](../../assets/health/copy-health-light-6.png#only-light)
![copy-health](../../assets/health/copy-health-dark-6.png#only-dark)

**Step 2:** After clicking on **Copy Status Summary**,  a success message saying **Copied.**

![copied](../../assets/health/copied-light-7.png#only-light)
![copied](../../assets/health/copied-dark-7.png#only-dark)

### Refresh Status Summary

The **Refresh Status Summary** option updates the Health Section with the latest data. This ensures that you see the most current performance metrics and system status.

**Step 1:** Click the **vertical ellipsis** from the right side of the summary section and choose **Refresh Status Summary** to update the latest data.  

![refresh-health](../../assets/health/refresh-health-light-8.png#only-light)
![refresh-health](../../assets/health/refresh-health-dark-8.png#only-dark)

## Restart Analytics Engine

The **Restart Analytics Engine** option restarts the analytics processing system. This helps resolve issues and ensures that analytics data is accurately processed.

**Step 1:** Click the **vertical ellipsis** from the right side of the summary section and choose **Restart Analytics Engine** from the drop-down menu. 

![restart-analytics](../../assets/health/restart-analytics-light-9.png#only-light)
![restart-analytics](../../assets/health/restart-analytics-dark-9.png#only-dark)

**Step 2:** A modal window will pop up. Click the **Restart** button in this window to restart the analytics engine. Restarting the engine helps resolve any issues and ensures that your analytics data is up-to-date and accurately processed.

![restart](../../assets/health/restart-light-10.png#only-light)
![restart](../../assets/health/restart-dark-10.png#only-dark)

**Step 3:** After clicking on **Restart**button a success message saying **Successfully triggered Analytics Engine restart.**

![successfully-triggered](../../assets/health/successfully-triggered-light-11.png#only-light)
![successfully-triggered](../../assets/health/successfully-triggered-dark-11.png#only-dark)

