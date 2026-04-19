---
description: Request body for posting a new comment.
layout: schema
name: PostCommentRequest
properties_list:
- description: The text content of the comment.
  name: message
  type: string
- description: The comment to reply to, if any. This must be a root comment. Creating a reply to a reply is not supported.
  name: comment_id
  type: string
provider_name: Figma
provider_slug: figma
schema_file: json-schema/figma-rest-post-comment-request-schema.json
slug: figma-rest-post-comment-request
tags:
- Collaboration
- Design
- Graphics
- Interfaces
- Prototypes
- Prototyping
- UI/UX
title: PostCommentRequest
---
