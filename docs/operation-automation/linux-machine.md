# Linux machine

You can automate Qualytics operations on a Linux machine by scheduling them with cron jobs. This guide walks you through setting up a scheduled curl command to trigger exports at defined intervals.

## Prerequisites
Before proceeding, ensure that you have the following:

1. Access to the terminal on your machine.
2. The `curl` command-line tool installed.
3. The desired Qualytics instance details, including the instance URL and authentication token.


## Steps to Create a Scheduled Operation

### 1. Open the Crontab Editor

Run the following command in your terminal to open the crontab editor:

```bash
crontab -e
```

### 2. Add the Cron Job Entry

In the crontab editor, add the following line to execute the curl command at your specified schedule:

```bash
<cronjob-expression> /usr/bin/curl --request POST --url 'https://<your-instance>.qualytics.io/api/export/<operation>?datastore=<datastore-id>&containers=<container-id-one>&containers=<container-id-two>' --header 'Authorization: Bearer <your-token>' >> <path-to-show-logs> 2>&1
```

### 3. Example:
For example, to run the command every 5 minutes:

```bash
*/5 * * * * /usr/bin/curl --request POST --url 'https://your-instance.qualytics.io/api/export/anomalies?datastore=123&containers=14&containers=16' --header 'Authorization: Bearer eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9...' >> /path/to/show/logs.txt 2>&1
```
### 4. Verify or List Cron Jobs:

```bash
crontab -l
```

Customize the placeholders based on your specific details and requirements. Save the crontab file to activate the scheduled operation.