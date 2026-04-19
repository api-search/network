---
description: Request to create a commercial lines quote
layout: schema
name: QuoteRequest
properties_list:
- description: Insurance product type
  name: product_type
  type: string
- description: US state abbreviation
  name: state
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
- description: Requested coverage details
  name: coverages
  type: array
- description: AmTrust agent identifier
  name: agent_id
  type: string
provider_name: AmTrust Financial Services
provider_slug: amtrust-financial-services
schema_file: json-schema/amtrust-financial-services-quote-request-schema.json
slug: amtrust-financial-services-quote-request
tags:
- Commercial Insurance
- Insurance
- Property And Casualty
- Small Business
- Workers Compensation
title: QuoteRequest
---
