# Complex Data Types

Qualytics provides comprehensive support for **complex data types** (Arrays, Structs, and nested combinations) across the entire data quality pipeline: schema discovery, profiling, quality checks (scanning), anomaly reporting, and automatic constraint inference.

!!! warning "DFS Datastores Only"
    Complex data type support is currently available for **DFS (Data File System) datastores** only (e.g., Amazon S3, Azure Data Lake, Google Cloud Storage). It is **not supported** for JDBC-based datastores. For more information on DFS datastores, see the [DFS Datastore Overview](../source-datastore/add-datastores/overview-of-a-dfs-datastore.md){target="_blank"}.

## What Are Complex Data Types?

Most data fields are simple (scalar) values like a single number, string, date, or boolean. **Complex data types** contain structured or repeated data within a single field.

Think of it this way:

- A **simple field** is like a single box holding one item, such as a name, a price, or a date.
- A **complex field** is like a box that contains other boxes inside it, such as a list of tags, a customer record with multiple sub-fields, or an order with multiple line items.

Here are the three main types:

| Type | What It Is | Real-World Analogy | Example |
| :---- | :---- | :---- | :---- |
| **Array** | A list of values in a single field | A shopping list with multiple items | `tags`: `["billing", "prod", "alerts"]` |
| **Struct** | A group of named sub-fields | A contact card with name, email, phone | `user`: `{first: "Alice", last: "Smith"}` |
| **Nested** | Arrays of Structs, Structs within Structs, etc. | An order with multiple line items, each having a name and price | `items`: `[{sku: "SKU-1001", price: 29.99}]` |

## Why Does This Matter?

Modern data formats (JSON, Parquet, Avro) commonly use complex types. Without proper support, quality checks could only validate flat, scalar columns, leaving structured and nested data completely unmonitored.

**In simple terms:** If your data has lists or nested records inside a single column, you need complex type support to validate it.

With complex type support, you can answer questions like:

- "Are all email addresses in the list valid?"
- "Does the tags list have at least 2 items?"
- "Is the user's country one of US, CA, or GB?"
- "Is every item's price between 0 and 200?"

## Why Should You Use Complex Data Type Checks?

### 1. Validate Data You Couldn't Before

Without complex type support, arrays and structs were invisible to quality checks. Now you can monitor **every level** of your nested data.

### 2. Catch Hidden Issues Early

A table might look fine at first glance (no missing rows, no schema errors), but inside an array, there could be null elements, unexpected values, or duplicates. Complex type checks catch these **before they reach dashboards or models**.

### 3. No New Rules to Learn

Qualytics reuses the same quality check rules you already know (`notNull`, `between`, `expectedValues`, etc.) and makes them work intelligently with arrays and structs. No special syntax or new rule types required.

### 4. Automatic Discovery

When you profile your data, Qualytics **automatically discovers** all nested fields and makes them individually checkable. You don't need to configure anything. Just profile and start creating checks.

## Real-Life Example: E-Commerce Order Validation

### The Situation

An e-commerce company stores order data in Parquet files on **Amazon S3**. Each order record contains a `line_items` field, which is an **Array of Structs** where each item has a `sku`, `quantity`, and `price`.

```json
{
  "order_id": "ORD-9921",
  "customer": { "name": "Alice Smith", "country": "US" },
  "line_items": [
    { "sku": "SKU-1001", "quantity": 2, "price": 29.99 },
    { "sku": "SKU-1002", "quantity": -1, "price": 49.99 }
  ]
}
```

### The Problem

The data pipeline ran without errors: no missing rows, no schema mismatches. However, some financial reports were showing **incorrect revenue totals**. The issue was hidden inside the nested `line_items` array: some items had **negative quantities**, which should never happen.

### The Solution

After profiling the data in Qualytics, the team discovered the nested fields `line_items.sku`, `line_items.quantity`, and `line_items.price`. They set up the following quality checks:

| Check | Rule | What It Validates |
| :---- | :---- | :---- |
| Every quantity must be positive | `positive` on `line_items.quantity` | Ensures no negative or zero quantities appear inside any order |
| Every SKU must match a pattern | `matchesPattern` on `line_items.sku` | Ensures all SKUs follow the `SKU-NNNN` format |
| Every price must be in range | `between` on `line_items.price` | Ensures all prices are between 0.01 and 10,000 |
| Customer country must be valid | `expectedValues` on `customer.country` | Ensures the country code is one of the allowed values |
| Each order must have at least 1 item | `minLength` on `line_items` with `is_element_context: true` | Ensures no empty orders exist |

### The Outcome

The next scan immediately flagged **23 orders with negative quantities** and **4 orders with unrecognized SKU formats**. The root cause was traced to an upstream system migration that introduced bad default values. The checks now run automatically on every scan, preventing bad data from reaching financial reports.

---

## Supported Complex Types

| Type | Example | Profiling | Scanning | Constraint Inference |
| :---- | :---- | :---- | :---- | :---- |
| Array of primitives | `Array[String]`, `Array[Long]`, `Array[Double]`, `Array[Boolean]` | Yes | Yes | Yes |
| Array of Structs | `Array[Struct{city: String, zip: String}]` | Yes | Yes (sub-field checks) | Yes |
| Struct | `Struct{version: String, active: Boolean}` | Yes | Yes (dot-path access) | Yes |
| Nested Struct | `Struct{inner: Struct{val: String}}` (up to 4+ levels deep) | Yes | Yes | Yes |
| Struct containing Array | `Struct{items: Array[String]}` | Yes | Yes | Yes |
| Array of Structs with Arrays | `Array[Struct{tags: Array[String]}]` | Yes | Yes | Yes |
| Array of Arrays | `Array[Array[String]]` | Yes | Yes | Limited |
| **Map types** | `Map[String, T]` | **No** | **No** | **No** |

!!! warning "Known Limitation"
    Map types (key-value pairs with variable keys) are not supported. Map fields are automatically skipped during profiling. Do not create quality checks targeting Map fields.

### What the Columns Mean

**Profiling:** Complex types require additional profiling logic beyond what scalar fields need:

- **Array-level statistics** are computed: min/max/mean array length, std dev of length, and total element count. These metrics don't exist for scalar fields.
- **Element-level statistics** treat each array element as a value and compute distinct count, min/max (numeric arrays), and min/max string length (string arrays). A separate element histogram shows the frequency distribution of individual values inside arrays.
- **Projection** of Array[Struct] fields into individual sub-fields (e.g., `items.sku`, `items.price`) happens during profiling. This is the step that creates the dot-path fields you use for quality checks.

**Scanning:** The scan engine handles complex types differently from scalar fields:

