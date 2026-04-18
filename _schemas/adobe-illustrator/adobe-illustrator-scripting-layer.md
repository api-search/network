---
description: Layer from Adobe Illustrator API
layout: schema
name: Layer
properties_list:
- description: Unique identifier of the layer.
  name: id
  type: string
- description: Name of the layer.
  name: name
  type: string
- description: Whether the layer is visible.
  name: visible
  type: boolean
- description: Whether the layer is locked.
  name: locked
  type: boolean
- description: Whether the layer is printable.
  name: printable
  type: boolean
- description: Whether the layer is in preview mode.
  name: preview
  type: boolean
- description: Whether to dim placed images.
  name: dimPlacedImages
  type: boolean
- description: The layer highlight color.
  name: color
  type: string
- description: Layer opacity as a percentage (0-100).
  name: opacity
  type: number
- description: Blending mode for the layer.
  name: blendingMode
  type: string
- description: Whether the layer is a clipping mask.
  name: isClippingMask
  type: boolean
- description: Whether the layer is sliced.
  name: sliced
  type: boolean
- description: Whether the layer contains selected artwork.
  name: hasSelectedArtwork
  type: boolean
- description: Number of path items in the layer.
  name: pathItemCount
  type: integer
- description: Number of text frames in the layer.
  name: textFrameCount
  type: integer
- description: Number of sublayers.
  name: sublayerCount
  type: integer
provider_name: Adobe Illustrator
provider_slug: adobe-illustrator
schema_file: json-schema/adobe-illustrator-scripting-layer-schema.json
slug: adobe-illustrator-scripting-layer
tags:
- Creative Cloud
- Design
- Illustrator
- Vector Graphics
title: Layer
---
