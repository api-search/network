---
description: Defines a group of related metrics collected for a target. Each metric group has a name, collection frequency, and a set of metric columns.
layout: schema
name: MetricGroup
properties_list:
- description: Unique name of the metric group.
  name: metricGroupName
  type: string
- description: Human-readable display name.
  name: displayName
  type: string
- description: Description of what this metric group measures.
  name: description
  type: string
- description: Collection interval in seconds.
  name: collectionFrequency
  type: integer
- description: List of metric columns in this group.
  name: metricColumns
  type: array
provider_name: Oracle Enterprise Manager
provider_slug: oracle-enterprise-manager
schema_file: json-schema/oracle-enterprise-manager-cloud-control-metric-group-schema.json
slug: oracle-enterprise-manager-cloud-control-metric-group
tags:
- Cloud Management
- Database Management
- Enterprise Management
- Infrastructure Management
- Monitoring
- Oracle
title: MetricGroup
---
