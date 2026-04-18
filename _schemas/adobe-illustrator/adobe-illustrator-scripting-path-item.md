---
description: PathItem from Adobe Illustrator API
layout: schema
name: PathItem
properties_list:
- description: Unique identifier of the path item.
  name: id
  type: string
- description: Name of the path item.
  name: name
  type: string
- description: Whether the path is closed.
  name: closed
  type: boolean
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
- description: Stroke cap style.
  name: strokeCap
  type: string
- description: Stroke join style.
  name: strokeJoin
  type: string
- description: Dash pattern for the stroke.
  name: strokeDashes
  type: array
- description: Opacity as a percentage (0-100).
  name: opacity
  type: number
- description: Blending mode.
  name: blendingMode
  type: string
- description: Position [x, y] in points.
  name: position
  type: array
- description: Width in points.
  name: width
  type: number
- description: Height in points.
  name: height
  type: number
- description: Array of path points defining the path shape.
  name: pathPoints
  type: array
- description: Area of the path in square points.
  name: area
  type: number
- description: Length of the path in points.
  name: length
  type: number
- description: Whether this path item is a guide.
  name: guides
  type: boolean
- description: Whether this path item is a clipping path.
  name: clipping
  type: boolean
- description: Name of the containing layer.
  name: layer
  type: string
provider_name: Adobe Illustrator
provider_slug: adobe-illustrator
schema_file: json-schema/adobe-illustrator-scripting-path-item-schema.json
slug: adobe-illustrator-scripting-path-item
tags:
- Creative Cloud
- Design
- Illustrator
- Vector Graphics
title: PathItem
---
