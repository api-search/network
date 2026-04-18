---
description: The rotation applied to text in a cell.
layout: schema
name: TextRotation
properties_list:
- description: The angle between the standard orientation and the desired orientation. Measured in degrees. Valid values are between -90 and 90.
  name: angle
  type: integer
- description: If true, text reads top to bottom, but the orientation of individual characters is unchanged.
  name: vertical
  type: boolean
provider_name: Google Sheets
provider_slug: google-sheets
schema_file: json-schema/google-sheets-text-rotation-schema.json
slug: google-sheets-text-rotation
tags:
- Google Workspace
- Productivity
- Spreadsheets
title: TextRotation
---
