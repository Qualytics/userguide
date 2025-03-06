# Installing Python on Windows

Installing Python on Windows is simple and requires a compatible system, administrative access, and an internet connection. It can be installed through the Microsoft Store or the official website, with options to configure settings for seamless use. Verifying the installation ensures Python is ready for development, and setting environment variables can help with advanced tasks.

Let's get started 🚀

## Prerequisites 

Before you begin, ensure you meet the following requirements:

* **System Requirements:** Windows 7 or later with sufficient disk space.

* **Administrative Privileges:** You need admin rights to install Python and make changes to system settings.

* **Internet Connection:** A stable internet connection is required for downloading the installer.

## Method 1: Install Python from the Microsoft Store

**Step 1:** Click the Windows icon in the bottom-left corner of the screen, type **Microsoft Store** in the search bar.

![python-microsoft-store](../assets/cli/window-1.png)

**Step 2:**  Click on the Microsoft Store app to open it.

![python-microsoft-store](../assets/cli/microsoft-2.png)

A **Microsoft Store** window will open, displaying a home screen with featured apps, games, and promotions.

![python-microsoft-store](../assets/cli/home-3.png)

**Step 3:** Click the search bar, type **Python**, and press Enter to search.

![python-microsoft-store](../assets/cli/search-4.png)

**Step 4:** A list of available Python versions appears. Select the latest version published by the Python Software Foundation to open its installation page.

![python-microsoft-store](../assets/cli/version-5.png)

**Step 5:** Click on the Python version you wish to install.

For demonstration purposes, we will install **Python 3.12**.

![python-microsoft-store](../assets/cli/latest-6.png)

**Step 6:** Click the Get button to start the download and installation process.

![python-microsoft-store](../assets/cli/install-7.png)

**Step 7:** Once the download and installation are complete, click the Downloads button in the left panel of the Microsoft Store to view the downloaded application.

![python-microsoft-store](../assets/cli/downloads-8.png)

**Step 8:** Click the Open button next to the downloaded Python version.

![python-microsoft-store](../assets/cli/open-9.png) 
   
**Step 9:** A modal command prompt window will open. In the command prompt, type **python --version** and press **Enter**.

![python-microsoft-store](../assets/cli/check-version-9.png)

If the installed Python version appears, it confirms that Python has been successfully installed on your system.

![python-microsoft-store](../assets/cli/version-number-10.png)

## Method 2: Installing Python from the Official Website

**Step 1:** Open a web browser and navigate to the **[Downloads for Windows section](https://www.python.org/downloads/windows/)** of the official Python website.

![python-microsoft-store](../assets/cli/download-windows-11.png)

In the **Downloads** section, you will see different Python versions listed under **Stable Releases** and **Pre-releases**. Each version includes multiple installer options, such as:

* **Windows installer (64-bit)** – For 64-bit systems

* **Windows installer (32-bit)** – For 32-bit systems

* **Windows installer (ARM64)** – For ARM-based systems

Choose the appropriate installer based on your system requirements before proceeding with the download.

![python-microsoft-store](../assets/cli/releases-12.png)

**Step 2:** Click the link to download the file. For demonstration purposes, we have selected the **Download Windows installer (64-bit)**.

![python-microsoft-store](../assets/cli/installer-13.png)

**Step 3:** Locate the downloaded Python installer on your system and click to open it.

![python-microsoft-store](../assets/cli/locate-file-14.png)

**Step 4:** Once the Python installer opens, the installation window shows two checkboxes:

![python-microsoft-store](../assets/cli/checkboxes-15.png)

* **Admin privileges:** Check the box labelled **Admin Privileges** parameter controls whether to install Python for the current or all system users. This option allows you to change the installation folder for Python.

![python-microsoft-store](../assets/cli/first-checkbox-16.png)

* **Add Python to Path:** Check the box labeled Add Python to PATH important for running Python from the command line.

![python-microsoft-store](../assets/cli/second-checkbox-17.png)

**Step 5:** Click **Install Now** option for the recommended installation.

![python-microsoft-store](../assets/cli/install-now-18.png)

Once installation is complete, you’ll see an option to Disable path length limit. Click this option if prompted, as it can prevent issues with long file paths during development.

![python-microsoft-store](../assets/cli/disable-path-19.png)

**Step 6:** Click **Close** to exit the installer.

![python-microsoft-store](../assets/cli/close-20.png)

**Step 7**: Verify the installation by opening a Command Prompt and typing:

!!! syntax
    python --version

![python-microsoft-store](../assets/cli/checked-version-21.png)

If Python is installed correctly, it should display the installed version:

!!! example 
    C:\Users\user\>python --version Python 3.12.4

![python-microsoft-store](../assets/cli/version-numbered-22.png)


## Setting Up Environment Variables

If the Python installer does not include the Add Python to PATH checkbox or you have not selected that option, continue in this step. Otherwise, skip these steps.

**Step 1:** Open File Explorer (Win +E) and navigate to where Python is installed. The default location is:

!!! example 
    C:\Users\win 10\AppData\Roaming\Microsoft\Windows\Start Menu\Programs\Python 3.12 

![python-microsoft-store](../assets/cli/locate-path-23.png)

**Step 2:** Copy this path, then press **Win + R** on your keyboard, type sysdm.cpl, and press Enter.

![python-microsoft-store](../assets/cli/win-r-24.png)

   
**Step 3:** A modal window system properties will appear. Click on the **Advanced Tab.**

![python-microsoft-store](../assets/cli/advanced-25.png)

**Step 4:** Click on the Environment Variable button.

![python-microsoft-store](../assets/cli/environment-variables-26.png)

A modal window will appear. Under **System Variables**, select **Path** and click on **Edit button.**

![python-microsoft-store](../assets/cli/system-variables-27.png)

Paste the copied Python installation path.

![python-microsoft-store](../assets/cli/edit-environment-variable-28.png)

**Step 5**: Also, add the Scripts folder path:

!!! example
    C:\Users\YourUsername\AppData\Local\Programs\Python\Python3x\Scripts 
 
![python-microsoft-store](../assets/cli/scripts-29.png)

**Step 6:** Click **OK** to save the changes and restart your computer.

![python-microsoft-store](../assets/cli/click-ok-30.png)

**Step 7:** Open the Command Prompt and type:

!!! syntax
    python --version 

![python-microsoft-store](../assets/cli/check-version-last-31.png)

If Python is installed correctly, it should display the installed version:

!!! example
    C:\Users\user\>python --version Python 3.12.4 

![python-microsoft-store](../assets/cli/version-number-last-32.png)