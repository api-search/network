---
description: Document from Adobe Illustrator API
layout: schema
name: Document
properties_list:
- description: Unique identifier of the document.
  name: id
  type: string
- description: Name of the document.
  name: name
  type: string
- description: Full file path of the document.
  name: fullName
  type: string
- description: Whether the document has been saved.
  name: saved
  type: boolean
- description: The document color mode.
  name: documentColorSpace
  type: string
- description: Document width in points.
  name: width
  type: number
- description: Document height in points.
  name: height
  type: number
- description: Ruler units used in the document.
  name: rulerUnits
  type: string
- description: The ruler origin point [x, y].
  name: rulerOrigin
  type: array
- description: Number of layers in the document.
  name: layerCount
  type: integer
- description: Number of artboards in the document.
  name: artboardCount
  type: integer
- description: Name of the currently active layer.
  name: activeLayer
  type: string
provider_name: Adobe Illustrator
provider_slug: adobe-illustrator
schema_file: json-schema/adobe-illustrator-scripting-document-schema.json
slug: adobe-illustrator-scripting-document
tags:
- Creative Cloud
- Design
- Illustrator
- Vector Graphics
title: Document
---
