---
class_count: 1
classes:
- Gratuity
context_file: json-ld/adyen-management-gratuity-context.jsonld
context_url: https://raw.githubusercontent.com/api-evangelist/adyen/refs/heads/main/json-ld/adyen-management-gratuity-context.jsonld
description: JSON-LD context defining the semantic vocabulary for Adyen Management Gratuity from Adyen.
layout: jsonld
name: Adyen Management Gratuity Context
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
  name: allowCustomAmount
  type: boolean
- container: ''
  name: currency
  type: string
- container: set
  name: predefinedTipEntries
  type: string
- container: ''
  name: usePredefinedTipEntries
  type: boolean
property_count: 4
provider_name: Adyen
provider_slug: adyen
slug: adyen-management-gratuity-context
tags:
- Payments
- Financial Services
- Fintech
- JSON-LD
- Linked Data
- Semantic Web
---
