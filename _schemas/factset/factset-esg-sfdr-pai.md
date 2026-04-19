---
description: ''
layout: schema
name: sfdrPai
properties_list:
- description: FactSet Entity Identifier. Six alpha-numeric characters, excluding vowels, with a -E suffix (XXXXXX-E).
  name: fsymId
  type: string
- description: Identifier that was used for the request.
  name: requestId
  type: string
- description: Codes for the General, Mandatory and Additional PAI indicators
  name: subTopicCode
  type: string
- description: Names for the General, Mandatory and Additional PAI indicators
  name: subTopicName
  type: string
- description: The type of indicator - General, Additional & Mandatory
  name: indicatorType
  type: string
- description: The Reporting period end date expressed in YYYY-MM-DD format
  name: periodEndDate
  type: string
- description: The reporting period of the company expressed in YYYY format
  name: reportingPeriod
  type: string
- description: The units of measurements for the indicators
  name: standardizedUnit
  type: string
- description: The PAI calculations based on the company-reported data, some metrics sourced from Factset Databases and Truvalue SASB Spotlights
  name: standardizedValue
  type: string
provider_name: Factset
provider_slug: factset
schema_file: json-schema/factset-esg-sfdr-pai-schema.json
slug: factset-esg-sfdr-pai
tags:
- Financial
- Financial Data
- Investment Analytics
- Market Data
- Portfolio Analytics
- Research
title: sfdrPai
---
