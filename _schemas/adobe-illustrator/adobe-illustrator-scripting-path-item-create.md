---
description: PathItemCreate from Adobe Illustrator API
layout: schema
name: PathItemCreate
properties_list:
- description: Name of the path item.
  name: name
  type: string
- description: Type of path to create.
  name: pathType
  type: string
- description: Array of path points for freeform paths. Required when pathType is "freeform".
  name: pathPoints
  type: array
- description: Position [x, y] in points.
  name: position
  type: array
- description: Width in points (for rectangle, ellipse).
  name: width
  type: number
- description: Height in points (for rectangle, ellipse).
  name: height
  type: number
- description: Corner radius for rounded rectangle.
  name: cornerRadius
  type: number
- description: Number of sides for polygon.
  name: sides
  type: integer
- description: Number of points for star.
  name: points
  type: integer
- description: Inner radius for star.
  name: innerRadius
  type: number
- description: Whether the path has a fill.
  name: filled
  type: boolean
- description: ''
  name: fillColor
  type: object
- description: Whether the path has a stroke.
  name: stroked
  type: boolean
- description: ''
  name: strokeColor
  type: object
- description: Stroke width in points.
  name: strokeWidth
  type: number
- description: Opacity as a percentage (0-100).
  name: opacity
  type: number
- description: Target layer name.
  name: layer
  type: string
provider_name: Adobe Illustrator
provider_slug: adobe-illustrator
schema_file: json-schema/adobe-illustrator-scripting-path-item-create-schema.json
slug: adobe-illustrator-scripting-path-item-create
tags:
- Creative Cloud
- Design
- Illustrator
- Vector Graphics
title: PathItemCreate
---
