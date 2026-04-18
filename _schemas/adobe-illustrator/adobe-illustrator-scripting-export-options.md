---
description: ExportOptions from Adobe Illustrator API
layout: schema
name: ExportOptions
properties_list:
- description: File path for the exported file.
  name: filePath
  type: string
- description: Export format.
  name: format
  type: string
- description: Range of artboards to export (e.g., "1-3" or "1,3,5"). Empty string exports all artboards.
  name: artboardRange
  type: string
- description: Horizontal scaling factor as a percentage.
  name: horizontalScale
  type: number
- description: Vertical scaling factor as a percentage.
  name: verticalScale
  type: number
- description: Export resolution in PPI.
  name: resolution
  type: number
- description: Whether to use anti-aliasing.
  name: antiAliasing
  type: boolean
- description: Whether to preserve transparency.
  name: transparency
  type: boolean
provider_name: Adobe Illustrator
provider_slug: adobe-illustrator
schema_file: json-schema/adobe-illustrator-scripting-export-options-schema.json
slug: adobe-illustrator-scripting-export-options
tags:
- Creative Cloud
- Design
- Illustrator
- Vector Graphics
title: ExportOptions
---
