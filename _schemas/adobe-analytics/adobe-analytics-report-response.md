---
description: The result of an analytics report request
layout: schema
name: ReportResponse
properties_list:
- description: Total number of result pages
  name: totalPages
  type: integer
- description: Number of rows in this response
  name: numberOfElements
  type: integer
- description: ''
  name: rows
  type: array
- description: Column metadata for the report
  name: columns
  type: object
- description: Totals and summary statistics
  name: summaryData
  type: object
provider_name: Adobe Analytics
provider_slug: adobe-analytics
schema_file: json-schema/adobe-analytics-report-response-schema.json
slug: adobe-analytics-report-response
tags:
- Adobe
- Analytics
- Business Intelligence
- Customer Intelligence
- Digital Marketing
- Marketing
- Web Analytics
title: ReportResponse
---
