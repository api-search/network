---
description: Represents a table in a Word document.
layout: schema
name: Table
properties_list:
- description: Unique identifier of the table.
  name: id
  type: string
- description: Number of rows in the table.
  name: rowCount
  type: integer
- description: Number of columns in the table.
  name: columnCount
  type: integer
- description: Style name applied to the table.
  name: style
  type: string
- description: Table alignment.
  name: alignment
  type: string
- description: Number of header rows.
  name: headerRowCount
  type: integer
provider_name: Microsoft Word
provider_slug: microsoft-word
schema_file: json-schema/javascript-api-table-schema.json
slug: javascript-api-table
tags:
- Documents
- Microsoft 365
- Office
- Productivity
- Word Processing
title: Table
---
