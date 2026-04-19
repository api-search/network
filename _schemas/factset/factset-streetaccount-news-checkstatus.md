---
description: ''
layout: schema
name: checkstatus
properties_list:
- description: Defines the name of the product
  name: product
  type: string
- description: Unique id to get the xml files for the requested date
  name: jobID
  type: string
- description: Returns any of the 2 results Submitted ->Running->Completed and Failed
  name: status
  type: string
- description: Returns how much percentage of task is completed for the requested jobID
  name: percentDone
  type: integer
- description: The date from which the data is required in YYYY-MM-DDTHH:MM:SSZ format
  name: startDate
  type: string
- description: The date until which the data is fetched in YYYY-MM-DDTHH:MM:SSZ format
  name: endDate
  type: string
- description: Returns the part number of the jobID
  name: part
  type: integer
provider_name: Factset
provider_slug: factset
schema_file: json-schema/factset-streetaccount-news-checkstatus-schema.json
slug: factset-streetaccount-news-checkstatus
tags:
- Financial
- Financial Data
- Investment Analytics
- Market Data
- Portfolio Analytics
- Research
title: checkstatus
---
