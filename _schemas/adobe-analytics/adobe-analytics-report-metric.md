---
description: A metric included in a report request
layout: schema
name: ReportMetric
properties_list:
- description: The metric ID (e.g. metrics/visits)
  name: id
  type: string
- description: Column identifier for this metric in the response
  name: columnId
  type: string
- description: Metric-level filter IDs referencing metricFilters
  name: filters
  type: array
- description: Sort direction for this metric
  name: sort
  type: string
provider_name: Adobe Analytics
provider_slug: adobe-analytics
schema_file: json-schema/adobe-analytics-report-metric-schema.json
slug: adobe-analytics-report-metric
tags:
- Adobe
- Analytics
- Business Intelligence
- Customer Intelligence
- Digital Marketing
- Marketing
- Web Analytics
title: ReportMetric
---
