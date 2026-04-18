---
description: Represents a column in an Excel table.
layout: schema
name: TableColumn
properties_list:
- description: Unique identifier for the column.
  name: id
  type: string
- description: Zero-based index of the column.
  name: index
  type: integer
- description: The name of the column.
  name: name
  type: string
- description: Raw values of the column.
  name: values
  type: array
provider_name: Microsoft Excel
provider_slug: microsoft-excel
schema_file: json-schema/excel-graph-api-table-column-schema.json
slug: excel-graph-api-table-column
tags:
- Automation
- Data Analysis
- Microsoft
- Microsoft 365
- Office
- Spreadsheets
title: TableColumn
---
