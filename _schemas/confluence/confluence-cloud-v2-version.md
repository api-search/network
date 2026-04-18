---
description: Version information for content.
layout: schema
name: Version
properties_list:
- description: The ISO 8601 timestamp of this version.
  name: createdAt
  type: string
- description: The message associated with this version.
  name: message
  type: string
- description: The version number.
  name: number
  type: integer
- description: Whether this was a minor edit.
  name: minorEdit
  type: boolean
- description: The Atlassian account ID of the version author.
  name: authorId
  type: string
provider_name: Confluence
provider_slug: confluence
schema_file: json-schema/confluence-cloud-v2-version-schema.json
slug: confluence-cloud-v2-version
tags:
- Collaboration
- Content Management
- Documentation
- Knowledge Base
- Wiki
title: Version
---
