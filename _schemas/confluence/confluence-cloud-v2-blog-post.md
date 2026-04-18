---
description: Represents a Confluence blog post.
layout: schema
name: BlogPost
properties_list:
- description: The unique identifier of the blog post.
  name: id
  type: string
- description: The current status of the blog post.
  name: status
  type: string
- description: The title of the blog post.
  name: title
  type: string
- description: The ID of the space this blog post belongs to.
  name: spaceId
  type: string
- description: The Atlassian account ID of the blog post author.
  name: authorId
  type: string
- description: The ISO 8601 timestamp when the blog post was created.
  name: createdAt
  type: string
provider_name: Confluence
provider_slug: confluence
schema_file: json-schema/confluence-cloud-v2-blog-post-schema.json
slug: confluence-cloud-v2-blog-post
tags:
- Collaboration
- Content Management
- Documentation
- Knowledge Base
- Wiki
title: BlogPost
---
