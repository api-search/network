---
description: ''
layout: schema
name: getfiles
properties_list:
- description: Defines the name of the product
  name: product
  type: string
- description: The startDate from which the data is required in YYYY-MM-DDTHH:MM:SSZ format
  name: startDate
  type: string
- description: The endDate until which the data is fetched in YYYY-MM-DDTHH:MM:SSZ format
  name: endDate
  type: string
- description: Unique id to get the xml files for the requested date
  name: jobID
  type: string
- description: Defines the status of the request
  name: status
  type: string
- description: Link to download the zip file which contains xml files
  name: url
  type: string
- description: Returns the part number of the jobID
  name: part
  type: integer
provider_name: Factset
provider_slug: factset
schema_file: json-schema/factset-streetaccount-news-getfiles-schema.json
slug: factset-streetaccount-news-getfiles
tags:
- Financial
- Financial Data
- Investment Analytics
- Market Data
- Portfolio Analytics
- Research
title: getfiles
---
