---
description: A comment on a design
layout: schema
name: Comment
properties_list:
- description: The comment type
  name: type
  type: string
- description: The comment ID
  name: id
  type: string
- description: The comment text. User mentions use the format [user_id:team_id].
  name: message
  type: string
- description: Unix timestamp in seconds when the comment was created
  name: created_at
  type: integer
- description: Unix timestamp in seconds when the comment was last updated
  name: updated_at
  type: integer
- description: Dictionary of mentioned users, keyed by their mention identifier
  name: mentions
  type: object
provider_name: Canva
provider_slug: canva
schema_file: json-schema/canva-connect-comment-schema.json
slug: canva-connect-comment
tags:
- Apps
- Automation
- Brand Management
- Collaboration
- Design
- Graphics
- Marketing
- Print
- Templates
- Visual Content
title: Comment
---
