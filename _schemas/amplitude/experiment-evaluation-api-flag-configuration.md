---
description: FlagConfiguration schema from Amplitude Experiment Evaluation API
layout: schema
name: FlagConfiguration
properties_list:
- description: The unique key identifying the flag.
  name: key
  type: string
- description: Metadata about the flag configuration.
  name: metadata
  type: object
- description: Array of targeting segments for this flag.
  name: segments
  type: array
- description: Map of variant keys to variant configuration objects.
  name: variants
  type: object
provider_name: Amplitude
provider_slug: amplitude
schema_file: json-schema/experiment-evaluation-api-flag-configuration-schema.json
slug: experiment-evaluation-api-flag-configuration
tags:
- A/B Testing
- Analytics
- Experimentation
- Feature Flags
- Product Analytics
- User Behavior
title: FlagConfiguration
---
