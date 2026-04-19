---
description: The contents and style of a row in a table.
layout: schema
name: TableRow
properties_list:
- description: The zero-based start index of this row.
  name: startIndex
  type: integer
- description: The zero-based end index of this row, exclusive.
  name: endIndex
  type: integer
- description: The contents and style of each cell in this row.
  name: tableCells
  type: array
- description: ''
  name: suggestedInsertionIds
  type: array
- description: ''
  name: suggestedDeletionIds
  type: array
- description: ''
  name: suggestedTableRowStyleChanges
  type: object
provider_name: Google Docs
provider_slug: google-docs
schema_file: json-schema/google-docs-v1-table-row-schema.json
slug: google-docs-v1-table-row
tags:
- Collaboration
- Documents
- Google Workspace
- Productivity
- Word Processing
title: TableRow
---
