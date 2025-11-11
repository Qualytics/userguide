# Containers Overview

Containers are fundamental entities representing structured data sets. These containers could manifest as tables in JDBC datastores or as files within DFS datastores. They play a pivotal role in data organization, profiling, and quality checks within the Qualytics application.

Let’s get started 🚀

## Container Types

There are two main types of containers in Qualytics:

### JDBC Container

JDBC containers are virtual representations of database objects, making it easier to work with data stored in relational databases.

!!! note
    For more information, please refer to the [jdbc container section](../container/container-types.md#jdbc-container).
    
### DFS Container

DFS containers are used to represent files stored in distributed file systems, such as Hadoop or cloud storage.

!!! note 
    For more information, please refer to the [DFS container section](../container/container-types.md#dfs-container).

## Computed Tables

Computed Tables allow you to create derived tables using SQL-like transformations on your source datastore containers.

!!! note
    For more information, please refer to the [Computed Tables Documentation](../container/computed-tables-and-files/computed-tables.md)   

## Computed Files

Computed Files allow you to generate new file-based datasets derived from existing containers within your selected datastore.

!!! note
    For more information, please refer to the [Computed Files Documentation](../container/computed-tables-and-files/computed-files.md)    

## Computed Joins

A Computed Join Container allows you to combine data from two containers, which can be from the same source datastore or different source datastores (e.g., a database table vs. a file system container).

!!! note
    For more information, please refer to the [Computed Join Documentation](../container/computed-join.md)

## Container Attributes

### Totals

Totals are calculated from sampled data, not the full dataset. Values may differ from actual totals across all records.
    
!!! note
    For more information, please refer to the [container attributes documentation](../container/container-attributes.md).

## Actions on Container

Users can perform various operations on containers to manage datasets effectively. The actions are divided into three main sections: **Settings**, **Add**, and **Run**. Each section contains specific options to perform different tasks.

!!! note
    For more information, please refer to the [actions on container documentation](../container/actions-on-container.md).

## Field Profiles

After profiling a container, individual field profiles offer granular insights:

!!! note
    For more information, please refer to the [field profiles documentation](../container/field-profiles.md).
