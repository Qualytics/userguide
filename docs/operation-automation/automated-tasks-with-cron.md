# Qualytics Scheduled Operations

Users may want to create their own scheduled operations in Qualytics for various reasons, such as automating routine tasks, data exports, or running specific operations at regular intervals. This guide will walk you through the process of creating a scheduled task.

## On Linux machine

### Prerequisites
Before proceeding, ensure that you have the following:

1. Access to the terminal on your machine.
2. The `curl` command-line tool installed.
3. The desired Qualytics instance details, including the instance URL and authentication token.


### Steps to Create a Scheduled Operation

#### 1. Open the Crontab Editor

Run the following command in your terminal to open the crontab editor:

```bash
crontab -e
```

#### 2. Add the Cron Job Entry

In the crontab editor, add the following line to execute the curl command at your specified schedule:

```bash
<cronjob-expression> /usr/bin/curl --request POST --url 'https://<your-instance>.qualytics.io/api/export/<operation>?datastore=<datastore-id>&containers=<container-id-one>&containers=<container-id-two>' --header 'Authorization: Bearer <your-token>' >> <path-to-show-logs> 2>&1
```

#### 3. Example:
For example, to run the command every 5 minutes:

```bash
*/5 * * * * /usr/bin/curl --request POST --url 'https://your-instance.qualytics.io/api/export/anomalies?datastore=123&containers=14&containers=16' --header 'Authorization: Bearer eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9...' >> /path/to/show/logs.txt 2>&1
```
#### 4. Verify or List Cron Jobs:

```bash
crontab -l
```

Customize the placeholders based on your specific details and requirements. Save the crontab file to activate the scheduled operation.


## On Windows machine
### Prerequisites
Before proceeding, ensure that you have the following:

1. Access to the PowerShell on your machine.
3. The desired Qualytics instance details, including the instance URL and authentication token.


### Steps to Create a Scheduled Operation

#### 1. Open your text editor of your preference and add the script entry

In the text editor, add the following line to execute the `Invoke-RestMethod` command:

```bash
Invoke-RestMethod -Method 'Post' -Uri https://<your-instance>/api/export/anomalies?datastore=<datastore-id>&containers=<container-id-one>&containers=<container-id-two> -Headers @{'Authorization' = 'Bearer <your-token>'; 'Content-Type' = 'application/json'}
```

#### 2. Example:
For example, to run the command every 5 minutes:

```bash
Invoke-RestMethod -Method 'Post' -Uri https://your-instance.qualytics.io/api/export/anomalies?datastore=123&containers=44&containers=22 -Headers @{'Authorization' = 'Bearer eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9...'; 'Content-Type' = 'application/json'}
```

Customize the placeholders based on your specific details and requirements. Save the script with the desired name with the extension `.ps1`.

#### 3. Add the script to the Task Scheduler:

1. **Open Task Scheduler:**
    - Press `Win + S` to open the Windows search bar.
    - Type "Task Scheduler" and select it from the search results.

2. **Create a Basic Task:**
    - In the Task Scheduler window, click on `Create Basic Task...` on the right-hand side.

3. **Provide a Name and Description:**
    - Enter a name and description for your task. Click `Next` to proceed.

4. **Choose Trigger:**
    - Select when you want the task to start. Options include `Daily`, `Weekly`, or `At log on`.
    - Choose the one that fits your schedule. Click `Next`.

5. **Set the Start Date and Time:**
    - If you selected a trigger that requires a specific start date and time, set it accordingly. Click `Next`.

6. **Choose Action:**
    - Select `Start a program` as the action and click `Next`.

7. **Specify the Program/Script:**
    - In the `Program/script` field, provide the path to PowerShell executable (`powershell.exe`), typically located at `C:\Windows\System32\WindowsPowerShell\v1.0\powershell.exe`. Alternatively, you can just type `powershell.exe`.
    - In the `Add arguments (optional)` field, provide the path to your PowerShell script. For example: `-File "C:\Path\To\Your\GeneratedScript.ps1"`.
    - Click `Next`.

8. **Review Settings:**
    - Review your task settings. If everything looks correct, click `Finish`.

9. **Finish:**
    - You should now see your task listed in the Task Scheduler Library.

## Installing Qualytics CLI:

### Prerequisites
Before installing the Qualytics CLI, ensure you have the following prerequisites:

`Python`: Make sure Python is installed on your machine. You can download Python from python.org.

`pip` (Python Package Installer): Verify that pip is installed. It usually comes with Python installations.

Qualytics Account: Obtain your Qualytics API access token.

### Installation
Open a Terminal and Install Qualytics CLI:

```bash
pip install qualytics-cli
```

### Verify Installation:

```bash
qualytics --version
```

### Initialization:

To use the Qualytics CLI, initialize it with your Qualytics instance details and API token:

```bash
qualytics init --url "your-domain.qualytics.io/api" --token "your-bearer-token"
```
    
_Replace placeholders with your Qualytics instance URL and API token._


## Automated Setup Using Qualytics CLI:

### For Linux and Windows Users

Use the Qualytics CLI to schedule a task automatically.

```bash
qualytics schedule export-metadata --crontab "<cronjob-expression>" --datastore <datastore-id> --containers <container-ids> --options <metadata-options>
```

_Replace placeholders as needed._

### Behaviour on Linux:

It will create the files inside your `home/user/.qualytics` folder.

The schedule operations commands are going to be located in `home/user/.qualytics/schedule-operation.txt`.
You can see some files with the `option` you selected with the logs of the cronjob run.

It will already create for you a cronjob expression, you can run `crontab -l` to list all cronjobs.

### Behaviour on Windows:

It will create the files inside your `home/user/.qualytics` folder.

The script files will be located in `home/user/.qualytics` with a pattern `task_scheduler_script_<option-you-selected>_<datastore-number>.ps1` and it's just a matter for you to follow the step above to create the Task Scheduler.

## Explanation of Placeholders:

* `<cronjob-expression>`: Replace this with your desired cron expression. For example, `*/5 * * * *` means "every 5 minutes." You can check `crontab.guru` for more examples.

* `<your-instance>`: Replace with the actual Qualytics instance URL.

* `<operation>`: Replace with the specific operation (e.g., "anomalies", "checks" or "field-profiles").

* `<datastore-id>`: Replace with the ID of the target datastore.

* `<container-id-one>` and `<container-id-two>`: Replace with the IDs of the containers. You can add more containers as needed.

* `<container-ids>`: Comma-separated list of containers IDs or array-like format. Example: "1, 2, 3" or "[1,2,3]".

* `<options>`: Comma-separated list of op to export or all for everything. Example: anomalies, checks, field-profiles or all.

* `<your-token>`: Replace with the access token obtained from Qualytics (`Settings` -> `Security` -> `API Keys`).

* `<path-to-show-logs>`: Replace with the file path where you want to store the logs.