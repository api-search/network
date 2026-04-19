---
class_count: 1
classes:
- CardData
context_file: json-ld/adyen-terminal-card-data-context.jsonld
context_url: https://raw.githubusercontent.com/api-evangelist/adyen/refs/heads/main/json-ld/adyen-terminal-card-data-context.jsonld
description: JSON-LD context defining the semantic vocabulary for Adyen Terminal Card Data from Adyen.
layout: jsonld
name: Adyen Terminal Card Data Context
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
  name: PaymentBrand
  type: string
- container: ''
  name: MaskedPan
  type: string
- container: ''
  name: PaymentAccountRef
  type: string
- container: ''
  name: EntryMode
  type: string
- container: ''
  name: CardCountryCode
  type: integer
- container: ''
  name: ProtectedCardData
  type: string
- container: ''
  name: SensitiveCardData
  type: string
- container: set
  name: AllowedProductCode
  type: integer
- container: set
  name: AllowedProduct
  type: string
- container: ''
  name: PaymentToken
  type: string
- container: set
  name: CustomerOrder
  type: string
property_count: 11
provider_name: Adyen
provider_slug: adyen
slug: adyen-terminal-card-data-context
tags:
- Payments
- Financial Services
- Fintech
- JSON-LD
- Linked Data
- Semantic Web
---
