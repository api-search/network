---
description: A formula expression that combines one or more query results
layout: schema
name: QueryFormula
properties_list:
- description: The formula expression using query names as variables (e.g., query1 + query2)
  name: formula
  type: string
- description: An optional alias for the formula result used in the response
  name: alias
  type: string
- description: Optional limit configuration for top/bottom N results
  name: limit
  type: object
provider_name: Datadog
provider_slug: datadog
schema_file: json-schema/datadog-metrics-query-formula-schema.json
slug: datadog-metrics-query-formula
tags:
- Analytics
- Dashboards
- Monitoring
- Platform
- T1
- Visualizations
title: QueryFormula
---
