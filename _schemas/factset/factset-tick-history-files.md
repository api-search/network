---
description: Array of data objects
layout: schema
name: files
properties_list:
- description: Name of the file(s) generated for the query requested
  name: fileName
  type: string
- description: Download link for the TickHistory file with requested parameters <p>This download link will expire after 24 hours</p>
  name: url
  type: string
provider_name: Factset
provider_slug: factset
schema_file: json-schema/factset-tick-history-files-schema.json
slug: factset-tick-history-files
tags:
- Financial
- Financial Data
- Investment Analytics
- Market Data
- Portfolio Analytics
- Research
title: files
---
