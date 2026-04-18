---
description: PerformanceMetric schema from Palo Alto Networks Autonomous DEM API
layout: schema
name: PerformanceMetric
properties_list:
- description: Time bucket for the aggregated metric.
  name: timestamp
  type: string
- description: User identifier.
  name: user_id
  type: string
- description: Site name.
  name: site_name
  type: string
- description: Application identifier if metric is application-specific.
  name: app_id
  type: string
- description: Type of performance metric.
  name: metric_type
  type: string
- description: Metric value in the appropriate unit for the metric type.
  name: value
  type: number
- description: Unit of measurement (e.g., ms, pct, Mbps).
  name: unit
  type: string
- description: Network segment this metric applies to.
  name: segment
  type: string
- description: Number of measurement samples in this time bucket.
  name: sample_count
  type: integer
provider_name: Palo Alto Networks
provider_slug: palo-alto-networks
schema_file: json-schema/autonomous-dem-api-performance-metric-schema.json
slug: autonomous-dem-api-performance-metric
tags:
- Cloud Security
- Cybersecurity
- Firewall
- Network Security
- SASE
- SOAR
- Threat Intelligence
- XDR
title: PerformanceMetric
---
