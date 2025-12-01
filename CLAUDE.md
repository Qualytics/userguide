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
