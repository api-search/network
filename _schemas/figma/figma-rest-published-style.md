---
description: A published style from a team or file library.
layout: schema
name: PublishedStyle
properties_list:
- description: The globally unique identifier for the style.
  name: key
  type: string
- description: The key of the Figma file containing the style.
  name: file_key
  type: string
- description: The node ID of the style within the file.
  name: node_id
  type: string
- description: A URL to a thumbnail image of the style.
  name: thumbnail_url
  type: string
- description: The name of the style.
  name: name
  type: string
- description: The description of the style.
  name: description
  type: string
- description: ''
  name: style_type
  type: string
- description: A user-defined sort position for the style.
  name: sort_position
  type: string
- description: ''
  name: created_at
  type: string
- description: ''
  name: updated_at
  type: string
provider_name: Figma
provider_slug: figma
schema_file: json-schema/figma-rest-published-style-schema.json
slug: figma-rest-published-style
tags:
- Collaboration
- Design
- Graphics
- Interfaces
- Prototypes
- Prototyping
- UI/UX
title: PublishedStyle
---
