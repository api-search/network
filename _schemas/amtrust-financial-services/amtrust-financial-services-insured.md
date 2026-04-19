---
description: Business insured information
layout: schema
name: Insured
properties_list:
- description: Legal business name
  name: name
  type: string
- description: Federal Employer Identification Number
  name: fein
  type: string
- description: NCCI or state class code
  name: class_code
  type: string
- description: ''
  name: address
  type: object
- description: Years the business has been operating
  name: years_in_business
  type: integer
- description: Total annual payroll
  name: payroll
  type: number
- description: Total number of employees
  name: employee_count
  type: integer
provider_name: AmTrust Financial Services
provider_slug: amtrust-financial-services
schema_file: json-schema/amtrust-financial-services-insured-schema.json
slug: amtrust-financial-services-insured
tags:
- Commercial Insurance
- Insurance
- Property And Casualty
- Small Business
- Workers Compensation
title: Insured
---
