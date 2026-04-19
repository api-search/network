---
description: Identifier Resolution data object.
layout: schema
name: identifierResolution
properties_list:
- description: Identifier inputted in the request.
  name: requestId
  type: string
- description: The type of identifier inputted in the request
  name: inputSymbolType
  type: string
- description: Name of the requested identifier
  name: name
  type: string
- description: The 3 digit fref exchange code for the primary exchange of the security
  name: frefListingExchange
  type: string
- description: The 3 digit ISO code for the currency
  name: currency
  type: string
provider_name: Factset
provider_slug: factset
schema_file: json-schema/factset-symbology-identifier-resolution-schema.json
slug: factset-symbology-identifier-resolution
tags:
- Financial
- Financial Data
- Investment Analytics
- Market Data
- Portfolio Analytics
- Research
title: identifierResolution
---
