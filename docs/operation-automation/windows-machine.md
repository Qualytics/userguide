# Windows machine

Automate Qualytics operations on Windows using PowerShell and Task Scheduler. This guide shows how to set up and run scheduled export tasks.

## Prerequisites
Before proceeding, ensure that you have the following:

1. Access to PowerShell on your machine.
2. The desired Qualytics instance details, including the instance URL and authentication token.


## Steps to Create a Scheduled Operation

### 1. Open your text editor of your preference and add the script entry

In the text editor, add the following line to execute the `Invoke-RestMethod` command:

```bash
Invoke-RestMethod -Method 'Post' -Uri https://<your-instance>/api/export/anomalies?datastore=<datastore-id>&containers=<container-id-one>&containers=<container-id-two> -Headers @{'Authorization' = 'Bearer <your-token>'; 'Content-Type' = 'application/json'}
```

### 2. Example:

For example, to run the command every 5 minutes:

```bash
Invoke-RestMethod -Method 'Post' -Uri https://your-instance.qualytics.io/api/export/anomalies?datastore=123&containers=44&containers=22 -Headers @{'Authorization' = 'Bearer eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9...'; 'Content-Type' = 'application/json'}
```

Customize the placeholders based on your specific details and requirements. Save the script with the desired name with the extension `.ps1`.

### 3. Add the script to the Task Scheduler:

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