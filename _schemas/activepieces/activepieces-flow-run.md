---
description: A flow execution run
layout: schema
name: FlowRun
properties_list:
- description: Flow run ID
  name: id
  type: string
- description: Run creation timestamp
  name: created
  type: string
- description: Last update timestamp
  name: updated
  type: string
- description: Project ID
  name: projectId
  type: string
- description: Flow ID
  name: flowId
  type: string
- description: Run status
  name: status
  type: string
- description: Run start time
  name: startTime
  type: string
- description: Run finish time
  name: finishTime
  type: string
- description: Execution duration in milliseconds
  name: duration
  type: integer
provider_name: Activepieces
provider_slug: activepieces
schema_file: json-schema/activepieces-flow-run-schema.json
slug: activepieces-flow-run
tags:
- Automation
- No-Code
- Open Source
- Workflow
- AI Agents
- MCP
title: FlowRun
---
