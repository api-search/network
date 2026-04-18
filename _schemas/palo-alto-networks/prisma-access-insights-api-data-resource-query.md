---
description: Query parameters for a data resource request
layout: schema
name: DataResourceQuery
properties_list:
- description: Query definition including filters and time range
  name: query
  type: object
- description: Maximum number of results to return
  name: count
  type: integer
- description: Histogram aggregation configuration
  name: histogram
  type: object
- description: Properties to group results by
  name: group_by
  type: array
- description: Sort configuration for results
  name: sort
  type: object
provider_name: Palo Alto Networks
provider_slug: palo-alto-networks
schema_file: json-schema/prisma-access-insights-api-data-resource-query-schema.json
slug: prisma-access-insights-api-data-resource-query
tags:
- Cloud Security
- Cybersecurity
- Firewall
- Network Security
- SASE
- SOAR
- Threat Intelligence
- XDR
title: DataResourceQuery
---
