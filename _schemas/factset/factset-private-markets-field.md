---
description: ''
layout: schema
name: field
properties_list:
- description: Data item to be used as `fields` input in `/factset-private-markets/v#/` endpoint.
  name: field
  type: string
- description: Plain text name of the field.
  name: name
  type: string
- description: 'Corresponding endpoint to input field item. For example, fields returning the category ''FINANCIALS'' should be used in the /financials endpoint. The same follows data items falling in the category for '
  name: category
  type: string
- description: The factor for the field (e.g. 1000 = thousands).
  name: factor
  type: integer
- description: The name of the data item as it appears in the Standard Data Feed (SDF). A null value represents items available only in API.
  name: sdfName
  type: string
provider_name: Factset
provider_slug: factset
schema_file: json-schema/factset-private-markets-field-schema.json
slug: factset-private-markets-field
tags:
- Financial
- Financial Data
- Investment Analytics
- Market Data
- Portfolio Analytics
- Research
title: field
---
