---
class_count: 6
classes:
- QuoteRequest
- QuoteResponse
- PolicyResponse
- Insured
- name
- description
context_file: json-ld/amtrust-financial-services-context.jsonld
context_url: https://raw.githubusercontent.com/api-evangelist/amtrust-financial-services/refs/heads/main/json-ld/amtrust-financial-services-context.jsonld
description: JSON-LD context defining the semantic vocabulary for Amtrust Financial Services from AmTrust Financial Services.
layout: jsonld
name: Amtrust Financial Services Context
namespaces:
- prefix: amtrust
  uri: https://amtrustfinancial.com/schema/
- prefix: schema
  uri: https://schema.org/
- prefix: xsd
  uri: http://www.w3.org/2001/XMLSchema#
properties:
- container: ''
  name: productType
  type: string
- container: ''
  name: state
  type: string
- container: ''
  name: effectiveDate
  type: date
- container: ''
  name: expirationDate
  type: date
- container: ''
  name: premium
  type: decimal
- container: ''
  name: policyNumber
  type: string
- container: ''
  name: quoteId
  type: string
- container: ''
  name: status
  type: string
- container: ''
  name: classCode
  type: string
- container: ''
  name: payroll
  type: decimal
- container: ''
  name: employeeCount
  type: integer
- container: ''
  name: createdAt
  type: dateTime
- container: ''
  name: boundAt
  type: dateTime
property_count: 13
provider_name: AmTrust Financial Services
provider_slug: amtrust-financial-services
slug: amtrust-financial-services-context
tags:
- Commercial Insurance
- Insurance
- Property And Casualty
- Small Business
- Workers Compensation
- JSON-LD
- Linked Data
- Semantic Web
---
