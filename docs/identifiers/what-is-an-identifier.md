# What is an Identifier?

* `Identifier` is a Field that can be used to group records in a Table Container into distinct ordered partitions in support of incremental operations:
    1. `A whole number` - all records with the same partition_id value are considered part of the same partition.

    2. `A float or timestamp` - all records between two defined values are considered part of the same partition (the defining values will be set by incremental `Scan` / `Profile` business logic).

Since Partitions are required to support `Incremental` Operations, an Incremental Identifier is required for every Table Container. 

---

# Managing an Identifier

* You can manage an identifier in the Tables view of a selected datastore, just opening the options of a specific `table`/`file`:
 
    ![Screenshot](../assets/identifiers/identifiers-light.png#only-light)
    ![Screenshot](../assets/identifiers/identifiers-dark.png#only-dark)

* In the pop-up modal, specific configuration is displayed and can be edited:
  
    ![Screenshot](../assets/identifiers/identifier-screen-light.png#only-light)
    ![Screenshot](../assets/identifiers/identifier-screen-dark.png#only-dark)

     1. `Strategy` <!-- - TODO add details -->
        * `None`
            - No incremental strategy, it will run full
        * `Last modified`
            - Available types are `Date` or `Timestamp` was last modified.
            - The "Last Modified" option uses a "last modified column" to track changes in the data set. 
            - This column typically contains a timestamp or date value that indicates when a record was last modified. 
            - The system can then compare the values in the "last modified column" to a previous timestamp or date, and only read and update the records that have been modified since that time.
        * `Batch value`
            - Available types are `Integral` or `Fractional`.
            - The "Batch Value" option uses a "batch value column" to track changes in the data set.
            - This column typically contains a incremental value that increases as new data is added to the system.
            - The system can then compare the current "batch value" with the previous one and only read and update the records that have a higher "batch value".
            - The "Batch value" option is useful when you have data coming from a system that doesn't have a modification timestamp, so in order to track changes this option could be useful, depending on the use case.
        !!! info
            - Both options are useful for incremental strategy, it depends on the availability of the data and how it is modeled. 
            - Both options will allow you to track and process only the data that has changed since the last time the system was run, reducing the amount of data that needs to be read and processed, and increasing the efficiency of your system.
    2. `Partition Field`
        * A Field that can be used by Apache Spark to group the records in a Dataframe into smaller sets that fit within Spark worker’s memory. The ideal Partition Identifier is an Incremental Identifier of type `datetime`, however alternatives are identified and exposed to the user.

    !!! info
        If no partition identifier can be identified, then repeatable ordering candidates (order by fields) are used for less efficient processing of containers with a very large number of rows.
