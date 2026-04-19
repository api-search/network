---
description: Creative rotation configuration controlling how creatives are served within an ad.
layout: schema
name: CreativeRotation
properties_list:
- description: Type of creative rotation.
  name: type
  type: string
- description: Strategy for calculating creative weights.
  name: weightCalculationStrategy
  type: string
- description: Creative assignments in this creative rotation.
  name: creativeAssignments
  type: array
- description: Creative optimization configuration used for this creative rotation.
  name: creativeOptimizationConfigurationId
  type: string
provider_name: Google Campaign Manager
provider_slug: google-campaign-manager
schema_file: json-schema/google-campaign-manager-creative-rotation-schema.json
slug: google-campaign-manager-creative-rotation
tags:
- Advertising
- Analytics
- Campaign Management
- Digital Marketing
- Reporting
title: CreativeRotation
---
