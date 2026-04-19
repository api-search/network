---
description: Time series data for a single metric.
layout: schema
name: MetricTimeSeries
properties_list:
- description: Name of the target.
  name: targetName
  type: string
- description: Type of the target.
  name: targetType
  type: string
- description: Name of the metric group.
  name: metricGroupName
  type: string
- description: Name of the metric column.
  name: metricColumnName
  type: string
- description: Key value for the metric row.
  name: key
  type: string
- description: ''
  name: dataPoints
  type: array
provider_name: Oracle Enterprise Manager
provider_slug: oracle-enterprise-manager
schema_file: json-schema/oracle-enterprise-manager-cloud-control-metric-time-series-schema.json
slug: oracle-enterprise-manager-cloud-control-metric-time-series
tags:
- Cloud Management
- Database Management
- Enterprise Management
- Infrastructure Management
- Monitoring
- Oracle
title: MetricTimeSeries
---
