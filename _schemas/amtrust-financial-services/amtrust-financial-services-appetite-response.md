---
description: Coverage appetite check result
layout: schema
name: AppetiteResponse
properties_list:
- description: Whether AmTrust has appetite for this risk
  name: eligible
  type: boolean
- description: Available products for this risk
  name: products
  type: array
- description: Whether the policy can be bound online
  name: bind_online
  type: boolean
- description: Reason if not eligible
  name: reason
  type: string
provider_name: AmTrust Financial Services
provider_slug: amtrust-financial-services
schema_file: json-schema/amtrust-financial-services-appetite-response-schema.json
slug: amtrust-financial-services-appetite-response
tags:
- Commercial Insurance
- Insurance
- Property And Casualty
- Small Business
- Workers Compensation
title: AppetiteResponse
---
