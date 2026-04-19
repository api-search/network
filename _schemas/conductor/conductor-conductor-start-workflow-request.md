---
description: ''
layout: schema
name: StartWorkflowRequest
properties_list:
- description: Name of the workflow to start
  name: name
  type: string
- description: Version of the workflow
  name: version
  type: integer
- description: Correlation ID for the workflow instance
  name: correlationId
  type: string
- description: Priority of the workflow (0-99)
  name: priority
  type: integer
- description: Input parameters for the workflow
  name: input
  type: object
- description: Task to domain mapping for routing
  name: taskToDomain
  type: object
- description: Path to externally stored input payload
  name: externalInputPayloadStoragePath
  type: string
provider_name: Conductor
provider_slug: conductor
schema_file: json-schema/conductor-conductor-start-workflow-request-schema.json
slug: conductor-conductor-start-workflow-request
tags:
- Automation
- Orchestration
- State
- Tasks
- Workflows
title: StartWorkflowRequest
---
