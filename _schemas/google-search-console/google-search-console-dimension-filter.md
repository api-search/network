---
description: A filter on a specific dimension.
layout: schema
name: DimensionFilter
properties_list:
- description: The dimension to filter on.
  name: dimension
  type: string
- description: How to filter. The contains operator performs a case-insensitive substring match. The equals operator performs a case-sensitive exact match. The notContains and notEquals operators are the negations o
  name: operator
  type: string
- description: The value to filter on. For country, use the 3-letter country code (ISO 3166-1 alpha-3). For device, use DESKTOP, MOBILE, or TABLET.
  name: expression
  type: string
provider_name: Google Search Console
provider_slug: google-search-console
schema_file: json-schema/google-search-console-dimension-filter-schema.json
slug: google-search-console-dimension-filter
tags:
- Analytics
- Google
- Search
- SEO
- Webmaster Tools
title: DimensionFilter
---
