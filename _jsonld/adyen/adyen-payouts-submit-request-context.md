---
class_count: 1
classes:
- SubmitRequest
context_file: json-ld/adyen-payouts-submit-request-context.jsonld
context_url: https://raw.githubusercontent.com/api-evangelist/adyen/refs/heads/main/json-ld/adyen-payouts-submit-request-context.jsonld
description: JSON-LD context defining the semantic vocabulary for Adyen Payouts Submit Request from Adyen.
layout: jsonld
name: Adyen Payouts Submit Request Context
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
  name: additionalData
  type: reference
- container: ''
  name: amount
  type: string
- container: ''
  name: dateOfBirth
  type: date
- container: ''
  name: entityType
  type: string
- container: ''
  name: fraudOffset
  type: integer
- container: ''
  name: merchantAccount
  type: string
- container: ''
  name: nationality
  type: string
- container: ''
  name: recurring
  type: string
- container: ''
  name: reference
  type: string
- container: ''
  name: selectedRecurringDetailReference
  type: string
- container: ''
  name: shopperEmail
  type: string
- container: ''
  name: shopperName
  type: string
- container: ''
  name: shopperReference
  type: string
- container: ''
  name: shopperStatement
  type: string
- container: ''
  name: socialSecurityNumber
  type: string
property_count: 15
provider_name: Adyen
provider_slug: adyen
slug: adyen-payouts-submit-request-context
tags:
- Payments
- Financial Services
- Fintech
- JSON-LD
- Linked Data
- Semantic Web
---
