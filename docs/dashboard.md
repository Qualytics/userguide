# Dashboard

Upon signing in to Qualytics, users are greeted with a thoughtfully designed dashboard that offers intuitive navigation and quick access to essential features and datasets, ensuring an efficient and comprehensive data quality management experience.

In this documentation, we will explore every component of the Qualytics dashboard. 

Let’s get started 🚀

## Global Search 

The Global Search feature in Qualytics is designed to streamline the process of finding crucial assets such as Datastores, Containers, and Fields. This enhancement provides quick and precise search results, significantly improving navigation and user interaction. By entering keywords in the search bar located at the top of the dashboard, users can efficiently locate specific data elements, facilitating better data management and access. This functionality is especially useful for large datasets, ensuring users can swiftly find the information they need without navigating through multiple layers of the interface. 

!!! tip
    Press the shortcut key: Ctrl+K for quick access to Global Search

![global-search](../assets/dashboard/global-search-light.png#only-light)
![global-search](../assets/dashboard/global-search-dark.png#only-dark)

## In-App Notifications

In-app notifications in Qualytics are real-time alerts that keep users informed about various events related to their data operations and quality checks. These notifications are displayed within the Qualytics interface and cover a range of activities, including operation completions, anomaly detections, and service level agreement (SLA) status updates.

![nav-notification](../assets/dashboard/nav-notification-light.png#only-light)
![nav-notification](../assets/dashboard/nav-notification-dark.png#only-dark)

## Discover

The **Discover** option in Qualytics features a dropdown menu that provides access to various resources and tools to help users navigate and utilize the platform effectively. The menu includes the following options:

**Resources:**

- **User Guide**: Opens the comprehensive user guide for Qualytics, which provides detailed instructions and information on how to use the platform effectively.

- **SparkSQL**: Directs users to resources or documentation related to using SparkSQL within the Qualytics platform, aiding in advanced data querying and analysis.

**API:**

- **Docs**: Opens the API documentation, offering detailed information on how to interact programmatically with the Qualytics platform. This is essential for developers looking to integrate Qualytics with other systems or automate tasks.

- **Playground**: Provides access to an interactive environment where users can test and experiment with API calls. This feature is particularly useful for developers who want to understand how the API works and try out different queries before implementing them in their applications.

![discovery](../assets/dashboard/discovery-light.png#only-light)
![discovery](../assets/dashboard/discovery-dark.png#only-dark)

## Theme

Qualytics offers both dark mode and light mode to enhance user experience and cater to different preferences and environments.

**Light Mode:**

- This is the default visual theme of Qualytics, featuring a light background with dark text.

- It provides a clean and bright interface, which is ideal for use in well-lit environments.

- To switch from dark mode to light mode, click on the same **Light Mode** button.

**Dark Mode:**

- Dark mode features a dark background with light text, reducing eye strain and glare, especially in low-light environments.

- It is designed to be easier on the eyes during prolonged usage and can help save battery life on devices.

- To activate dark mode, click on the same **Dark Mode** button.

![light-mode-theme](../assets/dashboard/light-mode-theme.png#only-light)
![dark-mode-theme](../assets/dashboard/dark-mode-theme.png#only-dark)

## View Mode

In Qualytics, users have the option to switch between two display modes: List View and Card View. These modes are available on the Source Datastore page, Enrichment Datastore page, and Library page, allowing users to choose their preferred method of displaying information.

- **List View**: List View arranges items in a linear, vertical list format. This mode focuses on providing detailed information in a compact and organized manner. To activate List View, click the "List View" button (represented by an icon with three horizontal lines) located at the top of the page.

- **Card View**: Card View displays items as individual cards arranged in a grid. Each card typically includes a summary of the most important information about the item. To switch to Card View, click the "Card View" button (represented by an icon with a grid of squares) located at the top of the page. 

![view-mode](../assets/dashboard/view-mode-light.png#only-light)
![view-mode](../assets/dashboard/view-mode-dark.png#only-dark)

## User Profile 

The user profile section in Qualytics provides essential information and settings related to the user's account. Here's an explanation of each element:

- **Name**: Displays the user's email address used as the account identifier.

- **Role**: Indicates the user's role within the Qualytics platform (e.g., Admin), which defines their level of access and permissions.

- **Teams**: Shows the teams to which the user belongs (e.g., Public), helping organize users and manage permissions based on group membership.

- **Preview Features**: A toggle switch that enables or disables preview features. When turned on, it adds an AI Readiness Benchmark for the Quality Score specifically on the Explore page. 

- **Logout**: A button that logs the user out of their Qualytics account, ending the current session and returning them to the login page.

- **Version**: Displays the current version of the Qualytics platform being used, which is helpful for troubleshooting and ensuring compatibility with other tools and features.

![profile-menu](../assets/dashboard/profile-menu-light.png#only-light)
![profile-menu](../assets/dashboard/profile-menu-dark.png#only-dark)

## Navigation Menu (Left Sidebar)

The left sidebar of the dashboard contains the primary navigation menu, which allows users to quickly access various functionalities of the Qualytics platform. The menu items include:

### Source Datastores (Default View)

Lists all the source datastores at the left sidebar connected to Qualytics. Also provides the option to: 

- Add a new source datastore 

- Search from existing source datastores 

- Sort existing datastores based on the name, records, checks, etc. 

- Filter source datastores 

![source-datastore-nav](../assets/dashboard/source-datastore-nav-light.png#only-light)
![source-datastore-nav](../assets/dashboard/source-datastore-nav-dark.png#only-dark)

### Enrichment Datastores

Lists all the enrichment datastores at the left sidebar connected to Qualytics. Also provides the option to:. 

- Add an enrichment datastore 
- Search from existing enrichment datastores 
- Sort existing datastores based on the name, records, checks, etc. 

![enrichment-datastore-nav](../assets/dashboard/enrichment-datastore-nav-light.png#only-light)
![enrichment-datastore-nav](../assets/dashboard/enrichment-datastore-nav-dark.png#only-dark)

## Explore

The Explore dashboard in Qualytics enables effective data management and analysis through several key sections:

- **Insights**: Offers an overview of anomaly detection and data monitoring, allowing users to filter by source datastores, tags, and dates. It displays profile data, applied checks, quality scores, records scanned, and more. Moreover, you can also export the insight reports into a PDF format.  

- **Activity**: Provides a detailed view of operations (catalog, profile, and scan) across source datastores with a heatmap to visualize daily activities and detected anomalies.

- **Profiles**: Unifies all containers, including tables, views, computed tables, computed files, and fields, with search, sort, and filter functionalities.

- **Checks**: Shows all applied checks, both inferred and authored, across source datastores to monitor and manage data quality rules.

- **Anomalies**: Lists all detected anomalies across source datastores for quick identification and resolution of issues.

![explore-nav](../assets/dashboard/explore-nav-light.png#only-light)
![explore-nav](../assets/dashboard/explore-nav-dark.png#only-dark)

### Library

The library dashboard allows for managing check templates and editing applied checks in source datastores with two main functionalities:

- **Add Check Templates**: Easily add new templates to apply standardized checks across datastores.

- **Export Check Templates**: Export template metadata to a specified Enrichment datastore.

!!! tip
    You can also search, sort, and filter checks across the source datastores

![library-access](../assets/dashboard/library-access-light.png#only-light)
![library-access](../assets/dashboard/library-access-dark.png#only-dark)

### Global Settings

Manage global configurations with the following options:

- **Tags**: Categorize and prioritize entities, configure notifications, and associate tags with properties.

- **Notifications**: Set notifications for completed operations and identified anomalies.

- **Connection**: Manage datastore sources (add, edit, delete).

- **Integration**: Configure parameters for integrating external tools.

- **Security**: Manage teams, roles, and user access.

- **Tokens**: Create tokens for secure API interactions.

- **Health**: Monitor and restart the Qualytics deployment.

![global-settings](../assets/dashboard/global-settings-light.png#only-light)
![global-settings](../assets/dashboard/global-settings-dark.png#only-dark)
