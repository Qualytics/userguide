"""Pre-commit hook: scans markdown files for image references and checks
that the referenced files exist on disk.

Handles:
  - Markdown images:  ![alt](path/to/image.png)
  - Fragments:        ![alt](path/to/image.png#only-light)
  - Attribute lists:  ![alt](path/to/image.png){: style="..."}
  - Relative paths:   ../assets/foo.png, ../../assets/bar.png
  - Absolute paths:   /assets/foo.png (resolved from docs/)
"""

import os
import re
import sys
from pathlib import Path

DOCS_DIR = Path("docs")

# Match ![alt text](image_path) — captures the path inside parentheses
IMAGE_PATTERN = re.compile(r"!\[[^\]]*\]\(([^)]+)\)")


def check_images():
    errors = []

    for md_file in sorted(DOCS_DIR.rglob("*.md")):
        content = md_file.read_text(encoding="utf-8", errors="replace")

        for match in IMAGE_PATTERN.finditer(content):
            raw_path = match.group(1).strip()

            # Skip external URLs and data URIs
            if re.match(r"^(https?://|data:)", raw_path):
                continue

            # Strip fragment (#only-light, #only-dark, etc.)
            img_path = raw_path.split("#")[0]

            # Strip attribute list suffix ({: ...})
            img_path = img_path.split("{")[0].strip()

            # Skip empty paths
            if not img_path:
                continue

            # Resolve the path
            if img_path.startswith("/"):
                resolved = DOCS_DIR / img_path.lstrip("/")
            else:
                resolved = md_file.parent / img_path

            # Normalize (resolve ../ segments)
            resolved = resolved.resolve()

            if not resolved.is_file():
                line_num = content[: match.start()].count("\n") + 1
                errors.append(
                    (str(md_file), line_num, img_path, str(resolved))
                )

    # Output
    print()
    print("=== Broken Image Check ===")

    if errors:
        print()
        for md_file, line_num, img_path, resolved in errors:
            print(f"  [broken] {md_file}:{line_num} -> {img_path}")
            print(f"           expected at: {resolved}")
        print()
        print(f"Found {len(errors)} broken image reference(s)")
        print("===========================")
        print()
        return 1
    else:
        print("All image references are valid")
        print("===========================")
        print()
        return 0


if __name__ == "__main__":
    sys.exit(check_images())
