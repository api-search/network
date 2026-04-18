---
description: A metric query definition referencing a Datadog metrics query expression
layout: schema
name: MetricQueryDefinition
properties_list:
- description: A unique name used to reference this query in formula expressions
  name: name
  type: string
- description: The data source for the query
  name: data_source
  type: string
- description: The Datadog metrics query string (e.g., avg:system.cpu.user{*} by {host})
  name: query
  type: string
provider_name: Datadog
provider_slug: datadog
schema_file: json-schema/datadog-metrics-metric-query-definition-schema.json
slug: datadog-metrics-metric-query-definition
tags:
- Analytics
- Dashboards
- Monitoring
- Platform
- T1
- Visualizations
title: MetricQueryDefinition
---
