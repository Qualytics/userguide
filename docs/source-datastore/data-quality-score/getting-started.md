# Getting Started with Datastore Quality Score

Data Quality Scores give you a quantified, at-a-glance measure (0–100) of how healthy your data is across every datastore, container, and field in Qualytics. Scores are calculated automatically after every Profile and Scan operation, recorded as time series, and composed of 8 quality dimensions — so you can track improvements, prioritize remediation, and report on data governance.

In this section you will learn how scores are calculated, how to configure scoring settings, and how to use scores to monitor data quality. Any user with the **Member** role can view scores; editing score settings requires the **Editor** team permission.

<div class="grid cards" markdown>

-   :material-book-open-outline:{ .lg .middle } **Introduction**

    ---

    Learn how quality scores are calculated, the score hierarchy (field → container → datastore), the 8 dimensions, and what triggers recalculations.

    [:octicons-arrow-right-24: Introduction](introduction.md)

-   :material-shield-lock-outline:{ .lg .middle } **Permissions**

    ---

    See which roles can view quality scores and edit scoring settings.

    [:octicons-arrow-right-24: Permissions](permissions.md)

-   :material-tune:{ .lg .middle } **Settings**

    ---

    Configure the decay period and dimension weights for a datastore.

    [:octicons-arrow-right-24: Settings](../managing-datastores/quality-score-settings.md)

-   :material-scale-balance:{ .lg .middle } **Weighting**

    ---

    Understand how rule type, anomaly, and tag weights combine to determine check importance.

    [:octicons-arrow-right-24: Weighting](../../weight/weighting.md)

-   :material-api:{ .lg .middle } **API**

    ---

    Retrieve and update quality score settings and access historical score data via the API.

    [:octicons-arrow-right-24: API](api.md)

-   :material-help-circle-outline:{ .lg .middle } **FAQ**

    ---

    Troubleshooting, decay period behavior, dimension weights, independent settings, recalculations, and more.

    [:octicons-arrow-right-24: FAQ](faq.md)

</div>
