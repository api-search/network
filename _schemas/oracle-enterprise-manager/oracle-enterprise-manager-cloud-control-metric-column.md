---
description: A single metric column within a metric group.
layout: schema
name: MetricColumn
properties_list:
- description: Name of the metric column.
  name: columnName
  type: string
- description: Human-readable display name.
  name: displayName
  type: string
- description: Data type of the metric column.
  name: columnType
  type: string
- description: Whether this column is a key column.
  name: isKey
  type: boolean
- description: Unit of measurement for the metric.
  name: unit
  type: string
provider_name: Oracle Enterprise Manager
provider_slug: oracle-enterprise-manager
schema_file: json-schema/oracle-enterprise-manager-cloud-control-metric-column-schema.json
slug: oracle-enterprise-manager-cloud-control-metric-column
tags:
- Cloud Management
- Database Management
- Enterprise Management
- Infrastructure Management
- Monitoring
- Oracle
title: MetricColumn
---
