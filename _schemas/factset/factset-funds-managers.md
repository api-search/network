---
description: ''
layout: schema
name: managers
properties_list:
- description: FactSet Security Identifier. Six alpha-numeric characters, excluding vowels, with a -S suffix (XXXXXX-S), resolved from the requestId of the Fund requested.
  name: fsymId
  type: string
- description: Proper Name of the Fund Manager
  name: managerName
  type: string
- description: Proper Title of the Fund Manager
  name: managerTitle
  type: string
- description: Phone Number of the Fund Manager
  name: managerPhone
  type: string
- description: Inception Date of the Fund Manager
  name: managerInceptionDate
  type: string
- description: Job Identifier for the Fund Manager
  name: managerJobId
  type: integer
- description: The requested Id sent as input.
  name: requestId
  type: string
provider_name: Factset
provider_slug: factset
schema_file: json-schema/factset-funds-managers-schema.json
slug: factset-funds-managers
tags:
- Financial
- Financial Data
- Investment Analytics
- Market Data
- Portfolio Analytics
- Research
title: managers
---
