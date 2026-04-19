---
description: Segment schema from Amplitude Experiment Management API
layout: schema
name: Segment
properties_list:
- description: The display name of the segment.
  name: name
  type: string
- description: Array of targeting conditions that define this segment.
  name: conditions
  type: array
- description: The variant key to assign when this segment matches.
  name: variant
  type: string
- description: The percentage of matching users to include (0-100).
  name: percentage
  type: integer
provider_name: Amplitude
provider_slug: amplitude
schema_file: json-schema/experiment-management-api-segment-schema.json
slug: experiment-management-api-segment
tags:
- A/B Testing
- Analytics
- Experimentation
- Feature Flags
- Product Analytics
- User Behavior
title: Segment
---
