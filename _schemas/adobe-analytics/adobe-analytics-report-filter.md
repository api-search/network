---
description: A filter applied to a report
layout: schema
name: ReportFilter
properties_list:
- description: Filter type
  name: type
  type: string
- description: ISO 8601 date range (e.g. 2024-01-01T00:00:00/2024-01-31T23:59:59)
  name: dateRange
  type: string
- description: ID of an existing segment to apply as a filter
  name: segmentId
  type: string
- description: Dimension for breakdown filter
  name: dimension
  type: string
- description: Dimension item ID for breakdown filter
  name: itemId
  type: string
provider_name: Adobe Analytics
provider_slug: adobe-analytics
schema_file: json-schema/adobe-analytics-report-filter-schema.json
slug: adobe-analytics-report-filter
tags:
- Adobe
- Analytics
- Business Intelligence
- Customer Intelligence
- Digital Marketing
- Marketing
- Web Analytics
title: ReportFilter
---
