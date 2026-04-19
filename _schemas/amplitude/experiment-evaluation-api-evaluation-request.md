---
description: EvaluationRequest schema from Amplitude Experiment Evaluation API
layout: schema
name: EvaluationRequest
properties_list:
- description: The user ID to evaluate experiments and flags for.
  name: user_id
  type: string
- description: The device ID to evaluate experiments and flags for.
  name: device_id
  type: string
- description: User properties to use for targeting rule evaluation.
  name: user_properties
  type: object
- description: Group type to group name mappings for group-level targeting.
  name: groups
  type: object
- description: Group properties to use for targeting rule evaluation.
  name: group_properties
  type: object
provider_name: Amplitude
provider_slug: amplitude
schema_file: json-schema/experiment-evaluation-api-evaluation-request-schema.json
slug: experiment-evaluation-api-evaluation-request
tags:
- A/B Testing
- Analytics
- Experimentation
- Feature Flags
- Product Analytics
- User Behavior
title: EvaluationRequest
---
