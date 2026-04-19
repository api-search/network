---
description: Request body for querying data from a document.
layout: schema
name: QueryDocumentRequest
properties_list:
- description: URL of the document to query (PDF or image).
  name: url
  type: string
- description: AgentQL query string for structured data extraction.
  name: query
  type: string
- description: Natural language description of the data to extract.
  name: prompt
  type: string
provider_name: AgentQL
provider_slug: agentql
schema_file: json-schema/agentql-query-document-request-schema.json
slug: agentql-query-document-request
tags:
- Agents
- Artificial Intelligence
- Web Scraping
- Data Extraction
- Browser Automation
- REST API
title: QueryDocumentRequest
---
