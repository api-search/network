---
description: The quantitative measurements of a report. For example, the metric `eventCount` is the total number of events. Requests are allowed up to 10 metrics.
layout: schema
name: Metric
properties_list:
- description: A mathematical expression for derived metrics. For example, the metric Event count per user is `eventCount/totalUsers`.
  name: expression
  type: string
- description: Indicates if a metric is invisible in the report response. If a metric is invisible, the metric will not produce a column in the response, but can be used in `metricFilter`, `orderBys`, or a metric `e
  name: invisible
  type: boolean
- description: The name of the metric. See the [API Metrics](https://developers.google.com/analytics/devguides/reporting/data/v1/api-schema#metrics) for the list of metric names supported by core reporting methods s
  name: name
  type: string
provider_name: Google Analytics
provider_slug: google-analytics
schema_file: json-schema/data-api-metric-schema.json
slug: data-api-metric
tags:
- Analytics
- Data
- Google
- Metrics
- Reporting
- Web Analytics
- Machine Learning
- Attribution
title: Metric
---
