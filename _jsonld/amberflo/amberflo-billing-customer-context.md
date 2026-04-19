---
class_count: 5
classes:
- Customer
- createTime
- updateTime
- description
- CustomerRequest
context_file: json-ld/amberflo-billing-customer-context.jsonld
context_url: https://raw.githubusercontent.com/api-evangelist/amberflo/refs/heads/main/json-ld/amberflo-billing-customer-context.jsonld
description: JSON-LD context defining the semantic vocabulary for Amberflo Billing Customer from Amberflo.
layout: jsonld
name: Amberflo Billing Customer Context
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
  name: deleteTime
  type: integer
- container: ''
  name: customerId
  type: string
- container: ''
  name: customerName
  type: string
- container: ''
  name: customerEmail
  type: string
- container: ''
  name: enabled
  type: boolean
- container: ''
  name: test
  type: boolean
- container: ''
  name: lifecycleStage
  type: string
- container: ''
  name: deactivateTimeStamp
  type: integer
- container: ''
  name: traits
  type: reference
- container: ''
  name: address
  type: string
property_count: 10
provider_name: Amberflo
provider_slug: amberflo
slug: amberflo-billing-customer-context
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
