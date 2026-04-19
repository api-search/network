---
class_count: 1
classes:
- MerchantRiskIndicator
context_file: json-ld/adyen-payments-merchant-risk-context.jsonld
context_url: https://raw.githubusercontent.com/api-evangelist/adyen/refs/heads/main/json-ld/adyen-payments-merchant-risk-context.jsonld
description: JSON-LD context defining the semantic vocabulary for Adyen Payments Merchant Risk from Adyen.
layout: jsonld
name: Adyen Payments Merchant Risk Context
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
  name: addressMatch
  type: boolean
- container: ''
  name: deliveryAddressIndicator
  type: string
- container: ''
  name: deliveryEmail
  type: string
- container: ''
  name: deliveryEmailAddress
  type: string
- container: ''
  name: deliveryTimeframe
  type: string
- container: ''
  name: giftCardAmount
  type: string
- container: ''
  name: giftCardCount
  type: integer
- container: ''
  name: giftCardCurr
  type: string
- container: ''
  name: preOrderDate
  type: dateTime
- container: ''
  name: preOrderPurchase
  type: boolean
- container: ''
  name: preOrderPurchaseInd
  type: string
- container: ''
  name: reorderItems
  type: boolean
- container: ''
  name: reorderItemsInd
  type: string
- container: ''
  name: shipIndicator
  type: string
property_count: 14
provider_name: Adyen
provider_slug: adyen
slug: adyen-payments-merchant-risk-context
tags:
- Payments
- Financial Services
- Fintech
- JSON-LD
- Linked Data
- Semantic Web
---
