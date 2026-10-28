#!/usr/bin/env python3
"""Insert a link to a new month's recap page into README.md's timeline.

Used by .github/workflows/new-month-stub.yml to keep the README in sync
whenever the bot creates a new pages/<Month><Year>.md stub. Safe to run
more than once: it is a no-op if the link is already present.
"""
import re
import sys
from pathlib import Path


def main():
    if len(sys.argv) != 3:
        print("Usage: add_month_to_readme.py <Month> <Year>", file=sys.stderr)
        sys.exit(1)

    month, year = sys.argv[1], sys.argv[2]
    readme = Path(__file__).resolve().parent.parent / "README.md"
    text = readme.read_text()

    link_line = f"- [{month}](pages/{month}{year})"
    if link_line in text:
        print("Link already present, skipping.")
        return

    year_heading = f"### {year}"

    if year_heading in text:
        # Insert as the first bullet right after the year heading's own line.
        pattern = re.compile(rf"^{re.escape(year_heading)}[^\n]*\n", re.MULTILINE)
        m = pattern.search(text)
        insert_at = m.end()
        text = text[:insert_at] + link_line + "\n" + text[insert_at:]
    else:
        # New year: insert a whole new section right before the first
        # existing "### " year heading under "## Previous meetings".
        marker = "## Previous meetings"
        idx = text.index(marker)
        next_heading = re.search(r"^### ", text[idx:], re.MULTILINE)
        insert_at = idx + next_heading.start() if next_heading else len(text)
        new_section = f"{year_heading}  \n{link_line}\n\n"
        text = text[:insert_at] + new_section + text[insert_at:]

    readme.write_text(text)
    print(f"Added {link_line} under {year_heading}")


if __name__ == "__main__":
    main()
