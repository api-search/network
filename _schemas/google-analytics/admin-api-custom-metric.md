---
description: A definition for a custom metric.
layout: schema
name: CustomMetric
properties_list:
- description: Optional. Description for this custom dimension. Max length of 150 characters.
  name: description
  type: string
- description: 'Required. Display name for this custom metric as shown in the Analytics UI. Max length of 82 characters, alphanumeric plus space and underscore starting with a letter. Legacy system-generated display '
  name: displayName
  type: string
- description: Required. The type for the custom metric's value.
  name: measurementUnit
  type: string
- description: 'Output only. Resource name for this CustomMetric resource. Format: properties/{property}/customMetrics/{customMetric}'
  name: name
  type: string
- description: Required. Immutable. Tagging name for this custom metric. If this is an event-scoped metric, then this is the event parameter name. May only contain alphanumeric and underscore charactes, starting wit
  name: parameterName
  type: string
- description: Optional. Types of restricted data that this metric may contain. Required for metrics with CURRENCY measurement unit. Must be empty for metrics with a non-CURRENCY measurement unit.
  name: restrictedMetricType
  type: array
- description: Required. Immutable. The scope of this custom metric.
  name: scope
  type: string
provider_name: Google Analytics
provider_slug: google-analytics
schema_file: json-schema/admin-api-custom-metric-schema.json
slug: admin-api-custom-metric
tags:
- Analytics
- Data
- Google
- Metrics
- Reporting
- Web Analytics
- Machine Learning
- Attribution
title: CustomMetric
---
