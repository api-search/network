---
description: A single row of search analytics data. Contains dimension keys and their associated metric values.
layout: schema
name: SearchAnalyticsRow
properties_list:
- description: A list of dimension values for this row, in the same order as the dimensions specified in the request. For country, the value is a 3-letter country code. For device, the value is DESKTOP, MOBILE, or T
  name: keys
  type: array
- description: The number of clicks from Google Search results that landed on the property.
  name: clicks
  type: number
- description: The number of times a link to the property appeared in search results and was seen by a user (not necessarily scrolled into view).
  name: impressions
  type: number
- description: 'Click-through rate: the ratio of clicks to impressions, expressed as a decimal between 0 and 1.'
  name: ctr
  type: number
- description: The average position of the property in search results, where 1 is the topmost position. The value is averaged across all queries and pages.
  name: position
  type: number
provider_name: Google Search Console
provider_slug: google-search-console
schema_file: json-schema/google-search-console-search-analytics-row-schema.json
slug: google-search-console-search-analytics-row
tags:
- Analytics
- Google
- Search
- SEO
- Webmaster Tools
title: SearchAnalyticsRow
---
