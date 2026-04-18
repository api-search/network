---
description: Artboard from Adobe Illustrator API
layout: schema
name: Artboard
properties_list:
- description: Zero-based index of the artboard.
  name: index
  type: integer
- description: Name of the artboard.
  name: name
  type: string
- description: Bounding rectangle [left, top, right, bottom] in points.
  name: artboardRect
  type: array
- description: Ruler origin point [x, y].
  name: rulerOrigin
  type: array
- description: Ruler pixel aspect ratio.
  name: rulerPAR
  type: number
- description: Whether to show the center mark.
  name: showCenter
  type: boolean
- description: Whether to show cross hairs.
  name: showCrossHairs
  type: boolean
- description: Whether to show safe areas.
  name: showSafeAreas
  type: boolean
provider_name: Adobe Illustrator
provider_slug: adobe-illustrator
schema_file: json-schema/adobe-illustrator-scripting-artboard-schema.json
slug: adobe-illustrator-scripting-artboard
tags:
- Creative Cloud
- Design
- Illustrator
- Vector Graphics
title: Artboard
---
