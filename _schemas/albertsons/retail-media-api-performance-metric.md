---
description: Performance metrics for an advertising campaign at a given time period.
layout: schema
name: Performance Metric
properties_list:
- description: Date of the metric data point.
  name: date
  type: string
- description: Campaign identifier associated with these metrics.
  name: campaignId
  type: string
- description: Number of ad impressions served.
  name: impressions
  type: integer
- description: Number of ad clicks recorded.
  name: clicks
  type: integer
- description: Number of conversions attributed to the campaign.
  name: conversions
  type: integer
- description: Total ad spend in USD for the period.
  name: spend
  type: number
- description: Return on ad spend ratio.
  name: roas
  type: number
- description: Click-through rate as a decimal (clicks / impressions).
  name: clickThroughRate
  type: number
provider_name: albertsons
provider_slug: albertsons
schema_file: json-schema/retail-media-api-performance-metric-schema.json
slug: retail-media-api-performance-metric
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
title: Performance Metric
---
