---
description: A USDA AMS market news report entry.
layout: schema
name: Report
properties_list:
- description: Unique identifier for the report.
  name: slug_id
  type: string
- description: Unique name for the report.
  name: slug_name
  type: string
- description: Date the report data covers.
  name: report_date
  type: string
- description: Date and time the report was published.
  name: published_date
  type: string
- description: Agricultural commodity covered by the report.
  name: commodity
  type: string
- description: Type of market covered (Weekly Summary, Daily, etc.).
  name: market_type
  type: string
- description: USDA AMS office that published the report.
  name: office
  type: string
- description: Section name within the report.
  name: section_name
  type: string
provider_name: Agricultural Marketing Service
provider_slug: agricultural-marketing-service
schema_file: json-schema/mars-api-report-schema.json
slug: mars-api-report
tags:
- Agriculture
- Federal Government
- Market News
- Livestock
- Dairy
- Fruits And Vegetables
- Cotton
- Tobacco
title: Report
---
