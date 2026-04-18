---
description: Represents a comment in a Word document.
layout: schema
name: Comment
properties_list:
- description: Unique identifier of the comment.
  name: id
  type: string
- description: Name of the comment author.
  name: authorName
  type: string
- description: Email of the comment author.
  name: authorEmail
  type: string
- description: Text content of the comment.
  name: content
  type: string
- description: When the comment was created.
  name: createdDate
  type: string
- description: Whether the comment has been resolved.
  name: resolved
  type: boolean
provider_name: Microsoft Word
provider_slug: microsoft-word
schema_file: json-schema/javascript-api-comment-schema.json
slug: javascript-api-comment
tags:
- Documents
- Microsoft 365
- Office
- Productivity
- Word Processing
title: Comment
---
