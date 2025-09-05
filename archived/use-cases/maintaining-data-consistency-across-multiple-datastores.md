# Maintaining Data Consistency Across Multiple Datastores

## Overview

This use case focuses on ensuring data consistency across various datastores, which is fundamental for data replication and migration tasks.

## Goal

The primary objective is to maintain data integrity and consistency across different datastores using Qualytics' `ExistsIn` and `dataDiff` checks.

## Prerequisites

- Access to multiple datastores
- Familiarity with the `ExistsIn` and `dataDiff` features in Qualytics
- Identified source and destination datastores for comparison

## Steps

1. Set up connections to the Source and Destination Datastores in Qualytucs by selecting "Add a Datastore" from Datastore Operations
2. Run a Profile Operation on the Source and Destination Datastores
3. Click Add a Check to add an authored check for `ExistsIn` or `dataDiff`
    - For verifying against a reference table of Account IDs or Zip Codes, we recommend using `ExistsIn`.
    - For validating full tables against each other, use `dataDiff`
4. Select your Source Tables/Files and fields, if applicable
5. The select your Target Tables/Files and fields, if applicable
6. Enter your description and add any Tags for downstream workflows
7. Run a Scan Operation to assert Checks and to find Anomalies
8. Review the results to identify any Anomalies

## Expected Outcome

Upon successful implementation of this use case, any Anomalies between datastores will be promptly highlighted, ensuring the integrity and consistency of your data.

## Troubleshooting

If Anomalies are identified, check the data replication process for any issues. If missing values are found, verify the completeness of data migration from the source datastore to the destination datastore. 
