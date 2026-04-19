---
description: BatchActivationItem schema from AB Tasty Decision API
layout: schema
name: BatchActivationItem
properties_list:
- description: Visitor ID
  name: vid
  type: string
- description: Variation group ID
  name: caid
  type: string
- description: Variation ID
  name: vaid
  type: string
- description: Time delta in milliseconds for offline/latent hits (0-4 hours)
  name: qt
  type: integer
provider_name: AB Tasty
provider_slug: ab-tasty
schema_file: json-schema/decision-api-batch-activation-item-schema.json
slug: decision-api-batch-activation-item
tags:
- Aggregation
- Experimentation
- Feature Flags
- Personalization
- A/B Testing
title: BatchActivationItem
---
