# Computed Join

A Computed Join Container allows you to combine data from two containers, which can be from the same source datastore or different source datastores (e.g., a database table vs. a file system container). You can choose the join type (Inner, Left, Right, or Full Outer) and apply transformations, filters, and custom queries to the joined result.
This feature is useful when you want to:

* Merge information from multiple source datastores into a single dataset.

* Perform cross-datastore analysis (e.g., JDBC tables with DFS files).

* Apply Spark SQL transformations and filters on top of the joined data.

Let's get started 🚀

## How It Works

The Add Computed Join form consists of:

| REF. | FIELDS  | DESCRIPTION  |
|------|----------------------------|---------------------------------------|
| 1 | **Name**               | The unique name for your computed join container.                                                                                                          |
| 2 | **Join Type**          | Choose one of the following:<br>• **Inner Join**: Keeps only rows with matching keys in both containers.<br>• **Left Join**: Keeps all rows from the left container, matching rows from the right.<br>• **Right Join**: Keeps all rows from the right container, matching rows from the left.<br>• **Full Outer Join**: Keeps all rows from both containers. |
| 3 | **Left Reference**     | • **Datastore**: Source datastore where the computed join container will be created.<br>• **Container**: The left container to join.<br>• **Field**: The key (column) to join on.<br>• **Prefix**: A label (e.g., `left`) applied to all columns from this container. |
| 4 | **Right Reference**    | • **Datastore**: Source datastore containing the second container.<br>• **Container**: The right container to join.<br>• **Field**: The key (column) to join on.<br>• **Prefix**: A label (e.g., `right`) applied to all columns from this container. |
| 5 | **Select Expression**  | A list of columns to include in the result. Columns are automatically prefixed (e.g., `left_name`, `right_name`) to avoid conflicts.                         |
| 6 | **Filter Clause (WHERE)** | Additional filters applied to the join result.                                                                                                            |

![computed-join](../assets/container/computed-join/computed-join-light.png)

## Example Use Case

**Scenario**

We want to join:

* **Left Container**: customers
* **Right Container**: orders
* **Join Key**: customer_id
* **Join Type**: Left Join
* **Prefixes**: cust_ and order_

### Input Tables

#### customers

| customer_id | name   | city   |
|-------------|--------|--------|
| 1           | Alice  | Berlin |
| 2           | Bob    | London |
| 3           | Charlie| Paris  |

#### orders

| order_id | customer_id | product  |
|----------|-------------|----------|
| 101      | 1           | Laptop   |
| 102      | 1           | Mouse    |
| 103      | 2           | Keyboard |

---

#### Joined Result (Left Join)

| cust_customer_id | cust_name | cust_city | order_order_id | order_product |
|------------------|-----------|-----------|----------------|---------------|
| 1                | Alice     | Berlin    | 101            | Laptop        |
| 1                | Alice     | Berlin    | 102            | Mouse         |
| 2                | Bob       | London    | 103            | Keyboard      |
| 3                | Charlie   | Paris     | NULL           | NULL          |

---

### Visual Diagram

```text

+------------+                 +--------+
| customers  |    LEFT JOIN    | orders |
+------------+ <-------------> +--------+
    |                               |
    +-- customer_id = customer_id --+

```
## API Example

### Endpoint

**Post:** `/api/containers` 

**Expected response:** `200 OK`

---

=== "Request Payload"
    ```json
    {
        "container_type": "computed_join",
        "name": "customer_orders_join",
        "select_clause": "cust_customer_id, cust_name, cust_city, order_order_id, order_product",
        "where_clause": null,
        "left_join_field_name": "customer_id",
        "left_prefix": "cust",
        "right_join_field_name": "customer_id",
        "right_prefix": "order",
        "join_type": "left",
        "left_container_id": 101,
        "right_container_id": 202
    }
    ```
## Tips

* Always set prefixes to avoid column name collisions.
* Use Select Expression to choose only the columns you need.
* Apply Filter Clause for better performance by reducing unnecessary data.
* Test the join type with sample data to verify expected behavior.