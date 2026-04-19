---
description: A single metric data point.
layout: schema
name: MetricDataPoint
properties_list:
- description: Name of the metric column.
  name: metricColumn
  type: string
- description: Numeric metric value.
  name: value
  type: number
- description: Key value identifying the metric row.
  name: key
  type: string
- description: Timestamp when the metric was collected.
  name: collectionTime
  type: string
provider_name: Oracle Enterprise Manager
provider_slug: oracle-enterprise-manager
schema_file: json-schema/oracle-enterprise-manager-cloud-control-metric-data-point-schema.json
slug: oracle-enterprise-manager-cloud-control-metric-data-point
tags:
- Cloud Management
- Database Management
- Enterprise Management
- Infrastructure Management
- Monitoring
- Oracle
title: MetricDataPoint
---
