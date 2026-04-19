---
description: Set a value or values for a custom field identified by the field 'Code'. Only one of the fields (IntegerValue / TextValue / FilePathValue etc) will be used, depending on the data type of the custom field corresponding to the 'Code' provided
layout: schema
name: CreateCustomFieldValueDto
properties_list:
- description: ''
  name: code
  type: string
- description: ''
  name: integerValue
  type: integer
- description: ''
  name: textValue
  type: string
- description: ''
  name: filePathValue
  type: string
- description: ''
  name: numericValue
  type: number
- description: ''
  name: dateValue
  type: string
- description: ''
  name: extendedTextValue
  type: string
- description: ''
  name: contactLookupValues
  type: array
- description: ''
  name: optionValue
  type: string
- description: ''
  name: optionValues
  type: array
provider_name: Factset
provider_slug: factset
schema_file: json-schema/factset-irn-notes-create-custom-field-value-dto-schema.json
slug: factset-irn-notes-create-custom-field-value-dto
tags:
- Financial
- Financial Data
- Investment Analytics
- Market Data
- Portfolio Analytics
- Research
title: CreateCustomFieldValueDto
---
