---
description: A base plan specifies the billing period and renewal type for a subscription. A subscription must have at least one base plan.
layout: schema
name: BasePlan
properties_list:
- description: The unique identifier for this base plan.
  name: basePlanId
  type: string
- description: The state of the base plan.
  name: state
  type: string
- description: Regional pricing configurations.
  name: regionalConfigs
  type: array
- description: Details for auto-renewing base plans.
  name: autoRenewingBasePlanType
  type: object
- description: Details for prepaid base plans.
  name: prepaidBasePlanType
  type: object
- description: List of up to 20 custom tags for this base plan.
  name: offerTags
  type: array
provider_name: Android
provider_slug: android
schema_file: json-schema/google-play-developer-base-plan-schema.json
slug: google-play-developer-base-plan
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
title: BasePlan
---
