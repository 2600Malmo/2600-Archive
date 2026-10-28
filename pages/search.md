---
layout: default
title: Search
permalink: /pages/search
search_exclude: true
---

## Search all talks

Search across every talk ever given at 2600 Malmö - by speaker, topic, or tag - without having to remember which month it happened in.

<input type="text" id="search-input" placeholder="e.g. OSINT, lockpicking, Sergei…" autocomplete="off" style="width: 100%; max-width: 480px; padding: 0.5em;">
<ul id="search-results"></ul>
<p id="search-status"></p>

<script src="https://cdn.jsdelivr.net/npm/lunr@2.3.9/lunr.min.js"></script>
<script src="{{ '/assets/js/search.js' | relative_url }}"></script>

[back](/)
