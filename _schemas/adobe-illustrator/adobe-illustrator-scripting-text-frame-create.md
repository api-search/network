---
description: TextFrameCreate from Adobe Illustrator API
layout: schema
name: TextFrameCreate
properties_list:
- description: Name of the text frame.
  name: name
  type: string
- description: Type of text frame to create.
  name: kind
  type: string
- description: The text content.
  name: contents
  type: string
- description: Position [x, y] in points.
  name: position
  type: array
- description: Width for area text frames.
  name: width
  type: number
- description: Height for area text frames.
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
- description: Target layer name.
  name: layer
  type: string
provider_name: Adobe Illustrator
provider_slug: adobe-illustrator
schema_file: json-schema/adobe-illustrator-scripting-text-frame-create-schema.json
slug: adobe-illustrator-scripting-text-frame-create
tags:
- Creative Cloud
- Design
- Illustrator
- Vector Graphics
title: TextFrameCreate
---
