---
description: A comment on a review, changelist, or other topic in Helix Swarm.
layout: schema
name: Comment
properties_list:
- description: The unique comment identifier.
  name: id
  type: integer
- description: File attachments on the comment.
  name: attachments
  type: array
- description: The comment body text.
  name: body
  type: string
- description: Inline context for file-level comments.
  name: context
  type: object
- description: Unix timestamp of the last edit, or null if not edited.
  name: edited
  type: integer
- description: Flags applied to the comment.
  name: flags
  type: array
- description: Usernames of users who liked the comment.
  name: likes
  type: array
- description: The task state of the comment.
  name: taskState
  type: string
- description: Unix timestamp when the comment was created.
  name: time
  type: integer
- description: The topic the comment belongs to, such as reviews/1234.
  name: topic
  type: string
- description: Unix timestamp of the last update.
  name: updated
  type: integer
- description: The username of the comment author.
  name: user
  type: string
provider_name: Perforce
provider_slug: perforce
schema_file: json-schema/perforce-helix-swarm-comment-schema.json
slug: perforce-helix-swarm-comment
tags: []
title: Comment
---
