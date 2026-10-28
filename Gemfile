source "https://rubygems.org"

# Latest Jekyll instead of the `github-pages` gem, which still pins Jekyll to
# 3.10.0 and a fixed plugin whitelist. Building through our own
# .github/workflows/pages.yml (not the GitHub-managed build) lets us use any
# Jekyll version and plugin. The plugins below replace the ones the
# `github-pages` gem used to pull in for free and that this site relies on:
# jekyll-seo-tag (the theme's `{% seo %}` tag), jekyll-readme-index (serves
# README.md as the homepage) and jekyll-github-metadata (`site.github.*`
# used by the theme header).
gem "jekyll", "~> 4.4"
gem "jekyll-remote-theme", "~> 0.6"
gem "jekyll-seo-tag", "~> 2.8"
gem "jekyll-readme-index", "~> 0.3"
gem "jekyll-github-metadata", "~> 2.16"
gem "jekyll-feed", "~> 0.18"
gem "jekyll-sitemap", "~> 1.4"
gem "kramdown-parser-gfm", "~> 1.1"