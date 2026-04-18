---
description: Consumer segment definition
layout: schema
name: ConsumerSegment
properties_list:
- description: Unique segment identifier
  name: segment_id
  type: string
- description: Segment name
  name: name
  type: string
- description: Percentage of total market population
  name: size_pct
  type: number
- description: Average basket size in dollars
  name: avg_basket_size
  type: number
- description: Preferred shopping channels
  name: preferred_channels
  type: array
- description: Top categories for this segment
  name: key_categories
  type: array
provider_name: Circana
provider_slug: circana
schema_file: json-schema/liquid-data-consumer-segment-schema.json
slug: liquid-data-consumer-segment
tags:
- Analytics
- Consumer Data
- Market Research
- Retail
- CPG
- Point Of Sale
- Consumer Insights
- Business Intelligence
title: ConsumerSegment
---
