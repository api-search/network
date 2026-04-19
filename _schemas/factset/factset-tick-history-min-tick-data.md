---
description: Returns Tick History Response.
layout: schema
name: MinTickData
properties_list:
- description: Timestamp of when request was made
  name: requestTimestamp
  type: string
- description: Timestamp when the file was last updated
  name: updateTimestamp
  type: string
- description: Contains list of Files
  name: listOfFiles
  type: array
provider_name: Factset
provider_slug: factset
schema_file: json-schema/factset-tick-history-min-tick-data-schema.json
slug: factset-tick-history-min-tick-data
tags:
- Financial
- Financial Data
- Investment Analytics
- Market Data
- Portfolio Analytics
- Research
title: MinTickData
---
