# Snowflake

## Steps to setup Snowflake

---
Fill the form with the credentials of your data source.

![Screenshot](../assets/datastores/snowflake/create-datastore-light.png#only-light){: style="height:auto;width:450px;"}
![Screenshot](../assets/datastores/snowflake/create-datastore-dark.png#only-dark){: style="height:auto;width:450px;"}

Once the form is completed, it's necessary to test the connection to verify if Qualytics is able to connect to your source of data. A successful message will be shown:

![Screenshot](../assets/datastores/test-connection/test-connection-light.png#only-light){: style="width:450px;"}
![Screenshot](../assets/datastores/test-connection/test-connection-dark.png#only-dark){: style="width:450px;"}

!!! warning 
    By clicking on the `Finish` button, it will create the Datastore and skipping the configuration of an Enrichment Datastore.

    - To configure an Enrichment Datastore in another moment, please refer [to this section](/userguide/enrichment/create-enrichment-datastore/)

!!! note 
    It is important to associate an `Enrichment Datastore` with your new Datastore

    - The `Enrichment Datastore` will allow Qualytics to record `enrichment data`, copies of the source `anomalous data` and additional `metadata` for your `Datastore`

## Configuring an Enrichment Datastore

- If you have an `Enrichment Datastore` already setup, you can link it by enable to use an existing Enrichment Datastore:

    ![Screenshot](../assets/enrichment/amazon-s3/associate-enrichment-datastore-light.png#only-light){: style="width:450px"}
    ![Screenshot](../assets/enrichment/amazon-s3/associate-enrichment-datastore-dark.png#only-dark){: style="width:450px"}

- If you don't have an `Enrichment Datastore`, you can create one at the same page:

    ![Screenshot](../assets/enrichment/amazon-s3/create-enrichment-datastore-light.png#only-light){: style="width:450px"}
    ![Screenshot](../assets/enrichment/amazon-s3/create-enrichment-datastore-dark.png#only-dark){: style="width:450px"}

Once the form is completed, it's necessary to test the connection. A successful message will be shown:

![Screenshot](../assets/enrichment/test-connection-light.png#only-light){: style="width:450px;"}
![Screenshot](../assets/enrichment/test-connection-dark.png#only-dark){: style="width:450px;"}

!!! warning 
    By clicking on the `Finish` button, it will create the Datastore and link or create the Enrichment Datastore

---
## Fields
### `Name` <spam id='required'>`required`</spam>

* The datastore name  to be created in Qualytics App

### `Account` <spam id='required'>`required`</spam>

* Host url to be connected.
* Hostname in the form 
```text
    https://<account_name>.<region>.snowflakecomputing.com.
```

* You can check [here](https://docs.snowflake.com/en/user-guide/admin-account-identifier.html) for more details.

### `Role` <spam id='required'>`required`</spam>

* Set this to the name of role that you want to use or which the account user has access to.

### `Warehouse` <spam id='required'>`required`</spam>

* The `warehouse` name that you want to use or which the account user has access to.

### `Database` <spam id='required'>`required`</spam>

* The `database` name to be connected or which the account user has access to.

### `Schema` <spam id='required'>`required`</spam>

* The `schema` name to be connected or which the account user has access to.

### `User` <spam id='required'>`required`</spam>

* The `user` that has access to the `Snowflake Data Warehouse` application.
### `Password` <spam id='required'>`required`</spam>

* The `password` that has access to the `Snowflake Data Warehouse` application.


### Snowflake `Qualytics` Warehouse <spam id='required'>`required`</spam>

#### Create a Warehouse

1. To create a warehouse with minimum requirements, you can use the following command:

    ```sql
        CREATE WAREHOUSE qualytics_wh
        WITH
            WAREHOUSE_SIZE = 'XSMALL'
            AUTO_SUSPEND = 60
            AUTO_RESUME = TRUE;
    ```

2. To give a specific warehouse as the default for a user:

    ```sql
        ALTER USER <username> SET DEFAULT_WAREHOUSE = qualytics_wh;
    ```

### `Datastore` Snowflake privileges permissions <spam id='required'>`required`</spam>

#### Creating a Custom Read-Only Role

1. Create a new role called `qualytics_read_role` by running the following command:
    
    ```sql
        CREATE ROLE qualytics_read_role;
        GRANT USAGE ON WAREHOUSE qualytics_wh TO ROLE qualytics_read_role;
    ```

2. Grant the `USAGE` privilege on the database, specific schema and table to the `qualytics_read_role` by running the following command:

    ```sql
        GRANT USAGE ON DATABASE <database_name> TO ROLE qualytics_read_role;
        GRANT USAGE ON SCHEMA <database_name>.<schema_name> TO ROLE qualytics_read_role;
        GRANT SELECT ON TABLE <database_name>.<schema_name>.<table_name> TO ROLE qualytics_read_role;

        GRANT SELECT ON ALL TABLES IN SCHEMA <database_name>.<schema_name> TO ROLE qualytics_read_role;
        GRANT SELECT ON ALL VIEWS IN SCHEMA <database_name>.<schema_name> TO ROLE qualytics_read_role;

        GRANT SELECT ON FUTURE TABLES IN SCHEMA <database_name>.<schema_name> TO ROLE qualytics_read_role;
        GRANT SELECT ON FUTURE VIEWS IN SCHEMA <database_name>.<schema_name> TO ROLE qualytics_read_role;
    ```


3. Assign the `qualytics_read_role` to the desired user by running the following command:

    ```sql
        GRANT ROLE qualytics_read_role TO USER <user_name>;
    ```

### `Enrichment Datastore` Snowflake privileges permissions <spam id='required'>`required`</spam>

#### Creating a Custom Read-Write Role

1. Create a new role called `qualytics_readwrite_role` by running the following command:

    ```sql
        CREATE ROLE qualytics_readwrite_role;
        GRANT USAGE ON WAREHOUSE qualytics_wh TO ROLE qualytics_readwrite_role;
    ```

2. Grant the `USAGE` and `MODIFY` privileges on the enrichment schema within the specific database and schema to the `qualytics_readwrite_role` by running the following command:

    ```sql
        GRANT USAGE, MODIFY ON DATABASE <database_name> TO ROLE qualytics_readwrite_role;
        GRANT USAGE, MODIFY ON SCHEMA <database_name>.<qualytics_schema> TO ROLE qualytics_readwrite_role;
        GRANT CREATE TABLE ON SCHEMA <database_name>.<qualytics_schema> TO ROLE qualytics_readwrite_role;
        GRANT SELECT ON FUTURE VIEWS IN SCHEMA <database_name>.<qualytics_schema> TO ROLE qualytics_readwrite_role;
        GRANT SELECT ON FUTURE TABLES IN SCHEMA <database_name>.<qualytics_schema> TO ROLE qualytics_readwrite_role;
        GRANT SELECT ON ALL TABLES IN SCHEMA <database_name>.<qualytics_schema> TO ROLE qualytics_readwrite_role;
        GRANT SELECT ON ALL VIEWS IN SCHEMA <database_name>.<qualytics_schema> TO ROLE qualytics_readwrite_role;
    ```

3. Assign the `qualytics_readwrite_role` to the desired user by running the following command:

    ```sql
        GRANT ROLE qualytics_readwrite_role TO USER <user_name>;
    ```

## Information on how to connect with Snowflake Data Warehouse

---

* [Configuring Snowflake Data Warehouse](https://docs.snowflake.com/en/user-guide/jdbc-configure.html)
* [Connecting Snowflake](https://docs.snowflake.com/en/user-guide-connecting.html)