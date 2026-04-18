---
description: A single aggregation group result.
layout: schema
name: LogAggregateGroup
properties_list:
- description: The field values that define this aggregation group. Keys are the groupBy field names, values are the field values for this group.
  name: groupByFields
  type: object
- description: The number of log records in this aggregation group.
  name: count
  type: integer
provider_name: Dynatrace
provider_slug: dynatrace
schema_file: json-schema/log-monitoring-api-v2-log-aggregate-group-schema.json
slug: log-monitoring-api-v2-log-aggregate-group
tags:
- AI Operations
- Analytics
- APM
- Application Performance Monitoring
- Application Security
- Automation
- Cloud Monitoring
- Digital Experience Management
- Intelligence
- Observability
title: LogAggregateGroup
---
