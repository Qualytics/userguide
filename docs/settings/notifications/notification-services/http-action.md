# HTTP Action

Integrating HTTP Action notifications allows users to receive timely updates or alerts directly to a specified server endpoint. By setting up HTTP Action notifications with specific trigger conditions, you can ensure that you are instantly informed about critical events, such as operation completions or anomalies detected. This approach enables you to take immediate action when necessary, helping to address issues quickly and maintain the smooth and efficient operation of your processes.

## Navigation to Notifications

**Step 1:** Log in to your Qualytics account and click the **“Settings”** button on the left side panel of the interface. 

![Setting](../../../assets/notifications/services/http-action/settings-light-1.png#only-light)
![Setting](../../../assets/notifications/services/http-action/settings-dark-1.png#only-dark)

**Step 2:** Click on the **“Notifications”** tab.

![Notification](../../../assets/notifications/services/http-action/notification-light-2.png#only-light)
![Notification](../../../assets/notifications/services/http-action/notification-dark-2.png#only-dark)

## Add HTTP Action Notification

**Step 1:** Click on the **“Add Notifications”** button located in the top right corner.

![Add Noti](../../../assets/notifications/services/http-action/add-notification-light-3.png#only-light)
![Add Noti](../../../assets/notifications/services/http-action/add-notification-dark-3.png#only-dark)

A modal window, **“Add Notification Rule”** will appear, providing options to set notification rules.

![Modal-Window](../../../assets/notifications/services/http-action/modal-window-light-4.png#only-light)
![Modal-Window](../../../assets/notifications/services/http-action/modal-window-dark-4.png#only-dark)

**Step 2:** Enter the following details to add the notification rule.

**1. Name:** Enter a specific and descriptive title to your notification rule to easily identify its purpose.

**2. Description:** Provide a brief description of what the notification rule does or when it should trigger.

**3. Trigger When**: Select the event or condition from the dropdown menu that will trigger the notification. Below is the list of available events you can choose from:

- **Operation Completion:** This type of notification is triggered whenever an operation, such as a catalog, profile, or scan, is completed on a source datastore.  Upon completion, teams are promptly notified through in-app notifications and, the HTTP Action. For example, the team is notified whenever the catalog operation is completed, helping them proceed with the profile operation on the datastore. 

- **An Anomaly is Identified:** This type of notification is triggered when any single anomaly is identified in the data. The notification message typically includes the type of anomaly detected and the datastore where it was found. It provides specific information about the anomaly type, which helps quickly understand the issue's nature.

!!! tip 
    Users can specify a minimum anomaly weight for this trigger condition. This threshold ensures that only anomalies with a weight equal to or greater than the specified value will trigger a notification. If no value is set, all detected anomalies, regardless of their weight, will generate notifications. This feature helps prioritize alerts based on the importance of the anomalies, allowing users to focus on more critical issues.  |

- **Anomalies are Detected in a Table or File:** This notification is triggered when multiple anomalies are detected within a specific table or file. It includes information about the number of anomalies found and the specific scan target within the datastore. This is useful for assessing the overall health of a particular datastore. No concept of weights

| Factors | An Anomaly is Identified | Anomalies are Detected in a Table or File |
|-------- | -------|-------|
| Trigger Event | Notifies for individual anomaly detection | Notifies for multiple anomalies within a specific table or file |
| Notification Content | Focuses on the type of anomaly and the affected datastore. | Provide a count of anomalies and specifies the scan target within the datastore. |
| Notification Targeting  | Tags, Weight or both  | Only Tags  |

- **A Freshness SLA Violation Occurs:** This type of notification is triggered when data within a datastore does not meet the defined freshness criteria, violating the Service Level Agreement (SLA). The notification message typically includes details about the extent of the violation, the specific datastore affected, and the freshness threshold that   
  was breached. This helps the team take prompt corrective actions to ensure data timeliness and reliability.

![Screenshot](../../../assets/notifications/services/http-action/enter-details-light-5.png#only-light)
![Screenshot](../../../assets/notifications/services/http-action/enter-details-dark-5.png#only-dark)

**4.** **Message:** Enter your custom message using variables in the Message field, where you can specify the content of the notification that will be sent out. 

!!! tip 
    You can write your custom notification message by utilizing the autocomplete feature. This feature allows you to easily insert internal variables such as **{{rule_name}}**, **{{container_name}}**, and **{{datastore_name}}**. As you start typing, the autocomplete will suggest and recommend relevant variables in the dropdown.  

![Screenshot](../../../assets/notifications/services/http-action/message-light-6.png#only-light)
![Screenshot](../../../assets/notifications/services/http-action/message-dark-6.png#only-dark)

**5.** **Datastore Tags:** Use the drop-down menu to **select the datastore tags**. Notifications will be generated for only those source datastores that have the datastore tags you select in this step. For example, if you select **“critical”** datastore tag from the dropdown menu, notifications will be generated only for source datastores having the "critical" tag applied to them. 

!!! note 
    If you choose "An Anomaly is Detected" as the trigger condition, you'll need to define the Anomaly's Tag and set a minimum Anomaly weight. This means that only anomalies with a weight equal to or greater than the specified value will trigger a notification. If no value is set, the weight will be ignored. 

![Screenshot](../../../assets/notifications/services/http-action/tags-light-7.png#only-light)
![Screenshot](../../../assets/notifications/services/http-action/tags-dark-7.png#only-dark)

**6. Notification Channel:** Select **“HTTP Action”** as your notification channel and enter the details where you want the notification to be sent.

![Screenshot](../../../assets/notifications/services/http-action/notification-channel-light-8.png#only-light)
![Screenshot](../../../assets/notifications/services/http-action/notification-channel-dark-8.png#only-dark)

**Step 3:** Enter the following detail where you want the notification to be sent.

**1. Action URL:** Enter the **“Action URL”** in this field, which specifies the server endpoint for the HTTP request, defining where data will be sent or retrieved. It must be correctly formatted and accessible, including the protocol (http or https), domain, and path.

**2. HTTP Verbs:** HTTP verbs specify the actions performed on server resources. Common verbs include:

- **POST:** Use POST to send data to the server to create something new. For example, it's used for submitting forms or uploading files. The server processes this data and creates a new resource.

- **PUT:** Updates or creates a resource, replacing it entirely if it already exists. For example, updating a user’s profile information or creating a new record with specific details.

- **GET:** Retrieves data from the server without making any modifications. For example, requesting a webpage or fetching user details from a database.

![Screenshot](../../../assets/notifications/services/http-action/details-light-9.png#only-light)
![Screenshot](../../../assets/notifications/services/http-action/details-dark-9.png#only-dark)

**3. Username:** Enter the username needed for authentication. 

**4. Auth Type:** This field specifies how to authenticate requests. Choose the method that fits your needs:

- **Basic:** Uses a username and password sent with each request. Example: **“Authorization: Basic <base64-encoded-credentials>”.**

- **Bearer:** Uses a token included in the request header to access resources. Example: **“Authorization: Bearer <your-token>”.**  
    
- **Digest:** Provides a more secure authentication method by using a hashed combination of the username, password, and request details. Example: **Authorization: Digest username=" <username> ", realm=" <realm> ", nonce=" <nonce> ", uri=" <uri> ", response=" <response> ".**  
    
![Screenshot](../../../assets/notifications/services/http-action/details-light-10.png#only-light)
![Screenshot](../../../assets/notifications/services/http-action/details-dark-10.png#only-dark)

**5. Secret:**  Enter the password or token used for authentication. This is paired with the **Username** and **Auth Type** to securely access the server. Keep the secret confidential to ensure security.

![Screenshot](../../../assets/notifications/services/http-action/details-light-11.png#only-light)
![Screenshot](../../../assets/notifications/services/http-action/details-dark-11.png#only-dark)

## Test HTTP Action Notification

**Step 1:**  Click the **"Test Notification"** button to verify the correctness of the Action URL. If the URL is correct, a confirmation message saying **"Notification successfully sent"** will appear, confirming that the HTTP action is set up and functioning properly.

![Screenshot](../../../assets/notifications/services/http-action/test-noti-light-12.png#only-light)
![Screenshot](../../../assets/notifications/services/http-action/test-noti-dark-12.png#only-dark)

If you enter an incorrect Action URL, you will receive a failure message. For example, if you enter an incorrect URL endpoint like **“test-message”**, you will see a failure message indicating **"failure: HTTP action returned 404: {"error": "Error: Endpoint not found with that path and method"}."** This message shows that the specified endpoint could not be found.

![Screenshot](../../../assets/notifications/services/http-action/failed-noti-light-13.png#only-light)
![Screenshot](../../../assets/notifications/services/http-action/failed-noti-dark-13.png#only-dark)

## Save HTTP Action Notification

Once you have provided all the necessary values, set the trigger conditions for the notification, and verify the correctness of the Action URL, click the **"Save"** button.

![Screenshot](../../../assets/notifications/services/http-action/save-button-light-14.png#only-light)
![Screenshot](../../../assets/notifications/services/http-action/save-button-dark-14.png#only-dark)

After clicking the **“Save”** button, a success message will be displayed saying "Notification Successfully Created". 
 
![Screenshot](../../../assets/notifications/services/http-action/created-notification-light-15.png#only-light)
![Screenshot](../../../assets/notifications/services/http-action/created-notification-dark-15.png#only-dark)