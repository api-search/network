---
class_count: 30
classes:
- CartItem
- productId
- quantity
- CartItemInput
- Cart
- id
- items
- OrderInput
- cartId
- storeId
- fulfillmentType
- paymentMethodId
- Order
- status
- OrderList
- orders
- LoyaltyAccount
- accountId
- memberId
- pointsBalance
- tier
- LoyaltyTransaction
- type
- points
- description
- LoyaltyTransactionList
- transactions
- ErrorResponse
- code
- message
context_file: json-ld/advance-auto-parts-commerce-api-context.jsonld
context_url: https://raw.githubusercontent.com/api-evangelist/advance-auto-parts/refs/heads/main/json-ld/advance-auto-parts-commerce-api-context.jsonld
description: JSON-LD context defining the semantic vocabulary for Advance Auto Parts Commerce Api from Advance Auto Parts.
layout: jsonld
name: Advance Auto Parts Commerce Api Context
namespaces:
- prefix: aap
  uri: https://api.advanceautoparts.com/commerce/v1/vocab#
- prefix: schema
  uri: https://schema.org/
- prefix: xsd
  uri: http://www.w3.org/2001/XMLSchema#
properties:
- container: ''
  name: unitPrice
  type: decimal
- container: ''
  name: subtotal
  type: decimal
- container: ''
  name: total
  type: decimal
- container: ''
  name: createdAt
  type: dateTime
- container: ''
  name: rewardValue
  type: decimal
- container: ''
  name: date
  type: dateTime
property_count: 6
provider_name: Advance Auto Parts
provider_slug: advance-auto-parts
slug: advance-auto-parts-commerce-api-context
tags:
- Automotive
- E-Commerce
- Parts Catalog
- Retail
- Supply Chain
- JSON-LD
- Linked Data
- Semantic Web
---
