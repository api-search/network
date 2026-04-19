---
description: Flag schema from Amplitude Experiment Management API
layout: schema
name: Flag
properties_list:
- description: The unique identifier for the flag.
  name: id
  type: string
- description: The project ID the flag belongs to.
  name: projectId
  type: string
- description: The unique key used to reference the flag in code.
  name: key
  type: string
- description: The display name of the flag.
  name: name
  type: string
- description: A description of the flag's purpose.
  name: description
  type: string
- description: Whether the flag is enabled.
  name: enabled
  type: boolean
- description: The evaluation mode, either local or remote.
  name: evaluationMode
  type: string
- description: The property used for bucketing users into variants.
  name: bucketingKey
  type: string
- description: The salt used for hashing during bucketing.
  name: bucketingSalt
  type: string
- description: Array of variant configurations.
  name: variants
  type: array
- description: Array of deployment IDs the flag is deployed to.
  name: deployments
  type: array
- description: Array of targeting segment configurations.
  name: segments
  type: array
- description: The current state of the flag.
  name: state
  type: string
provider_name: Amplitude
provider_slug: amplitude
schema_file: json-schema/experiment-management-api-flag-schema.json
slug: experiment-management-api-flag
tags:
- A/B Testing
- Analytics
- Experimentation
- Feature Flags
- Product Analytics
- User Behavior
title: Flag
---
