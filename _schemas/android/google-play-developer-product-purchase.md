---
description: Represents an in-app product purchase. Contains the purchase state, consumption status, and order information.
layout: schema
name: ProductPurchase
properties_list:
- description: Resource type identifier.
  name: kind
  type: string
- description: Time the product was purchased (milliseconds since Epoch).
  name: purchaseTimeMillis
  type: string
- description: The purchase state of the order. 0 = Purchased, 1 = Canceled, 2 = Pending.
  name: purchaseState
  type: integer
- description: The consumption state of the in-app product. 0 = Yet to be consumed, 1 = Consumed.
  name: consumptionState
  type: integer
- description: Developer-specified string for additional transaction information.
  name: developerPayload
  type: string
- description: The order ID associated with the purchase.
  name: orderId
  type: string
- description: The type of purchase. 0 = Test (sandbox), 1 = Promo, 2 = Rewarded.
  name: purchaseType
  type: integer
- description: The acknowledgement state of the in-app product. 0 = Yet to be acknowledged, 1 = Acknowledged.
  name: acknowledgementState
  type: integer
- description: The purchase token generated at the time of purchase.
  name: purchaseToken
  type: string
- description: The in-app product SKU.
  name: productId
  type: string
- description: The quantity associated with the purchase.
  name: quantity
  type: integer
- description: An obfuscated version of the ID uniquely associated with the user's account in your app.
  name: obfuscatedExternalAccountId
  type: string
- description: An obfuscated version of the ID uniquely associated with the user's profile in your app.
  name: obfuscatedExternalProfileId
  type: string
- description: ISO 3166-1 alpha-2 billing region code of the user.
  name: regionCode
  type: string
- description: The quantity eligible for refund.
  name: refundableQuantity
  type: integer
provider_name: Android
provider_slug: android
schema_file: json-schema/google-play-developer-product-purchase-schema.json
slug: google-play-developer-product-purchase
tags:
- AI
- Android
- Automotive
- Google
- Machine Learning
- Mobile Development
- SDK
- TV
- Wearables
title: ProductPurchase
---
