---
layout: default
title: Browse by tag
permalink: /pages/tags
search_exclude: true
---

## Browse talks by tag

{% assign all_tags = "" | split: "," %}
{% for talk in site.talks %}
{% assign all_tags = all_tags | concat: talk.tags %}
{% endfor %}
{% assign unique_tags = all_tags | uniq | sort %}

{% if unique_tags.size == 0 %}
No tagged talks yet.
{% else %}
{% for tag in unique_tags %}
### <a id="{{ tag }}"></a>#{{ tag }}

{% assign tagged = site.talks | where_exp: "t", "t.tags contains tag" | sort: "date" | reverse %}
{% for talk in tagged %}
- [{{ talk.title }}]({{ talk.url | relative_url }}) &mdash; {{ talk.month_name }}
{% endfor %}

{% endfor %}
{% endif %}

[back](/)
