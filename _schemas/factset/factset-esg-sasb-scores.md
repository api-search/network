---
description: ''
layout: schema
name: sasbScores
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
- description: The specific SASB 'category' the score is referring to.
  name: sasbCategory
  type: string
- description: The SASB Score value for the given 'scoreType' and 'category'. When scoreType = ESG_RANK, the data type will be string, otherwise data type will be a number with double format.
  name: sasbScore
  type: object
- description: 'The name of the specific SASB Score type being shown in the response. This will be represented by the scoreTypes input: PULSE, INSIGHT, MOMENTUM, ART_VOL_TTM, CAT_VOL_TTM, or DYNAMIC_MAT.'
  name: scoreType
  type: string
provider_name: Factset
provider_slug: factset
schema_file: json-schema/factset-esg-sasb-scores-schema.json
slug: factset-esg-sasb-scores
tags:
- Financial
- Financial Data
- Investment Analytics
- Market Data
- Portfolio Analytics
- Research
title: sasbScores
---
