---
layout: default
title: Browse by speaker
permalink: /pages/speakers
search_exclude: true
---

## Browse talks by speaker

{% assign grouped = site.talks | concat: site.legacy_talks | group_by: "speaker" | sort: "name" %}
{% if grouped.size == 0 %}
No talks recorded yet.
{% else %}
{% for group in grouped %}
### {{ group.name }}

{% assign sorted_items = group.items | sort: "date" | reverse %}
{% for talk in sorted_items %}
- [{{ talk.title }}]({{ talk.page_url | default: talk.url | relative_url }}) &mdash; {{ talk.month_name }}
{% endfor %}

{% endfor %}
{% endif %}

[back](/)
