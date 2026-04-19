---
description: Request to check coverage appetite
layout: schema
name: AppetiteRequest
properties_list:
- description: US state abbreviation
  name: state
  type: string
- description: NCCI or state class code for the business
  name: class_code
  type: string
- description: Insurance product type
  name: product_type
  type: string
- description: Annual payroll amount
  name: payroll
  type: number
provider_name: AmTrust Financial Services
provider_slug: amtrust-financial-services
schema_file: json-schema/amtrust-financial-services-appetite-request-schema.json
slug: amtrust-financial-services-appetite-request
tags:
- Commercial Insurance
- Insurance
- Property And Casualty
- Small Business
- Workers Compensation
title: AppetiteRequest
---
