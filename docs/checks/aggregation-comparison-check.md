# Aggregation comparison <spam id='multiple-fields'>`multiple fields`</spam>

---
*Evaluates the two aggregation expressions and evaluates their values with the given comparison operator*

The two aggregation expressions can be evaluates on distinct tables and datastores and use any valid [Spark SQL aggregation](https://spark.apache.org/docs/latest/sql-ref-functions-builtin.html#aggregate-functions).

Valid comparison values are
-  lt = less than
-  lte = less than or equal to
-  eq = equal to
-  gte = greater than or equal to
-  gt = greater than


![Screenshot](../assets/checks/rule-types/aggregation-comparison-check-dark)


Note: this check allows the user to define a separate filter for the target table versus the reference table. The target table's filter is labeled "Filter Clause" while the reference table's filter is distinguished with the label "Reference Filter"
