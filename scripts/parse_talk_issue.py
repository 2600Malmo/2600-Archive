#!/usr/bin/env python3
"""Parse an "Add a talk recap" issue form body into a _talks/*.md entry.

Reads the issue body from stdin and writes:
  - _talks/<Month><Year>/<slug>.md
  - pages/<Month><Year>.md (only if it doesn't exist yet)

Then prints `key=value` lines on stdout meant to be appended to
$GITHUB_OUTPUT by the calling workflow step.
"""
import re
import sys
from pathlib import Path

MONTHS = [
    "January", "February", "March", "April", "May", "June",
    "July", "August", "September", "October", "November", "December",
]

REPO_ROOT = Path(__file__).resolve().parent.parent


def parse_sections(body):
    """Split a GitHub issue-form body into {heading: answer} pairs."""
    parts = re.split(r"^### (.+)$", body, flags=re.MULTILINE)
    sections = {}
    it = iter(parts[1:])
    for heading, content in zip(it, it):
        sections[heading.strip()] = content.strip()
    return sections


def slugify(text):
    slug = re.sub(r"[^a-z0-9]+", "-", text.lower()).strip("-")
    return slug or "talk"


def get(sections, label):
    value = sections.get(label, "").strip()
    return "" if value.lower() == "_no response_" else value


def fail(message):
    print(f"::error::{message}", file=sys.stderr)
    sys.exit(1)


def main():
    body = sys.stdin.read()
    sections = parse_sections(body)

    month_label = get(sections, "Month of the meetup")
    title = get(sections, "Talk title")
    speaker = get(sections, "Speaker name")
    speaker_url = get(sections, "Speaker link (optional)")
    tags_raw = get(sections, "Tags (optional, comma separated)")
    description = get(sections, "Short description")
    slides_url = get(sections, "Slides link (optional)")

    if not title or not speaker or not description:
        fail("Missing required field(s): title, speaker, and description are required.")

    m = re.match(r"^([A-Za-z]+)\s+(\d{4})$", month_label)
    if not m or m.group(1) not in MONTHS:
        fail(f"Could not parse month '{month_label}'. Expected e.g. 'October 2026'.")
    month, year = m.group(1), m.group(2)
    month_key = f"{month}{year}"
    month_name = f"{month} {year}"

    slug = slugify(title)
    talk_dir = REPO_ROOT / "_talks" / month_key
    talk_dir.mkdir(parents=True, exist_ok=True)
    talk_path = talk_dir / f"{slug}.md"

    front = [
        "---",
        f"date: {year}-{MONTHS.index(month) + 1:02d}-01",
        f'month_key: "{month_key}"',
        f'month_name: "{month_name}"',
        f'speaker: "{speaker}"',
    ]
    if speaker_url:
        front.append(f'speaker_url: "{speaker_url}"')
    front.append(f'title: "{title}"')
    if tags_raw:
        tags = [t.strip() for t in tags_raw.split(",") if t.strip()]
        front.append("tags: [" + ", ".join(tags) + "]")
    if slides_url:
        front += ["links:", '  - label: "Slides"', f'    url: "{slides_url}"']
    front.append("---")

    talk_path.write_text("\n".join(front) + "\n" + description + "\n")

    month_page = REPO_ROOT / "pages" / f"{month_key}.md"
    new_month_page = not month_page.exists()
    if new_month_page:
        month_page.write_text(
            "---\n"
            "layout: month\n"
            f'month_key: "{month_key}"\n'
            f'month_name: "{month_name}"\n'
            f'title: "{month_name}"\n'
            "---\n"
        )

    print(f"talk_path={talk_path.relative_to(REPO_ROOT)}")
    print(f"month_key={month_key}")
    print(f"month_name={month_name}")
    print(f"month={month}")
    print(f"year={year}")
    print(f"title={title}")
    print(f"new_month_page={'true' if new_month_page else 'false'}")


if __name__ == "__main__":
    main()
