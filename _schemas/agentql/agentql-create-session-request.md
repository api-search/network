---
description: Request body for creating a remote browser session.
layout: schema
name: CreateSessionRequest
properties_list:
- description: Operating system to simulate in the browser user agent.
  name: browser_ua_preset
  type: string
- description: Browser behavior profile.
  name: browser_profile
  type: string
- description: Seconds of inactivity before the session is automatically terminated.
  name: inactivity_timeout_seconds
  type: integer
- description: Proxy configuration for the browser session.
  name: proxy
  type: object
provider_name: AgentQL
provider_slug: agentql
schema_file: json-schema/agentql-create-session-request-schema.json
slug: agentql-create-session-request
tags:
- Agents
- Artificial Intelligence
- Web Scraping
- Data Extraction
- Browser Automation
- REST API
title: CreateSessionRequest
---
