---
description: Localized listing information for a subscription.
layout: schema
name: SubscriptionListing
properties_list:
- description: BCP-47 language tag (e.g., en-US).
  name: languageCode
  type: string
- description: The title of the subscription in this locale.
  name: title
  type: string
- description: A list of benefits shown to the user on platforms such as the Play Store. Limited to four benefits.
  name: benefits
  type: array
- description: The description of the subscription in this locale.
  name: description
  type: string
provider_name: Android
provider_slug: android
schema_file: json-schema/google-play-developer-subscription-listing-schema.json
slug: google-play-developer-subscription-listing
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
title: SubscriptionListing
---
