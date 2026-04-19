---
description: Schema for an Amplitude experiment or feature flag configuration including variants, targeting segments, and deployment settings.
layout: schema
name: Amplitude Experiment
properties_list:
- description: The unique identifier for the experiment or flag.
  name: id
  type: string
- description: The project ID the experiment belongs to.
  name: projectId
  type: string
- description: The unique key used to reference the experiment or flag in code.
  name: key
  type: string
- description: The display name of the experiment or flag.
  name: name
  type: string
- description: A description of the experiment's purpose and hypothesis.
  name: description
  type: string
- description: The type of configuration.
  name: type
  type: string
- description: Whether the experiment or flag is currently enabled.
  name: enabled
  type: boolean
- description: The evaluation mode determining where variants are computed.
  name: evaluationMode
  type: string
- description: The lifecycle state of the experiment or flag.
  name: state
  type: string
- description: The user property used for deterministic bucketing.
  name: bucketingKey
  type: string
- description: The salt used with the bucketing key for hash computation.
  name: bucketingSalt
  type: string
- description: Array of variant configurations for the experiment.
  name: variants
  type: array
- description: Array of targeting segments that control which users see which variants.
  name: segments
  type: array
- description: Array of deployment IDs where this experiment is active.
  name: deployments
  type: array
- description: The variant key that was rolled out after the experiment concluded.
  name: rolledOutVariant
  type: string
- description: The date and time the experiment started.
  name: startDate
  type: string
- description: The date and time the experiment ended.
  name: endDate
  type: string
provider_name: Amplitude
provider_slug: amplitude
schema_file: json-schema/amplitude-experiment-schema.json
slug: amplitude-experiment
tags:
- A/B Testing
- Analytics
- Experimentation
- Feature Flags
- Product Analytics
- User Behavior
title: Amplitude Experiment
---
