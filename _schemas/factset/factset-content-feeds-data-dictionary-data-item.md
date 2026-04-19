---
description: ''
layout: schema
name: DataItem
properties_list:
- description: Unique identifier for the data item
  name: id
  type: integer
- description: Name of the data item
  name: name
  type: string
- description: Description of the data item
  name: description
  type: string
- description: Flag indicating if the user is entitled to access the data in their subscriptions
  name: entitled
  type: boolean
- description: Flag indicating if this item is available in a data feed
  name: dataFeed
  type: boolean
- description: Flag indicating if this item is available in an api
  name: api
  type: boolean
- description: Flag indicating if this product is maintained by RDF/UCF
  name: referenceDataFeed
  type: boolean
provider_name: Factset
provider_slug: factset
schema_file: json-schema/factset-content-feeds-data-dictionary-data-item-schema.json
slug: factset-content-feeds-data-dictionary-data-item
tags:
- Financial
- Financial Data
- Investment Analytics
- Market Data
- Portfolio Analytics
- Research
title: DataItem
---
