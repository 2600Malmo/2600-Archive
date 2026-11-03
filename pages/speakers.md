---
layout: default
title: Browse by speaker
permalink: /pages/speakers
search_exclude: true
---

## Browse talks by speaker

{% assign grouped = site.talks | group_by: "speaker" | sort: "name" %}
{% if grouped.size == 0 %}
No talks recorded yet.
{% else %}
{% for group in grouped %}
### {{ group.name }}

{% assign sorted_items = group.items | sort: "date" | reverse %}
<ul>
{% for talk in sorted_items %}
<li><a href="{{ talk.url | relative_url | escape }}">{{ talk.title | escape }}</a> &mdash; {{ talk.month_name | escape }}</li>
{% endfor %}
</ul>

{% endfor %}
{% endif %}

[back](/)
