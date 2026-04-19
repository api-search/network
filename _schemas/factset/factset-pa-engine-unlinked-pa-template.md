---
description: ''
layout: schema
name: UnlinkedPATemplate
properties_list:
- description: Template id.
  name: id
  type: string
- description: Template directory.
  name: directory
  type: string
- description: Template type id
  name: templateTypeId
  type: string
- description: snapshot.
  name: snapshot
  type: boolean
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
- description: Template description.
  name: description
  type: string
- description: Template name.
  name: name
  type: string
- description: Unlinked template category
  name: category
  type: string
provider_name: Factset
provider_slug: factset
schema_file: json-schema/factset-pa-engine-unlinked-pa-template-schema.json
slug: factset-pa-engine-unlinked-pa-template
tags:
- Financial
- Financial Data
- Investment Analytics
- Market Data
- Portfolio Analytics
- Research
title: UnlinkedPATemplate
---
