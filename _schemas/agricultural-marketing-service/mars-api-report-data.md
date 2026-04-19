---
description: Detailed commodity price and market data from a report.
layout: schema
name: Report Data
properties_list:
- description: Unique identifier for the report.
  name: slug_id
  type: string
- description: Name of the report.
  name: slug_name
  type: string
- description: Date the report data covers.
  name: report_date
  type: string
- description: Date the report was published.
  name: published_date
  type: string
- description: Agricultural commodity.
  name: commodity
  type: string
- description: Class or category within the commodity.
  name: class
  type: string
- description: Grade or quality designation.
  name: grade
  type: string
- description: Number of head (animals) in the report.
  name: head_count
  type: integer
- description: Price per hundredweight (CWT).
  name: price_per_cwt
  type: number
- description: Unit of price measurement.
  name: price_unit
  type: string
- description: Geographic region covered.
  name: region
  type: string
provider_name: Agricultural Marketing Service
provider_slug: agricultural-marketing-service
schema_file: json-schema/mars-api-report-data-schema.json
slug: mars-api-report-data
tags:
- Agriculture
- Federal Government
- Market News
- Livestock
- Dairy
- Fruits And Vegetables
- Cotton
- Tobacco
title: Report Data
---
