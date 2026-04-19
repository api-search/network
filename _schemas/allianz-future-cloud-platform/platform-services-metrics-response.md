---
description: Platform metrics for a service or overall platform
layout: schema
name: MetricsResponse
properties_list:
- description: Service the metrics apply to (null for platform-wide)
  name: service_id
  type: string
- description: Time range the metrics cover
  name: time_range_minutes
  type: integer
- description: Average CPU utilization percentage
  name: cpu_utilization
  type: number
- description: Average memory utilization percentage
  name: memory_utilization
  type: number
- description: Requests per minute
  name: request_rate
  type: number
- description: Error rate as a percentage
  name: error_rate
  type: number
- description: 99th percentile response latency in milliseconds
  name: p99_latency_ms
  type: integer
provider_name: Allianz Future Cloud Platform
provider_slug: allianz-future-cloud-platform
schema_file: json-schema/platform-services-metrics-response-schema.json
slug: platform-services-metrics-response
tags:
- Cloud Platform
- Enterprise
- Financial Services
- Insurance
- Platform Engineering
- Kubernetes
title: MetricsResponse
---
