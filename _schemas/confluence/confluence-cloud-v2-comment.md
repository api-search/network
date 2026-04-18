---
description: Represents a comment on a Confluence page or blog post.
layout: schema
name: Comment
properties_list:
- description: The unique identifier of the comment.
  name: id
  type: string
- description: The current status of the comment.
  name: status
  type: string
- description: The title of the comment (typically auto-generated).
  name: title
  type: string
- description: The ID of the blog post the comment is on, if applicable.
  name: blogPostId
  type: string
- description: The ID of the page the comment is on, if applicable.
  name: pageId
  type: string
- description: The ID of the parent comment, if this is a reply.
  name: parentCommentId
  type: string
- description: The Atlassian account ID of the comment author.
  name: authorId
  type: string
- description: The ISO 8601 timestamp when the comment was created.
  name: createdAt
  type: string
- description: Resolution status for inline comments.
  name: resolutionStatus
  type: string
provider_name: Confluence
provider_slug: confluence
schema_file: json-schema/confluence-cloud-v2-comment-schema.json
slug: confluence-cloud-v2-comment
tags:
- Collaboration
- Content Management
- Documentation
- Knowledge Base
- Wiki
title: Comment
---
