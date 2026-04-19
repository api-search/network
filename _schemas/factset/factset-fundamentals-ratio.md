---
description: A single pre-calculated financial ratio for a security and fiscal period.
layout: schema
name: Ratio
properties_list:
- description: Identifier that was used for the request.
  name: requestId
  type: string
- description: FactSet Regional Security Identifier.
  name: fsymId
  type: '[''string'', ''null'']'
- description: The ratio metric identifier.
  name: metric
  type: '[''string'', ''null'']'
- description: Periodicity of the fiscal period.
  name: periodicity
  type: '[''string'', ''null'']'
- description: Fiscal period indicator.
  name: fiscalPeriod
  type: '[''integer'', ''null'']'
- description: Fiscal year in YYYY format.
  name: fiscalYear
  type: '[''integer'', ''null'']'
- description: The normalized date the fiscal period ended.
  name: fiscalEndDate
  type: '[''string'', ''null'']'
- description: ISO 4217 currency code.
  name: currency
  type: '[''string'', ''null'']'
- description: The calculated ratio value.
  name: value
  type: '[''number'', ''null'']'
provider_name: Factset
provider_slug: factset
schema_file: json-schema/factset-fundamentals-ratio-schema.json
slug: factset-fundamentals-ratio
tags:
- Financial
- Financial Data
- Investment Analytics
- Market Data
- Portfolio Analytics
- Research
title: Ratio
---
