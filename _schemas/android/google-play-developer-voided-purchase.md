---
description: A purchase that has been voided (cancelled, refunded, or charged back).
layout: schema
name: VoidedPurchase
properties_list:
- description: Resource type identifier.
  name: kind
  type: string
- description: The token which uniquely identifies the purchase.
  name: purchaseToken
  type: string
- description: Time at which the purchase was made (milliseconds since Epoch).
  name: purchaseTimeMillis
  type: string
- description: Time at which the purchase was voided (milliseconds since Epoch).
  name: voidedTimeMillis
  type: string
- description: The order ID associated with the voided purchase.
  name: orderId
  type: string
- description: The source of the voiding. 0 = User, 1 = Developer, 2 = Google.
  name: voidedSource
  type: integer
- description: The reason for voiding. 0 = Other, 1 = Remorse, 2 = Not received, 3 = Defective, 4 = Accidental purchase, 5 = Fraud, 6 = Friendly fraud, 7 = Chargeback.
  name: voidedReason
  type: integer
- description: The voided quantity as related to multi-quantity purchases.
  name: voidedQuantity
  type: integer
provider_name: Android
provider_slug: android
schema_file: json-schema/google-play-developer-voided-purchase-schema.json
slug: google-play-developer-voided-purchase
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
title: VoidedPurchase
---
