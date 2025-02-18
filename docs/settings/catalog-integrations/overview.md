# Data Catalog Integrations

The Qualytics platform seamlessly integrates with enterprise data catalogs, enabling organizations to:
- Surface data quality insights directly within existing catalog tools
- Automatically sync metadata between platforms in real-time
- Leverage data catalog tags for quality classification
- Push quality alerts and anomaly notifications to catalog users
- Maintain consistent metadata across platforms
- Track data quality metrics within your data governance framework

These catalog integrations ensure that data quality insights are readily available to users within their preferred data discovery and governance platforms.

## Setting Up Catalog Integration

Navigate to Settings > Integration to configure your data catalog connection:

![setting](../../assets/integrations/overview/setting-button-light.png#only-light)
![setting](../../assets/integrations/overview/setting-button-dark.png#only-dark)

![tab](../../assets/integrations/overview/tab-button-light.png#only-light)
![tab](../../assets/integrations/overview/tab-button-dark.png#only-dark)

![integration](../../assets/integrations/overview/add-integration-button-light.png#only-light)
![integration](../../assets/integrations/overview/add-integration-button-dark.png#only-dark)

## Supported Data Catalogs

Currently, Qualytics supports integration with the following data catalog platforms:

### Atlan

The Atlan integration enables bidirectional metadata synchronization, providing:
- Automated metadata push from Qualytics to Atlan
- Real-time metadata pull from Atlan to Qualytics
- Automatic updates based on key events
- Flexible tag management options
- Simple API-based authentication

For detailed configuration steps, see the [**Atlan**](./atlan.md) documentation.

### Alation

The Alation integration supports comprehensive metadata exchange:
- Bidirectional metadata synchronization
- Real-time quality metric updates
- Selective synchronization of active checks
- Configurable tag conflict resolution
- Token-based secure authentication

For detailed configuration steps, see the [**Alation**](./alation.md) documentation.

## Synchronization Options

Qualytics provides flexible synchronization methods to match your workflow:

### Manual Sync

Trigger complete metadata synchronization on-demand:
![mannual](../../assets/integrations/overview/mannual-light.png#only-light)
![mannual](../../assets/integrations/overview/mannual-dark.png#only-dark)

For detailed steps, see the [**Synchronization**](atlan.md/#synchronization) section.

### Event Driven

Enable automatic synchronization based on platform events:
![event](../../assets/integrations/overview/event-light.png#only-light)
![event](../../assets/integrations/overview/event-dark.png#only-dark)

| Event  | Description |
| :---- | :---- |
| Run an Operation (Profile Or Scan) | Sync all target containers for the operation. |
| Archive an Anomaly (including bulk) | Sync the container in which the anomaly was identified. |
| Archive a Check ( including bulk) | Sync the container to which the check belongs. |
