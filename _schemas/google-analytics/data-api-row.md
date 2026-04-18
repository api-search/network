---
description: 'Report data for each row. For example if RunReportRequest contains: ```none "dimensions": [ { "name": "eventName" }, { "name": "countryId" } ], "metrics": [ { "name": "eventCount" } ] ``` One row with ''in_app_purchase'' as the eventName, ''JP'' as the countryId, and 15 as the eventCount, would be: ```none "dimensionValues": [ { "value": "in_app_purchase" }, { "value": "JP" } ], "metricValues": [ { "value": "15" } ] ```'
layout: schema
name: Row
properties_list:
- description: List of requested dimension values. In a PivotReport, dimension_values are only listed for dimensions included in a pivot.
  name: dimensionValues
  type: array
- description: List of requested visible metric values.
  name: metricValues
  type: array
provider_name: Google Analytics
provider_slug: google-analytics
schema_file: json-schema/data-api-row-schema.json
slug: data-api-row
tags:
- Analytics
- Data
- Google
- Metrics
- Reporting
- Web Analytics
- Machine Learning
- Attribution
title: Row
---
