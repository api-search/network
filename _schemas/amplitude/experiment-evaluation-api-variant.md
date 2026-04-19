---
description: Variant schema from Amplitude Experiment Evaluation API
layout: schema
name: Variant
properties_list:
- description: The variant key identifying this variant.
  name: key
  type: string
- description: The variant value or payload.
  name: value
  type: string
- description: An optional JSON payload associated with the variant.
  name: payload
  type: object
- description: Metadata about the variant assignment.
  name: metadata
  type: object
provider_name: Amplitude
provider_slug: amplitude
schema_file: json-schema/experiment-evaluation-api-variant-schema.json
slug: experiment-evaluation-api-variant
tags:
- A/B Testing
- Analytics
- Experimentation
- Feature Flags
- Product Analytics
- User Behavior
title: Variant
---
