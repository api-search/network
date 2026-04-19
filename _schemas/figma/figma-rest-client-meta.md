---
description: Position metadata for a pinned comment. Describes where the comment marker is located on the canvas.
layout: schema
name: ClientMeta
properties_list:
- description: X coordinate of the comment pin.
  name: x
  type: number
- description: Y coordinate of the comment pin.
  name: y
  type: number
- description: The node ID the comment is pinned to.
  name: node_id
  type: string
- description: Offset from the node origin.
  name: node_offset
  type: object
provider_name: Figma
provider_slug: figma
schema_file: json-schema/figma-rest-client-meta-schema.json
slug: figma-rest-client-meta
tags:
- Collaboration
- Design
- Graphics
- Interfaces
- Prototypes
- Prototyping
- UI/UX
title: ClientMeta
---
