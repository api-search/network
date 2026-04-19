---
class_count: 1
classes:
- SubmitResponse
context_file: json-ld/adyen-payouts-submit-response-context.jsonld
context_url: https://raw.githubusercontent.com/api-evangelist/adyen/refs/heads/main/json-ld/adyen-payouts-submit-response-context.jsonld
description: JSON-LD context defining the semantic vocabulary for Adyen Payouts Submit Response from Adyen.
layout: jsonld
name: Adyen Payouts Submit Response Context
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
  name: pspReference
  type: string
- container: ''
  name: refusalReason
  type: string
- container: ''
  name: resultCode
  type: string
property_count: 4
provider_name: Adyen
provider_slug: adyen
slug: adyen-payouts-submit-response-context
tags:
- Payments
- Financial Services
- Fintech
- JSON-LD
- Linked Data
- Semantic Web
---
