## Understanding Your System Health Page

This page gives you a real-time overview of your system's resources, helping you monitor performance and diagnose potential issues.


![Screenshot](../../assets/health/health-light.png#only-light)
![Screenshot](../../assets/health/health-dark.png#only-dark)

!!!info
	A simple indicator (e.g., green checkmark for "Healthy", red exclamation mark for "Critical").

## Summary

![Screenshot](../../assets/health/summary-light.png#only-light)
![Screenshot](../../assets/health/summary-dark.png#only-dark)

   - **Current Platform Version:** The active version of your platform's core software. This is important for compatibility and troubleshooting.
   - **Database Status:**  Confirms a  connection to your database. A status of "OK" means connectivity is working. 
   - **RabbitMQ  State:** Confirms that RabbitMQ, your message broker service, is functioning correctly with "OK" status.

## Analytics Engine

![Screenshot](../../assets/health/analytics-engine-light.png#only-light)
![Screenshot](../../assets/health/analytics-engine-dark.png#only-dark)

   - **Build Date:** The date the Analytics Engine was built.
   - **Implementation Version:** The specific version of the Analytics Engine codebase in use.
   - **Spark Version:**  The version of the Apache Spark processing engine, used by your Analytics Engine.
   - **Max Executors, Cores Per Executor, Max Memory Per Executor:**  These show configuration settings for the Analytics Engine's resources, controlling how much computing power it can utilize.
   - **Max DataFrame Size:** This determines the maximum size of dataframes the Analytics Engine can process.
   - **Thread Pool State:** This provides technical detail on the status of threads, used by the Analytics Engine for parallel processing. 

## Using the Health Page

* **Baseline Health:** Refer to this page for a standard reading of your system's usual operating state.
* **Issue Identification:**  If you experience slowdowns or errors, check this page:
    - A non-"OK" status for Database or RabbitMQ indicates a critical issue.
    - Changes in Analytics Engine configuration might affect performance.
* **Version Tracking:**  Confirm the versions currently in use before updates or when troubleshooting compatibility issues.

**Important Notes:**

* If a component displays a status other than "OK", seek further documentation or consult your technical support team.
* The Analytics Engine section provides advanced information for technical users and developers.

