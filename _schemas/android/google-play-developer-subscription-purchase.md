---
description: Represents a subscription purchase. Contains the subscription state, expiry time, auto-renewal status, and cancellation details.
layout: schema
name: SubscriptionPurchase
properties_list:
- description: Resource type identifier.
  name: kind
  type: string
- description: Time at which the subscription was granted (milliseconds since Epoch).
  name: startTimeMillis
  type: string
- description: Time at which the subscription will expire (milliseconds since Epoch). For cancelled subscriptions, this is when access ends.
  name: expiryTimeMillis
  type: string
- description: Time at which the subscription was canceled by the user (milliseconds since Epoch). Only present if cancelReason is 0.
  name: userCancellationTimeMillis
  type: string
- description: Whether the subscription will automatically be renewed.
  name: autoRenewing
  type: boolean
- description: ISO 4217 currency code for the subscription price.
  name: priceCurrencyCode
  type: string
- description: Price of the subscription in micro-units of the currency. For example, 7990000 represents $7.99.
  name: priceAmountMicros
  type: string
- description: ISO 3166-1 alpha-2 country code of the user at the time the subscription was granted.
  name: countryCode
  type: string
- description: Developer-specified string for additional information.
  name: developerPayload
  type: string
- description: The payment state of the subscription. 0 = Payment pending, 1 = Payment received, 2 = Free trial, 3 = Pending deferred upgrade/downgrade.
  name: paymentState
  type: integer
- description: The reason a subscription was cancelled or not auto-renewed. 0 = User cancelled, 1 = System cancelled (billing issue), 2 = Replaced with a new subscription, 3 = Developer cancelled.
  name: cancelReason
  type: integer
- description: The purchase token of the previous subscription if this subscription is a replacement (upgrade/downgrade).
  name: linkedPurchaseToken
  type: string
- description: The type of purchase. 0 = Test (sandbox), 1 = Promo.
  name: purchaseType
  type: integer
- description: The order ID of the latest recurring order.
  name: orderId
  type: string
- description: The acknowledgement state. 0 = Yet to be acknowledged, 1 = Acknowledged.
  name: acknowledgementState
  type: integer
- description: User account identifier in the third-party service.
  name: externalAccountId
  type: string
- description: The type of promotion applied on this purchase. 0 = One-time code, 1 = Vanity code.
  name: promotionType
  type: integer
- description: The promotion code applied on this purchase.
  name: promotionCode
  type: string
- description: Obfuscated user account ID in the third-party service.
  name: obfuscatedExternalAccountId
  type: string
- description: Obfuscated user profile ID in the third-party service.
  name: obfuscatedExternalProfileId
  type: string
provider_name: Android
provider_slug: android
schema_file: json-schema/google-play-developer-subscription-purchase-schema.json
slug: google-play-developer-subscription-purchase
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
title: SubscriptionPurchase
---
