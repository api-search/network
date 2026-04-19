---
class_count: 2
classes:
- SaleItemRebate
- SaleItem
context_file: json-ld/adyen-terminal-sale-item-context.jsonld
context_url: https://raw.githubusercontent.com/api-evangelist/adyen/refs/heads/main/json-ld/adyen-terminal-sale-item-context.jsonld
description: JSON-LD context defining the semantic vocabulary for Adyen Terminal Sale Item from Adyen.
layout: jsonld
name: Adyen Terminal Sale Item Context
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
  name: ItemID
  type: integer
- container: ''
  name: ProductCode
  type: integer
- container: ''
  name: EanUpc
  type: integer
- container: ''
  name: UnitOfMeasure
  type: string
- container: ''
  name: Quantity
  type: string
- container: ''
  name: ItemAmount
  type: decimal
- container: ''
  name: RebateLabel
  type: string
- container: ''
  name: UnitPrice
  type: decimal
- container: ''
  name: TaxCode
  type: integer
- container: ''
  name: SaleChannel
  type: integer
- container: ''
  name: ProductLabel
  type: string
- container: ''
  name: AdditionalProductInfo
  type: string
property_count: 12
provider_name: Adyen
provider_slug: adyen
slug: adyen-terminal-sale-item-context
tags:
- Payments
- Financial Services
- Fintech
- JSON-LD
- Linked Data
- Semantic Web
---
