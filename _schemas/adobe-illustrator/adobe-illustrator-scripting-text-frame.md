---
description: TextFrame from Adobe Illustrator API
layout: schema
name: TextFrame
properties_list:
- description: Unique identifier of the text frame.
  name: id
  type: string
- description: Name of the text frame.
  name: name
  type: string
- description: Type of text frame.
  name: kind
  type: string
- description: The text content of the frame.
  name: contents
  type: string
- description: Position [x, y] in points.
  name: position
  type: array
- description: Width of the text frame in points.
  name: width
  type: number
- description: Height of the text frame in points.
  name: height
  type: number
- description: Text orientation.
  name: orientation
  type: string
- description: ''
  name: characterAttributes
  type: object
- description: ''
  name: paragraphAttributes
  type: object
- description: Opacity as a percentage (0-100).
  name: opacity
  type: number
- description: Name of the containing layer.
  name: layer
  type: string
provider_name: Adobe Illustrator
provider_slug: adobe-illustrator
schema_file: json-schema/adobe-illustrator-scripting-text-frame-schema.json
slug: adobe-illustrator-scripting-text-frame
tags:
- Creative Cloud
- Design
- Illustrator
- Vector Graphics
title: TextFrame
---
