---
description: Request body for executing a KQL query against a Log Analytics workspace.
layout: schema
name: QueryBody
properties_list:
- description: The KQL query to execute against the workspace.
  name: query
  type: string
- description: ISO 8601 duration or time interval for the query timespan.
  name: timespan
  type: string
- description: List of additional workspace IDs for cross-workspace queries.
  name: workspaces
  type: array
provider_name: Azure Log Analytics
provider_slug: azure-log-analytics
schema_file: json-schema/query-api-query-body-schema.json
slug: query-api-query-body
tags:
- Analytics
- Azure
- Cloud
- Logging
- Monitoring
title: QueryBody
---
