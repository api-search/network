---
description: Metadata for a single available fundamental metric including its category, data type, and documentation reference.
layout: schema
name: Metric
properties_list:
- description: Metric identifier to be used as input in the metrics parameter.
  name: metric
  type: '[''string'', ''null'']'
- description: Plain text name of the metric.
  name: name
  type: '[''string'', ''null'']'
- description: Primary category such as INCOME_STATEMENT, BALANCE_SHEET, CASH_FLOW, or RATIOS.
  name: category
  type: '[''string'', ''null'']'
- description: Sub-category such as ASSETS, SUPPLEMENTAL, SHAREHOLDERS_EQUITY, VALUATION, PROFITABILITY, etc.
  name: subcategory
  type: '[''string'', ''null'']'
- description: Online Assistant Page ID in D***** format for methodology lookup.
  name: oaPageId
  type: '[''string'', ''null'']'
- description: Online Assistant URL for methodology definitions.
  name: oaUrl
  type: '[''string'', ''null'']'
- description: The factor for the metric (e.g. 1000000 = millions).
  name: factor
  type: '[''integer'', ''null'']'
- description: Standard Data Feed package availability. BASIC or ADVANCED. Null indicates API-only availability.
  name: sdfPackage
  type: '[''string'', ''null'']'
- description: The data type for the metric (date, doubleArray, float, floatArray, intArray, string, stringArray).
  name: dataType
  type: '[''string'', ''null'']'
provider_name: Factset
provider_slug: factset
schema_file: json-schema/factset-fundamentals-metric-schema.json
slug: factset-fundamentals-metric
tags:
- Financial
- Financial Data
- Investment Analytics
- Market Data
- Portfolio Analytics
- Research
title: Metric
---
