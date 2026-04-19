---
class_count: 2
classes:
- LineItem
- description
context_file: json-ld/adyen-checkout-line-item-context.jsonld
context_url: https://raw.githubusercontent.com/api-evangelist/adyen/refs/heads/main/json-ld/adyen-checkout-line-item-context.jsonld
description: JSON-LD context defining the semantic vocabulary for Adyen Checkout Line Item from Adyen.
layout: jsonld
name: Adyen Checkout Line Item Context
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
  name: amountExcludingTax
  type: integer
- container: ''
  name: amountIncludingTax
  type: integer
- container: ''
  name: brand
  type: string
- container: ''
  name: color
  type: string
- container: ''
  name: id
  type: string
- container: ''
  name: imageUrl
  type: string
- container: ''
  name: itemCategory
  type: string
- container: ''
  name: manufacturer
  type: string
- container: ''
  name: productUrl
  type: string
- container: ''
  name: quantity
  type: integer
- container: ''
  name: receiverEmail
  type: string
- container: ''
  name: size
  type: string
- container: ''
  name: sku
  type: string
- container: ''
  name: taxAmount
  type: integer
- container: ''
  name: taxPercentage
  type: integer
- container: ''
  name: upc
  type: string
property_count: 16
provider_name: Adyen
provider_slug: adyen
slug: adyen-checkout-line-item-context
tags:
- Payments
- Financial Services
- Fintech
- JSON-LD
- Linked Data
- Semantic Web
---
