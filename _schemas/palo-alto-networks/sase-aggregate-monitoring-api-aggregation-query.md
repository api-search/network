---
description: AggregationQuery schema from Palo Alto Networks SASE Aggregate Monitoring API
layout: schema
name: AggregationQuery
properties_list:
- description: Tenant Service Group ID to scope the query. Data from all descendant TSGs within this scope is included.
  name: tsg_id
  type: string
- description: Key-value filter conditions to apply to the query. Filter keys are data-type specific (e.g., severity, category, app_name).
  name: filter
  type: object
- description: Time range for the query.
  name: time_range
  type: object
- description: Maximum number of result rows to return.
  name: count
  type: integer
- description: Configuration for time-series histogram output. When specified, results are bucketed by time.
  name: histogram
  type: object
- description: Dimension fields to group results by. Supported values are data-type specific.
  name: group_by
  type: array
- description: Sort order for results.
  name: sort
  type: array
provider_name: Palo Alto Networks
provider_slug: palo-alto-networks
schema_file: json-schema/sase-aggregate-monitoring-api-aggregation-query-schema.json
slug: sase-aggregate-monitoring-api-aggregation-query
tags:
- Cloud Security
- Cybersecurity
- Firewall
- Network Security
- SASE
- SOAR
- Threat Intelligence
- XDR
title: AggregationQuery
---
