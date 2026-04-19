---
description: Returns Tick History Files
layout: schema
name: TickDataLevel2
properties_list:
- description: The status of the request
  name: status
  type: string
- description: Timestamp of when request was made
  name: requestTimestamp
  type: string
- description: :"Timestamp when the file was last updated"
  name: updateTimestamp
  type: string
- description: Data Object
  name: listOfFiles
  type: array
provider_name: Factset
provider_slug: factset
schema_file: json-schema/factset-tick-history-tick-data-level2-schema.json
slug: factset-tick-history-tick-data-level2
tags:
- Financial
- Financial Data
- Investment Analytics
- Market Data
- Portfolio Analytics
- Research
title: TickDataLevel2
---
