---
description: Represents a color in the RGBA color space. Values are in the range [0, 1].
layout: schema
name: Color
properties_list:
- description: The amount of red in the color as a value in the range [0, 1].
  name: red
  type: number
- description: The amount of green in the color as a value in the range [0, 1].
  name: green
  type: number
- description: The amount of blue in the color as a value in the range [0, 1].
  name: blue
  type: number
- description: The fraction of this color that should be applied to the pixel. A value of 1.0 corresponds to a solid color.
  name: alpha
  type: number
provider_name: Google Sheets
provider_slug: google-sheets
schema_file: json-schema/google-sheets-color-schema.json
slug: google-sheets-color
tags:
- Google Workspace
- Productivity
- Spreadsheets
title: Color
---
