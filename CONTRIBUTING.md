---
layout: default
title: Contributing to the archive
search_exclude: true
---

# Contributing to the archive

## Where to make changes

- `_talks/<Month><Year>/<slug>.md`: the title, speaker, tags, description, links and embedded media for one talk, workshop or game session. Use this folder for every year, including older meetings.
- `slides/<Month><Year>/`: uploaded presentation files and other materials. Link to them using `/slides/...`, not `../slides/...`, so links work on both the talk and month pages.
- `pages/<Month><Year>.md`: month settings and meeting-wide notes, such as a cancellation or anniversary. Do not copy talk descriptions here. The month layout includes them automatically.
- `pages/search.md`, `pages/speakers.md`, `pages/tags.md`: site navigation, not talk content.

To correct a talk, find its file in `_talks/` and edit that file only. Its month page, search entry and speaker/tag listings update when the site is built. Keep the filename unchanged when correcting a title so existing links continue to work.

## Add a talk

The easiest option is the **Add a talk recap** form under this repository's Issues tab. It opens a pull request automatically. For a manual pull request, add a file such as `_talks/November2026/example-talk.md`:

```yaml
---
date: 2026-11-06
month_key: "November2026"
month_name: "November 2026"
speaker: "Speaker name"
speaker_url: "https://example.com/"
title: "Example talk"
tags: [web-security, workshop]
links:
  - label: "Slides"
    url: "/slides/November2026/example-talk.pdf"
---
The full talk description goes here. Markdown and embedded media are supported.
```

`date`, `month_key`, `month_name`, `speaker` and `title` are required. The date is the meetup date. If only the month is known for a historical talk, use its first day. `speaker_url`, `tags` and `links` are optional. Reuse existing tags where possible. Quote YAML strings containing special characters. Escape double quotes inside double-quoted strings as `\"`.

Links can go in `links` or in the description. Do not put the same link in both places. Titles may contain characters such as `|`, `&` and brackets. They do not need to be renamed for the site to display them correctly.

If the month page does not exist, add `pages/November2026.md`:

```yaml
---
layout: month
month_key: "November2026"
month_name: "November 2026"
title: "November 2026"
---
```

Add the month to the README timeline with `python3 scripts/add_month_to_readme.py November 2026`. The issue-form automation handles both steps for you.

## Check changes locally

Use a current Ruby version supported by the `github-pages` gem, for example Ruby 3.3, and Bundler:

```sh
bundle install
bundle exec ruby scripts/check_archive.rb
bundle exec jekyll serve --host 127.0.0.1
```

The check builds the site in a temporary directory and verifies the archive structure, rendered talk links, search index and local materials. The preview is available at http://127.0.0.1:4000.