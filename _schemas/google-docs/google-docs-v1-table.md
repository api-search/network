---
description: A StructuralElement representing a table.
layout: schema
name: Table
properties_list:
- description: Number of rows in the table.
  name: rows
  type: integer
- description: Number of columns in the table.
  name: columns
  type: integer
- description: The contents and style of each row.
  name: tableRows
  type: array
- description: ''
  name: suggestedInsertionIds
  type: array
- description: ''
  name: suggestedDeletionIds
  type: array
provider_name: Google Docs
provider_slug: google-docs
schema_file: json-schema/google-docs-v1-table-schema.json
slug: google-docs-v1-table
tags:
- Collaboration
- Documents
- Google Workspace
- Productivity
- Word Processing
title: Table
---
