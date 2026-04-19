---
description: Quote response
layout: schema
name: QuoteResponse
properties_list:
- description: Unique quote identifier
  name: quote_id
  type: string
- description: Quote status
  name: status
  type: string
- description: Annual premium amount
  name: premium
  type: number
- description: Insurance product type
  name: product_type
  type: string
- description: Policy effective date
  name: effective_date
  type: string
- description: Policy expiration date
  name: expiration_date
  type: string
- description: ''
  name: insured
  type: object
- description: Whether this quote can be bound online
  name: bind_online
  type: boolean
- description: Quote creation timestamp
  name: created_at
  type: string
- description: Quote expiration timestamp
  name: expires_at
  type: string
provider_name: AmTrust Financial Services
provider_slug: amtrust-financial-services
schema_file: json-schema/amtrust-financial-services-quote-response-schema.json
slug: amtrust-financial-services-quote-response
tags:
- Commercial Insurance
- Insurance
- Property And Casualty
- Small Business
- Workers Compensation
title: QuoteResponse
---
