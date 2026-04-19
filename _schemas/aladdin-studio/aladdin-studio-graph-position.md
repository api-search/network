---
description: A security position within a portfolio
layout: schema
name: Position
properties_list:
- description: Security identifier
  name: securityId
  type: string
- description: Security name
  name: securityName
  type: string
- description: Number of shares or units held
  name: quantity
  type: number
- description: Current market value in portfolio base currency
  name: marketValue
  type: number
- description: Portfolio weight as decimal
  name: weight
  type: number
- description: Security trading currency
  name: currency
  type: string
- description: Asset class classification
  name: assetClass
  type: string
- description: GICS sector
  name: sector
  type: string
provider_name: Aladdin Studio
provider_slug: aladdin-studio
schema_file: json-schema/aladdin-studio-graph-position-schema.json
slug: aladdin-studio-graph-position
tags:
- Financial
- Investment Management
- Portfolio Analytics
- Risk Management
- Asset Management
- BlackRock
- Data Cloud
title: Position
---
