---
description: ''
layout: schema
name: UnlinkedPATemplateParameters
properties_list:
- description: The directory to create an unlinked PA template
  name: directory
  type: string
- description: Template type id
  name: templateTypeId
  type: string
- description: Template description
  name: description
  type: string
- description: List of accounts
  name: accounts
  type: array
- description: List of benchmarks
  name: benchmarks
  type: array
- description: List of columns for the PA calculation
  name: columns
  type: array
- description: List of groupings for the PA calculation
  name: groups
  type: array
- description: Currency ISO code for calculation.
  name: currencyisocode
  type: string
- description: PA storage type. It can be GROUPS or GROUPSALL or TOTALS or SECURITIES.
  name: componentdetail
  type: string
provider_name: Factset
provider_slug: factset
schema_file: json-schema/factset-pa-engine-unlinked-pa-template-parameters-schema.json
slug: factset-pa-engine-unlinked-pa-template-parameters
tags:
- Financial
- Financial Data
- Investment Analytics
- Market Data
- Portfolio Analytics
- Research
title: UnlinkedPATemplateParameters
---
