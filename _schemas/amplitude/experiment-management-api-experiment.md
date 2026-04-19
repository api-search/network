---
description: Experiment schema from Amplitude Experiment Management API
layout: schema
name: Experiment
properties_list:
- description: The unique identifier for the experiment.
  name: id
  type: string
- description: The project ID the experiment belongs to.
  name: projectId
  type: string
- description: The unique key used to reference the experiment in code.
  name: key
  type: string
- description: The display name of the experiment.
  name: name
  type: string
- description: A description of the experiment's purpose.
  name: description
  type: string
- description: Whether the experiment is enabled.
  name: enabled
  type: boolean
- description: The evaluation mode, either local or remote.
  name: evaluationMode
  type: string
- description: The property used for bucketing.
  name: bucketingKey
  type: string
- description: The salt used for hashing.
  name: bucketingSalt
  type: string
- description: Array of variant configurations including control and treatment groups.
  name: variants
  type: array
- description: Array of deployment IDs.
  name: deployments
  type: array
- description: Array of targeting segments.
  name: segments
  type: array
- description: The current state of the experiment.
  name: state
  type: string
- description: The variant key that was rolled out, if the experiment has concluded.
  name: rolledOutVariant
  type: string
- description: The date and time the experiment started running.
  name: startDate
  type: string
- description: The date and time the experiment stopped running.
  name: endDate
  type: string
provider_name: Amplitude
provider_slug: amplitude
schema_file: json-schema/experiment-management-api-experiment-schema.json
slug: experiment-management-api-experiment
tags:
- A/B Testing
- Analytics
- Experimentation
- Feature Flags
- Product Analytics
- User Behavior
title: Experiment
---
