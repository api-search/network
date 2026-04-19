---
description: Inserts rows into a table.
layout: schema
name: InsertTableRowsRequest
properties_list:
- description: The table to insert rows into.
  name: tableObjectId
  type: string
- description: Whether to insert new rows below the reference cell location.
  name: insertBelow
  type: boolean
- description: The number of rows to be inserted.
  name: number
  type: integer
provider_name: Google Slides
provider_slug: google-slides
schema_file: json-schema/google-slides-insert-table-rows-request-schema.json
slug: google-slides-insert-table-rows-request
tags:
- Collaboration
- Google Workspace
- Presentations
- Productivity
- Slides
title: InsertTableRowsRequest
---
