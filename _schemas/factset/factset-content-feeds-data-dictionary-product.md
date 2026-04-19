---
description: ''
layout: schema
name: Product
properties_list:
- description: Unique identifier for the product
  name: id
  type: string
- description: Name of the product
  name: name
  type: string
- description: URL to the product page on the Open:FactSet Marketplace
  name: ofmLink
  type: string
- description: The id defining a product in the Open:FactSet Marketplace
  name: ofmProductId
  type: string
- description: Flag indicating if the user is entitled to access the data in their subscriptions
  name: entitled
  type: boolean
- description: Name of the Data Provider for the product
  name: providerName
  type: string
- description: Flag indicating if this product is available in a data feed
  name: dataFeed
  type: boolean
- description: Flag indicating if this product is available in an api
  name: api
  type: boolean
- description: Flag indicating if this product is maintained by RDF/UCF
  name: referenceDataFeed
  type: boolean
provider_name: Factset
provider_slug: factset
schema_file: json-schema/factset-content-feeds-data-dictionary-product-schema.json
slug: factset-content-feeds-data-dictionary-product
tags:
- Financial
- Financial Data
- Investment Analytics
- Market Data
- Portfolio Analytics
- Research
title: Product
---
