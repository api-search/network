---
description: ''
layout: schema
name: TableField
properties_list:
- description: Unique identifier for a combination of table and data field
  name: id
  type: string
- description: Unique identifier for the data item
  name: dataItemId
  type: string
- description: Name of the data field
  name: name
  type: string
- description: Data type of the data field
  name: dataType
  type: string
- description: Column position of the data field within the table
  name: position
  type: integer
- description: Flag indicating if the data field is a primary key.
  name: isPrimaryKey
  type: boolean
- description: Flag indicating if a data field is nullable
  name: nullable
  type: boolean
- description: Flag indicating if the field's value is determined by a code value in its row. The monetary, splitAffected and unitFactor fields for that value will also be inherited from the code.
  name: hasCodeDependency
  type: boolean
- description: Flag indicating if the data field contained in this TableField is monetary. If true, this field can have exchange rates applied to convert to other currencies
  name: monetary
  type: boolean
- description: Flag indicating if the data field contained in this TableField can be affected by splits
  name: splitAffected
  type: boolean
- description: Factor to indicate what units that the data field is displayed in. If null, the field does not need to have a factor applied to obtain the real value
  name: unitFactor
  type: string
- description: A description of the data field within the context of its table
  name: description
  type: string
provider_name: Factset
provider_slug: factset
schema_file: json-schema/factset-content-feeds-data-dictionary-table-field-schema.json
slug: factset-content-feeds-data-dictionary-table-field
tags:
- Financial
- Financial Data
- Investment Analytics
- Market Data
- Portfolio Analytics
- Research
title: TableField
---
