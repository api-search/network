---
description: ''
layout: schema
name: sasbRanks
properties_list:
- description: Date for the period requested expressed in YYYY-MM-DD format.
  name: date
  type: string
- description: FactSet Entity Identifier. Six alpha-numeric characters, excluding vowels, with a -E suffix (XXXXXX-E).
  name: fsymId
  type: string
- description: Identifier that was used for the request.
  name: requestId
  type: string
- description: The specific SASB 'category' the Rank is referring to.
  name: sasbCategory
  type: string
- description: The SASB Rank for the given category in Proper format. |Rank|Industry Percentile Range (%)| ||| |Leader|90 - 100| |Above Average|70 - 89.9| |Average|30 - 69.9| |Below Average|10 - 29.9| |Laggard|0 - 9
  name: sasbRank
  type: string
provider_name: Factset
provider_slug: factset
schema_file: json-schema/factset-esg-sasb-ranks-schema.json
slug: factset-esg-sasb-ranks
tags:
- Financial
- Financial Data
- Investment Analytics
- Market Data
- Portfolio Analytics
- Research
title: sasbRanks
---
