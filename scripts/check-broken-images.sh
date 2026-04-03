#!/usr/bin/env bash
# Pre-commit hook: scans markdown files for image references and checks
# that the referenced files exist on disk.
#
# Handles:
#   - Markdown images:  ![alt](path/to/image.png)
#   - Fragments:        ![alt](path/to/image.png#only-light)
#   - Attribute lists:  ![alt](path/to/image.png){: style="..."}
#   - Relative paths:   ../assets/foo.png, ../../assets/bar.png
#   - Absolute paths:   /assets/foo.png (resolved from docs/)

python3 scripts/check-broken-images.py