- **Arrays are validated element-wise**. For example, `notNull` on `items.sku` checks every element in every row's array, not just one value per row.
- **Dot-paths are navigated** to reach nested struct sub-fields within the source data.

**Constraint Inference:** The inference engine must understand which check types and thresholds are valid for arrays vs scalars:

- `minLength`/`maxLength` on an Array field checks **array length** (number of elements), not string length.
- `expectedValues` on an Array[String] infers from **element values**, not the whole array as a blob.
- "Limited" (Array of Arrays) means the engine cannot generate meaningful constraints for doubly-nested structures.

---

## How Fields Are Discovered and Named

All fields, including both top-level parents and complex type sub-fields, only appear in the UI after you run a [**Profile**](../source-datastore/operations/profile.md){target="_blank"} operation. The profile operation discovers all fields, projects complex types (Array[Struct], nested Structs) into dot-path sub-fields, and computes statistical profiles.

!!! warning "Important"
    You must run a **profile** operation before any fields appear in the field list. This is when complex type sub-fields (e.g., `items.sku`, `user.name.first`) are created via projection.

**In simple terms:** If you have a `user` struct with a `name` sub-field that has a `first` value, Qualytics names it `user.name.first`, and you can create quality checks on it just like any other field.

### Naming Convention

```
Top-level fields:      id, event_time, tags
Struct sub-fields:     metadata.version, metadata.active
Nested Struct fields:  user.profile.name
Array[Struct] fields:  items.sku, items.price.amount
```

### Examples

Given this data structure:

```json
{
  "id": 1,
  "tags": ["billing", "prod"],
  "user": {
    "name": { "first": "Alice", "last": "Smith" },
    "emails": ["alice@example.com"]
  },
  "items": [
    { "sku": "SKU-1001", "price": { "amount": 29.99, "currency": "USD" } }
  ],
  "metadata": { "source": "api" }
}
```

After running a **profile** operation, Qualytics discovers all fields, both top-level and projected sub-fields:

| Field Path | Type | Origin |
| :---- | :---- | :---- |
| `id` | Long | declared |
| `tags` | Array[String] | declared |
| `user` | Struct | declared |
| `user.name.first` | String | projected |
| `user.name.last` | String | projected |
| `user.emails` | Array[String] | projected |
| `items` | Array[Struct] | declared |
| `items.sku` | String | projected |
| `items.price.amount` | Double | projected |
| `items.price.currency` | String | projected |
| `metadata.source` | String | projected |

!!! tip
    When creating quality checks, use these dot-notation paths exactly as they appear in the field list. For example, to check that every item's SKU matches a pattern, target the field `items.sku`.

### How Array[Struct] Fields Are Projected

When Qualytics encounters an Array of Structs column, it automatically **projects** (extracts) each struct member into its own independent field. This is the key mechanism that makes nested data quality-checkable.

**Example:** A column `line_items: Array[Struct{sku: String, qty: Int, price: Decimal}]` becomes:

```
line_items             (Array[Struct], parent field, declared)
├── line_items.sku       (Array[String], projected sub-field)
├── line_items.qty       (Array[Integer], projected sub-field)
└── line_items.price     (Array[Decimal], projected sub-field)
```

Each projected sub-field becomes its own array column and receives full array-level + element-level profiling. Quality checks can target each sub-field independently. For example, you can check that every `price` element is positive, or that every `sku` matches a pattern.

**For deeply nested structures** like `Array[Array[Struct{a: String, b: Int}]]`, Qualytics handles the nesting transparently so you see the projected sub-fields just like any other field. The original schema type is preserved in metadata, so the UI and API always show the true declared type.

### Struct Fields in the UI Sidebar

Struct fields appear as **expandable nodes** in the field sidebar tree. Clicking a struct parent reveals its child fields. A dedicated **"Fields" tab** appears on the parent field's detail page, listing all child sub-fields. This hierarchy makes it easy to navigate complex schemas.

---

## Field Metadata

After profiling, Qualytics provides metadata that helps you understand how each field was discovered and how its type was determined.

### Column Origin

Tells you **how the field got into your field list**:

| Value | Meaning | Example |
| :---- | :---- | :---- |
| `declared` | The field was discovered directly from the source schema | `id`, `tags`, `user` |
| `projected` | The field was created by expanding a complex type (e.g., extracting sub-fields from a Struct or Array of Structs) | `items.sku`, `user.name.first`, `items.price.amount` |

!!! tip
    Top-level fields are always "declared". Dot-notation sub-fields extracted from Structs or Arrays of Structs are "projected".

### Type Source

Tells you **how the data type was determined**:

| Value | Meaning | Example |
| :---- | :---- | :---- |
| `schema` | The data type came from the source schema definition | Parquet files with explicit `Array[String]` type definitions |
| `inferred` | The data type was deduced by analyzing the actual data values | JSON files where types are inferred from values |

### Element Type Source

Same concept as Type Source, but specifically for **array element types**. Only populated when the field is an Array type.

- Tracks whether the element type (e.g., `String` in `Array[String]`) came from the schema or was inferred from values.
- **Type inference within arrays:** Qualytics performs type inference on array elements. For example, an `Array[String]` where all elements are numeric strings (e.g., `["100", "200", "350"]`) will have its element type inferred as `Integral`. This enables numeric checks like `between` and `notNegative` on arrays that are technically typed as strings but contain numeric data.

!!! note
    These metadata fields appear in the field details and field profile responses in the Qualytics UI and API.

---

## Profiling Behavior

When you run a [**Profile**](../source-datastore/operations/profile.md){target="_blank"} operation on data containing complex types, Qualytics generates rich statistical profiles, just as it does for scalar fields, but with additional metrics specific to arrays and their elements.

**In simple terms:** Profiling tells you "what does my data look like?" For arrays, you get two layers of answers: what the arrays look like (sizes, completeness) **and** what the values inside the arrays look like (ranges, patterns, distribution).

### General Profiling Behavior

- **Array fields** are fully profiled with both array-level and element-level statistics.
- **Struct sub-fields** are discovered and appear as individual fields with dot-notation paths. Each sub-field is profiled independently.
- **Nested combinations** are fully supported. Arrays of Structs, Structs within Structs, etc. are all flattened and profiled.
- **Map fields** are unsupported and are automatically skipped during profiling. Other fields in the same dataset are still profiled normally.

### Array-Level Statistics

