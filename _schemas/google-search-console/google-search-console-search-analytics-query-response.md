---
description: Response for a search analytics query.
layout: schema
name: SearchAnalyticsQueryResponse
properties_list:
- description: A list of rows grouped by the requested dimensions. Rows are ordered by click count descending. If no data is available for the specified date range and filters, this field is omitted.
  name: rows
  type: array
- description: How the results were aggregated.
  name: responseAggregationType
  type: string
provider_name: Google Search Console
provider_slug: google-search-console
schema_file: json-schema/google-search-console-search-analytics-query-response-schema.json
slug: google-search-console-search-analytics-query-response
tags:
- Analytics
- Google
- Search
- SEO
- Webmaster Tools
title: SearchAnalyticsQueryResponse
---
