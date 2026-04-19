---
description: ''
layout: schema
name: errorResponse
properties_list:
- description: status
  name: status
  type: string
- description: timestamp in YYYY-MM-DD HH:MM:SS.SSS
  name: timestamp
  type: string
- description: The Endpoint path {package}/version/{endpoint}
  name: path
  type: string
- description: The plain text error message
  name: message
  type: string
- description: subErrors related to the error message. Null if not applicable.
  name: subErrors
  type: object
provider_name: Factset
provider_slug: factset
schema_file: json-schema/factset-esg-error-response-schema.json
slug: factset-esg-error-response
tags:
- Financial
- Financial Data
- Investment Analytics
- Market Data
- Portfolio Analytics
- Research
title: errorResponse
---
