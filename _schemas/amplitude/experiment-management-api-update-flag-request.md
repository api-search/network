---
description: UpdateFlagRequest schema from Amplitude Experiment Management API
layout: schema
name: UpdateFlagRequest
properties_list:
- description: The updated display name.
  name: name
  type: string
- description: The updated description.
  name: description
  type: string
- description: Whether the flag should be enabled.
  name: enabled
  type: boolean
- description: Updated variant configurations.
  name: variants
  type: array
- description: Updated targeting segment configurations.
  name: segments
  type: array
provider_name: Amplitude
provider_slug: amplitude
schema_file: json-schema/experiment-management-api-update-flag-request-schema.json
slug: experiment-management-api-update-flag-request
tags:
- A/B Testing
- Analytics
- Experimentation
- Feature Flags
- Product Analytics
- User Behavior
title: UpdateFlagRequest
---
