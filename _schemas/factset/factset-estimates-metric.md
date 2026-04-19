---
description: ''
layout: schema
name: metric
properties_list:
- description: Metric identifier to be used as `metrics` input in the FactSet Estimate endpoints.
  name: metric
  type: string
- description: Plain text name of the metric.
  name: name
  type: string
- description: Primary Category of metric item, such as, FINANCIAL_STATEMENT or INDUSTRY_METRIC
  name: category
  type: string
- description: Sub-category of metric items, such as the INCOME_STATEMENT or AIRLINES.
  name: subcategory
  type: string
- description: The Online Assistant Page URL, used to lookup the definition and methodology of the requested item.
  name: OAurl
  type: string
provider_name: Factset
provider_slug: factset
schema_file: json-schema/factset-estimates-metric-schema.json
slug: factset-estimates-metric
tags:
- Financial
- Financial Data
- Investment Analytics
- Market Data
- Portfolio Analytics
- Research
title: metric
---
