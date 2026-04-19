---
class_count: 2
classes:
- PaginatedGetCardOrderItemResponse
- PaginatedGetCardOrderResponse
context_file: json-ld/adyen-configuration-paginated-get-context.jsonld
context_url: https://raw.githubusercontent.com/api-evangelist/adyen/refs/heads/main/json-ld/adyen-configuration-paginated-get-context.jsonld
description: JSON-LD context defining the semantic vocabulary for Adyen Configuration Paginated Get from Adyen.
layout: jsonld
name: Adyen Configuration Paginated Get Context
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
- container: set
  name: data
  type: string
- container: ''
  name: hasNext
  type: boolean
- container: ''
  name: hasPrevious
  type: boolean
- container: set
  name: cardOrders
  type: string
property_count: 4
provider_name: Adyen
provider_slug: adyen
slug: adyen-configuration-paginated-get-context
tags:
- Payments
- Financial Services
- Fintech
- JSON-LD
- Linked Data
- Semantic Web
---
