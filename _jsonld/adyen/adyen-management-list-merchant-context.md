---
class_count: 2
classes:
- ListMerchantResponse
- ListMerchantUsersResponse
context_file: json-ld/adyen-management-list-merchant-context.jsonld
context_url: https://raw.githubusercontent.com/api-evangelist/adyen/refs/heads/main/json-ld/adyen-management-list-merchant-context.jsonld
description: JSON-LD context defining the semantic vocabulary for Adyen Management List Merchant from Adyen.
layout: jsonld
name: Adyen Management List Merchant Context
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
  name: Links
  type: string
- container: set
  name: data
  type: string
- container: ''
  name: itemsTotal
  type: integer
- container: ''
  name: pagesTotal
  type: integer
property_count: 4
provider_name: Adyen
provider_slug: adyen
slug: adyen-management-list-merchant-context
tags:
- Payments
- Financial Services
- Fintech
- JSON-LD
- Linked Data
- Semantic Web
---
