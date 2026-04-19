---
description: ''
layout: schema
name: response_details
properties_list:
- description: Type of Asset Class
  name: index
  type: string
- description: Symbol is the only value that should be passed back to any FactSet services to retrieve data
  name: symbol
  type: string
- description: Name of the related entity
  name: name
  type: string
- description: Displays Entity ID's for public companies and only if the asset class is equities
  name: entity_id
  type: string
provider_name: Factset
provider_slug: factset
schema_file: json-schema/factset-id-lookup-response_details-schema.json
slug: factset-id-lookup-response_details
tags:
- Financial
- Financial Data
- Investment Analytics
- Market Data
- Portfolio Analytics
- Research
title: response_details
---
