---
description: ''
layout: schema
name: gics
properties_list:
- description: FactSet Entity Identifier by default, otherwise returns FactSet Regional Identifier. This is a six alpha-numeric characters, excluding vowels, with an -E suffix (XXXXXX-E).
  name: fsymId
  type: string
- description: Date in YYYY-MM-DD for the classification record from GICS Direct
  name: date
  type: string
- description: GICS Sector Name in Proper Format.
  name: gicsSectorName
  type: string
- description: GICS Sector Number
  name: gicsSectorNumber
  type: string
- description: GICS Industry Group Name in Proper Format.
  name: gicsIndustryGroupName
  type: string
- description: GICS Industry Group Number
  name: gicsIndustryGroupNumber
  type: string
- description: GICS Industry Name in Proper Format.
  name: gicsIndustryName
  type: string
- description: GICS Industry Number
  name: gicsIndustryNumber
  type: string
- description: GICS Sub-Industry Name in Proper Format.
  name: gicsSubIndustryName
  type: string
- description: GICS Industry Number.
  name: gicsSubIndustryNumber
  type: string
- description: Identifier specified in the request
  name: requestId
  type: string
provider_name: Factset
provider_slug: factset
schema_file: json-schema/factset-classifications-gics-schema.json
slug: factset-classifications-gics
tags:
- Financial
- Financial Data
- Investment Analytics
- Market Data
- Portfolio Analytics
- Research
title: gics
---
