---
description: Properties of a flow run.
layout: schema
name: FlowRunProperties
properties_list:
- description: The timestamp when the flow run started.
  name: startTime
  type: string
- description: The timestamp when the flow run ended. Null if still running.
  name: endTime
  type: '[''string'', ''null'']'
- description: The current status of the flow run.
  name: status
  type: string
- description: Correlation information for the flow run.
  name: correlation
  type: object
- description: Information about the trigger that initiated the flow run.
  name: trigger
  type: object
provider_name: Microsoft Power Platform APIs
provider_slug: power-platform
schema_file: json-schema/power-platform-flow-run-properties-schema.json
slug: power-platform-flow-run-properties
tags:
- Business Applications
- Copilot Studio
- Dataverse
- Low-Code
- Microsoft
- No-Code
- Power Pages
- Power Platform
title: FlowRunProperties
---
