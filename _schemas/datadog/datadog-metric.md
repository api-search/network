---
description: 'A metric series submitted to the Datadog Metrics API. Represents a named time series of numeric data points associated with optional tags, host, and resource metadata. Metric series are used to track performance, health, and business KPIs in Datadog dashboards and monitors. Datadog supports four metric types: gauge (instantaneous value), count (cumulative count), rate (per-second rate), and distribution (histogram across all hosts).'
layout: schema
name: Datadog Metric Series
properties_list:
- description: The name of the metric to submit. Must not exceed 200 characters. Only ASCII alphanumerics, underscores, and periods are allowed. Metric names are case-sensitive and conventionally use dot notation to
  name: metric
  type: string
- description: 'The metric type code indicating how Datadog should interpret and store the data points. 0=unspecified (defaults to gauge), 1=count (cumulative number of events), 2=rate (per-second rate computed from '
  name: type
  type: integer
- description: Ordered list of data points for this metric series. Each point contains a Unix timestamp and a numeric value. Points are stored in order and used for graphing, alerting, and analytics. A single submis
  name: points
  type: array
- description: List of tags to apply to this metric series in key:value format (e.g., env:production, region:us-east-1). Tags enable filtering, grouping, and scoping in dashboards and monitors. Maximum of 100 tags p
  name: tags
  type: array
- description: The hostname of the machine that produced this metric data. Associates the metric with a specific host in the Datadog Infrastructure list and host map. If omitted, the metric is not associated with an
  name: host
  type: string
- description: For rate and count metric types, the time interval in seconds over which the metric was collected. Required when submitting rate or count metrics to enable proper normalization.
  name: interval
  type: integer
- description: The unit of measurement for the metric values (e.g., byte, second, request, query, error). Units are displayed in Datadog dashboards and monitors to provide context for the metric values.
  name: unit
  type: string
- description: A list of resources associated with this metric series. Resources link the metric to infrastructure entities such as hosts, containers, services, or cloud resources. Each resource has a name and type.
  name: resources
  type: array
- description: The name of the source integration or technology that is submitting this metric (e.g., aws, nginx, kubernetes). Used for categorization and filtering in the Metrics Explorer.
  name: source_type_name
  type: string
provider_name: Datadog
provider_slug: datadog
schema_file: json-schema/datadog-metric-schema.json
slug: datadog-metric
tags:
- Analytics
- Dashboards
- Monitoring
- Platform
- T1
- Visualizations
title: Datadog Metric Series
---
