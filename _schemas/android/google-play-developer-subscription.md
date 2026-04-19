---
description: A subscription product defined in the Google Play Console. Contains base plans, listings, and tax and compliance settings.
layout: schema
name: Subscription
properties_list:
- description: The package name of the parent app.
  name: packageName
  type: string
- description: The unique product ID of the subscription.
  name: productId
  type: string
- description: The set of base plans for this subscription. A subscription must have at least one base plan.
  name: basePlans
  type: array
- description: The localized listings for this subscription. Must have at least one listing.
  name: listings
  type: array
- description: Whether this subscription is archived.
  name: archived
  type: boolean
provider_name: Android
provider_slug: android
schema_file: json-schema/google-play-developer-subscription-schema.json
slug: google-play-developer-subscription
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
title: Subscription
---
