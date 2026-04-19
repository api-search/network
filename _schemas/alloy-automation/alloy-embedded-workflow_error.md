---
description: A workflow execution error record
layout: schema
name: WorkflowError
properties_list:
- description: Unique identifier for the error
  name: errorId
  type: string
- description: Workflow identifier where the error occurred
  name: workflowId
  type: string
- description: Human-readable error description
  name: message
  type: string
- description: Timestamp when the error occurred
  name: occurredAt
  type: string
provider_name: Alloy Automation
provider_slug: alloy-automation
schema_file: json-schema/alloy-embedded-workflow_error-schema.json
slug: alloy-embedded-workflow_error
tags:
- Automation
- Embedded Integrations
- Integrations
- iPaaS
- Unified API
- Workflows
title: WorkflowError
---
