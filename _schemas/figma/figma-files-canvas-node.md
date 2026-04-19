---
description: A canvas (page) in the document.
layout: schema
name: CanvasNode
properties_list:
- description: A string uniquely identifying this node within the document.
  name: id
  type: string
- description: The name given to the node by the user in the tool.
  name: name
  type: string
- description: The type of the node.
  name: type
  type: string
- description: An array of top level layers on the canvas.
  name: children
  type: array
provider_name: Figma
provider_slug: figma
schema_file: json-schema/figma-files-canvas-node-schema.json
slug: figma-files-canvas-node
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
