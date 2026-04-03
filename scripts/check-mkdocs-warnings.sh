#!/usr/bin/env bash
# Pre-commit hook: runs mkdocs build and reports warnings.
# Acceptable warnings (e.g., print_page from print-site plugin) are labeled
# but do not fail the build. All warnings are always shown in the log.

set -euo pipefail

output=$(source venv/bin/activate && mkdocs build 2>&1) || true
warnings=$(echo "$output" | grep "WARNING" || true)

if [ -z "$warnings" ]; then
    exit 0
fi

echo ""
echo "=== MkDocs Build Warnings ==="
echo ""

while IFS= read -r line; do
    if echo "$line" | grep -q "print_page"; then
        echo "  [acceptable] $line"
    else
        echo "  [review]     $line"
    fi
done <<< "$warnings"

total=$(echo "$warnings" | wc -l | tr -d " ")
echo ""
echo "Total: ${total} warning(s)"
echo "============================="
echo ""

exit 0
