---
description: Bound policy details
layout: schema
name: PolicyResponse
properties_list:
- description: Unique AmTrust policy number
  name: policy_number
  type: string
- description: Policy status
  name: status
  type: string
- description: Insurance product type
  name: product_type
  type: string
- description: Annual premium
  name: premium
  type: number
- description: ''
  name: effective_date
  type: string
- description: ''
  name: expiration_date
  type: string
- description: ''
  name: insured
  type: object
- description: ''
  name: bound_at
  type: string
provider_name: AmTrust Financial Services
provider_slug: amtrust-financial-services
schema_file: json-schema/amtrust-financial-services-policy-response-schema.json
slug: amtrust-financial-services-policy-response
tags:
- Commercial Insurance
- Insurance
- Property And Casualty
- Small Business
- Workers Compensation
title: PolicyResponse
---
