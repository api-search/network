---
description: A PageElement kind representing a table.
layout: schema
name: Table
properties_list:
- description: Number of rows in the table.
  name: rows
  type: integer
- description: Number of columns in the table.
  name: columns
  type: integer
- description: Properties and contents of each row. Cells that span multiple rows are contained in only one of these rows and have a rowSpan greater than 1.
  name: tableRows
  type: array
- description: Properties of each column.
  name: tableColumns
  type: array
- description: Properties of horizontal cell borders.
  name: horizontalBorderRows
  type: array
- description: Properties of vertical cell borders.
  name: verticalBorderRows
  type: array
provider_name: Google Slides
provider_slug: google-slides
schema_file: json-schema/google-slides-table-schema.json
slug: google-slides-table
tags:
- Collaboration
- Google Workspace
- Presentations
- Productivity
- Slides
title: Table
---
