---
description: Campaign schema from AB Tasty Decision API
layout: schema
name: Campaign
properties_list:
- description: Campaign ID
  name: id
  type: string
- description: Variation group ID (corresponds to a scenario in Flagship)
  name: variationGroupId
  type: string
- description: ''
  name: variation
  type: object
provider_name: AB Tasty
provider_slug: ab-tasty
schema_file: json-schema/decision-api-campaign-schema.json
slug: decision-api-campaign
tags:
- Aggregation
- Experimentation
- Feature Flags
- Personalization
- A/B Testing
title: Campaign
---
