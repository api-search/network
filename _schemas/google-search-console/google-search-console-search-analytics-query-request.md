---
description: Request body for querying search analytics data. Defines the date range, dimensions, filters, and aggregation type for the query.
layout: schema
name: SearchAnalyticsQueryRequest
properties_list:
- description: Start date of the requested date range, in YYYY-MM-DD format. Must be less than or equal to the end date. Data is available starting from the date the site was added to Search Console.
  name: startDate
  type: string
- description: End date of the requested date range, in YYYY-MM-DD format. Must be greater than or equal to the start date. There is a processing delay of approximately 2-3 days.
  name: endDate
  type: string
- description: Zero or more dimensions to group results by. Results are grouped in the order that dimensions are specified. Valid dimensions are date, query, page, country, device, and searchAppearance.
  name: dimensions
  type: array
- description: Filter results to the specified search type. Defaults to web.
  name: type
  type: string
- description: Zero or more groups of dimension filters. All filter groups are ANDed together. Within a group, filters are combined using the group type (AND by default).
  name: dimensionFilterGroups
  type: array
- description: How data is aggregated. If auto, data is aggregated by property type. If byPage, all data is aggregated by page. If byProperty, all data is aggregated by property.
  name: aggregationType
  type: string
- description: Maximum number of rows to return. Valid range is 1 to 25000. Default is 1000.
  name: rowLimit
  type: integer
- description: Zero-based index of the first row in the response. Must be a non-negative number. Default is 0.
  name: startRow
  type: integer
- description: The data state to filter on. If set to final, only finalized data is returned. If set to all, both finalized and fresh data are included.
  name: dataState
  type: string
provider_name: Google Search Console
provider_slug: google-search-console
schema_file: json-schema/google-search-console-search-analytics-query-request-schema.json
slug: google-search-console-search-analytics-query-request
tags:
- Analytics
- Google
- Search
- SEO
- Webmaster Tools
title: SearchAnalyticsQueryRequest
---
