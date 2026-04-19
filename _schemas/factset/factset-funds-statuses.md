---
description: ''
layout: schema
name: statuses
properties_list:
- description: FactSet Security Identifier. Six alpha-numeric characters, excluding vowels, with a -S suffix (XXXXXX-S), resolved from the requestId of the Fund requested.
  name: fsymId
  type: string
- description: Binary flag to indicate whether the fund is currently active, where 1 is active and 0 is inactive.
  name: activeFlag
  type: integer
- description: Returns a binary indicator of whether the specified share class is currently active, where 1 is active and 0 is inactive.
  name: shrClassActiveFlag
  type: integer
- description: Returns a binary indicator of whether the specified fund is available in the FactSet Funds Database (FFD).
  name: isonFFD
  type: integer
- description: The requested Id sent as input.
  name: requestId
  type: string
provider_name: Factset
provider_slug: factset
schema_file: json-schema/factset-funds-statuses-schema.json
slug: factset-funds-statuses
tags:
- Financial
- Financial Data
- Investment Analytics
- Market Data
- Portfolio Analytics
- Research
title: statuses
---
