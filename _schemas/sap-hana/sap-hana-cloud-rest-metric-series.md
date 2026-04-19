---
description: A time series of metric data points for a specific metric type on an SAP HANA Cloud service instance.
layout: schema
name: MetricSeries
properties_list:
- description: The type of metric (e.g., cpu_usage, memory_used, disk_used, active_connections).
  name: metricType
  type: string
- description: The unit of measurement (e.g., percent, bytes, count).
  name: unit
  type: string
- description: The time-ordered list of metric data points.
  name: dataPoints
  type: array
provider_name: SAP HANA
provider_slug: sap-hana
schema_file: json-schema/sap-hana-cloud-rest-metric-series-schema.json
slug: sap-hana-cloud-rest-metric-series
tags:
- Analytics
- Cloud
- Database
- Enterprise
- In-Memory
title: MetricSeries
---
