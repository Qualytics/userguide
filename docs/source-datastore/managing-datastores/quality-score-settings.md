# Quality Score Settings

Configure the decay period and dimension weights that control how quality scores are calculated for your datastore.

!!! note "Permission Required"
    You need the **Member** user role and **Editor** team permission on the datastore to edit quality score settings. See the [Permissions](../data-quality-score/permissions.md){:target="_blank"} page for details.

!!! warning "Score Impact"
    Changing the decay period or dimension weights triggers an **immediate recalculation** of all quality scores for the datastore. This may cause scores to increase or decrease depending on the new configuration.

## Steps

**Step 1**: Navigate to your datastore overview and click the **Settings :material-cog:** button located at the top-right corner of the interface.

![settings-button](../../assets/source-datastores/data-quality-score/managing/settings/step-1-settings-button.png)

**Step 2**: A dropdown menu will appear. Click on **Score :material-numeric-8-circle-outline:** to open the quality score settings.

![score-menu](../../assets/source-datastores/data-quality-score/managing/settings/step-2-score-menu.png)

**Step 3**: The **Quality Score Settings** modal will appear with the decay period and dimension weights configuration.

!!! info "Understanding the Dimensions"
    For a detailed explanation of each quality dimension (what it measures, examples, and how they combine), see the [Quality Score Introduction](../data-quality-score/introduction.md#the-8-quality-dimensions){:target="_blank"} page.

![quality-score-settings](../../assets/source-datastores/data-quality-score/managing/settings/step-3-quality-score-settings.png)

**Step 4**: Configure the **Decay Period** — the number of days of historical data used to calculate the quality score.

![decay-period](../../assets/source-datastores/data-quality-score/managing/settings/step-4-decay-period.png)

| Setting | Default | Range | Step | Description |
| :--- | :---: | :---: | :---: | :--- |
| Decay Period | 180 days | 7–180 days | 7 days | How far back in time Qualytics looks when calculating scores. Shorter periods give a more real-time view; longer periods provide a broader historical perspective. |

**Step 5**: Adjust the **Dimension Weights** to control the importance of each quality factor in the total score. Use the slider to set each dimension's weight.

![dimension-weight-detail](../../assets/source-datastores/data-quality-score/managing/settings/step-5-dimension-weight-detail.png)

| Setting | Default | Range | Step | Description |
| :--- | :---: | :---: | :---: | :--- |
| Dimension Weight | 1.0 | 0–2.0 | 0.1 | Controls how much each dimension impacts the container score. Setting a weight to **0** disables the dimension — it turns grey and no longer affects the score. Setting it to **2.0** doubles its influence. |

**Step 6**: Click the **Save** button to apply the quality score settings.

![save-button](../../assets/source-datastores/data-quality-score/managing/settings/step-6-save-button.png)

After clicking **Save**, a success notification will confirm that the settings have been applied. The quality scores for all containers and fields in the datastore will be recalculated based on the new configuration.

!!! info "Datastore vs. Container Settings"
    Datastores and containers each have their **own independent settings**. Changing one does not affect the other. See the [Quality Score Introduction](../data-quality-score/introduction.md#independent-settings-per-level){:target="_blank"} for details on how this works.
