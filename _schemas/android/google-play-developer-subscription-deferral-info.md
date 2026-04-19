---
description: Contains the new desired expiry time for a subscription deferral.
layout: schema
name: SubscriptionDeferralInfo
properties_list:
- description: The expected expiry time for the subscription. If the current expiry time does not match, the deferral will not occur.
  name: expectedExpiryTimeMillis
  type: string
- description: The desired next expiry time to assign to the subscription. Must be later than the current expiry time.
  name: desiredExpiryTimeMillis
  type: string
provider_name: Android
provider_slug: android
schema_file: json-schema/google-play-developer-subscription-deferral-info-schema.json
slug: google-play-developer-subscription-deferral-info
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
title: SubscriptionDeferralInfo
---
