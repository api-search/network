---
class_count: 1
classes:
- FraudResult
context_file: json-ld/adyen-payouts-fraud-result-context.jsonld
context_url: https://raw.githubusercontent.com/api-evangelist/adyen/refs/heads/main/json-ld/adyen-payouts-fraud-result-context.jsonld
description: JSON-LD context defining the semantic vocabulary for Adyen Payouts Fraud Result from Adyen.
layout: jsonld
name: Adyen Payouts Fraud Result Context
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
  name: accountScore
  type: integer
- container: set
  name: results
  type: string
property_count: 2
provider_name: Adyen
provider_slug: adyen
slug: adyen-payouts-fraud-result-context
tags:
- Payments
- Financial Services
- Fintech
- JSON-LD
- Linked Data
- Semantic Web
---
