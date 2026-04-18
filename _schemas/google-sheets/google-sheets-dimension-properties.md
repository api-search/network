---
description: Properties about a dimension.
layout: schema
name: DimensionProperties
properties_list:
- description: True if this dimension is being filtered.
  name: hiddenByFilter
  type: boolean
- description: True if this dimension is explicitly hidden.
  name: hiddenByUser
  type: boolean
- description: The height (for rows) or width (for columns) of the dimension in pixels.
  name: pixelSize
  type: integer
- description: The developer metadata associated with a single row or column.
  name: developerMetadata
  type: array
provider_name: Google Sheets
provider_slug: google-sheets
schema_file: json-schema/google-sheets-dimension-properties-schema.json
slug: google-sheets-dimension-properties
tags:
- Google Workspace
- Productivity
- Spreadsheets
title: DimensionProperties
---
