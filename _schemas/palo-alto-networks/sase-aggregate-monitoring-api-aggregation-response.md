---
description: AggregationResponse schema from Palo Alto Networks SASE Aggregate Monitoring API
layout: schema
name: AggregationResponse
properties_list:
- description: Total number of matching records before count limit.
  name: total
  type: integer
- description: Number of records returned.
  name: count
  type: integer
- description: ''
  name: time_range
  type: object
- description: Array of result objects. Schema varies by query type and group_by dimensions.
  name: data
  type: array
- description: Time-series histogram buckets when histogram configuration was specified in the query.
  name: histogram
  type: array
provider_name: Palo Alto Networks
provider_slug: palo-alto-networks
schema_file: json-schema/sase-aggregate-monitoring-api-aggregation-response-schema.json
slug: sase-aggregate-monitoring-api-aggregation-response
tags:
- Cloud Security
- Cybersecurity
- Firewall
- Network Security
- SASE
- SOAR
- Threat Intelligence
- XDR
title: AggregationResponse
---
