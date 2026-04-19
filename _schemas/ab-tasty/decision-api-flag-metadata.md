---
description: FlagMetadata schema from AB Tasty Decision API
layout: schema
name: FlagMetadata
properties_list:
- description: Campaign ID
  name: campaignId
  type: string
- description: Campaign name
  name: campaignName
  type: string
- description: Campaign slug (if configured)
  name: slug
  type: string
- description: Campaign type
  name: type
  type: string
- description: Variation group ID
  name: variationGroupId
  type: string
- description: Variation group name
  name: variationGroupName
  type: string
- description: Variation ID
  name: variationId
  type: string
- description: Variation name
  name: variationName
  type: string
- description: Indicates if the variation is a reference variation
  name: reference
  type: boolean
provider_name: AB Tasty
provider_slug: ab-tasty
schema_file: json-schema/decision-api-flag-metadata-schema.json
slug: decision-api-flag-metadata
tags:
- Aggregation
- Experimentation
- Feature Flags
- Personalization
- A/B Testing
title: FlagMetadata
---
