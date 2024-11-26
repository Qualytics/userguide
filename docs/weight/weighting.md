# Weight Mechanism 

Weight Mechanism for checks is designed to evaluate and prioritize checks based on three key factors: Rule Type Weighting, Anomaly Weighting, and Tag Weighting.

Let’s get started 🚀

### 1. Rule Type Weighting

Each quality check rule type has a specific weight based on its importance. The rule types are divided into three categories:

#### High Importance (Weight: 3)

These rules are assigned the highest weight of 3 to reflect their crucial role in maintaining data quality.

| **No.** | **Rule Type**                  | **Weight** |
|---------|---------------------------------|------------|
| 1       | Entity Resolution               | 3          |
| 2       | Expected Schema                 | 3          |
| 3       | Matches Pattern                 | 3          |
| 4       | Predicted By                    | 3          |
| 5       | Satisfies Expression            | 3          |
| 6       | Contains Social Security Number | 3          |
| 7       | Time Distribution Size          | 3          |
| 8       | User Defined Function           | 3          |
| 9       | Is Replica Of                   | 3          |
| 10      | Metric                          | 3          |
| 11      | Aggregation Comparison          | 3          |
| 12      | Is Address                      | 3          |

#### Medium Importance (Weight: 2)

These rules are assigned the medium weight of 2 to reflect their role in maintaining data quality.

| **No.** | **Rule Type**                  | **Weight** |
|---------|---------------------------------|------------|
| 1       | Any Not Null                    | 2          |
| 2       | Between                         | 2          |
| 3       | Between Times                   | 2          |
| 4       | Contains Credit Card            | 2          |
| 5       | Contains Email                  | 2          |
| 6       | Equal To                        | 2          |
| 7       | Equal To Field                  | 2          |
| 8       | Exists In                       | 2          |
| 9       | Not Exists In                   | 2          |
| 10      | Expected Values                 | 2          |
| 11      | Greater Than Field              | 2          |
| 12      | Less Than Field                 | 2          |
| 13      | Not Future                      | 2          |
| 14      | Required Values                 | 2          |
| 15      | Unique                          | 2          |
| 16      | Contains URL                    | 2          |
| 17      | Min Partition Size              | 2          |
| 18      | Is Credit Card                  | 2          |
| 19      | Volumetric                      | 2          |

#### Low Importance (Weight: 1)

These rules are assigned the lowest weight of 1 to reflect their role in maintaining data quality.

| **No.** | **Rule Type**                  | **Weight** |
|---------|---------------------------------|------------|
| 1       | After Date Time                 | 1          |
| 2       | Before DateTime                 | 1          |
| 3       | Distinct Count                  | 1          |
| 4       | Field Count                     | 1          |
| 5       | Is Type                         | 1          |
| 6       | Max Length                      | 1          |
| 7       | Max Value                       | 1          |
| 8       | Min Length                      | 1          |
| 9       | Min Value                       | 1          |
| 10      | Not Exists In                   | 1          |
| 11      | Not Negative                    | 1          |
| 12      | Not Null                        | 1          |
| 13      | Positive                        | 1          |
| 14      | Sum                             | 1          |

### 2. Anomaly Weighting

Anomalies can impact the importance of a check by adjusting its weight. The adjustment is based on whether the check has anomalies and whether it is authored or inferred:

1. **Authored Check with Anomalies**:
**-** The check's weight increases by **12 points**.

2. **Authored Check without Anomalies**:
**-** The check's weight increases by **9 points**.

3. **Inferred Check with Anomalies**:
**-** The check's weight increases by **6 points**.

4. **Inferred Check without Anomalies**:
**-** The check's weight remains **0 points**.

### 3. Tag Weighting

Tags can further modify the weight of a check. When tags with weight modifiers are applied, their weights are added to the check’s total weight.

- **Tag with Weight Modifier**: Each tag that has a specific weight modifier will contribute to the overall weight of the check. For example, if **Tag B** has a weight of **2**, it will add **2 points** to the total weight of the check.

## Example of Weight Calculation 

Let's break down an example calculation for a check of type **Authored**, using the **isCreditCard** rule (Medium Importance), with no anomalies, and **Tag B** applied:

## Step-by-Step Calculation

- **Step 1: Rule Type Weight** – The **isCreditCard** rule has a weight of **2** (Medium Importance).
- **Step 2: Anomaly Weight** – An **Authored Check** without anomalies adds **9 points**.
- **Step 3: Tag Weight** – **Tag B** adds **2 points**.

**Total Weight** = 2 (rule type) + 9 (no anomalies) + 2 (Tag B) = **13 points**

## Additional Notes

If the table itself has a **Tag A** with a weight of **10**, the check will inherit that tag. In this case, the total weight will include both tag weights.

**Total Weight** = 2 (rule type) + 9 (no anomalies) + 2 (Tag B) + 10 (Tag A) = **23 points**

## Quick Calculation Formula

To make the calculation easier, here are the quick formulas for different types of checks:

- **For Authored Checks with Anomalies**:  
  `[Rule Type Weight] + 12 (Anomaly) + Check’s Tag Weight + Table’s Tag Weight`
  
- **For Authored Checks without Anomalies**:  
  `[Rule Type Weight] + 9 (No Anomaly) + Check’s Tag Weight + Table’s Tag Weight`
  
- **For Inferred Checks with Anomalies**:  
  `[Rule Type Weight] + 6 (Anomaly) + Check’s Tag Weight + Table’s Tag Weight`
  
- **For Inferred Checks without Anomalies**:  
  `[Rule Type Weight] + 0 (No Anomaly) + Check’s Tag Weight + Table’s Tag Weight`

## Example Calculation (Extended)

Let's extend the example with the inclusion of both **Tag A** and **Tag B**:

- **For Authored Checks with Anomalies**:  
  `[Rule Type Weight] + 12 + 10 (Tag A) + 2 (Tag B)`
  
- **For Authored Checks without Anomalies**:  
  `[Rule Type Weight] + 9 + 10 (Tag A) + 2 (Tag B)`
  
- **For Inferred Checks with Anomalies**:  
  `[Rule Type Weight] + 6 + 10 (Tag A) + 2 (Tag B)`
  
- **For Inferred Checks without Anomalies**:  
  `[Rule Type Weight] + 0 + 10 (Tag A) + 2 (Tag B)`

  
