---
description: A single metric data point at a specific timestamp.
layout: schema
name: MetricDataPoint
properties_list:
- description: ISO 8601 timestamp for the data point.
  name: timestamp
  type: string
- description: The metric value at the given timestamp.
  name: value
  type: number
- description: The minimum value observed during the aggregation interval.
  name: min
  type: number
- description: The maximum value observed during the aggregation interval.
  name: max
  type: number
- description: The average value observed during the aggregation interval.
  name: avg
  type: number
provider_name: SAP HANA
provider_slug: sap-hana
schema_file: json-schema/sap-hana-cloud-rest-metric-data-point-schema.json
slug: sap-hana-cloud-rest-metric-data-point
tags:
- Analytics
- Cloud
- Database
- Enterprise
- In-Memory
title: MetricDataPoint
---
