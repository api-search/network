---
description: CreateFlagRequest schema from Amplitude Experiment Management API
layout: schema
name: CreateFlagRequest
properties_list:
- description: The unique key for the flag.
  name: key
  type: string
- description: The display name of the flag.
  name: name
  type: string
- description: A description of the flag's purpose.
  name: description
  type: string
- description: Array of variant configurations.
  name: variants
  type: array
- description: The property used for bucketing.
  name: bucketingKey
  type: string
provider_name: Amplitude
provider_slug: amplitude
schema_file: json-schema/experiment-management-api-create-flag-request-schema.json
slug: experiment-management-api-create-flag-request
tags:
- A/B Testing
- Analytics
- Experimentation
- Feature Flags
- Product Analytics
- User Behavior
title: CreateFlagRequest
---
