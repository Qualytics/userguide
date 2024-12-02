#           **Rule Types Overview**

In Qualytics, a variety of rule types are provided to maintain data quality and integrity.These rules define specific criteria that data must meet, and checks apply these rules during the validation process.

Here’s an overview of the rule types and their purposes:

# Check Rule Types

| Rule Type                                                                             | Description                                                                                        |
|---------------------------------------------------------------------------------------|----------------------------------------------------------------------------------------------------|
| [After Date Time](../checks/after-date-check.md)                                      | Asserts that the field is a timestamp later than a specific date and time.                         |
| [Any Not Null](../checks/any-not-null-check.md)                                       | Asserts that one of the fields must not be null.                                                    |
| [Before DateTime](../checks/before-date-time-check.md)                                | Asserts that the field is a timestamp earlier than a specific date and time.                       |
| [Between](../checks/between-check.md)                                                 | Asserts that values are equal to or between two numbers.                                           |
| [Between Times](../checks/between-times-check.md)                                     | Asserts that values are equal to or between two dates or times.                                    |
| [Contains Credit Card](../checks/contains-credit-card-check.md)                       | Asserts that the values contain a credit card number.                                              |
| [Contains Email](../checks/contains-email-check.md)                                   | Asserts that the values contain email addresses.                                                   |
| [Contains Social Security Number](../checks/contains-social-security-number-check.md) | Asserts that the values contain social security numbers.                                 |
| [Contains Url](../checks/contains-url.md)                                             | Asserts that the values contain valid URLs.                                                        |
| [Distinct Count](../checks/distinct-count-check.md)                                   | Asserts on the approximate count distinct of the given column.                                      |
| [Entity Resolution](../checks/entity-resolution.md)                                   | Asserts that every distinct entity is appropriately represented once and only once                                                 |
| [Equal To Field](../checks/equal-to-field-check.md)                                   | Asserts that this field is equal to another field.                                                 |
| [Exists in](../checks/exists-in-check.md)                                             | Asserts if the rows of a compared table/field of a specific Datastore exists in the selected table/field.|
| [Expected Schema](../checks/expected-schema-check.md)                                 | Asserts that all selected fields are present and that all declared data types match expectations.                                 |
| [Expected Values](../checks/expected-values-check.md)                                 | Asserts that values are contained within a list of expected values.                                 |
| [Field Count](../checks/field-count-check.md)                                         | Asserts that there must be exactly a specified number of fields.                                    |
| [Greater Than](../checks/greater-than-check.md)                                       | Asserts that the field is a number greater than (or equal to) a value.                              |
| [Greater Than Field](../checks/greater-than-field-check.md)                           | Asserts that this field is greater than another field.                                              |
| [Is Address](../checks/is-address.md)                                                 | Asserts that the values contain the specified required elements of an address.|
| [Is Credit Card](../checks/is-credit-card-check.md)                                   | Asserts that the values are credit card numbers.                                                    |
| [Is Replica Of](../checks/is-replica-of-check.md)                                     | Asserts that the dataset created by the targeted field(s) is replicated by the referred field(s).     |
| [Is Type](../checks/is-type-check.md)                                                 | Asserts that the data is of a specific type.                                                       |
| [Less Than](../checks/less-than-check.md)                                             | Asserts that the field is a number less than (or equal to) a value.                                 |
| [Less Than Field](../checks/less-than-field-check.md)                                 | Asserts that this field is less than another field.                                                 |
| [Matches Pattern](../checks/matches-pattern-check.md)                                 | Asserts that a field must match a pattern.                                                          |
| [Max Length](../checks/max-length-check.md)                                           | Asserts that a string has a maximum length.                                                         |
| [Max Value](../checks/max-value-check.md)                                             | Asserts that a field has a maximum value.                                                           |
| [Metric](../checks/metric-check.md)                                                   | Records the value of the selected field during each scan operation and asserts that the value is within a specified range (inclusive).|
| [Min Length](../checks/min-length-check.md)                                           | Asserts that a string has a minimum length.                                                         |
| [Min Partition Size](../checks/min-partition-size-check.md)                           | Asserts the minimum number of records that should be loaded from each file or table partition.      |
| [Min Value](../checks/min-value-check.md)                                             | Asserts that a field has a minimum value.                                                           |
| [Not Exists In](../checks/not-exists-in-check.md)                                     | Asserts that values assigned to this field do not exist as values in another field.                 |
| [Not Future](../checks/not-future-check.md)                                           | Asserts that the field's value is not in the future.                                                |
| [Not Negative](../checks/not-negative-check.md)                                       | Asserts that this is a non-negative number.                                                         |
| [Not Null](../checks/not-null-check.md)                                               | Asserts that the field's value is not explicitly set to nothing.                                    |
| [Positive](../checks/positive-check.md)                                               | Asserts that this is a positive number.                                                             |
| [Predicted By](../checks/predicted-by-check.md)                                       | Asserts that the actual value of a field falls within an expected predicted range.                  |
| [Required Values](../checks/required-values-check.md)                                 | Asserts that all of the defined values must be present at least once within a field.                |
| [Satisfies Expression](../checks/satisfies-expression-check.md)                       | Evaluates the given expression (any valid `Spark SQL`) for each record.                             |
| [Sum](../checks/sum-check.md)                                                         | Asserts that the sum of a field is a specific amount.                                               |
| [Time Distribution Size](../checks/time-distribution-size-check.md)                   | Asserts that the count of records for each interval of a timestamp is between two numbers.          |
| [Unique](../checks/unique-check.md)                                                   | Asserts that the field's value is unique.                                                           |
| [User Defined Function](../checks/user-defined-function-check.md)                     | Asserts that the given user-defined function (as `Scala` script) evaluates to true over the field's value.|
| [Volumetric Check](../checks/volumetric-check.md)                                     | Asserts that the volume of the data asset has not changed by more than an inclusive percentage amount for the prescribed moving daily average.|