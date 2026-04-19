---
description: Request body for creating or updating a connection
layout: schema
name: UpsertConnectionRequest
properties_list:
- description: Connection name
  name: name
  type: string
- description: Piece package name
  name: pieceName
  type: string
- description: Project ID
  name: projectId
  type: string
- description: ''
  name: type
  type: string
- description: Authentication credentials
  name: value
  type: object
provider_name: Activepieces
provider_slug: activepieces
schema_file: json-schema/activepieces-upsert-connection-request-schema.json
slug: activepieces-upsert-connection-request
tags:
- Automation
- No-Code
- Open Source
- Workflow
- AI Agents
- MCP
title: UpsertConnectionRequest
---
