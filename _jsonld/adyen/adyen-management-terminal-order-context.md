---
class_count: 2
classes:
- TerminalOrderRequest
- TerminalOrder
context_file: json-ld/adyen-management-terminal-order-context.jsonld
context_url: https://raw.githubusercontent.com/api-evangelist/adyen/refs/heads/main/json-ld/adyen-management-terminal-order-context.jsonld
description: JSON-LD context defining the semantic vocabulary for Adyen Management Terminal Order from Adyen.
layout: jsonld
name: Adyen Management Terminal Order Context
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
  name: billingEntityId
  type: string
- container: ''
  name: customerOrderReference
  type: string
- container: set
  name: items
  type: string
- container: ''
  name: orderType
  type: string
- container: ''
  name: shippingLocationId
  type: string
- container: ''
  name: taxId
  type: string
- container: ''
  name: billingEntity
  type: string
- container: ''
  name: id
  type: string
- container: ''
  name: orderDate
  type: string
- container: ''
  name: shippingLocation
  type: string
- container: ''
  name: status
  type: string
- container: ''
  name: trackingUrl
  type: string
property_count: 12
provider_name: Adyen
provider_slug: adyen
slug: adyen-management-terminal-order-context
tags:
- Payments
- Financial Services
- Fintech
- JSON-LD
- Linked Data
- Semantic Web
---
