---
description: Detailed report information
layout: schema
name: ReportDetail
properties_list:
- description: Unique report identifier
  name: report_id
  type: string
- description: Report name
  name: name
  type: string
- description: Report processing status
  name: status
  type: string
- description: Report creation timestamp
  name: created_at
  type: string
- description: Report completion timestamp
  name: completed_at
  type: string
- description: Primary category for the report
  name: category
  type: string
- description: Type of report
  name: report_type
  type: string
- description: Number of data rows in completed report
  name: row_count
  type: integer
- description: Estimated completion time for processing reports
  name: estimated_completion
  type: string
provider_name: Circana
provider_slug: circana
schema_file: json-schema/liquid-data-report-detail-schema.json
slug: liquid-data-report-detail
tags:
- Analytics
- Consumer Data
- Market Research
- Retail
- CPG
- Point Of Sale
- Consumer Insights
- Business Intelligence
title: ReportDetail
---
