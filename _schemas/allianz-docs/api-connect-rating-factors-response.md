---
description: Detailed premium breakdown and rating factors for an estimate
layout: schema
name: RatingFactorsResponse
properties_list:
- description: Unique identifier for the estimate
  name: estimate_id
  type: string
- description: Base premium before adjustments
  name: base_premium
  type: number
- description: Additional risk-based premium loading
  name: risk_loading
  type: number
- description: Applied discounts
  name: discounts
  type: number
- description: Government stamp duty
  name: stamp_duty
  type: number
- description: Final annual premium after all adjustments
  name: annual_premium
  type: number
- description: Currency code
  name: currency
  type: string
- description: List of individual rating factors applied
  name: factors
  type: array
provider_name: Allianz
provider_slug: allianz-docs
schema_file: json-schema/api-connect-rating-factors-response-schema.json
slug: api-connect-rating-factors-response
tags:
- Financial Services
- Insurance
- Asset Management
title: RatingFactorsResponse
---
