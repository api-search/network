---
description: Request body for creating a comment
layout: schema
name: CreateCommentRequest
properties_list:
- description: Comment text (1-2048 characters). Mention users with [user_id:team_id] format.
  name: message
  type: string
- description: User ID to assign the comment to
  name: assignee_id
  type: string
provider_name: Canva
provider_slug: canva
schema_file: json-schema/canva-connect-create-comment-request-schema.json
slug: canva-connect-create-comment-request
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
title: CreateCommentRequest
---
