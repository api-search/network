---
description: An object returning the results for a single identifier and formula. This is the base of the response object. The result attribute depends on the formula requested. Response objects with the various result attribute types are outlined in separate schemas.
layout: schema
name: time_series_result_object_nonflattened_base
properties_list:
- description: Indicates that there was an error in the execution of the FQL Formula. * Zero success * Non-zero failure
  name: error
  type: integer
- description: If error is non-zero, errorMessage will display the FQL formula error.
  name: errorMessage
  type: string
- description: FQL formula requested.
  name: formula
  type: string
- description: Display Name.
  name: displayName
  type: string
- description: Identifier requested.
  name: requestId
  type: string
- description: 'The **fsymId** field returned is the FactSet Default Permanent Identifier for the `requestId`. For all supported `requestId` symbol types, the `fsymId` parameter will return the Regional Level PermId '
  name: fsymId
  type: string
- description: Type of data returned in `result`
  name: dataType
  type: string
- description: Type of object returned in `result`
  name: objectType
  type: string
provider_name: Factset
provider_slug: factset
schema_file: json-schema/factset-formula-time_series_result_object_nonflattened_base-schema.json
slug: factset-formula-time_series_result_object_nonflattened_base
tags:
- Financial
- Financial Data
- Investment Analytics
- Market Data
- Portfolio Analytics
- Research
title: time_series_result_object_nonflattened_base
---
