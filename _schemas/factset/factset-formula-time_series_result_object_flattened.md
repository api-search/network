---
description: 'Data model returned when the parameter **flatten=Y** is used in the request. This flattened, simplified JSON output returned from **flatten=Y** can be conceptualized as a table (rows and columns) where each data object in the result is a row in the table and each field names is a column name. The response will contain at least one data object for each requestId containing the requestId, fsymId (if requested), date (if applicable) and Key-Value pairs for each data item (formula). The number of data objects (rows) per requestId is dependent the the objectTypes of the formulas requested. Formulas that have associated dates (TIMESERIES objectType in the standard **flatten=N** response model) will result in a data object for each date for each requestId. **flatten=N TIMESERIES Representation** ```json [ { "requestId": "id", "formula": "formulaName1", "result": { "values": [a,b], "dates": [DATE1,DATE2] }, "objectType": "TIMESERIES", "dataType": "DOUBLE" }, { "requestId": "id", "formula":
  "formulaName2", "result": { "values": [c,d], "dates": [DATE2,DATE3] }, "objectType": "TIMESERIES", "dataType": "DOUBLE" } ] ``` **flatten=Y TIMESERIES Representation** ```json [ { "requestId": "id", "formulaName1": a, "formulaName2": null, "date": DATE1 }, { "requestId": "id", "formulaName1": b, "formulaName2": c, "date": DATE2 }, { "requestId": "id", "formulaName1": null, "formulaName2": d, "date": DATE3 } ] ``` Formulas that result in an array (no associated dates, ARRAY objectType in the standard **flatten=N** response model) can be thought of as a column in a table. Each element in the array will be in a separate data object. The first element of the array starts in the first data object for that requestId and then then the second element of the array in the second data object for that requestId and so on (regardless of dates from other formulas). **flatten=N ARRAY Representation** ```json [ { "requestId": "id", "formula": "formulaName", "result": [a,b,c], "objectType": "ARRAY", "dataType":
  "DOUBLE" } ] ``` **flatten=Y ARRAY Representation** ```json [ { "requestId": "id", "formulaName": a, }, { "requestId": "id", "formulaName": b, }, { "requestId": "id", "formulaName": c, } ] ``` Scalar data items (SCALAR objectType in the standard **flatten=N** response model) will be repeated in each data object for the requestId. **flatten=N SCALAR Representation** ```json [ { "requestId": "id", "formula": "formulaName", "result": a, "objectType": "ARRAY", "dataType": "DOUBLE" } ] ``` **flatten=Y SCALAR Representation** ```json [ { "requestId": "id", "formulaName": a, } ] ``` Formulas that result in a matrix (2 dimensional array, MATRIX objectType in the standard **flatten=N** response model) can be thought of as returning a table where each array in the array of arrays is a row in the table. This can be extended to the flattened result structure where each data object is a row in a table. The formula will have as many attributes (appended by [n]) as number of columns in the matrix result.
  **flatten=N MATRIX Representation** ```json [ { "requestId": "id" "formula": "formulaName", "result": [ [a,b,c], [d,e,f] ], "objectType": "MATRIX", "dataType": "DOUBLE" } ] ``` **flatten=Y MATRIX Representation** ```json [ { "requestId": "id" "formulaName[0]": a, "formulaName[1]": b, "formulaName[2]": c }, { "requestId": "id" "formulaName[0]": d, "formulaName[1]": e, "formulaName[2]": f } ] ```'
layout: schema
name: time_series_result_object_flattened
properties_list:
- description: Identifier requested.
  name: requestId
  type: string
- description: 'The **fsymId** field returned is the FactSet Default Permanent Identifier for the `requestId`. For all supported `requestId` symbol types, the `fsymId` parameter will return the Regional Level PermId '
  name: fsymId
  type: string
- description: Date associated with FQL formula.
  name: date
  type: string
provider_name: Factset
provider_slug: factset
schema_file: json-schema/factset-formula-time_series_result_object_flattened-schema.json
slug: factset-formula-time_series_result_object_flattened
tags:
- Financial
- Financial Data
- Investment Analytics
- Market Data
- Portfolio Analytics
- Research
title: time_series_result_object_flattened
---
