---
description: Response containing tabular query results from a KQL query execution.
layout: schema
name: QueryResults
properties_list:
- description: Array of result tables.
  name: tables
  type: array
- description: Error information for partial errors.
  name: error
  type: object
provider_name: Azure Log Analytics
provider_slug: azure-log-analytics
schema_file: json-schema/query-api-query-results-schema.json
slug: query-api-query-results
tags:
- Analytics
- Azure
- Cloud
- Logging
- Monitoring
title: QueryResults
---
