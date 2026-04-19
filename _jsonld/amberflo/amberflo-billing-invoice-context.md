---
class_count: 1
classes:
- Invoice
context_file: json-ld/amberflo-billing-invoice-context.jsonld
context_url: https://raw.githubusercontent.com/api-evangelist/amberflo/refs/heads/main/json-ld/amberflo-billing-invoice-context.jsonld
description: JSON-LD context defining the semantic vocabulary for Amberflo Billing Invoice from Amberflo.
layout: jsonld
name: Amberflo Billing Invoice Context
namespaces:
- prefix: amberflo
  uri: https://amberflo.io/schema/
- prefix: schema
  uri: https://schema.org/
- prefix: dcterms
  uri: http://purl.org/dc/terms/
- prefix: xsd
  uri: http://www.w3.org/2001/XMLSchema#
properties:
- container: ''
  name: invoiceId
  type: string
- container: ''
  name: customerId
  type: string
- container: ''
  name: startTime
  type: integer
- container: ''
  name: endTime
  type: integer
- container: ''
  name: totalAmount
  type: decimal
- container: ''
  name: currency
  type: string
- container: ''
  name: status
  type: string
property_count: 7
provider_name: Amberflo
provider_slug: amberflo
slug: amberflo-billing-invoice-context
tags:
- Usage-Based Billing
- Metering
- FinOps
- AI Cost Management
- Billing
- Monetization
- JSON-LD
- Linked Data
- Semantic Web
---
