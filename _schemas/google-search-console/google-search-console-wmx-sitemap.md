---
description: Information about a sitemap submitted to Search Console. Includes processing status, error counts, and content details.
layout: schema
name: WmxSitemap
properties_list:
- description: The URL of the sitemap.
  name: path
  type: string
- description: Date and time when the sitemap was last submitted to Search Console.
  name: lastSubmitted
  type: string
- description: Whether the sitemap is still being processed.
  name: isPending
  type: boolean
- description: Whether this is a sitemap index file.
  name: isSitemapsIndex
  type: boolean
- description: The type of content in the sitemap.
  name: type
  type: string
- description: Date and time when the sitemap was last downloaded by Google.
  name: lastDownloaded
  type: string
- description: Number of warnings for the sitemap.
  name: warnings
  type: integer
- description: Number of errors for the sitemap.
  name: errors
  type: integer
- description: Content details for this sitemap, broken down by content type.
  name: contents
  type: array
provider_name: Google Search Console
provider_slug: google-search-console
schema_file: json-schema/google-search-console-wmx-sitemap-schema.json
slug: google-search-console-wmx-sitemap
tags:
- Analytics
- Google
- Search
- SEO
- Webmaster Tools
title: WmxSitemap
---
