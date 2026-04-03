"""Pre-commit hook: detects URL and anchor changes compared to the main branch.

Compares the current state of all modified markdown files against the main
branch to detect:
  - File renames/moves (full URL path changes)
  - File deletions (URL removed entirely)
  - Heading renames (anchor slug changes)
  - Heading deletions (anchor removed)

Generates a report (.anchor-changes.md) so that internal references and
external links (SEO) can be updated before merging.

The report is gitignored and regenerated on each commit attempt.
"""

import re
import subprocess
import sys
from pathlib import Path

DOCS_DIR = Path("docs")
REPORT_FILE = Path(".anchor-changes.md")
BASE_BRANCH = "main"
SITE_URL = "https://userguide.qualytics.io"
LOCAL_URL = "http://localhost:8000"


def slugify(text: str) -> str:
    """Convert a heading to an MkDocs-style anchor slug."""
    text = re.sub(r"\*\*([^*]+)\*\*", r"\1", text)  # bold
    text = re.sub(r"\*([^*]+)\*", r"\1", text)  # italic
    text = re.sub(r"`([^`]+)`", r"\1", text)  # inline code
    text = re.sub(r"\[([^\]]+)\]\([^)]+\)", r"\1", text)  # links
    text = re.sub(r"[^\w\s-]", "", text)  # remove special chars
    text = text.strip().lower()
    text = re.sub(r"[\s]+", "-", text)  # spaces to hyphens
    return text


def extract_headings(content: str) -> list[tuple[str, str]]:
    """Extract (heading_text, anchor_slug) pairs from markdown content."""
    headings = []
    for match in re.finditer(r"^(#{1,6})\s+(.+)$", content, re.MULTILINE):
        text = match.group(2).strip()
        slug = slugify(text)
        if slug:
            headings.append((text, slug))
    return headings


def get_main_content(filepath: str) -> str | None:
    """Get the version of a file from the main branch."""
    try:
        result = subprocess.run(
            ["git", "show", f"{BASE_BRANCH}:{filepath}"],
            capture_output=True,
            text=True,
        )
        if result.returncode == 0:
            return result.stdout
    except Exception:
        pass
    return None


def file_to_url_path(filepath: str) -> str:
    """Convert docs/path/to/file.md to path/to/file/."""
    path = filepath.removeprefix("docs/")
    if path.endswith("/index.md"):
        path = path.removesuffix("index.md")
    elif path.endswith(".md"):
        path = path.removesuffix(".md") + "/"
    return path


def get_changed_files_vs_main() -> dict[str, list[str]]:
    """Get all file changes compared to main branch.

    Returns dict with keys: modified, deleted, renamed.
    Renamed entries are tuples of (old_path, new_path).
    """
    changes = {"modified": [], "deleted": [], "renamed": []}

    result = subprocess.run(
        ["git", "diff", "--name-status", "-M", f"{BASE_BRANCH}...HEAD"],
        capture_output=True,
        text=True,
    )

    if result.returncode != 0:
        # Fallback: compare working tree against main directly
        result = subprocess.run(
            ["git", "diff", "--name-status", "-M", BASE_BRANCH],
            capture_output=True,
            text=True,
        )

    if result.returncode != 0:
        return changes

    for line in result.stdout.strip().split("\n"):
        if not line:
            continue
        parts = line.split("\t")
        status = parts[0]

        if status == "D" and len(parts) >= 2:
            f = parts[1]
            if f.startswith("docs/") and f.endswith(".md"):
                changes["deleted"].append(f)
        elif status.startswith("R") and len(parts) >= 3:
            old_f, new_f = parts[1], parts[2]
            if old_f.startswith("docs/") and old_f.endswith(".md"):
                changes["renamed"].append((old_f, new_f))
        elif status in ("M", "A") and len(parts) >= 2:
            f = parts[1]
            if f.startswith("docs/") and f.endswith(".md"):
                changes["modified"].append(f)

    # Also pick up unstaged changes in working tree not yet committed
    result = subprocess.run(
        ["git", "diff", "--name-only", "--diff-filter=ACM"],
        capture_output=True,
        text=True,
    )
    if result.returncode == 0:
        for f in result.stdout.strip().split("\n"):
            if f.endswith(".md") and f.startswith("docs/") and f not in changes["modified"]:
                changes["modified"].append(f)

    return changes


