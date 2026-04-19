---
description: Inserts columns into a table.
layout: schema
name: InsertTableColumnsRequest
properties_list:
- description: The table to insert columns into.
  name: tableObjectId
  type: string
- description: Whether to insert new columns to the right of the reference cell location.
  name: insertRight
  type: boolean
- description: The number of columns to be inserted.
  name: number
  type: integer
provider_name: Google Slides
provider_slug: google-slides
schema_file: json-schema/google-slides-insert-table-columns-request-schema.json
slug: google-slides-insert-table-columns-request
tags:
- Collaboration
- Google Workspace
- Presentations
- Productivity
- Slides
title: InsertTableColumnsRequest
---
