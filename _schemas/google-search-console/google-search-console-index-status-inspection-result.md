---
description: Index status inspection results for a URL.
layout: schema
name: IndexStatusInspectionResult
properties_list:
- description: The overall verdict for the index status of the URL.
  name: verdict
  type: string
- description: The coverage state of the URL, indicating whether and how it appears in the index. Common values include Submitted and indexed, Crawled - currently not indexed, Discovered - currently not indexed, and
  name: coverageState
  type: string
- description: Whether the page is blocked by robots.txt.
  name: robotsTxtState
  type: string
- description: Whether the page is blocked from indexing via noindex directives.
  name: indexingState
  type: string
- description: The last time this URL was crawled by Google, in RFC 3339 format.
  name: lastCrawlTime
  type: string
- description: The result of the page fetch during the last crawl.
  name: pageFetchState
  type: string
- description: The URL that Google selected as canonical for this page.
  name: googleCanonical
  type: string
- description: The canonical URL declared by the page via rel=canonical or the Canonical HTTP header.
  name: userCanonical
  type: string
- description: Any sitemaps that include this URL.
  name: sitemap
  type: array
- description: URLs that refer to this URL, as discovered during crawling.
  name: referringUrls
  type: array
- description: The user agent type used to crawl the URL.
  name: crawledAs
  type: string
provider_name: Google Search Console
provider_slug: google-search-console
schema_file: json-schema/google-search-console-index-status-inspection-result-schema.json
slug: google-search-console-index-status-inspection-result
tags:
- Analytics
- Google
- Search
- SEO
- Webmaster Tools
title: IndexStatusInspectionResult
---
