---
description: Schema for a Confluence Cloud page resource as returned by the REST API v2. A page is the primary content type in Confluence, representing a wiki-style document within a space.
layout: schema
name: Confluence Page
properties_list:
- description: The unique identifier of the page. Represented as a string in the v2 API.
  name: id
  type: string
- description: The current lifecycle status of the page.
  name: status
  type: string
- description: The title of the page. Must be unique within the space for current pages.
  name: title
  type: string
- description: The ID of the space this page belongs to.
  name: spaceId
  type: string
- description: The ID of the parent page. Null for top-level pages in a space.
  name: parentId
  type:
  - string
  - 'null'
- description: The type of the parent entity.
  name: parentType
  type: string
- description: The ordinal position of this page among its siblings in the page tree.
  name: position
  type:
  - integer
  - 'null'
- description: The Atlassian account ID of the user who originally created the page.
  name: authorId
  type: string
- description: The Atlassian account ID of the current page owner.
  name: ownerId
  type: string
- description: The Atlassian account ID of the previous page owner.
  name: lastOwnerId
  type:
  - string
  - 'null'
- description: The ISO 8601 date-time when the page was originally created.
  name: createdAt
  type: string
- description: ''
  name: version
  type: object
- description: ''
  name: body
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
  name: likes
  type: object
- description: ''
  name: versions
  type: object
- description: ''
  name: _links
  type: object
provider_name: Confluence
provider_slug: confluence
schema_file: json-schema/confluence-page-schema.json
slug: confluence-page
tags:
- Collaboration
- Content Management
- Documentation
- Knowledge Base
- Wiki
title: Confluence Page
---
