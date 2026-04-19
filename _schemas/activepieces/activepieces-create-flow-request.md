---
description: Request body for creating a flow
layout: schema
name: CreateFlowRequest
properties_list:
- description: Flow display name
  name: displayName
  type: string
- description: Project ID to create flow in
  name: projectId
  type: string
- description: Optional folder ID
  name: folderId
  type: string
- description: Optional template to base the flow on
  name: templateId
  type: string
- description: Custom metadata
  name: metadata
  type: object
provider_name: Activepieces
provider_slug: activepieces
schema_file: json-schema/activepieces-create-flow-request-schema.json
slug: activepieces-create-flow-request
tags:
- Automation
- No-Code
- Open Source
- Workflow
- AI Agents
- MCP
title: CreateFlowRequest
---
