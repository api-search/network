---
description: Optional configuration parameters for the query.
layout: schema
name: QueryParams
properties_list:
- description: Extraction speed mode. Fast is quicker but may miss dynamic content.
  name: mode
  type: string
- description: Milliseconds to wait for dynamic content to load before extraction.
  name: wait_for
  type: integer
- description: If true, scroll to the bottom of the page before extraction.
  name: scroll_to_bottom
  type: boolean
- description: If true, include a base64-encoded screenshot in the response.
  name: include_screenshot
  type: boolean
- description: Browser profile to use for the request.
  name: browser_profile
  type: string
provider_name: AgentQL
provider_slug: agentql
schema_file: json-schema/agentql-query-params-schema.json
slug: agentql-query-params
tags:
- Agents
- Artificial Intelligence
- Web Scraping
- Data Extraction
- Browser Automation
- REST API
title: QueryParams
---
