---
description: Deployment schema from Amplitude Experiment Management API
layout: schema
name: Deployment
properties_list:
- description: The unique identifier for the deployment.
  name: id
  type: string
- description: The project the deployment belongs to.
  name: projectId
  type: string
- description: The display label for the deployment.
  name: label
  type: string
- description: The deployment key used for API authentication.
  name: key
  type: string
- description: Whether the deployment has been deleted.
  name: deleted
  type: boolean
provider_name: Amplitude
provider_slug: amplitude
schema_file: json-schema/experiment-management-api-deployment-schema.json
slug: experiment-management-api-deployment
tags:
- A/B Testing
- Analytics
- Experimentation
- Feature Flags
- Product Analytics
- User Behavior
title: Deployment
---
