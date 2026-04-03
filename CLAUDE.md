# CLAUDE.md

This file provides guidance to Claude Code (claude.ai/code) when working with code in this repository.

## Project Overview

This is the Qualytics User Guide documentation repository, built with [Material for MkDocs](https://squidfunk.github.io/mkdocs-material/). It documents the Qualytics data quality platform.

## Common Commands

```bash
# Activate virtual environment first
source venv/bin/activate

# Serve documentation locally (default: http://localhost:8000)
mkdocs serve

# Serve on custom port
mkdocs serve -a localhost:8080

# Build static site
mkdocs build

# Run spell check
pre-commit run --all-files
```

## Setup (if venv doesn't exist)

```bash
python3 -m venv venv
source venv/bin/activate
pip install -r requirements.txt
pre-commit install
```

## Repository Structure

- `docs/` - All documentation markdown files
- `mkdocs.yml` - Site configuration, navigation tree, and plugins
- `docs/components/` - Reusable markdown snippets (anomaly-support, comparators, general-props)
- `overrides/` - MkDocs theme customizations
- `docs/assets/` - Images and static files
- `contributing/check-content-template-guide.md` - Template for writing quality check rule documentation

## Documentation Conventions

### Reusable Components

Quality check documentation uses include-markdown to pull in shared content:

```markdown
{%
    include-markdown "components/general-props/index.md"
    start='<!-- all-props--start -->'
    end='<!-- all-props--end -->'
%}
```

Available component arguments:
- General props: `all-props`, `filter-only`, `coverage-only`, `none-props`
- Anomaly support: `all-types`, `record-only`, `shape-only`

### Quality Check Documentation Structure

When documenting a quality check rule, follow `contributing/check-content-template-guide.md`:
1. Definition
2. In-Depth Overview (optional)
3. Field Scope (Single/Multiple/Calculated) with Accepted Types table
4. General Properties (via include-markdown)
5. Specific Properties
6. Anomaly Types (via include-markdown)
7. Example with: Objective, Sample Data table, Anomaly Explanation, Flowchart (mermaid), SQL query, Potential Violation Messages

### Spell Checking

The repository uses `typos` via pre-commit for spell checking. Custom word allowances are in `.typos.toml`. Files in `docs/assets/`, `venv/`, and dotfiles are excluded.

## Pre-Commit Hooks

The repository uses two pre-commit hooks (configured in `.pre-commit-config.yaml`):

1. **typos** - Spell checking across all docs (custom words in `.typos.toml`)
2. **mkdocs-warnings** - Runs `mkdocs build` and surfaces any `WARNING` lines (broken links, missing nav entries, etc.)

Run all hooks manually:

```bash
pre-commit run --all-files
```

### MkDocs Validation

The `mkdocs.yml` has a `validation` section that controls which link/reference issues produce warnings during build. The current pre-commit hook runs `mkdocs build` in non-strict mode and reports warnings without failing the build — this is intentional to avoid blocking commits on acceptable warnings.

If stricter validation is needed in the future:

- **Granular control:** Expand the `validation` section in `mkdocs.yml` to enable/disable specific checks (anchors, absolute links, unrecognized links, omitted nav files)
- **Strict mode:** Change the hook to use `mkdocs build --strict` to turn all warnings into errors (only do this after resolving or filtering out all existing warnings)
- **Filtered strict mode:** Keep non-strict but update the hook's grep to exclude known acceptable warning patterns and fail on the rest

```yaml
# Example: expanded validation config in mkdocs.yml
validation:
  nav:
    omitted_files: info
    absolute_links: warn
  links:
    anchors: warn
    absolute_links: warn
    unrecognized_links: warn
```

### Adding New Pre-Commit Checks

Additional tools that can be added to `.pre-commit-config.yaml` for catching more issues:

- **markdownlint-cli2** - Catches malformed tables, inconsistent list formatting, missing blank lines around fences
- **lychee** - Validates all links including images, anchors, and external URLs
