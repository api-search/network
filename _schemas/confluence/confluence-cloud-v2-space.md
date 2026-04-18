---
description: Represents a Confluence space.
layout: schema
name: Space
properties_list:
- description: The unique identifier of the space.
  name: id
  type: string
- description: The key of the space, used in URLs.
  name: key
  type: string
- description: The name of the space.
  name: name
  type: string
- description: The type of space.
  name: type
  type: string
- description: The status of the space.
  name: status
  type: string
- description: The Atlassian account ID of the space creator.
  name: authorId
  type: string
- description: The ISO 8601 timestamp when the space was created.
  name: createdAt
  type: string
- description: The ID of the space homepage.
  name: homepageId
  type: string
provider_name: Confluence
provider_slug: confluence
schema_file: json-schema/confluence-cloud-v2-space-schema.json
slug: confluence-cloud-v2-space
tags:
- Collaboration
- Content Management
- Documentation
- Knowledge Base
- Wiki
title: Space
---
