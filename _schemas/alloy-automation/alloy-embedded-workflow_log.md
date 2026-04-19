---
description: A workflow execution log entry
layout: schema
name: WorkflowLog
properties_list:
- description: Unique identifier for the log entry
  name: logId
  type: string
- description: Workflow identifier
  name: workflowId
  type: string
- description: Execution status
  name: status
  type: string
- description: Timestamp when the workflow was executed
  name: executedAt
  type: string
- description: Execution duration in milliseconds
  name: duration
  type: integer
provider_name: Alloy Automation
provider_slug: alloy-automation
schema_file: json-schema/alloy-embedded-workflow_log-schema.json
slug: alloy-embedded-workflow_log
tags:
- Automation
- Embedded Integrations
- Integrations
- iPaaS
- Unified API
- Workflows
title: WorkflowLog
---
