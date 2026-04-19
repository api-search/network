---
description: Price estimate result with premium amounts
layout: schema
name: PriceEstimateResponse
properties_list:
- description: Unique identifier for the generated estimate
  name: estimate_id
  type: string
- description: Insurance product type
  name: product_type
  type: string
- description: Annual insurance premium amount
  name: annual_premium
  type: number
- description: Monthly insurance premium amount
  name: monthly_premium
  type: number
- description: Currency code for the premium amounts
  name: currency
  type: string
- description: Date until which this estimate is valid
  name: valid_until
  type: string
provider_name: Allianz
provider_slug: allianz-docs
schema_file: json-schema/api-connect-price-estimate-response-schema.json
slug: api-connect-price-estimate-response
tags:
- Financial Services
- Insurance
- Asset Management
title: PriceEstimateResponse
---
