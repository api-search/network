---
description: The position of an embedded object such as a chart.
layout: schema
name: EmbeddedObjectPosition
properties_list:
- description: The sheet this is on.
  name: sheetId
  type: integer
- description: The position at which the object is overlaid on top of a grid.
  name: overlayPosition
  type: object
- description: If true, the embedded object is put on a new sheet whose ID is chosen for you.
  name: newSheet
  type: boolean
provider_name: Google Sheets
provider_slug: google-sheets
schema_file: json-schema/google-sheets-embedded-object-position-schema.json
slug: google-sheets-embedded-object-position
tags:
- Google Workspace
- Productivity
- Spreadsheets
title: EmbeddedObjectPosition
---
