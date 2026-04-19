---
description: Request body for querying usage data
layout: schema
name: UsageQueryRequest
properties_list:
- description: Name of the meter to query
  name: meterApiName
  type: string
- description: Query start time in Unix seconds
  name: startTimeInSeconds
  type: integer
- description: Query end time in Unix seconds
  name: endTimeInSeconds
  type: integer
- description: Aggregation function to apply
  name: aggregation
  type: string
- description: Time interval for grouping results
  name: timeGroupingInterval
  type: string
- description: Dimensions to group results by
  name: groupBy
  type: array
- description: List of customer IDs to filter by
  name: customerFilter
  type: array
- description: Key-value filter for dimension-based filtering
  name: filter
  type: object
provider_name: Amberflo
provider_slug: amberflo
schema_file: json-schema/metering-usage-query-request-schema.json
slug: metering-usage-query-request
tags:
- Usage-Based Billing
- Metering
- FinOps
- AI Cost Management
- Billing
- Monetization
title: UsageQueryRequest
---
