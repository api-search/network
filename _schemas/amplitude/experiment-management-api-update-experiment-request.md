---
description: UpdateExperimentRequest schema from Amplitude Experiment Management API
layout: schema
name: UpdateExperimentRequest
properties_list:
- description: The updated display name.
  name: name
  type: string
- description: The updated description.
  name: description
  type: string
- description: Whether the experiment should be enabled.
  name: enabled
  type: boolean
- description: Updated variant configurations.
  name: variants
  type: array
- description: Updated targeting segments.
  name: segments
  type: array
provider_name: Amplitude
provider_slug: amplitude
schema_file: json-schema/experiment-management-api-update-experiment-request-schema.json
slug: experiment-management-api-update-experiment-request
tags:
- A/B Testing
- Analytics
- Experimentation
- Feature Flags
- Product Analytics
- User Behavior
title: UpdateExperimentRequest
---
