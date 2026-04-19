---
description: A single phase of a subscription offer. Defines pricing for a specific period.
layout: schema
name: SubscriptionOfferPhase
properties_list:
- description: The number of times this phase repeats. If 0, the phase repeats indefinitely.
  name: recurrenceCount
  type: integer
- description: Duration of a single period in ISO 8601 format.
  name: duration
  type: string
- description: Regional pricing for this phase.
  name: regionalConfigs
  type: array
provider_name: Android
provider_slug: android
schema_file: json-schema/google-play-developer-subscription-offer-phase-schema.json
slug: google-play-developer-subscription-offer-phase
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
title: SubscriptionOfferPhase
---
