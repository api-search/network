---
description: A comment on a ticket.
layout: schema
name: Comment
properties_list:
- description: The ID of the comment.
  name: id
  type: integer
- description: The type of the comment.
  name: type
  type: string
- description: The plain text body of the comment.
  name: body
  type: string
- description: The HTML body of the comment.
  name: html_body
  type: string
- description: The plain text body with formatting stripped.
  name: plain_body
  type: string
- description: Whether the comment is public (visible to the requester).
  name: public
  type: boolean
- description: The ID of the comment author.
  name: author_id
  type: integer
- description: Attachments on the comment.
  name: attachments
  type: array
- description: When the comment was created (ISO 8601).
  name: created_at
  type: string
provider_name: Zendesk
provider_slug: zendesk
schema_file: json-schema/zendesk-support-comment-schema.json
slug: zendesk-support-comment
tags:
- Chat
- CRM
- Help Center
- Sell
- Support
- T1
- Talk
- Ticketing
- Tickets
title: Comment
---
