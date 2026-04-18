---
description: Describes the visible dimension columns and rows in the report response.
layout: schema
name: Pivot
properties_list:
- description: Dimension names for visible columns in the report response. Including "dateRange" produces a date range column; for each row in the response, dimension values in the date range column will indicate th
  name: fieldNames
  type: array
- description: The number of unique combinations of dimension values to return in this pivot. The `limit` parameter is required. A `limit` of 10,000 is common for single pivot requests. The product of the `limit` fo
  name: limit
  type: string
- description: Aggregate the metrics by dimensions in this pivot using the specified metric_aggregations.
  name: metricAggregations
  type: array
- description: The row count of the start row. The first row is counted as row 0.
  name: offset
  type: string
- description: Specifies how dimensions are ordered in the pivot. In the first Pivot, the OrderBys determine Row and PivotDimensionHeader ordering; in subsequent Pivots, the OrderBys determine only PivotDimensionHea
  name: orderBys
  type: array
provider_name: Google Analytics
provider_slug: google-analytics
schema_file: json-schema/data-api-pivot-schema.json
slug: data-api-pivot
tags:
- Analytics
- Data
- Google
- Metrics
- Reporting
- Web Analytics
- Machine Learning
- Attribution
title: Pivot
---
