---
description: Represents a cell range in a worksheet.
layout: schema
name: Range
properties_list:
- description: Range reference in A1-style notation.
  name: address
  type: string
- description: Range reference in locale-specific notation.
  name: addressLocal
  type: string
- description: Number of cells in the range.
  name: cellCount
  type: integer
- description: Number of columns.
  name: columnCount
  type: integer
- description: Column number of the first cell.
  name: columnIndex
  type: integer
- description: Number of rows.
  name: rowCount
  type: integer
- description: Row number of the first cell.
  name: rowIndex
  type: integer
- description: Whether the range is hidden.
  name: hidden
  type: boolean
- description: Formulas in A1-style notation.
  name: formulas
  type: array
- description: Raw values of the range.
  name: values
  type: array
- description: Text values of the range.
  name: text
  type: array
- description: Number format codes.
  name: numberFormat
  type: array
- description: Type of data in each cell.
  name: valueTypes
  type: array
provider_name: Microsoft Excel
provider_slug: microsoft-excel
schema_file: json-schema/excel-graph-api-range-schema.json
slug: excel-graph-api-range
tags:
- Automation
- Data Analysis
- Microsoft
- Microsoft 365
- Office
- Spreadsheets
title: Range
---
