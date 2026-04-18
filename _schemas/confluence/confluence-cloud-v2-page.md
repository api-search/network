---
description: Represents a Confluence page.
layout: schema
name: Page
properties_list:
- description: The unique identifier of the page.
  name: id
  type: string
- description: The current status of the page.
  name: status
  type: string
- description: The title of the page.
  name: title
  type: string
- description: The ID of the space this page belongs to.
  name: spaceId
  type: string
- description: The ID of the parent page, if the page is nested.
  name: parentId
  type: string
- description: The type of the parent (page or space).
  name: parentType
  type: string
- description: The position of this page in the page tree relative to siblings.
  name: position
  type: integer
- description: The Atlassian account ID of the page author.
  name: authorId
  type: string
- description: The Atlassian account ID of the page owner.
  name: ownerId
  type: string
- description: The Atlassian account ID of the previous owner.
  name: lastOwnerId
  type: string
- description: The ISO 8601 timestamp when the page was created.
  name: createdAt
  type: string
provider_name: Confluence
provider_slug: confluence
schema_file: json-schema/confluence-cloud-v2-page-schema.json
slug: confluence-cloud-v2-page
tags:
- Collaboration
- Content Management
- Documentation
- Knowledge Base
- Wiki
title: Page
---
