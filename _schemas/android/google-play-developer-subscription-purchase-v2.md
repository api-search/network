---
description: Indicates the v2 subscription purchase details, including subscription state, line items, and external account information.
layout: schema
name: SubscriptionPurchaseV2
properties_list:
- description: Resource type identifier.
  name: kind
  type: string
- description: ISO 3166-1 alpha-2 billing region code.
  name: regionCode
  type: string
- description: The order ID of the latest order associated with this subscription.
  name: latestOrderId
  type: string
- description: Item-level info for a subscription purchase. Each line item corresponds to a base plan or offer.
  name: lineItems
  type: array
- description: Time at which the subscription was granted.
  name: startTime
  type: string
- description: The current state of the subscription.
  name: subscriptionState
  type: string
- description: The purchase token of the old subscription if replaced.
  name: linkedPurchaseToken
  type: string
- description: Additional context around paused subscriptions.
  name: pausedStateContext
  type: object
- description: Additional context around canceled subscriptions.
  name: canceledStateContext
  type: object
- description: The acknowledgement state of the subscription.
  name: acknowledgementState
  type: string
- description: User account identification in third-party services.
  name: externalAccountIdentifiers
  type: object
provider_name: Android
provider_slug: android
schema_file: json-schema/google-play-developer-subscription-purchase-v2-schema.json
slug: google-play-developer-subscription-purchase-v2
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
title: SubscriptionPurchaseV2
---
