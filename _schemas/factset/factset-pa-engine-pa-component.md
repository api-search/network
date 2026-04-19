---
description: ''
layout: schema
name: PAComponent
properties_list:
- description: Component identifier.
  name: id
  type: string
- description: List of accounts saved in the PA document.
  name: accounts
  type: array
- description: List of benchmarks saved in the PA document.
  name: benchmarks
  type: array
- description: ''
  name: currencyisocode
  type: string
- description: Is the component type snapshot or subperiod.
  name: snapshot
  type: boolean
- description: The path to the document
  name: path
  type: string
- description: Component name.
  name: name
  type: string
- description: Component category.
  name: category
  type: string
provider_name: Factset
provider_slug: factset
schema_file: json-schema/factset-pa-engine-pa-component-schema.json
slug: factset-pa-engine-pa-component
tags:
- Financial
- Financial Data
- Investment Analytics
- Market Data
- Portfolio Analytics
- Research
title: PAComponent
---
