# Getting Started with Datastore Quality Score

Data Quality Scores give you a quantified, at-a-glance measure (0–100) of how healthy your data is across every datastore, container, and field in Qualytics. Scores are calculated automatically after every Profile and Scan operation, recorded as time series, and composed of 8 quality dimensions — so you can track improvements, prioritize remediation, and report on data governance.

In this section you will find everything about data quality scores in the context of source datastores — from understanding how scores are calculated and how they influence your datastores, to configuring settings, permissions, API reference, and frequently asked questions.

## Deep Dive

Understand how data quality scores work, the 8 quality dimensions, decay periods, dimension weights, and the permissions required.

<div class="grid cards" markdown>

-   :material-book-open-outline:{ .lg .middle } **Introduction**

    ---

    Learn how quality scores are calculated, the score hierarchy (field → container → datastore), and what triggers recalculations.

    [:octicons-arrow-right-24: Introduction](introduction.md)

-   :material-shield-lock-outline:{ .lg .middle } **Permissions**

    ---

    See which roles can view quality scores and edit scoring settings.

    [:octicons-arrow-right-24: Permissions](permissions.md)

</div>

## Managing

Configure quality score settings for your datastores — adjust the decay period and dimension weights to align with your governance priorities.

<div class="grid cards" markdown>

-   :material-cog-outline:{ .lg .middle } **Settings**

    ---

    Step-by-step guide to configure the decay period and dimension weights for a datastore.

    [:octicons-arrow-right-24: Settings](../managing-datastores/quality-score-settings.md)

</div>

## Resources

<div class="grid cards" markdown>

-   :material-api:{ .lg .middle } **API**

    ---

    API endpoints to retrieve and update quality score settings and access historical score data.

    [:octicons-arrow-right-24: API](api.md)

-   :material-help-circle-outline:{ .lg .middle } **FAQ**

    ---

    Answers to common questions about data quality scores on source datastores.

    [:octicons-arrow-right-24: FAQ](faq.md)

</div>
