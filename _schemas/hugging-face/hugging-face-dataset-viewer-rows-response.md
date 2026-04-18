---
description: ''
layout: schema
name: RowsResponse
properties_list:
- description: Column definitions and types
  name: features
  type: array
- description: Row data
  name: rows
  type: array
- description: Total number of rows in the split
  name: num_rows_total
  type: integer
- description: Number of rows per page
  name: num_rows_per_page
  type: integer
- description: Whether this is a partial result
  name: partial
  type: boolean
provider_name: Hugging Face
provider_slug: hugging-face
schema_file: json-schema/hugging-face-dataset-viewer-rows-response-schema.json
slug: hugging-face-dataset-viewer-rows-response
tags: []
title: RowsResponse
---
