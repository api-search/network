---
description: The request to generate a report.
layout: schema
name: RunReportRequest
properties_list:
- description: The specification of cohorts for a cohort report. Cohort reports create a time series of user retention for the cohort. For example, you could select the cohort of users that were acquired in the firs
  name: cohortSpec
  type: object
- description: A currency code in ISO4217 format, such as "AED", "USD", "JPY". If the field is empty, the report uses the property's default currency.
  name: currencyCode
  type: string
- description: Date ranges of data to read. If multiple date ranges are requested, each response row will contain a zero based date range index. If two date ranges overlap, the event data for the overlapping days is
  name: dateRanges
  type: array
- description: To express dimension or metric filters. The fields in the same FilterExpression need to be either all dimensions or all metrics.
  name: dimensionFilter
  type: object
- description: The dimensions requested and displayed.
  name: dimensions
  type: array
- description: If false or unspecified, each row with all metrics equal to 0 will not be returned. If true, these rows will be returned if they are not separately removed by a filter. Regardless of this `keep_empty_
  name: keepEmptyRows
  type: boolean
- description: The number of rows to return. If unspecified, 10,000 rows are returned. The API returns a maximum of 250,000 rows per request, no matter how many you ask for. `limit` must be positive. The API can als
  name: limit
  type: string
- description: Aggregation of metrics. Aggregated metric values will be shown in rows where the dimension_values are set to "RESERVED_(MetricAggregation)".
  name: metricAggregations
  type: array
- description: To express dimension or metric filters. The fields in the same FilterExpression need to be either all dimensions or all metrics.
  name: metricFilter
  type: object
- description: The metrics requested and displayed.
  name: metrics
  type: array
- description: The row count of the start row. The first row is counted as row 0. When paging, the first request does not specify offset; or equivalently, sets offset to 0; the first request returns the first `limit
  name: offset
  type: string
- description: Specifies how rows are ordered in the response.
  name: orderBys
  type: array
- description: A Google Analytics GA4 property identifier whose events are tracked. Specified in the URL path and not the body. To learn more, see [where to find your Property ID](https://developers.google.com/analy
  name: property
  type: string
- description: Toggles whether to return the current state of this Analytics Property's quota. Quota is returned in [PropertyQuota](#PropertyQuota).
  name: returnPropertyQuota
  type: boolean
provider_name: Google Analytics
provider_slug: google-analytics
schema_file: json-schema/data-api-run-report-request-schema.json
slug: data-api-run-report-request
tags:
- Analytics
- Data
- Google
- Metrics
- Reporting
- Web Analytics
- Machine Learning
- Attribution
title: RunReportRequest
---
