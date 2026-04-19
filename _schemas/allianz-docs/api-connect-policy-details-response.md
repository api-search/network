---
description: Policy details and quote ready for binding
layout: schema
name: PolicyDetailsResponse
properties_list:
- description: Unique identifier for the completed quote
  name: quote_id
  type: string
- description: Assigned policy number
  name: policy_number
  type: string
- description: Status of the policy quote
  name: status
  type: string
- description: Insurance product type
  name: product_type
  type: string
- description: Annual premium for the policy
  name: annual_premium
  type: number
- description: Currency code
  name: currency
  type: string
provider_name: Allianz
provider_slug: allianz-docs
schema_file: json-schema/api-connect-policy-details-response-schema.json
slug: api-connect-policy-details-response
tags:
- Financial Services
- Insurance
- Asset Management
title: PolicyDetailsResponse
---
