---
layout: default
title: Browse by tag
permalink: /pages/tags
search_exclude: true
---

## Browse talks by tag

{% assign all_talks = site.talks %}
{% assign all_tags = "" | split: "," %}
{% for talk in all_talks %}
{% assign all_tags = all_tags | concat: talk.tags %}
{% endfor %}
{% assign unique_tags = all_tags | uniq | sort %}

{% if unique_tags.size == 0 %}
No tagged talks yet.
{% else %}
{% for tag in unique_tags %}
### <a id="{{ tag }}"></a>#{{ tag }}

{% assign tagged = all_talks | where_exp: "t", "t.tags contains tag" | sort: "date" | reverse %}
<ul>
{% for talk in tagged %}
<li><a href="{{ talk.url | relative_url | escape }}">{{ talk.title | escape }}</a> &mdash; {{ talk.month_name | escape }}</li>
{% endfor %}
</ul>

{% endfor %}
{% endif %}

[back](/)
