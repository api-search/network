---
description: VariantConfig schema from Amplitude Experiment Management API
layout: schema
name: VariantConfig
properties_list:
- description: The unique key for the variant.
  name: key
  type: string
- description: The display name of the variant.
  name: name
  type: string
- description: An optional JSON payload associated with the variant.
  name: payload
  type: object
- description: A description of what this variant does.
  name: description
  type: string
- description: The rollout weight as a percentage (0-100) controlling traffic allocation to this variant.
  name: rolloutWeight
  type: integer
provider_name: Amplitude
provider_slug: amplitude
schema_file: json-schema/experiment-management-api-variant-config-schema.json
slug: experiment-management-api-variant-config
tags:
- A/B Testing
- Analytics
- Experimentation
- Feature Flags
- Product Analytics
- User Behavior
title: VariantConfig
---
