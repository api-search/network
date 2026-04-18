---
description: Definition of an analytics report request
layout: schema
name: ReportRequest
properties_list:
- description: The report suite ID to run the report against
  name: rsid
  type: string
- description: Locale for response labels
  name: locale
  type: string
- description: List of global filters applied to the entire report
  name: globalFilters
  type: array
- description: Container defining the metrics to include in a report
  name: metricContainer
  type: object
- description: The primary dimension ID for the report (e.g. variables/page)
  name: dimension
  type: string
- description: Settings that control report output behavior
  name: settings
  type: object
- description: Statistical settings for the report
  name: statistics
  type: object
provider_name: Adobe Analytics
provider_slug: adobe-analytics
schema_file: json-schema/adobe-analytics-report-request-schema.json
slug: adobe-analytics-report-request
tags:
- Adobe
- Analytics
- Business Intelligence
- Customer Intelligence
- Digital Marketing
- Marketing
- Web Analytics
title: ReportRequest
---
