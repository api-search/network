---
description: ''
layout: schema
name: sdgScores
properties_list:
- description: Ending date for the period requested expressed in YYYY-MM-DD format.
  name: date
  type: string
- description: FactSet Entity Identifier. Six alpha-numeric characters, excluding vowels, with a -E suffix (XXXXXX-E).
  name: fsymId
  type: string
- description: Identifier that was used for the request.
  name: requestId
  type: string
- description: 'The name of the specific SDG Score type being shown in the response. This will be represented by the scoreTypes input: PULSE, INSIGHT, MOMENTUM, ART_VOL_TTM, CAT_VOL_TTM, or DYNAMIC_MAT.'
  name: scoreType
  type: string
provider_name: Factset
provider_slug: factset
schema_file: json-schema/factset-esg-sdg-scores-schema.json
slug: factset-esg-sdg-scores
tags:
- Financial
- Financial Data
- Investment Analytics
- Market Data
- Portfolio Analytics
- Research
title: sdgScores
---
