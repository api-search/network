---
description: Request body for generating a custom performance report.
layout: schema
name: Report Request
properties_list:
- description: List of campaign IDs to include in the report. Empty returns all.
  name: campaignIds
  type: array
- description: Start date for the report period (ISO 8601).
  name: startDate
  type: string
- description: End date for the report period (ISO 8601).
  name: endDate
  type: string
- description: Dimensions to group report data by.
  name: dimensions
  type: array
- description: Metrics to include in the report.
  name: metrics
  type: array
- description: Output format for the report.
  name: format
  type: string
provider_name: albertsons
provider_slug: albertsons
schema_file: json-schema/retail-media-api-report-request-schema.json
slug: retail-media-api-report-request
tags:
- Grocery
- Retail
- Retail Media
- Advertising
- Campaigns
- Analytics
- Consumer Goods
- Food
- Pharmacy
title: Report Request
---
