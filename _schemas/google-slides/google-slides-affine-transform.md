---
description: A 3x3 matrix that represents an affine transformation. The matrix maps a source coordinate (x, y) to a destination coordinate (x', y') according to matrix multiplication.
layout: schema
name: AffineTransform
properties_list:
- description: The X coordinate scaling element.
  name: scaleX
  type: number
- description: The Y coordinate scaling element.
  name: scaleY
  type: number
- description: The X coordinate shearing element.
  name: shearX
  type: number
- description: The Y coordinate shearing element.
  name: shearY
  type: number
- description: The X coordinate translation element.
  name: translateX
  type: number
- description: The Y coordinate translation element.
  name: translateY
  type: number
- description: The units for translate elements.
  name: unit
  type: string
provider_name: Google Slides
provider_slug: google-slides
schema_file: json-schema/google-slides-affine-transform-schema.json
slug: google-slides-affine-transform
tags:
- Collaboration
- Google Workspace
- Presentations
- Productivity
- Slides
title: AffineTransform
---
