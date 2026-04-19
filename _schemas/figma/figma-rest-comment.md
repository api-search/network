---
description: A comment or reply left by a user on a Figma file. Comments can be pinned to specific locations on the canvas.
layout: schema
name: Comment
properties_list:
- description: Unique identifier for the comment.
  name: id
  type: string
- description: The key of the file the comment belongs to.
  name: file_key
  type: string
- description: If present, the ID of the comment to which this is a reply.
  name: parent_id
  type: '[''string'', ''null'']'
- description: The UTC ISO 8601 time at which the comment was left.
  name: created_at
  type: string
- description: If set, the UTC ISO 8601 time the comment was resolved.
  name: resolved_at
  type: '[''string'', ''null'']'
- description: The content of the comment.
  name: message
  type: string
- description: Only set for top-level comments. The number displayed with the comment in the UI.
  name: order_id
  type: '[''string'', ''null'']'
- description: An array of emoji reactions to the comment.
  name: reactions
  type: array
provider_name: Figma
provider_slug: figma
schema_file: json-schema/figma-rest-comment-schema.json
slug: figma-rest-comment
tags:
- Collaboration
- Design
- Graphics
- Interfaces
- Prototypes
- Prototyping
- UI/UX
title: Comment
---
