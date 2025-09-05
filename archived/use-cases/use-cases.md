## Introduction

In this section, we present a variety of practical scenarios illustrating how Qualytics can be utilized to solve real-world problems and achieve specific goals.

Each use case is designed to deepen your understanding of how Qualytics functions in different contexts and situations. By exploring these examples, you'll gain valuable insights into how to optimally use the various features and capabilities of Qualytics to meet your particular needs.

We've sought to include a diverse set of scenarios to cater to a wide array of user requirements. However, please keep in mind that these use cases are simply starting points. The true potential of Qualytics lies in its adaptability and customizability to fit your unique circumstances and requirements.

- **Maintaining Data Consistency Across Multiple Datastores:**
    - Guaranteeing data consistency across various datastores is crucial for data replication and migration tasks. In this context, our unique features - `ExistsIn` and `dataDiff` checks - play a pivotal role. Regardless of the database technology involved, these checks help in comparing values across datastores, pinpointing any discrepancies or missing values. The `ExistsIn` check ensures that specific data exists in the destination datastore, while the `dataDiff` ensures that data integrity is maintained when comparing data between different sources. Thus, any inaccuracies or omissions are promptly highlighted, ensuring the integrity and consistency of your data.
    - [Click here to learn more about Maintaining Data Consistency](/docs/use-cases/maintaining-data-consistency-across-multiple-datastores.md)

- **Resting Anomaly Detection - Enterprise Data Warehouse:**
    - This use case involves a mixture of automated rule inference and notifications, with the potential inclusion of manually authored rules. The user establishes a connection between Qualytics and a chosen EDW, Data Lake, or Database (options include Snowflake, BigQuery, MSSQL, and more), then applies the platform's methodology to infer rules and detect anomalies.
    - [Click here to learn more about Resting Anomaly Detection]()

- **Entity Management with Metadata Analysis:**
    - Profiling data, generating metadata, and gaining insights for improved entity management and resolution. Since Qualytics trains on data actuals, being able to do a histogram diff between values that should be equivalent can aid significantly with entity management & resolution efforts.
    - [Click here to learn more about Entity Management](/docs/use-cases/entity-management.md)

