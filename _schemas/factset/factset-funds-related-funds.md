---
description: ''
layout: schema
name: relatedFunds
properties_list:
- description: FactSet Security Identifier. Six alpha-numeric characters, excluding vowels, with a -S suffix (XXXXXX-S), resolved from the requestId of the Fund requested.
  name: fsymId
  type: string
- description: The first related fund to the requestedId returned as a FactSet Permanent Security Identifier (XXXXXX-S).
  name: relatedFundIdOne
  type: string
- description: The second related fund to the requestedId returned as a FactSet Permanent Security Identifier (XXXXXX-S).
  name: relatedFundIdTwo
  type: string
- description: The third related fund to the requestedId returned as a FactSet Permanent Security Identifier (XXXXXX-S).
  name: relatedFundIdThree
  type: string
- description: The fourth related fund to the requestedId returned as a FactSet Permanent Security Identifier (XXXXXX-S).
  name: relatedFundIdFour
  type: string
- description: The fifth related fund to the requestedId returned as a FactSet Permanent Security Identifier (XXXXXX-S).
  name: relatedFundIdFive
  type: string
- description: The requested Id sent as input.
  name: requestId
  type: string
provider_name: Factset
provider_slug: factset
schema_file: json-schema/factset-funds-related-funds-schema.json
slug: factset-funds-related-funds
tags:
- Financial
- Financial Data
- Investment Analytics
- Market Data
- Portfolio Analytics
- Research
title: relatedFunds
---
