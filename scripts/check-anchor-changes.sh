#!/usr/bin/env bash
# Pre-commit hook: detects heading/anchor changes in modified markdown files.
# Generates .anchor-changes.md report (gitignored).

python3 scripts/check-anchor-changes.py
