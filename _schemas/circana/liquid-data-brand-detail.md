---
description: Detailed brand information
layout: schema
name: BrandDetail
properties_list:
- description: Unique brand identifier
  name: brand_id
  type: string
- description: Brand name
  name: name
  type: string
- description: Manufacturer or parent company name
  name: manufacturer
  type: string
- description: Categories the brand is present in
  name: categories
  type: array
- description: Number of UPCs under this brand
  name: upc_count
  type: integer
- description: Brand market presence information
  name: market_presence
  type: object
provider_name: Circana
provider_slug: circana
schema_file: json-schema/liquid-data-brand-detail-schema.json
slug: liquid-data-brand-detail
tags:
- Analytics
- Consumer Data
- Market Research
- Retail
- CPG
- Point Of Sale
- Consumer Insights
- Business Intelligence
title: BrandDetail
---
