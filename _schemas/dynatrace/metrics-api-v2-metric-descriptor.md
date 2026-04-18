---
description: Describes a single metric including its metadata, supported aggregations, entity dimensions, and default aggregation settings.
layout: schema
name: MetricDescriptor
properties_list:
- description: The fully qualified key of the metric, potentially including applied transformations. For example, builtin:host.cpu.usage:avg.
  name: metricId
  type: string
- description: The human-readable display name of the metric.
  name: displayName
  type: string
- description: A detailed description of what the metric measures.
  name: description
  type: string
- description: The unit of the metric values. For example, Percent, Byte, MilliSecond.
  name: unit
  type: string
- description: Whether ingesting this metric consumes Davis Data Units (DDUs).
  name: dduBillable
  type: boolean
- description: The Unix timestamp in milliseconds when the metric was created.
  name: created
  type: integer
- description: The Unix timestamp in milliseconds when the metric was last written.
  name: lastWritten
  type: integer
- description: The entity types that can be used to filter this metric, e.g., HOST, SERVICE, PROCESS_GROUP.
  name: entityType
  type: array
- description: The list of aggregation types supported for this metric. Valid values include min, max, sum, count, avg, median, and percentile.
  name: aggregationTypes
  type: array
- description: The list of dimension definitions for this metric. Each dimension provides a label for data splitting.
  name: dimensionDefinitions
  type: array
- description: The list of transformation expressions that can be applied to this metric using the metric selector.
  name: transformations
  type: array
- description: ''
  name: defaultAggregation
  type: object
provider_name: Dynatrace
provider_slug: dynatrace
schema_file: json-schema/metrics-api-v2-metric-descriptor-schema.json
slug: metrics-api-v2-metric-descriptor
tags:
- AI Operations
- Analytics
- APM
- Application Performance Monitoring
- Application Security
- Automation
- Cloud Monitoring
- Digital Experience Management
- Intelligence
- Observability
title: MetricDescriptor
---
