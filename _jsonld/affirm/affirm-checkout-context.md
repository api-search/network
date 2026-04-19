---
class_count: 11
classes:
- DiscountObject
- ItemObject
- MerchantObject
- name
- ContactObject
- email
- CheckoutRequest
- StoreObject
- NameObject
- AddressObject
- Checkout
context_file: json-ld/affirm-checkout-context.jsonld
context_url: https://raw.githubusercontent.com/api-evangelist/affirm/refs/heads/main/json-ld/affirm-checkout-context.jsonld
description: JSON-LD context defining the semantic vocabulary for Affirm Checkout from affirm.
layout: jsonld
name: Affirm Checkout Context
namespaces:
- prefix: affirm
  uri: https://affirm.com/schema/
- prefix: schema
  uri: https://schema.org/
- prefix: dcterms
  uri: http://purl.org/dc/terms/
- prefix: xsd
  uri: http://www.w3.org/2001/XMLSchema#
properties:
- container: ''
  name: discountAmount
  type: integer
- container: ''
  name: discountDisplayName
  type: string
- container: ''
  name: displayName
  type: string
- container: ''
  name: sku
  type: string
- container: ''
  name: unitPrice
  type: integer
- container: ''
  name: qty
  type: integer
- container: ''
  name: itemImageUrl
  type: reference
- container: ''
  name: itemUrl
  type: reference
- container: set
  name: categories
  type: ''
- container: ''
  name: publicApiKey
  type: string
- container: ''
  name: userConfirmationUrl
  type: reference
- container: ''
  name: userCancelUrl
  type: reference
- container: ''
  name: userConfirmationUrlAction
  type: string
- container: ''
  name: address
  type: string
- container: ''
  name: phoneNumber
  type: string
- container: ''
  name: merchant
  type: string
- container: ''
  name: shipping
  type: string
- container: ''
  name: billing
  type: string
- container: ''
  name: store
  type: string
- container: set
  name: items
  type: string
- container: ''
  name: discounts
  type: reference
- container: ''
  name: metadata
  type: reference
- container: ''
  name: orderId
  type: string
- container: ''
  name: currency
  type: string
- container: ''
  name: financingProgram
  type: string
- container: ''
  name: shippingAmount
  type: integer
- container: ''
  name: taxAmount
  type: integer
- container: ''
  name: total
  type: integer
- container: ''
  name: checkoutExpiration
  type: dateTime
- container: ''
  name: expirationTime
  type: dateTime
- container: ''
  name: first
  type: string
- container: ''
  name: last
  type: string
- container: ''
  name: full
  type: string
- container: ''
  name: line1
  type: string
- container: ''
  name: line2
  type: string
- container: ''
  name: city
  type: string
- container: ''
  name: state
  type: string
- container: ''
  name: zipcode
  type: string
- container: ''
  name: country
  type: string
- container: ''
  name: checkoutId
  type: string
- container: ''
  name: checkoutStatus
  type: string
- container: ''
  name: checkoutFlowType
  type: string
- container: ''
  name: financialProgramName
  type: string
- container: ''
  name: financialProgramExternalName
  type: string
- container: ''
  name: billingFrequency
  type: string
- container: ''
  name: apiVersion
  type: string
- container: ''
  name: productType
  type: string
- container: ''
  name: meta
  type: reference
- container: ''
  name: userTimezone
  type: string
- container: ''
  name: trackingUuid
  type: string
property_count: 50
provider_name: affirm
provider_slug: affirm
slug: affirm-checkout-context
tags:
- JSON-LD
- Linked Data
- Semantic Web
---
