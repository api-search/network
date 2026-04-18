---
description: A group-by configuration for aggregating log results by facet values
layout: schema
name: LogsGroupBy
properties_list:
- description: The log attribute or tag to group results by
  name: facet
  type: string
- description: The maximum number of unique facet values to return in results
  name: limit
  type: integer
- description: Sort configuration for group-by results
  name: sort
  type: object
provider_name: Datadog
provider_slug: datadog
schema_file: json-schema/datadog-logs-logs-group-by-schema.json
slug: datadog-logs-logs-group-by
tags:
- Analytics
- Dashboards
- Monitoring
- Platform
- T1
- Visualizations
title: LogsGroupBy
---
