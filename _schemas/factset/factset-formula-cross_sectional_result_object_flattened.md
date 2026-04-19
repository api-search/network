---
description: Data model returned when the parameter **flatten=Y** is used in the request. This flattened, simplified JSON data returned from **flatten=Y** can be conceptualized as a table (rows and columns) where each data object in the result is a row in the table and the field names are the column names. There will be one data object for each request containing the request, fsymId if requested, and Key-Value pairs for each data item (formula).
layout: schema
name: cross_sectional_result_object_flattened
properties_list:
- description: Identifier requested.
  name: requestId
  type: string
- description: 'The **fsymId** field returned is the FactSet Default Permanent Identifier for the `requestId`. For all supported `requestId` symbol types, the `fsymId` parameter will return the Regional Level PermId '
  name: fsymId
  type: string
provider_name: Factset
provider_slug: factset
schema_file: json-schema/factset-formula-cross_sectional_result_object_flattened-schema.json
slug: factset-formula-cross_sectional_result_object_flattened
tags:
- Financial
- Financial Data
- Investment Analytics
- Market Data
- Portfolio Analytics
- Research
title: cross_sectional_result_object_flattened
---