def main():
    all_changes = []
    changes = get_changed_files_vs_main()

    # 1. Detect file renames/moves (URL path changes)
    for old_file, new_file in changes["renamed"]:
        old_url = file_to_url_path(old_file)
        new_url = file_to_url_path(new_file)
        if old_url != new_url:
            all_changes.append({
                "type": "URL MOVED",
                "file": new_file,
                "old_url": old_url,
                "new_url": new_url,
                "detail": f"File renamed: {old_file} -> {new_file}",
            })

    # 2. Detect deleted files (URL removed entirely)
    for deleted_file in changes["deleted"]:
        old_url = file_to_url_path(deleted_file)
        all_changes.append({
            "type": "URL DELETED",
            "file": deleted_file,
            "old_url": old_url,
            "new_url": "---",
            "detail": "File deleted",
        })

    # 3. Detect anchor changes in modified files
    for filepath in changes["modified"]:
        path = Path(filepath)
        if not path.exists():
            continue

        current_content = path.read_text(encoding="utf-8", errors="replace")
        main_content = get_main_content(filepath)

        if main_content is None:
            # New file (not in main) — no comparison needed
            continue

        current_headings = extract_headings(current_content)
        current_slugs = {slug for _, slug in current_headings}

        old_headings = extract_headings(main_content)
        old_slugs = {slug for _, slug in old_headings}

        url_path = file_to_url_path(filepath)

        removed = old_slugs - current_slugs
        added = current_slugs - old_slugs

        if not removed:
            continue

        old_text_map = {slug: text for text, slug in old_headings}
        new_text_map = {slug: text for text, slug in current_headings}

        matched_removed = set()
        matched_added = set()

        # Pair removed/added anchors that likely represent renames
        for old_slug in sorted(removed):
            old_text = old_text_map.get(old_slug, "")
            best_match = None
            best_score = 0

            for new_slug in sorted(added):
                if new_slug in matched_added:
                    continue
                new_text = new_text_map.get(new_slug, "")
                old_words = set(old_text.lower().split())
                new_words = set(new_text.lower().split())
                if not old_words or not new_words:
                    continue
                overlap = len(old_words & new_words)
                total = len(old_words | new_words)
                score = overlap / total if total > 0 else 0
                if score > best_score and score >= 0.3:
                    best_score = score
                    best_match = new_slug

            if best_match:
                all_changes.append({
                    "type": "ANCHOR RENAMED",
                    "file": filepath,
                    "old_url": f"{url_path}#{old_slug}",
                    "new_url": f"{url_path}#{best_match}",
                    "detail": f"{old_text_map.get(old_slug, '')} -> {new_text_map.get(best_match, '')}",
                })
                matched_removed.add(old_slug)
                matched_added.add(best_match)

        for old_slug in sorted(removed - matched_removed):
            all_changes.append({
                "type": "ANCHOR REMOVED",
                "file": filepath,
                "old_url": f"{url_path}#{old_slug}",
                "new_url": "---",
                "detail": old_text_map.get(old_slug, ""),
            })

    # Always generate the report
    lines = [
        "# URL and Anchor Changes Report",
        "",
        f"Compared against `{BASE_BRANCH}` branch.",
        "",
        "The following URLs or anchors were changed, moved, or removed.",
        "Review this list and update any internal references or external links (SEO).",
        "",
    ]

    if all_changes:
        lines.extend([
            "| Type | File | Main (Live) | Current Branch | Detail |",
            "|------|------|-------------|----------------|--------|",
        ])

        for change in all_changes:
            old_full = f"{SITE_URL}/{change['old_url']}"
            if change["new_url"] == "---":
                new_full = "---"
            else:
                new_full = f"{LOCAL_URL}/{change['new_url']}"
            lines.append(
                f"| {change['type']} "
                f"| `{change['file']}` "
                f"| {old_full} "
                f"| {new_full} "
                f"| {change['detail']} |"
            )
    else:
        lines.append("No URL or anchor changes detected.")

    lines.append("")
    REPORT_FILE.write_text("\n".join(lines), encoding="utf-8")

    # Console output
    print()
    print("=== URL & Anchor Change Report ===")
    if all_changes:
        print()
        for change in all_changes:
            tag = change["type"].lower()
            print(f"  [{tag}] {SITE_URL}/{change['old_url']}")
            if change["new_url"] != "---":
                print(f"       -> {LOCAL_URL}/{change['new_url']}")
        print()
        print(f"Found {len(all_changes)} change(s)")
    else:
        print("No URL or anchor changes detected")
    print(f"Report: {REPORT_FILE}")
    print("==================================")
    print()

    return 0


if __name__ == "__main__":
    sys.exit(main())
