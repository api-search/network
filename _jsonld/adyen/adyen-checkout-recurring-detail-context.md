---
class_count: 2
classes:
- RecurringDetail
- name
context_file: json-ld/adyen-checkout-recurring-detail-context.jsonld
context_url: https://raw.githubusercontent.com/api-evangelist/adyen/refs/heads/main/json-ld/adyen-checkout-recurring-detail-context.jsonld
description: JSON-LD context defining the semantic vocabulary for Adyen Checkout Recurring Detail from Adyen.
layout: jsonld
name: Adyen Checkout Recurring Detail Context
namespaces:
- prefix: adyen
  uri: https://docs.adyen.com/schema/
- prefix: schema
  uri: https://schema.org/
- prefix: dcterms
  uri: http://purl.org/dc/terms/
- prefix: xsd
  uri: http://www.w3.org/2001/XMLSchema#
properties:
- container: ''
  name: brand
  type: string
- container: set
  name: brands
  type: string
- container: ''
  name: configuration
  type: reference
- container: ''
  name: fundingSource
  type: string
- container: ''
  name: group
  type: string
- container: set
  name: inputDetails
  type: string
- container: set
  name: issuers
  type: string
- container: ''
  name: recurringDetailReference
  type: string
- container: ''
  name: storedDetails
  type: string
- container: ''
  name: type
  type: string
property_count: 10
provider_name: Adyen
provider_slug: adyen
slug: adyen-checkout-recurring-detail-context
tags:
- Payments
- Financial Services
- Fintech
- JSON-LD
- Linked Data
- Semantic Web
---
