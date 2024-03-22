# DFS multi-token filename globbing

## Overview

Our data quality product offers a sophisticated feature that facilitates the organization and categorization of files on a distributed filesystem. This feature, known as Multi-Token Filename Globbing, enables the system to recursively scan files and intelligently group them based on shared filename conventions. It achieves this through a combination of filename pattern analysis and globbing techniques.

## Process

Delimiter Identification: The first step involves identifying a common delimiter in filenames, such as an underscore (_) or dash (-). This delimiter is used to split the filenames into tokens.
Tokenization and Grouping: Once the filenames are tokenized, the system groups them based on shared tokens. This is achieved through a method called applyMultiTokenGlobbing.
Glob Pattern Formation: The core of this feature lies in forming glob patterns that represent groups of files sharing a schema. These patterns are created using the tokens derived from the filenames.

## Methodology

- Initial Token Grouping: The method begins by grouping filenames based on each token. It considers the number of tokens and processes each token index separately.
- Left or Right Side Grouping Decision: The system decides whether to group tokens starting from the left side or the right side of the filename, based on the distribution of tokens.

- Pattern Creation Logic:

- For filenames with a single token, the system avoids globbing and keeps the filenames as they are.
- For multi-token filenames, the method constructs a container name (glob pattern) by iterating through each token.
- At each token, the method decides whether to include the token as-is or replace it with a wildcard (*). This decision is based on several factors, such as:
    - The uniqueness of the token in the context of other filenames.
    - The nature of the token (e.g., all letters).
    - The comparison of token counts in adjacent indexes.

- Special Cases Handling: The method includes logic to handle special cases, such as all-letter tokens, tokens at the beginning or end of a filename, and unique tokens.
- Glob Pattern Optimization: Finally, the system optimizes the glob patterns, ensuring that each pattern uniquely represents a group of files with a shared schema. This is done by comparing new patterns with existing ones and updating them based on the latest file modifications.

## Detailed Methodology: Multi-Token Filename Globbing

### Step-by-Step Process

#### Delimiter Identification and Tokenization

The system identifies a common delimiter in the filenames, typically an underscore (_) or dash (-), and splits the filenames into tokens.

#### Token Grouping and Indexing

- Each token in a filename is indexed (0, 1, 2, ...).
- Filenames are grouped based on the value of tokens at each index.

#### Determining Grouping Strategy

- The system decides whether to group tokens from the left (start of filename) or right (end of filename) based on the distribution and variation of tokens at each index.

#### Pattern Creation Logic

- Single-Token Filenames: No globbing is applied to filenames with only one token.
- Multi-Token Filenames: The method constructs glob patterns by analyzing each token. It considers factors like token uniqueness, commonality, and special cases like all-letter tokens.

##### Uniqueness vs. Commonality:

- Unique tokens (unique in their position across all filenames) are replaced with a wildcard "*".
- Common tokens across many files are kept as they are in the pattern.

##### Special Considerations for All-Letter Tokens:

- Tokens comprising entirely of letters are often grouped together, unless they are unique identifiers.
- Tokens at the start or end of a filename are treated with contextual logic, considering their potential roles (like identifiers or file types).

##### Adjacent Token Group Sizes:

The method compares the group sizes of adjacent tokens to determine if a token leads to a tighter grouping, influencing whether it's kept as literal or replaced with a wildcard.

#### Constructing Container Names (Glob Patterns)

- For each token index, the method constructs a container name, deciding whether to include the token as-is or replace it with "*".

- This decision is influenced by factors like the uniqueness of the token, the nature of the token (all letters or not), and the comparison of token counts in adjacent indexes.

#### Optimization and Finalization

- The system optimizes the glob patterns to ensure each pattern uniquely represents a group of files with a shared schema.
- It compares new patterns with existing ones and updates them based on the latest file modifications.


### Example Scenarios
- Filename: `"project_data_2023_v1.csv"`
    - Potential Pattern: `"project_data_*_*.csv"` (if "2023" and "v1" vary across files).
- Filename: `"user_123_profile_2023-06-01.json"`
    - Potential Pattern: `"user_*_profile_*.json"` (if "123" and dates vary, and "user" and "profile" are consistent).
- Filename: `"log2023-06_error.txt"`
    - Potential Pattern: `"*_error.txt"` (if dates vary but "error" is a constant token).

## Limitations

### Context

While the Multi-Token Filename Globbing feature is a powerful tool for organizing files in distributed filesystems, including object storage systems like AWS S3, Google Cloud Storage (GCS), and Azure Blob Storage, it's important to understand the limitations of using glob patterns with wildcards in these environments.

### Wildcard Mechanics in Directory Listings

#### Wildcard Character (*): 

In glob patterns, the asterisk (*) is used as a wildcard that matches any character, any number of times. This flexibility is powerful for grouping a wide range of file patterns but has limitations in precision.

#### Behavior in Object Storage Systems:

- Systems like AWS S3, GCS, and Azure Blob interpret the wildcard in a glob pattern to match any sequence of characters in a filename.
- This means a pattern with a wildcard can encompass a broad range of filenames, potentially grouping files that were not intended to be grouped together.

### Specific Limitation Example
Consider the following scenario to illustrate this limitation:

#### Intended File Grouping Patterns:
- Pattern A: `project_data_*.txt`
- Pattern B: `project_data_*_*.txt`
#### Example Filenames:
- `project_data_1234.txt`
- `project_data_1234_suffix.txt`

#### Limitation in Practice:

- In this case, Pattern A (`project_data_*.txt`) is intended to match files like project_data_1234.txt. However, due to the nature of the wildcard, this pattern will also inadvertently match `project_data_1234_suffix.txt`.

- The wildcard in Pattern A extends to any length of characters following project_data_, making it impossible to exclusively group files that strictly follow the `project_data_1234.txt` format without including those with additional suffixes like `project_data_1234_suffix.txt`.

### Addressing the Limitations: 

Understanding the inherent limitations of glob patterns, particularly when dealing with wildcards in object storage systems, is crucial for effective file management. 

When users encounter scenarios where filenames within a folder are incompatible due to these limitations, several practical options are available.

#### Ensure appropriate file grouping:

##### Separation into Distinct Folders: 

One effective strategy is to organize files with conflicting name formats into separate folders. 

By doing so, the resultant glob patterns within each folder will be distinct and won’t overlap, ensuring precise file grouping.

##### Leveraging Folder-Globbing Feature: 

For added flexibility, users can also utilize our folder-globbing feature. 

This feature simplifies the grouping process by aggregating all files in the same folder, regardless of their filename patterns. This approach is particularly useful in scenarios where filename-based grouping is less critical or when dealing with a wide variety of filename formats within the same directory.

##### Customized Filename Conventions: 

Users are encouraged to adopt filename conventions that align better with the capabilities and limitations of glob patterns. By designing filenames with clear, distinct segments and predictable structures, users can more effectively leverage the globbing feature for accurate file categorization.

## Conclusion

The Multi-Token Filename Globbing feature stands out as a powerful and efficient tool for organizing and categorizing files within a distributed filesystem. 

By astutely analyzing filename patterns and forming optimized glob patterns, this feature significantly streamlines the process of managing files that share common schemas, thereby elevating the overall data quality and accessibility within the system.



