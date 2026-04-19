---
description: Paginated search results for series queries.
layout: schema
name: SearchResults
properties_list:
- description: Total number of matching series across all pages.
  name: totalCount
  type: integer
- description: The current pagination offset.
  name: offset
  type: integer
- description: The maximum results per page.
  name: limit
  type: integer
- description: Array of matching series metadata.
  name: results
  type: array
provider_name: Moody's
provider_slug: moodys
schema_file: json-schema/moodys-data-buffet-search-results-schema.json
slug: moodys-data-buffet-search-results
tags:
- Climate Risk
- Compliance
- Credit Risk
- Economic Data
- Entity Verification
- Financial Analytics
- Insurance
- KYC
- Risk
- Screening
title: SearchResults
---
