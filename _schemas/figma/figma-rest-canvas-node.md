---
description: A canvas (page) in the Figma document.
layout: schema
name: CanvasNode
properties_list:
- description: A string uniquely identifying this node within the document.
  name: id
  type: string
- description: The name given to the page by the user.
  name: name
  type: string
- description: The type of the node.
  name: type
  type: string
- description: An array of top-level layers on the canvas.
  name: children
  type: array
provider_name: Figma
provider_slug: figma
schema_file: json-schema/figma-rest-canvas-node-schema.json
slug: figma-rest-canvas-node
tags:
- Collaboration
- Design
- Graphics
- Interfaces
- Prototypes
- Prototyping
- UI/UX
title: CanvasNode
---
