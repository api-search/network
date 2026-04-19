---
class_count: 4
classes:
- TerminalProductPrice
- TerminalProduct
- description
- name
context_file: json-ld/adyen-management-terminal-product-context.jsonld
context_url: https://raw.githubusercontent.com/api-evangelist/adyen/refs/heads/main/json-ld/adyen-management-terminal-product-context.jsonld
description: JSON-LD context defining the semantic vocabulary for Adyen Management Terminal Product from Adyen.
layout: jsonld
name: Adyen Management Terminal Product Context
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
  name: currency
  type: string
- container: ''
  name: value
  type: double
- container: ''
  name: id
  type: string
- container: set
  name: itemsIncluded
  type: string
- container: ''
  name: price
  type: string
property_count: 5
provider_name: Adyen
provider_slug: adyen
slug: adyen-management-terminal-product-context
tags:
- Payments
- Financial Services
- Fintech
- JSON-LD
- Linked Data
- Semantic Web
---