For every Array field, Qualytics computes statistics about the **arrays themselves** (how many elements each row's array contains):

| Metric | Description | Example |
| :---- | :---- | :---- |
| **Min Length** | The smallest number of elements in any array across all rows | A `tags` field where the smallest array has 2 elements |
| **Max Length** | The largest number of elements in any array across all rows | A `tags` field where the largest array has 5 elements |
| **Mean Length** | The average number of elements per array | If arrays have 2, 3, 4, 5 elements, mean = 3.5 |
| **Std Dev Length** | The standard deviation of array element counts | Measures how much array sizes vary across rows |
| **Total Element Count** | The total number of elements across all arrays in all rows | 100 rows with average 3 elements each = 300 |
| **Completeness** | The percentage of rows where the array is not null | If 5 out of 100 rows have null arrays, completeness = 0.95 |

!!! note
    `min_length` and `max_length` on an Array field refer to the **number of elements** in the array, not string character length. This is the same metric that the `minLength`/`maxLength` quality check rules validate when applied to arrays.

### Element-Level Statistics

For Array fields, Qualytics also profiles the **individual elements inside the arrays**. These statistics describe the values contained within the arrays:

| Metric | Description | Applies To |
| :---- | :---- | :---- |
| **Element Data Type** | The detected data type of elements (e.g., `String`, `Integral`, `Fractional`, `Boolean`, `Date`, `Timestamp`) | All Array fields |
| **Element Approx Distinct Count** | The approximate number of distinct element values across all arrays | All Array fields |
| **Element Min** | The minimum numeric element value across all arrays | `Array[Long]`, `Array[Double]` |
| **Element Max** | The maximum numeric element value across all arrays | `Array[Long]`, `Array[Double]` |
| **Element Min Length** | The shortest string element (by character count) across all arrays | `Array[String]` |
| **Element Max Length** | The longest string element (by character count) across all arrays | `Array[String]` |

**Example:** For a `scores` field of type `Array[Long]` containing values like `[85, 92, 78]`, `[60, 95]`, `[100, 45, 88]`:

- Element data type: `Integral`
- Element approx distinct count: ~8
- Element min: 45
- Element max: 100

### Value Distribution and Histograms

For scalar (non-array) fields, Qualytics produces a single histogram showing the distribution of values across rows. For **Array fields**, Qualytics produces **two separate distributions**, each answering a different question.

#### Array Value Distribution (Standard Histogram)

**What it answers:** "What does the overall column look like across rows?"

For array fields, the standard histogram shows the distribution of the **array as a column**. This is the same histogram type used for scalar fields. Depending on the field type, this may show the distribution of array sizes or the top-level column values.

**Example: `tags` field (Array[String])**

Suppose the `tags` field across 5 rows has these arrays:

- Row 1: `["billing", "prod"]` (2 elements)
- Row 2: `["billing", "staging", "alerts"]` (3 elements)
- Row 3: `["prod", "alerts"]` (2 elements)
- Row 4: `["billing"]` (1 element)
- Row 5: `["prod", "staging", "alerts", "export"]` (4 elements)

The **standard histogram** would represent the distribution at the column level. The accompanying array-level statistics would show:

- Min Length: 1 (smallest array)
- Max Length: 4 (largest array)
- Mean Length: 2.4 (average array size)

#### Element Value Distribution (Element Histogram)

**What it answers:** "What individual values appear inside the arrays, and how often?"

The element histogram is **unique to array fields**. It flattens all arrays across all rows and counts the frequency of each individual element value. This gives you a complete picture of the value landscape *inside* your arrays.

**Example: same `tags` field as above**

After flattening all arrays into individual elements:

- `"billing"` appears in rows 1, 2, 4 → count = 3
- `"prod"` appears in rows 1, 3, 5 → count = 3
- `"alerts"` appears in rows 2, 3, 5 → count = 3
- `"staging"` appears in rows 2, 5 → count = 2
- `"export"` appears in row 5 → count = 1

The **element histogram** would show:

| Value | Count | Ratio |
| :---- | :---- | :---- |
| `billing` | 3 | 0.250 |
| `prod` | 3 | 0.250 |
| `alerts` | 3 | 0.250 |
| `staging` | 2 | 0.167 |
| `export` | 1 | 0.083 |

#### Side-by-Side Comparison

| Aspect | Array Value Distribution | Element Value Distribution |
| :---- | :---- | :---- |
| **Scope** | One entry per row | One entry per element across all rows |
| **What it counts** | Arrays as column values | Individual values inside the arrays |
| **Question it answers** | "What do the arrays look like across my dataset?" | "What values appear inside the arrays, and how often?" |
| **Available for** | All field types (scalar and array) | **Array fields only** |
| **Use case** | Understanding column-level distribution, completeness | Identifying unexpected element values, informing `expectedValues` checks |

!!! tip
    The element histogram is invaluable for setting up `expectedValues` checks. If the element histogram shows 10 distinct tag values, you can use those exact values as your allowed list. If a new unexpected value appears in a future scan, the check will flag it as an anomaly.

### Scalar vs. Array Field Profiles

To make the difference concrete, here is a comparison of what profile data you get for a scalar field vs. an array field.

#### Scalar Field Profile (e.g., `age` of type `Long`)

| Metric | Example Value |
| :---- | :---- |
| Field Type | `Integral` |
| Completeness | 0.98 (98% non-null) |
| Approx Distinct Values | 45 |
| Min | 18 |
| Max | 65 |
| Mean | 34.2 |
| Std Dev | 12.1 |
| Q1 / Median / Q3 | 25 / 33 / 43 |
| Kurtosis / Skewness | -0.5 / 0.3 |
| Entropy | 3.8 |
| Histogram Buckets | `{18: 5, 19: 3, 20: 8, ...}` |

#### Array Field Profile (e.g., `tags` of type `Array[String]`)

| Metric | Example Value | Category |
| :---- | :---- | :---- |
| Field Type | `Array` | Basic |
| Completeness | 0.95 (95% of rows have non-null arrays) | Basic |
| Min Length | 1 (smallest array has 1 element) | **Array-level** |
| Max Length | 5 (largest array has 5 elements) | **Array-level** |
| Mean Length | 2.8 (average array has ~3 elements) | **Array-level** |
| Std Dev Length | 1.2 | **Array-level** |
| Total Element Count | 280 (across 100 rows) | **Array-level** |
| Histogram Buckets | Standard column distribution | Basic |
| Element Data Type | `String` | **Element-level** |
| Element Approx Distinct Count | 10 (10 unique tag values) | **Element-level** |
| Element Min Length | 4 chars (shortest tag: `"prod"`) | **Element-level** |
| Element Max Length | 10 chars (longest tag: `"onboarding"`) | **Element-level** |
| Element Histogram Buckets | `{"billing": 45, "prod": 38, "alerts": 32, ...}` | **Element-level** |

#### Array Field Profile for Numeric Types (e.g., `scores` of type `Array[Long]`)

| Metric | Example Value | Category |
| :---- | :---- | :---- |
| Field Type | `Array` | Basic |
| Completeness | 1.0 | Basic |
| Min Length | 2 | **Array-level** |
| Max Length | 5 | **Array-level** |
| Mean Length | 3.5 | **Array-level** |
| Total Element Count | 350 | **Array-level** |
| Element Data Type | `Integral` | **Element-level** |
| Element Approx Distinct Count | 85 | **Element-level** |
| Element Min | 0 (smallest value in any array) | **Element-level** |
| Element Max | 100 (largest value in any array) | **Element-level** |
| Element Histogram Buckets | `{0: 2, 1: 3, 2: 5, ...}` | **Element-level** |

!!! info "Key Takeaway"
    Array field profiles give you three layers of information: **(1)** basic field info like completeness, **(2)** array-level stats about array sizes, and **(3)** element-level stats about the values inside the arrays. This rich profiling data powers both the UI visualizations and the automatic constraint inference engine.

### Struct Field Profiling

For Struct fields, Qualytics provides:

| Feature | Description |
| :---- | :---- |
| **Sub-field Paths** | A list of the nested sub-field references (e.g., `["user.name", "user.age"]`) discovered within the struct |
| **Completeness** | Whether the struct field itself is null or not, across all rows |
| **Individual Sub-Field Profiles** | Each sub-field (accessed via dot-notation) gets its own full field profile with all applicable statistics |

**Example:** For a `user` struct containing `{name: {first: String, last: String}, age: Int}`:

- The `user` field profile shows sub-field paths: `["user.name.first", "user.name.last", "user.age"]`
- `user.name.first` gets its own profile with completeness, distinct count, histogram, etc.
- `user.age` gets its own profile with min, max, mean, histogram, etc.

### Profiling Summary by Complex Type

| Complex Type | Array-Level Stats | Element-Level Stats | Element Histogram | Sub-Field Discovery | Standard Histogram |
| :---- | :---- | :---- | :---- | :---- | :---- |
| **Array[Primitive]** (e.g., `Array[String]`) | Yes | Yes | Yes | N/A | Yes |
| **Array[Struct]** (e.g., `Array[Struct{...}]`) | Yes | Via projected sub-fields | Via projected sub-fields | Yes | Via sub-fields |
| **Struct** (e.g., `Struct{...}`) | N/A | N/A | N/A | Yes | Via sub-fields |
| **Nested Struct** (e.g., `Struct{inner: Struct{...}}`) | N/A | N/A | N/A | Yes (all levels) | Via sub-fields |
| **Array[Array[T]]** | Yes (outer array) | Limited | Limited | N/A | Limited |
| **Map[K,V]** | **Not supported** | **Not supported** | **Not supported** | **Not supported** | **Not supported** |

### Nested Array Profiling

For nested arrays that arise from struct projections (e.g., `orders.items.price` producing `Array[Array[Int]]`), Qualytics automatically flattens the nesting so that element-level statistics cover all values regardless of nesting depth.

For top-level `Array[Array[T]]` columns in the source schema, element statistics operate on the inner arrays as units rather than individual scalar values.

Array-level metrics like `minLength` / `maxLength` always measure the **outermost array dimension**, meaning how many top-level elements each row's array contains.

---

## Quality Check Rules for Arrays

One of the most important things to understand: **there are no dedicated "array" rule types**. You use the same quality check rules you already know (like `notNull`, `between`, `expectedValues`) and Qualytics makes them work intelligently with arrays.

**In simple terms:** If you know how to create a check on a regular field, you already know how to create a check on an array field.

### How It Works

When you create a quality check targeting an array field, Qualytics needs to know one thing: are you checking **the array itself** or **each element inside the array**?

Think of it like inspecting a bag of apples:

- **Array-level check:** "Does this bag have at least 3 apples?" (checking the container)
- **Element-level check:** "Is every apple in this bag fresh?" (checking each item)

For most rules, this is automatically determined. But for a few "dual-mode" rules, you control the behavior by setting a property called **`is_element_context`**.

### The `is_element_context` Property

The `is_element_context` property is a **boolean toggle** available on quality checks. It appears in the check's `properties` section and controls how a rule behaves when targeting an array field.

| Setting | Meaning |
| :---- | :---- |
| **Not set** or **`false`** | The rule operates at the **container/column level**, checking the array as a whole or the column value itself |
| **`true`** | The rule operates at the **element level**, validating every individual element inside the array |

!!! note
    Setting `is_element_context` on a non-array field has no effect and is silently ignored. The flag only changes behavior when the target field is an Array type.

### Dual-Mode Rules

These rules have **two distinct behaviors** depending on the flag. Qualytics does **not** auto-set the flag for these rules, so you must explicitly choose which mode you want.

| Rule | `is_element_context` NOT set (default) | `is_element_context: true` |
| :---- | :---- | :---- |
| **`notNull`** | Checks the **column value** is not null (the entire array exists) | Checks **every element** inside the array is not null |
| **`unique`** | Checks values are **unique across all rows** (standard row-uniqueness) | Checks all elements **within each array** are unique (no duplicates per row) |
| **`notEmpty`** | Checks a string is not empty (`""`) | Checks the array has **at least one element** (size > 0) |
| **`minLength`** | Checks a string has **at least N characters** | Checks the array has **at least N elements** |
| **`maxLength`** | Checks a string has **at most N characters** | Checks the array has **at most N elements** |

!!! warning
    For dual-mode rules, if you forget to set `is_element_context: true`, the rule will use its **default scalar behavior**, even when targeting an array field. This is by design, so that both container-level and element-level checks can coexist on the same field.

#### Example: Two Different Checks on the Same `tags` Array Field

| Check | `is_element_context` | What It Does |
| :---- | :---- | :---- |
| `notNull` on `tags` | Not set | Ensures the `tags` column is not null (the array itself exists) |
| `notNull` on `tags` | `true` | Ensures no individual tag element inside the array is null |
| `minLength` on `tags`, value=2 | Not set | Checks that tag strings are at least 2 characters long |
| `minLength` on `tags`, value=2 | `true` | Checks that the tags array has at least 2 elements |
| `unique` on `tags` | Not set | Checks that tags arrays are unique across rows |
| `unique` on `tags` | `true` | Checks that no single row's tags array has duplicate values |

Both the container-level and element-level variants can exist simultaneously on the same field. They are treated as separate checks.

### Auto-Set Rules

These rules **automatically** set `is_element_context: true` when you target an Array field. You do **not** need to set the flag yourself. Just create the check as you normally would and point it at the array field.

| Rule | Scalar Behavior (non-array field) | Array Behavior (auto element-wise) |
| :---- | :---- | :---- |
| **`between`** | Numeric value within min/max range | **Every element** must be within min/max |
| **`betweenTimes`** | Timestamp within time range | **Every timestamp element** within range |
| **`expectedValues`** | Value in allowed list | **Every element** must be in the allowed list |
| **`matchesPattern`** | String matches regex | **Every element** must match the regex |
| **`containsCreditCard`** | Detects credit card patterns | **Every element** checked for CC patterns |
| **`containsEmail`** | Detects email patterns | **Every element** checked for email patterns |
| **`containsSocialSecurityNumber`** | Detects SSN patterns | **Every element** checked for SSN patterns |
| **`containsUrl`** | Detects URL patterns | **Every element** checked for URL patterns |
| **`isCreditCard`** | Validates as credit card number | **Every element** validated as CC number |
| **`isType`** | String parseable as specified type | **Every element** parseable as type |
| **`notNegative`** | Value >= 0 | **Every element** must be >= 0 |
| **`positive`** | Value > 0 | **Every element** must be > 0 |
| **`notFuture`** | Timestamp not in future | **Every timestamp element** not in future |

!!! tip
    For auto-set rules, just create the check as you normally would. The system detects that the target field is an array and automatically enables element-wise validation. For example, creating a `containsEmail` check on an `emails` array field automatically validates every email address in every row's array.

### Rules That Do Not Support Arrays

These rules only work on scalar fields or operate at the dataset/shape level. They do not support `is_element_context`:

| Rule | Why No Array Support | Level |
| :---- | :---- | :---- |
| `satisfiesExpression` | Custom SQL expression (can reference `size(array)` manually) | Row-level |
| `anyNotNull` | Multi-field null check, scalar only | Row-level |
| `equalToField` / `greaterThanField` / `lessThanField` | Field-to-field comparison, scalar only | Row-level |
| `predictedBy` | Predicted value check, scalar only | Row-level |
| `afterDateTime` / `beforeDateTime` | Timestamp boundary, scalar only | Row-level |
| `requiredValues` | Checks that required values exist in the dataset (shape level) | Shape-level |
| `distinctCount` | Counts distinct values across the dataset | Shape-level |
| `fieldCount` | Counts fields in the dataset | Shape-level |
| `sum` | Sums numeric values across the dataset | Shape-level |
| `volumetric` | Row count validation | Shape-level |
| `freshness` | Data recency check | Shape-level |
| `metric` | Aggregate metric comparison | Shape-level |
| `maxValue` / `minValue` | Aggregate max/min across dataset | Shape-level |
| `dataDiff` / `isReplicaOf` | Cross-dataset comparison | Cross-dataset |
| `existsIn` / `notExistsIn` | Cross-dataset referential check | Cross-dataset |
| `expectedSchema` | Schema validation | Schema-level |

### Quick Decision Guide

Use this flowchart to decide how to set up your quality check on an array field:

``` mermaid
graph TD
    A["Is the target field an Array type?"] --> |No| B["Use the rule normally<br/>(scalar behavior)"]
    A --> |Yes| C["Is the rule in the<br/>Dual-Mode list?"]
    C --> |Yes| D["Do you want to check<br/>EACH ELEMENT?"]
    D --> |Yes| E["Set is_element_context: true"]
    D --> |No| F["Leave is_element_context unset<br/>(container-level check)"]
    C --> |No| G["Is the rule in the<br/>Auto-Set list?"]
    G --> |Yes| H["Just create the check normally<br/>(element-wise is automatic)"]
    G --> |No| I["Rule doesn't support arrays<br/>(use satisfiesExpression instead)"]
```

### Complete Rule Support Table

| Rule Type | Scalar Behavior | Array Behavior (element-wise) | `is_element_context` |
| :---- | :---- | :---- | :---- |
| `notNull` | Column value not null | Every element in the array is not null | **Dual-mode (you choose)** |
| `unique` | Value unique across rows | All elements within each array are unique (no duplicates) | **Dual-mode (you choose)** |
| `notEmpty` | String not empty (`""`) | Array has at least one element (`size > 0`) | **Dual-mode (you choose)** |
| `minLength` | String min char length | Array must have at least N elements | **Dual-mode (you choose)** |
| `maxLength` | String max char length | Array must have at most N elements | **Dual-mode (you choose)** |
| `between` | Row-level numeric range | Every element must be within min/max | Auto-set on arrays |
| `betweenTimes` | Timestamp range check | Every timestamp element within range | Auto-set on arrays |
| `expectedValues` | Value in allowed list | Every element must be in the allowed list | Auto-set on arrays |
| `matchesPattern` | Regex match | Every element must match the pattern | Auto-set on arrays |
| `containsCreditCard` | Pattern detection | Every element checked for credit card pattern | Auto-set on arrays |
| `containsEmail` | Pattern detection | Every element checked for email pattern | Auto-set on arrays |
| `containsSocialSecurityNumber` | Pattern detection | Every element checked for SSN pattern | Auto-set on arrays |
| `containsUrl` | Pattern detection | Every element checked for URL pattern | Auto-set on arrays |
| `isCreditCard` | Value is credit card number | Every element checked as credit card number | Auto-set on arrays |
| `isType` | String parseable as type | Every element parseable as type | Auto-set on arrays |
| `notNegative` | Value >= 0 | Every element must be >= 0 | Auto-set on arrays |
| `positive` | Value > 0 | Every element must be > 0 | Auto-set on arrays |
| `notFuture` | Timestamp not in future | Every timestamp element not in future | Auto-set on arrays |

### How Element-Level Validation Works

When an element-level check runs against an array, the check passes only if the condition holds for **every element** in the array. For nested structures (arrays within arrays), validation applies at every nesting level.

!!! warning
    An empty array automatically passes element-level checks (vacuous truth). If you need to ensure the array is non-empty, combine an element-level check with a container-level `notEmpty` check.

### Profiling vs. Check Assertions

Profiling computes aggregated statistics across all values, while check assertions validate each row individually. A row with 99 passing elements and 1 failing element counts as **1 failing row** because checks are all-or-nothing per row by design.

### Completeness: Three Independent Levels

For array fields, "completeness" is not a single number. Think of it like checking a carton of eggs: the carton can exist (column completeness), the carton can have eggs in it (non-emptiness), and each egg can be intact (element completeness). These are three independent questions:

| Level | What It Measures | How It's Checked |
| :---- | :---- | :---- |
| **Column completeness** | % of rows where the array column is not null | Standard `completeness` metric on the field profile |
| **Array non-emptiness** | % of rows where the array has at least 1 element | `notEmpty` rule (container-level) |
| **Element completeness** | % of elements across all arrays that are not null | `notNull` rule with `is_element_context: true` |

A row can have a non-null array that is empty. A non-empty array can contain null elements. These checks are fully independent and should be set up separately based on your data quality requirements.

---

## How Array Context Is Determined

A field is considered to be in "array context" if:

- The **field itself** is an Array type, **OR**
- **Any parent** in the dot-path is an Array type

This determines whether element-wise validation applies.

### Examples

```
tags                  → ARRAY CONTEXT (tags is Array[String])
items.sku             → ARRAY CONTEXT (items is Array[Struct], so sku is inside an array)
metadata.version      → NOT array context (metadata is Struct, version is a plain scalar)
items.features        → ARRAY CONTEXT (items is Array[Struct], features is Array[String], nested arrays)
```

!!! note
    When a field is in array context, auto-detected rules will validate each element. When it's not in array context (like `metadata.version`), rules work in their normal scalar mode.

---

## Automatic Constraint Inference

After profiling your data, Qualytics can automatically **suggest quality checks** for complex type fields. These suggestions are based on patterns detected in your data.

### Inferred Checks for Complex Types

| Suggested Check | Rule Type | Description |
| :---- | :---- | :---- |
| Array field not null | `notNull` | Array field must not be null |
| Struct field not null | `notNull` | Struct sub-field must not be null |
| Element pattern match | `matchesPattern` | Array elements must match a detected regex pattern |
| Numeric range | `between` | Numeric array elements must be within the observed range |
| Timestamp range | `betweenTimes` | Timestamp array elements must be within the observed range |

### Inference Behavior

The inference engine automatically skips check types that are not meaningful for complex types:

- `unique` checks are not suggested for complex type columns
- `expectedValues` is not suggested for `Array[Struct]` or `Array[Array]` fields

---

## Filtering Quality Checks by Element Context

You can filter your quality checks to show only container-level or element-level checks:

- **Element-level checks only:** Filter with `is_element_context = true` to see all checks that validate individual array elements.
- **Container-level checks only:** Filter with `is_element_context = false` to see all checks that validate the column/array as a whole.

This is useful when reviewing your check coverage on array fields, where you may have both types of checks active.

---

## Check Overlap Detection

Qualytics enforces a uniqueness constraint to prevent duplicate quality checks. You can have at most:

- **One check at 100% coverage** per combination of rule type + fields + filter + is_element_context
- **One check at less than 100% coverage** per the same combination

### What This Means in Practice

```
CONFLICT (will be rejected):
  minLength on tags, value=2, coverage=100%   ← First check, created OK
  minLength on tags, value=3, coverage=100%   ← REJECTED, same rule + field + coverage band

OK (different coverage bands):
  minLength on tags, value=2, coverage=100%   ← 100% coverage band
  minLength on tags, value=3, coverage=50%    ← Less-than-100% coverage band, no conflict
```

!!! warning
    The actual `value`, `min`, `max`, `list`, or `pattern` settings are **not** part of the overlap detection. Only the rule type, target fields, filter, element context setting, and coverage band matter.

!!! tip
    If you want to test multiple thresholds for the same rule on the same field (e.g., "at least 2 tags" AND "at least 3 tags"), use different coverage values for each check.

---

## Anomaly Messages

When quality checks on array fields detect issues, the anomaly messages clearly describe the problem.

### Record-Level Messages (Individual Row Violations)

These messages appear when a specific row fails a check:

| Check Scenario | Example Message |
| :---- | :---- |
| Array too short (`minLength`) | "The field 'tags' has an array with 1 elements, which is below the minimum length of 2" |
| Array too long (`maxLength`) | "The field 'tags' has an array with 6 elements, which exceeds the maximum length of 5" |
| Duplicate elements (`unique` + element context) | "The field 'tags' has an array containing duplicate elements" |
| Null elements (`notNull` + element context) | "The field 'tags' has an array containing null elements" |
| Empty array (`notEmpty`) | "The tags value is empty" |

### Shape-Level Messages (Dataset-Wide Aggregates)

These messages summarize violations across the entire dataset:

| Check Scenario | Example Message |
| :---- | :---- |
| Array too short (`minLength`) | "For the field 'tags', 4.000% of 100 records (4) have arrays below the minimum length of 2" |
| Array too long (`maxLength`) | "For the field 'tags', 12.000% of 100 records (12) have arrays exceeding the maximum length of 5" |
| Duplicate elements (`unique` + element context) | "For the field 'tags', 24.000% of 25 records (6) have arrays containing duplicate elements" |
| Null elements (`notNull` + element context) | "For the field 'tags', 4.000% of 25 records (1) have arrays containing null elements" |
| Empty array (`notEmpty`) | "In tags, 4.000% of 25 filtered records (1) are empty" |

---

## Configuring Quality Checks: Practical Examples

Now that you understand the concepts, let's put them into practice. This section provides **ready-to-use configuration examples** for every type of quality check on complex data types. Use these as templates when setting up your own checks.

!!! note
    In the examples below, replace field names with your actual field names. The JSON structures show the properties you need to set when creating each check.

### Array Size Checks

#### Minimum Array Length (`minLength`)

Ensure an array has at least a specified number of elements.

=== "Basic Example"

    Tags must have at least 2 elements:

    ```json
    {
      "fields": ["tags"],
      "rule": "minLength",
      "description": "Tags array must have at least 2 elements",
      "properties": {
        "value": 2
      }
    }
    ```

=== "Deeply Nested Field"

    User roles must have at least 1 element:

    ```json
    {
      "fields": ["user.profile.attributes.roles"],
      "rule": "minLength",
      "description": "User roles array must have at least 1 element",
      "properties": {
        "value": 1
      }
    }
    ```

#### Maximum Array Length (`maxLength`)

Ensure an array has at most a specified number of elements.

```json
{
  "fields": ["tags"],
  "rule": "maxLength",
  "description": "Tags array must have at most 5 elements",
  "properties": {
    "value": 5
  }
}
```

### Array Element Uniqueness and Completeness

#### No Duplicate Elements (`unique` with `is_element_context`)

Ensure that no array contains duplicate values.

```json
{
  "fields": ["tags"],
  "rule": "unique",
  "description": "Tags array must not contain duplicate values",
  "properties": {
    "is_element_context": true
  }
}
```

!!! warning
    You **must** set `"is_element_context": true`. Without it, `unique` checks uniqueness across rows (the standard scalar behavior), not within each array.

#### No Null Elements (`notNull` with `is_element_context`)

Ensure that no array contains null values.

```json
{
  "fields": ["tags"],
  "rule": "notNull",
  "description": "Tags array must not contain null elements",
  "properties": {
    "is_element_context": true
  }
}
```

!!! warning
    You **must** set `"is_element_context": true`. Without it, `notNull` checks whether the entire column is null, not whether individual elements are null.

#### Array Must Not Be Empty (`notEmpty`)

Ensure that every array has at least one element.

```json
{
  "fields": ["tags"],
  "rule": "notEmpty",
  "description": "Tags array must not be empty (must have at least one element)"
}
```

!!! note
    When applied to an array field, `notEmpty` checks that the array size is greater than 0. When applied to a string field, it checks that the string is not empty (`""`).

### Array Element Value Validation

These rules automatically validate every element in the array. No special flags needed.

#### Expected Values (`expectedValues`)

Ensure every element in the array is one of the allowed values.

=== "Primitive Array"

    ```json
    {
      "fields": ["tags"],
      "rule": "expectedValues",
      "description": "All tag values must be from the allowed set",
      "properties": {
        "list": ["alerts", "beta", "billing", "export", "ingest", "onboarding", "prod", "retention", "staging", "transform"]
      }
    }
    ```

=== "Array[Struct] Sub-Field"

    ```json
    {
      "fields": ["items.sku"],
      "rule": "expectedValues",
      "description": "All item SKUs must be from the known set",
      "properties": {
        "list": ["SKU-1001", "SKU-1002", "SKU-1003"]
      }
    }
    ```

#### Pattern Matching (`matchesPattern`)

Ensure every element in the array matches a regex pattern.

=== "Primitive Array"

    ```json
    {
      "fields": ["tags"],
      "rule": "matchesPattern",
      "description": "All tag values must be lowercase letters only",
      "properties": {
        "pattern": "^[a-z]+$"
      }
    }
    ```

=== "Array[Struct] Sub-Field"

    ```json
    {
      "fields": ["items.sku"],
      "rule": "matchesPattern",
      "description": "All item SKUs must match the SKU-NNNN pattern",
      "properties": {
        "pattern": "^SKU-\\d{4}$"
      }
    }
    ```

#### Numeric Range (`between`)

Ensure every numeric element in the array is within a range.

=== "Simple Array"

    ```json
    {
      "fields": ["scores"],
      "rule": "between",
      "description": "All score values must be between 0 and 100",
      "properties": {
        "min": 0,
        "max": 100
      }
    }
    ```

=== "Deeply Nested Sub-Field"

    ```json
    {
      "fields": ["items.price.amount"],
      "rule": "between",
      "description": "All item prices must be between 0 and 200",
      "properties": {
        "min": 0,
        "max": 200
      }
    }
    ```

#### Non-Negative Values (`notNegative`)

Ensure every numeric element in the array is zero or positive.

=== "Simple Array"

    ```json
    {
      "fields": ["scores"],
      "rule": "notNegative",
      "description": "All score values must be non-negative"
    }
    ```

=== "Array[Struct] Sub-Field"

    ```json
    {
      "fields": ["items.qty"],
      "rule": "notNegative",
      "description": "All item quantities must be non-negative"
    }
    ```

#### String Length on Array Elements (`minLength` / `maxLength`)

When applied to a string array *without* `is_element_context`, these check the character length of each string element.

```json
{
  "fields": ["tags"],
  "rule": "minLength",
  "description": "All tag values must have at least 2 characters",
  "properties": {
    "value": 2
  }
}
```

```json
{
  "fields": ["tags"],
  "rule": "maxLength",
  "description": "All tag values must have at most 15 characters",
  "properties": {
    "value": 15
  }
}
```

!!! note
    This is different from checking the *array size*. To check the number of elements in the array, see the [Array Size Checks](#array-size-checks) section above.

#### Email Pattern Detection (`containsEmail`)

Ensure every string element in the array contains a valid email address.

```json
{
  "fields": ["user.emails"],
  "rule": "containsEmail",
  "description": "All email values in the array must contain valid email addresses"
}
```

#### Credit Card Pattern Detection (`containsCreditCard`)

```json
{
  "fields": ["credit_cards_array"],
  "rule": "containsCreditCard",
  "description": "All values in credit cards array must contain valid credit card numbers"
}
```

#### URL Pattern Detection (`containsUrl`)

```json
{
  "fields": ["urls_array"],
  "rule": "containsUrl",
  "description": "All values in URLs array must contain valid URLs"
}
```

#### SSN Pattern Detection (`containsSocialSecurityNumber`)

```json
{
  "fields": ["ssns_array"],
  "rule": "containsSocialSecurityNumber",
  "description": "All values in SSNs array must contain valid SSN patterns"
}
```

### Struct Sub-Field Checks (Dot-Notation)

These use standard scalar rules targeting nested struct fields via their dot-notation paths.

=== "notNull"

    ```json
    {
      "fields": ["user.name.first"],
      "rule": "notNull",
      "description": "User first name must not be null"
    }
    ```

=== "expectedValues"

    ```json
    {
      "fields": ["geo.country"],
      "rule": "expectedValues",
      "description": "Country must be one of the allowed values",
      "properties": {
        "list": ["CA", "DE", "GB", "IN", "JP", "US"]
      }
    }
    ```

=== "between"

    ```json
    {
      "fields": ["metrics.cost.amount"],
      "rule": "between",
      "description": "Cost amount must be between 0.001 and 0.025",
      "properties": {
        "min": 0.001,
        "max": 0.025
      }
    }
    ```

=== "Deeply Nested (4 Levels)"

    ```json
    {
      "fields": ["session.attrs.utm.source"],
      "rule": "expectedValues",
      "description": "UTM source must be one of the known values",
      "properties": {
        "list": ["ads", "newsletter", "organic", "partner"]
      }
    }
    ```

### Expression Checks on Complex Data

Use `satisfiesExpression` to write custom validation expressions that can reference array sizes and struct fields.

=== "Array Size Functions"

    ```json
    {
      "fields": [],
      "rule": "satisfiesExpression",
      "description": "Tags must have at least 2 elements and items at least 1",
      "properties": {
        "expression": "size(tags) >= 2 AND size(items) >= 1"
      }
    }
    ```

=== "Struct Fields"

    ```json
    {
      "fields": [],
      "rule": "satisfiesExpression",
      "description": "Latency must be under 1000ms",
      "properties": {
        "expression": "metrics.latency_ms < 1000"
      }
    }
    ```

### Multi-Field Checks

#### At Least One Field Not Null (`anyNotNull`)

```json
{
  "fields": ["nullable_field_a", "nullable_field_b", "nullable_field_c"],
  "rule": "anyNotNull",
  "description": "At least one of the nullable fields must have a value"
}
```

### Shape-Level Checks (Dataset-Wide Validation)

These checks validate properties of the entire dataset, not individual records.

=== "Distinct Count"

    ```json
    {
      "fields": ["geo.country"],
      "rule": "distinctCount",
      "description": "There must be exactly 6 distinct countries",
      "properties": {
        "value": 6,
        "comparison": "eq"
      }
    }
    ```

=== "Field Count"

    ```json
    {
      "fields": [],
      "rule": "fieldCount",
      "description": "Dataset must have exactly 36 fields",
      "properties": {
        "value": 36,
        "comparison": "eq"
      }
    }
    ```

=== "Sum"

    ```json
    {
      "fields": ["id"],
      "rule": "sum",
      "description": "Sum of all IDs must equal 5050",
      "properties": {
        "value": 5050
      }
    }
    ```

---

## Quality Check Rule Reference

Complete reference of all quality check rules and their complex type support.

| Rule Name | Required Properties | Array Support | `is_element_context` |
| :---- | :---- | :---- | :---- |
| `minLength` | `value` (number) | On arrays: checks element count (dual-mode) | You choose |
| `maxLength` | `value` (number) | On arrays: checks element count (dual-mode) | You choose |
| `notNull` | None (or `is_element_context`) | Dual-mode: column null vs element null | You choose |
| `unique` | None (or `is_element_context`) | Dual-mode: row uniqueness vs element uniqueness | You choose |
| `notEmpty` | None (or `is_element_context`) | On arrays: checks `size(array) > 0` (dual-mode) | You choose |
| `expectedValues` | `list` (array of values) | Auto element-wise on arrays | Auto-detected |
| `matchesPattern` | `pattern` (regex string) | Auto element-wise on arrays | Auto-detected |
| `between` | `min`, `max` (numbers) | Auto element-wise on arrays | Auto-detected |
| `betweenTimes` | `min_time`, `max_time` | Auto element-wise on arrays | Auto-detected |
| `notNegative` | None | Auto element-wise on arrays | Auto-detected |
| `positive` | None | Auto element-wise on arrays | Auto-detected |
| `notFuture` | None | Auto element-wise on arrays | Auto-detected |
| `isType` | `field_type` | Auto element-wise on arrays | Auto-detected |
| `isCreditCard` | None | Auto element-wise on arrays | Auto-detected |
| `containsEmail` | None | Auto element-wise on arrays | Auto-detected |
| `containsCreditCard` | None | Auto element-wise on arrays | Auto-detected |
| `containsUrl` | None | Auto element-wise on arrays | Auto-detected |
| `containsSocialSecurityNumber` | None | Auto element-wise on arrays | Auto-detected |
| `satisfiesExpression` | `expression` (SQL expression) | Can reference `size(array)` in expression | N/A |
| `anyNotNull` | None (multi-field) | Scalar only | N/A |
| `distinctCount` | `value`, `comparison` | Shape-level | N/A |
| `fieldCount` | `value`, `comparison` | Shape-level | N/A |
| `sum` | `value` | Shape-level | N/A |

---

## Configuration

No special configuration is needed to enable complex type support. It is automatic:

- **If a field is an Array type**, array-specific checks and element-wise rules apply automatically.
- **If a field is a Struct type**, sub-fields are discovered during profiling and are individually checkable using dot-notation paths.
- **For dual-mode rules** (`minLength`, `maxLength`, `notNull`, `unique`, `notEmpty`), set `is_element_context: true` in the check properties to get array-element behavior.
- **For all other array-compatible rules**, element-wise validation is automatic when the target field is an array.

!!! tip "Summary"
    Profile your data, discover your fields (including complex ones), and create quality checks using the same rules you already know. Qualytics handles the complex type logic for you.

---

## UI Experience

### Visual Indicators

| Field Type | Icon | Badge |
| :---- | :---- | :---- |
| Array | `[ ]` brackets | Element type icon (e.g., small "Abc" for `Array[String]`) |
| Struct | `{ }` braces | None |
| Scalar | Type-specific | None |

Tooltips show the full composite type notation (e.g., `Array[Struct{sku: String, qty: Int}]`).

When a quality check has `is_element_context` active, the check form shows a visual indicator, an array icon with a tooltip explaining: *"Check runs on each element individually."*

### Field Navigation

- Complex type fields appear as **expandable nodes** in the sidebar tree
- Each sub-field has its own detail page with profile metrics, checks, and quality score
- A **"Fields" tab** appears on any parent field that has children, listing all child sub-fields
- Deleting a parent field **cascades** to delete all projected children

### Field Display

- **"Declared Type"** label means the field's type came from the source schema
- **"Inferred Type"** label means the field's type was determined by profiling
- For array fields, the label reflects the **element** type source specifically. So an array might show "Inferred Type" if its element type was inferred, even if the array column itself was declared in the schema

### Restrictions

- Complex type fields and projected sub-fields **cannot be renamed** because names come from the source schema structure
- Struct and MapType parent fields show only the type label with no numeric profiling metrics (the real data lives on the sub-fields)

---

## API Surface

Complex types work through **existing API endpoints** with additional response fields and query parameters. No new endpoints were needed.

| Endpoint | Complex Type Behavior |
| :---- | :---- |
| `GET /fields` | Returns all fields including projected ones. Use `parent_field_id` and `column_origin` filters to navigate the hierarchy |
| `GET /fields/{id}` | Includes `element_data_type`, `parent_field_id`, `column_origin`, `type_source`, `element_type_source` |
| `PUT /fields/{id}` | **Blocks rename** for Array, Struct, and MapType fields (returns HTTP 406) |
| `GET /field-profiles/{id}` | Returns array-level metrics, element-level metrics, element histogram buckets, and `sub_field_paths` |
| `GET /quality-checks` | Filterable by `is_element_context` to show only container-level or element-level checks |
| `POST /quality-checks` | Set `"is_element_context": true` in the check properties to create element-level checks |

---

## Limitations

| Limitation | Detail |
| :---- | :---- |
| **MapType not supported** | `Map[K,V]` columns are skipped during profiling. Other fields in the same dataset are still profiled |
| **DFS datastores only** | Complex data type support is available for DFS datastores only (not JDBC) |
| **No rename on complex fields** | Names come from the source schema and cannot be changed in Qualytics |
| **Empty array semantics** | For-all checks on empty arrays return `true` (vacuous truth). Pair with a `notEmpty` check if you need non-empty arrays |
| **Top-level `Array[Array[T]]`** | Element-level statistics operate on inner arrays as units rather than individual scalar values |
| **`unique` not inferred on complex fields** | The inference engine suppresses `unique` checks on arrays/structs because uniqueness on nested data is rarely meaningful |
| **`expectedValues` not inferred on `Array[Struct]`** | The combinatorial explosion of struct values produces unhelpful checks, so this combination is suppressed |
