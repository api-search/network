---
description: Summary information for a price estimate including status and premium
layout: schema
name: PriceEstimateSummary
properties_list:
- description: Unique identifier for the estimate
  name: estimate_id
  type: string
- description: Current status of the estimate
  name: status
  type: string
- description: Insurance product type
  name: product_type
  type: string
- description: Annual premium amount
  name: annual_premium
  type: number
- description: Currency code
  name: currency
  type: string
- description: Timestamp when the estimate was created
  name: created_at
  type: string
- description: Date until which the estimate is valid
  name: valid_until
  type: string
provider_name: Allianz
provider_slug: allianz-docs
schema_file: json-schema/api-connect-price-estimate-summary-schema.json
slug: api-connect-price-estimate-summary
tags:
- Financial Services
- Insurance
- Asset Management
title: PriceEstimateSummary
---
