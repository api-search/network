---
description: Historical Identifier Resolution data object.
layout: schema
name: identifierResolutionHistorical
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
- description: Type of identifier outputted.
  name: outputType
  type: string
- description: Requested identifier.
  name: value
  type: string
- description: Start Date in YYYY-MM-DD format.
  name: startDate
  type: string
- description: End Date in YYYY-MM-DD format.
  name: endDate
  type: string
provider_name: Factset
provider_slug: factset
schema_file: json-schema/factset-symbology-identifier-resolution-historical-schema.json
slug: factset-symbology-identifier-resolution-historical
tags:
- Financial
- Financial Data
- Investment Analytics
- Market Data
- Portfolio Analytics
- Research
title: identifierResolutionHistorical
---
