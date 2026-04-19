---
description: An individual line item within a v2 subscription purchase. Each line item represents a base plan or offer.
layout: schema
name: SubscriptionPurchaseLineItem
properties_list:
- description: The product ID of the subscription.
  name: productId
  type: string
- description: Time at which the subscription line item will expire.
  name: expiryTime
  type: string
- description: Details for auto-renewing plans.
  name: autoRenewingPlan
  type: object
- description: Details for prepaid plans.
  name: prepaidPlan
  type: object
- description: Details of the offer applied to this line item.
  name: offerDetails
  type: object
provider_name: Android
provider_slug: android
schema_file: json-schema/google-play-developer-subscription-purchase-line-item-schema.json
slug: google-play-developer-subscription-purchase-line-item
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
title: SubscriptionPurchaseLineItem
---
