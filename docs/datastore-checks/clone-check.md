# Clone Check

**Step 1:** Click the vertical ellipsis (⋮) next to the check (whether Active or Draft) that you want to clone and select **Edit** from the drop-down menu.

For Demonstration purposes, we have selected the **"Between"** check.

![clone-check](../assets/datastore-checks/clone-check/clone-check-light-78.png)

**Step 2:** A modal window will appear displaying the check details. Click on the **vertical ellipsis (⋮)** located in the upper-right corner of the modal window, and select **"Clone"** from the drop-down menu.

![clone-btn](../assets/datastore-checks/clone-check/clone-btn-light-79.png)

**Step 3:** After clicking the Clone button, a modal window will appear. This window allows you to adjust the cloned check's details.

![modal-window](../assets/datastore-checks/clone-check/modal-window-light-80.png)

**1.** If you toggle on the **"Associate with a Check Template"** option, the cloned check will be linked to a specific template.

![toggle-on](../assets/datastore-checks/clone-check/toggle-on-light-81.png)

Choose a **Template** from the drop-down menu that you want to associate with the cloned check. The check will inherit properties from the selected template.

* **Locked:** The check will automatically sync with any future updates made to the template, but you won't be able to modify the check's properties directly.

* **Unlocked:** You can modify the check, but future updates to the template will no longer affect this check.

![associate-check](../assets/datastore-checks/clone-check/associate-check-light-82.png)

**2.** If you toggle off the **"Associate with a Check Template"** option, the cloned check will not be linked to any template, which allows you full control to modify the properties independently.

![toggle-off](../assets/datastore-checks/clone-check/toggle-off-light-83.png)

Select the appropriate **Rule Type** for the check from the drop-down menu.

![rule-type](../assets/datastore-checks/clone-check/rule-type-light-84.png)

**Step 4:** Once you have selected the template or rule type, fill in the remaining [check details](https://userguide.qualytics.io/checks/checks-template/#:~:text=Enter%20the%20following%20details%20to%20add%20the%20check%20template%3A) as required. 

![check-detail](../assets/datastore-checks/clone-check/check-detail-light-85.png)

**Step 5:** After completing all the check details, click on the **"Validate"** button. This will perform a validation operation on the check without saving it. The validation allows you to verify that the logic and parameters defined for the check are correct. It ensures that the check will work as expected by running it against the data without committing any changes.

![validate-btn](../assets/datastore-checks/clone-check/validate-btn-light-86.png)

If the validation is successful, a green message saying **"Validation Successful"** will appear. 

![validation-success](../assets/datastore-checks/clone-check/validation-success-light-87.png)

If the validation fails, a red message saying **"Failed Validation"** will appear. This typically occurs when the check logic or parameters do not match the data properly.

![failed-validation](../assets/datastore-checks/clone-check/failed-validation-light-88.png)

**Step 6:** Once you have a successful validation, click the **"Save"** button. The system will save any modifications you've made to the check, and create a clone of that check on the basis of your changes.  

![save-btn](../assets/datastore-checks/clone-check/save-btn-light-89.png)

After clicking on the **"Save"** button, your check is successfully created and a success message will appear on the screen.