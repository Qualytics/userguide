# External Tags

External Tags in Qualytics make it easy to **keep your data catalog and Qualytics in sync** — so you never have to create the same tags twice.

They automatically bring in tags (like *Customer Data*, *Finance*, *PII*, etc.) from platforms such as **Atlan** or **Alation**, and apply them to the same data assets inside Qualytics.

## What Are External Tags?

**External Tags** are tags that come from an external data catalog, not from Qualytics itself.  
They’re **read-only**, meaning you can view and use them in Qualytics, but can’t edit or delete them there.

Instead, they stay connected to your catalog — whenever your catalog updates, Qualytics updates too.

### Example

Let’s say your team uses **Atlan** to tag assets with labels like:

- **Finance Data** – for tables related to financial reports  
- **Customer Data** – for customer information  
- **PII** – for sensitive or personally identifiable data  

Once Atlan is integrated, Qualytics will automatically import these same tags and show them as **External Tags**.  
You’ll see them in the tag list, filters, and on relevant assets — always in sync with your catalog.

## Why External Tags Matter

Without External Tags, teams often have to create the same tags separately in Qualytics — leading to confusion and duplicate work.  
With External Tags, you get:

- **Consistency** — the same tags appear across Atlan, Alation, and Qualytics  
- **Automatic sync** — no need to manually recreate or update tags  
- **Unified visibility** — see data quality insights for each tag  
- **Governance alignment** — your existing tagging standards stay intact  

In short, External Tags help Qualytics “speak the same language” as your data catalog.

## How It Works (Simple View)

| Step | What Happens |
|------|----------------|
| 1 | You connect [Atlan](../settings/catalog-integrations/atlan.md), [Alation](../settings/catalog-integrations/alation.md), or another supported catalog to Qualytics under **Settings → Integrations**. |
| 2 | Qualytics uses a secure API connection to read your catalog’s tags. |
| 3 | Those tags appear inside Qualytics automatically as **External Tags**. |
| 4 | Whenever a tag or asset updates in your catalog, Qualytics syncs those changes. |
| 5 | You can filter, sort, or view these tags — but editing happens in the catalog itself. |

## Real-Life Example

Imagine your company runs both a **data catalog (Atlan)** and a **data quality platform (Qualytics)**.

- In **Atlan**, your governance team adds a tag called **“Sensitive Data”** to all customer-related tables. 

- When synced, Qualytics automatically imports this tag and marks it as **External**.  

- Now, your data quality team can **filter all anomalies or checks by “Sensitive Data”** — without ever tagging them manually. 

- If the governance team later renames the tag to **“Confidential Data”**, Qualytics updates automatically.

This creates a single, reliable view of your data health — using the same tags everywhere.

## Use Cases

Here are a few practical examples of how teams use External Tags:

### Governance Teams

Use External Tags to track which datasets are **PII**, **Customer Data**, or **Financial Records** — without managing tags in multiple places.

### Data Engineers

Quickly filter quality checks in Qualytics by tags synced from your catalog — for example, view all *Finance* datasets with active anomalies.

### Compliance & Risk Teams

Easily identify sensitive assets tagged as **GDPR** or **Confidential** and monitor their data quality.

### Business Analysts

Filter dashboards and reports by External Tags like **Sales**, **Marketing**, or **Customer Behavior** to analyze data quality in context.

## Example in Action

Let’s take a real example:

1. In **Atlan**, a governance user tags three tables as **Finance**.  
2. Qualytics syncs with Atlan → those three tables now show **Finance (External)** tags in Qualytics.  
3. When viewing anomalies in Qualytics, you can filter by **Finance** to check if those datasets have open data quality issues.  
4. The moment the tag changes in Atlan, Qualytics updates it automatically — no manual work needed.

## Key Takeaways

- **External Tags** come from platforms like Atlan or Alation.  
- They are **read-only** in Qualytics but automatically stay up-to-date.  
- You can **filter, view, and analyze** your data quality using these tags.  
- All updates happen through integration — keeping catalog and Qualytics perfectly aligned.  