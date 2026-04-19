---
description: Response containing the remote browser session details.
layout: schema
name: CreateSessionResponse
properties_list:
- description: Unique identifier for the created session.
  name: session_id
  type: string
- description: WebSocket URL for Chrome DevTools Protocol access.
  name: cdp_url
  type: string
- description: ISO 8601 timestamp when the session will expire.
  name: expires_at
  type: string
provider_name: AgentQL
provider_slug: agentql
schema_file: json-schema/agentql-create-session-response-schema.json
slug: agentql-create-session-response
tags:
- Agents
- Artificial Intelligence
- Web Scraping
- Data Extraction
- Browser Automation
- REST API
title: CreateSessionResponse
---
