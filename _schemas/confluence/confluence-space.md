---
description: Schema for a Confluence Cloud space resource as returned by the REST API v2. A space is the top-level organizational container in Confluence, holding pages, blog posts, and other content.
layout: schema
name: Confluence Space
properties_list:
- description: The unique identifier of the space.
  name: id
  type: string
- description: The unique key of the space. Used in URLs and as a human-readable identifier. Must be alphanumeric and uppercase.
  name: key
  type: string
- description: The display name of the space.
  name: name
  type: string
- description: The type of space. Global spaces are accessible to all users; personal spaces belong to an individual user.
  name: type
  type: string
- description: The lifecycle status of the space.
  name: status
  type: string
- description: The Atlassian account ID of the user who created the space.
  name: authorId
  type: string
- description: The ISO 8601 date-time when the space was created.
  name: createdAt
  type: string
- description: The ID of the space homepage. Every space has a homepage that serves as the root of the page tree.
  name: homepageId
  type:
  - string
  - 'null'
- description: ''
  name: description
  type: object
- description: ''
  name: icon
  type: object
- description: ''
  name: labels
  type: object
- description: ''
  name: properties
  type: object
- description: ''
  name: operations
  type: object
- description: ''
  name: permissions
  type: object
- description: ''
  name: _links
  type: object
provider_name: Confluence
provider_slug: confluence
schema_file: json-schema/confluence-space-schema.json
slug: confluence-space
tags:
- Collaboration
- Content Management
- Documentation
- Knowledge Base
- Wiki
title: Confluence Space
---
