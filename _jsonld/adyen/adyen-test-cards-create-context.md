---
class_count: 2
classes:
- CreateTestCardRangesRequest
- CreateTestCardRangesResult
context_file: json-ld/adyen-test-cards-create-context.jsonld
context_url: https://raw.githubusercontent.com/api-evangelist/adyen/refs/heads/main/json-ld/adyen-test-cards-create-context.jsonld
description: JSON-LD context defining the semantic vocabulary for Adyen Test Cards Create from Adyen.
layout: jsonld
name: Adyen Test Cards Create Context
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
  name: accountCode
  type: string
- container: ''
  name: accountTypeCode
  type: string
- container: set
  name: testCardRanges
  type: string
- container: set
  name: rangeCreationResults
  type: string
property_count: 4
provider_name: Adyen
provider_slug: adyen
slug: adyen-test-cards-create-context
tags:
- Payments
- Financial Services
- Fintech
- JSON-LD
- Linked Data
- Semantic Web
---
