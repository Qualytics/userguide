The filter allows you to define a subset of data upon which the rule will operate.

It requires a valid **Spark SQL** expression that determines the criteria rows in the DataFrame should meet. This means the expression specifies which rows the DataFrame should include based on those criteria. Since it's applied directly to the Spark DataFrame, traditional SQL constructs like WHERE clauses **are not** supported.

??? example "Examples"
    **Direct Conditions**

    Simply specify the condition you want to be met.

    ???+ success "Correct usage"
        ```sql
        O_TOTALPRICE > 1000
        ```

        ```sql
        C_MKTSEGMENT = 'BUILDING'
        ```

    ???+ failure "Incorrect usage"
        ```sql
        WHERE O_TOTALPRICE > 1000
        ```

        ```sql
        WHERE C_MKTSEGMENT = 'BUILDING'
        ```

    **Combining Conditions**

    Combine multiple conditions using logical operators like `AND` and `OR`.

    ???+ success "Correct usage"
        ```sql
        O_ORDERPRIORITY = '1-URGENT' AND O_ORDERSTATUS = 'O'
        ```

        ```sql
        (L_SHIPDATE = '1998-09-02' OR L_RECEIPTDATE = '1998-09-01') AND L_RETURNFLAG = 'R'
        ```

    ???+ failure "Incorrect usage"
        ```sql
        WHERE O_ORDERPRIORITY = '1-URGENT' AND O_ORDERSTATUS = 'O'
        ```

        ```sql
        O_TOTALPRICE > 1000, O_ORDERSTATUS = 'O'
        ```

    **Utilizing Functions**

    Leverage Spark SQL functions to refine and enhance your conditions.

    ???+ success "Correct usage"
        ```sql
        RIGHT(
            O_ORDERPRIORITY,
            LENGTH(O_ORDERPRIORITY) - INSTR('-', O_ORDERPRIORITY)
        ) = 'URGENT'
        ```

        ```sql
        LEVENSHTEIN(C_NAME, 'Supplier#000000001') < 7
        ```

    ???+ failure "Incorrect usage"
        ```sql
        RIGHT(
            O_ORDERPRIORITY,
            LENGTH(O_ORDERPRIORITY) - CHARINDEX('-', O_ORDERPRIORITY)
        ) = 'URGENT'
        ```

        ```sql
        EDITDISTANCE(C_NAME, 'Supplier#000000001') < 7
        ```

    **Using scan-time variables**

    To refer to the current dataframe being analyzed, use the reserved dynamic variable `{{_qualytics_self}}`.

    ???+ success "Correct usage"
        ```sql
        O_ORDERSTATUS IN (
            SELECT DISTINCT O_ORDERSTATUS
            FROM {{_qualytics_self}}
            WHERE O_TOTALPRICE > 1000
        )
        ```

    ???+ failure "Incorrect usage"
        ```sql
        O_ORDERSTATUS IN (
            SELECT DISTINCT O_ORDERSTATUS
            FROM ORDERS
            WHERE O_TOTALPRICE > 1000
        )
        ```
    
    While subqueries can be useful, their application within filters in our context has limitations. For example, directly referencing other containers or the broader target container in such subqueries **is not supported**. Attempting to do so will result in an error.

    !!! warning "Important Note on `{{_qualytics_self}}`"
        The `{{_qualytics_self}}` keyword refers to the dataframe that's currently under examination. In the context of a full scan, this variable represents the entire target container. However, during incremental scans, it only reflects a subset of the target container, capturing just the incremental data. It's crucial to recognize that in such scenarios, using `{{_qualytics_self}}` may not encompass all entries from the target container.
