---
description: Request body for querying data from a web page.
layout: schema
name: QueryDataRequest
properties_list:
- description: The URL of the web page to query.
  name: url
  type: string
- description: Raw HTML content to query instead of a URL.
  name: html
  type: string
- description: AgentQL query string for structured data extraction.
  name: query
  type: string
- description: Natural language description of the data to extract (alternative to query).
  name: prompt
  type: string
- description: ''
  name: params
  type: object
provider_name: AgentQL
provider_slug: agentql
schema_file: json-schema/agentql-query-data-request-schema.json
slug: agentql-query-data-request
tags:
- Agents
- Artificial Intelligence
- Web Scraping
- Data Extraction
- Browser Automation
- REST API
title: QueryDataRequest
---
