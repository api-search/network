---
description: A set of published properties that can be applied to nodes.
layout: schema
name: PublishedStyle
properties_list:
- description: The unique identifier for the style
  name: key
  type: string
- description: The unique identifier of the Figma file that contains the style.
  name: file_key
  type: string
- description: ID of the style node within the figma file
  name: node_id
  type: string
- description: A URL to a thumbnail image of the style.
  name: thumbnail_url
  type: string
- description: The name of the style.
  name: name
  type: string
- description: The description of the style as entered by the publisher.
  name: description
  type: string
- description: The UTC ISO 8601 time when the style was created.
  name: created_at
  type: string
- description: The UTC ISO 8601 time when the style was last updated.
  name: updated_at
  type: string
- description: A user specified order number by which the style can be sorted.
  name: sort_position
  type: string
provider_name: Figma
provider_slug: figma
schema_file: json-schema/figma-styles-published-style-schema.json
slug: figma-styles-published-style
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
