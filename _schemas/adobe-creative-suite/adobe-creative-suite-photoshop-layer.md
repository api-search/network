---
description: Representation of a Photoshop document layer
layout: schema
name: Layer
properties_list:
- description: Unique layer identifier within the document
  name: id
  type: integer
- description: Layer stack index (0 = bottom)
  name: index
  type: integer
- description: Layer name as shown in the Layers panel
  name: name
  type: string
- description: Layer type
  name: type
  type: string
- description: Whether the layer is visible
  name: visible
  type: boolean
- description: Whether the layer is locked
  name: locked
  type: boolean
- description: Layer opacity from 0 to 255
  name: opacity
  type: integer
- description: Blend mode of the layer
  name: blendMode
  type: string
- description: Layer bounding box in pixels
  name: bounds
  type: object
- description: Child layers for group layers
  name: children
  type: array
provider_name: Adobe Creative Suite
provider_slug: adobe-creative-suite
schema_file: json-schema/adobe-creative-suite-photoshop-layer-schema.json
slug: adobe-creative-suite-photoshop-layer
tags:
- Creative
- Design
- Graphics
- Photography
- Video
title: Layer
---
