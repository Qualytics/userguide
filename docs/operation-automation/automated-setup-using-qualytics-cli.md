# Automated Setup Using Qualytics CLI:

Easily automate scheduled exports with the Qualytics CLI on both Linux and Windows. This setup generates the required scripts and cron/task entries for you, with simple placeholders to customize.

## For Linux and Windows Users

Use the Qualytics CLI to schedule a task automatically.

```bash
qualytics schedule export-metadata --crontab "<cronjob-expression>" --datastore <datastore-id> --containers <container-ids> --options <metadata-options>
```

_Replace placeholders as needed._

## Behaviour on Linux:

It will create the files inside your `home/user/.qualytics` folder.

The schedule operations commands are going to be located in `home/user/.qualytics/schedule-operation.txt`.
You can see some files with the `option` you selected with the logs of the cronjob run.

It will already create for you a cronjob expression, you can run `crontab -l` to list all cronjobs.

## Behaviour on Windows:

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
