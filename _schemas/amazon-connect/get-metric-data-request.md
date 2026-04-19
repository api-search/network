---
description: GetMetricDataRequest schema from Amazon Connect Service API
layout: schema
name: GetMetricDataRequest
properties_list:
- description: The timestamp, in UNIX Epoch time format, at which to start the reporting interval.
  name: StartTime
  type: string
- description: The timestamp, in UNIX Epoch time format, at which to end the reporting interval.
  name: EndTime
  type: string
- description: The queues, up to 100, or channels, to use to filter the metrics returned.
  name: Filters
  type: object
- description: ''
  name: Groupings
  type: array
- description: ''
  name: HistoricalMetrics
  type: array
- description: ''
  name: NextToken
  type: string
- description: ''
  name: MaxResults
  type: integer
provider_name: Amazon Connect
provider_slug: amazon-connect
schema_file: json-schema/get-metric-data-request-schema.json
slug: get-metric-data-request
tags:
- AWS
- Chat
- Contact Center
- Customer Service
- Voice
- AI
- Omnichannel
title: GetMetricDataRequest
---
