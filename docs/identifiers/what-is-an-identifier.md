# What is an Identifier?

* `Identifier` is a Field that can be used to help load the desired data from a Table in support of analysis. 

Two types of identifiers can be declared for a Table:
    1. `Partition Field` - used to divide the data in the table into distinct dataframes that can be analyzed in parallel.
    2. `Incremental Field` - used to track records in the table that have already been scanned in order to support Scan operations that only analyze new (not previously scanned) data.


!!! info
    * **Partition Field Selection**: When selecting a partition field for a table during catalog operation, we will attempt to select a field with no nulls where possible. 
    * **User-Specified Partition Fields**: Users are permitted to specify partition fields manually. While we ensure that the user selects a field of a supported data type, we do not currently enforce non-nullability or completeness. Care should be given to select partition fields with no or a low percentage of nulls in order to avoid unbalanced partitioning.
---

# Managing an Identifier

* You can manage an identifier in the Tables view of a selected datastore, just opening the options of a specific `table`/`file`:
 
    ![Screenshot](../assets/identifiers/identifiers-light.png#only-light)
    ![Screenshot](../assets/identifiers/identifiers-dark.png#only-dark)

* In the pop-up modal, specific configuration is displayed and can be edited:
  
    ![Screenshot](../assets/identifiers/identifier-screen-light.png#only-light)
    ![Screenshot](../assets/identifiers/identifier-screen-dark.png#only-dark)

     1. `Incremental Strategy` is the technique used to track which data from the table has already been scanned in support of incremental scan operations.
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
        * A Field that can be used to group the records in a Table into smaller sets that will be processed in parallel. The ideal Partition Identifier is an Incremental Identifier of type `datetime` such as a last-modified field, however alternatives are automatically identified and set during a Catalog operation.

    !!! info
        If no appropriate partition identifier can be selected, then repeatable ordering candidates (order by fields) are used for less efficient processing of containers with a very large number of rows.

    
