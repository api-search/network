---
description: ''
layout: schema
name: batchErrorObject
properties_list:
- description: A UUID for this particular occurrence of the problem.
  name: id
  type: string
- description: status
  name: code
  type: string
- description: The Endpoint path {package}/version/{endpoint}
  name: links
  type: object
- description: The plain text error message
  name: title
  type: string
provider_name: Factset
provider_slug: factset
schema_file: json-schema/factset-global-prices-batch-error-object-schema.json
slug: factset-global-prices-batch-error-object
tags:
- Financial
- Financial Data
- Investment Analytics
- Market Data
- Portfolio Analytics
- Research
title: batchErrorObject
---
