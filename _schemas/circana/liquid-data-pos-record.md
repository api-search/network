---
description: Individual point-of-sale data record
layout: schema
name: POSRecord
properties_list:
- description: Time period identifier
  name: period
  type: string
- description: Product category name
  name: category
  type: string
- description: Brand name
  name: brand
  type: string
- description: Universal Product Code
  name: upc
  type: string
- description: Total dollar sales for the period
  name: dollar_sales
  type: number
- description: Total unit sales for the period
  name: unit_sales
  type: integer
- description: Total volume sales (equivalent units)
  name: volume_sales
  type: number
- description: Average selling price
  name: avg_price
  type: number
- description: Percentage of stores carrying the product
  name: distribution_pct
  type: number
provider_name: Circana
provider_slug: circana
schema_file: json-schema/liquid-data-pos-record-schema.json
slug: liquid-data-pos-record
tags:
- Analytics
- Consumer Data
- Market Research
- Retail
- CPG
- Point Of Sale
- Consumer Insights
- Business Intelligence
title: POSRecord
---
