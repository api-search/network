---
description: The response report table corresponding to a request.
layout: schema
name: RunReportResponse
properties_list:
- description: Describes dimension columns. The number of DimensionHeaders and ordering of DimensionHeaders matches the dimensions present in rows.
  name: dimensionHeaders
  type: array
- description: Identifies what kind of resource this message is. This `kind` is always the fixed string "analyticsData#runReport". Useful to distinguish between response types in JSON.
  name: kind
  type: string
- description: If requested, the maximum values of metrics.
  name: maximums
  type: array
- description: Response's metadata carrying additional information about the report content.
  name: metadata
  type: object
- description: Describes metric columns. The number of MetricHeaders and ordering of MetricHeaders matches the metrics present in rows.
  name: metricHeaders
  type: array
- description: If requested, the minimum values of metrics.
  name: minimums
  type: array
- description: Current state of all quotas for this Analytics Property. If any quota for a property is exhausted, all requests to that property will return Resource Exhausted errors.
  name: propertyQuota
  type: object
- description: The total number of rows in the query result. `rowCount` is independent of the number of rows returned in the response, the `limit` request parameter, and the `offset` request parameter. For example i
  name: rowCount
  type: integer
- description: Rows of dimension value combinations and metric values in the report.
  name: rows
  type: array
- description: If requested, the totaled values of metrics.
  name: totals
  type: array
provider_name: Google Analytics
provider_slug: google-analytics
schema_file: json-schema/data-api-run-report-response-schema.json
slug: data-api-run-report-response
tags:
- Analytics
- Data
- Google
- Metrics
- Reporting
- Web Analytics
- Machine Learning
- Attribution
title: RunReportResponse
---
