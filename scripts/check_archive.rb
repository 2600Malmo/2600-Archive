require "jekyll"
require "json"
require "nokogiri"
require "tmpdir"
require "uri"

Jekyll::PluginManager.require_from_bundler

def check(condition, message)
  raise message unless condition
end

root = File.expand_path("..", __dir__)
check(!Dir.exist?(File.join(root, "_legacy_talks")), "Use _talks for all years")

Dir.mktmpdir("2600-archive-check-") do |destination|
  config = Jekyll.configuration(
    "source" => root,
    "destination" => destination,
    "quiet" => true,
    "strict_front_matter" => true,
    "incremental" => false
  )
  site = Jekyll::Site.new(config)
  site.process
  guide = site.pages.find { |page| page.path == "CONTRIBUTING.md" }
  check(guide && guide.data["layout"] == "default", "Contribution guide must be a themed Jekyll page")
  guide_html = Nokogiri::HTML(File.read(guide.destination(destination)))
  check(guide_html.at_css("#main_content h1"), "Contribution guide is missing its themed content")
  check(!File.exist?(File.join(destination, "CONTRIBUTING.md")), "Raw contribution guide must not be published")
  homepage = Nokogiri::HTML(File.read(File.join(destination, "index.html")))
  guide_link = homepage.css("a").find { |anchor| anchor.text == "contribution guide" }
  check(guide_link && guide_link["href"] == guide.url, "Homepage must link to the rendered contribution guide")

  talks = site.collections.fetch("talks").docs
  months = site.pages.select { |page| File.basename(page.path).match?(/\A[A-Z][a-z]+20\d\d\.md\z/) }
  check(!talks.empty?, "No talks found")
  months.each do |page|
    check(page.data["layout"] == "month", "#{page.path}: use layout: month")
    check(page.data["month_key"] == File.basename(page.path, ".md"), "#{page.path}: incorrect month_key")
    html = Nokogiri::HTML(File.read(page.destination(destination)))
    month_talks = talks.select { |talk| talk.data["month_key"] == page.data["month_key"] }
    month_talks.each do |talk|
      link = html.css("h3 a").find { |anchor| anchor["href"] == talk.url }
      check(link && link.text == talk.data["title"], "#{page.path}: missing or malformed talk link for #{talk.path}")
    end
    if month_talks.empty?
      expected = page.content.strip.empty?
      check(html.text.include?("We are brewing something cool! Stay tuned") == expected, "#{page.path}: incorrect empty-month message")
    end
  end

  index = JSON.parse(File.read(File.join(destination, "search.json")))
  urls = index.map { |entry| entry.fetch("url") }
  check(urls.uniq == urls, "Duplicate URLs in the search index")
  check(index.all? { |entry| !entry.fetch("content").strip.empty? }, "Empty entries in the search index")
  listings = %w[tags speakers].to_h do |name|
    page = site.pages.find { |item| item.data["permalink"] == "/pages/#{name}" }
    [name, Nokogiri::HTML(File.read(page.destination(destination)))]
  end

  talks.each do |talk|
    %w[date month_key month_name speaker title].each do |field|
      check(!talk.data[field].to_s.strip.empty?, "#{talk.path}: missing #{field}")
    end
    check(!talk.data.key?("page_url") && !talk.data.key?("output"), "#{talk.path}: obsolete legacy fields")
    check(months.any? { |page| page.data["month_key"] == talk.data["month_key"] }, "#{talk.path}: month page missing")
    check(urls.include?(talk.url), "#{talk.path}: missing search entry")
    entry = index.find { |item| item["url"] == talk.url }
    check(entry["title"] == talk.data["title"], "#{talk.path}: incorrect search title")
    check(File.file?(talk.destination(destination)), "#{talk.path}: talk page missing")
    html = Nokogiri::HTML(File.read(talk.destination(destination)))
    check(html.css("h2").any? { |heading| heading.text == talk.data["title"] }, "#{talk.path}: incorrect rendered title")
    listings.each do |name, listing|
      next if name == "tags" && Array(talk.data["tags"]).empty?
      links = listing.css("li a").select { |anchor| anchor["href"] == talk.url }
      check(!links.empty? && links.all? { |anchor| anchor.text == talk.data["title"] }, "#{name}: malformed title or link for #{talk.path}")
    end
  end

  outputs = talks + months
  outputs.each do |page|
    html = Nokogiri::HTML(File.read(page.destination(destination)))
    html.css("[href], [src]").each do |element|
      url = element["href"] || element["src"]
      next unless url&.include?("slides/")
      check(!url.start_with?("../slides/"), "#{page.path}: use /slides/ links")
      next unless url.start_with?("/slides/")
      path = URI::DEFAULT_PARSER.unescape(url.split(/[?#]/, 2).first.delete_prefix("/"))
      check(File.file?(File.join(destination, path)), "#{page.path}: missing material #{url}")
    end
  end

  puts "Archive checks passed: #{talks.size} talks, #{months.size} months, #{index.size} search entries"
end