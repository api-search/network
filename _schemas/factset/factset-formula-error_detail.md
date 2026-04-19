---
description: '`Error Object` is the response returned for an unsuccessful request.'
layout: schema
name: error_detail
properties_list:
- description: Unique identifier for the request. Also known as the chain id.
  name: id
  type: string
- description: Textual error code
  name: code
  type: string
- description: A short, human-readable summary of the problem
  name: title
  type: string
- description: timestamp in YYYY-MM-DD HH:MM:SS.SSS
  name: timestamp
  type: string
provider_name: Factset
provider_slug: factset
schema_file: json-schema/factset-formula-error_detail-schema.json
slug: factset-formula-error_detail
tags:
- Financial
- Financial Data
- Investment Analytics
- Market Data
- Portfolio Analytics
- Research
title: error_detail
---
