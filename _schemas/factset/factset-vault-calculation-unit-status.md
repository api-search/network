---
description: ''
layout: schema
name: CalculationUnitStatus
properties_list:
- description: The status of calculation unit.
  name: status
  type: string
- description: The error in a calculation unit.
  name: errors
  type: array
- description: The result URL of the calculation.
  name: result
  type: string
- description: The progress of the calculation unit.
  name: progress
  type: string
- description: The points for the calculation unit.
  name: points
  type: integer
- description: The warnings in a calculation unit.
  name: warnings
  type: array
provider_name: Factset
provider_slug: factset
schema_file: json-schema/factset-vault-calculation-unit-status-schema.json
slug: factset-vault-calculation-unit-status
tags:
- Financial
- Financial Data
- Investment Analytics
- Market Data
- Portfolio Analytics
- Research
title: CalculationUnitStatus
---
