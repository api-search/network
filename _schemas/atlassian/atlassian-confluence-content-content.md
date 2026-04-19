---
description: Base object for all content types.
layout: schema
name: Content
properties_list:
- description: ''
  name: id
  type: string
- description: Can be "page", "blogpost", "attachment" or "content"
  name: type
  type: string
- description: ''
  name: status
  type: string
- description: ''
  name: title
  type: string
- description: ''
  name: ancestors
  type: array
- description: ''
  name: operations
  type: array
- description: ''
  name: body
  type: object
- description: ''
  name: restrictions
  type: object
- description: ''
  name: macroRenderedOutput
  type: object
- description: ''
  name: extensions
  type: object
- description: ''
  name: _expandable
  type: object
provider_name: Atlassian
provider_slug: atlassian
schema_file: json-schema/atlassian-confluence-content-content-schema.json
slug: atlassian-confluence-content-content
tags:
- Code
- Collaboration
- Platform
- Productivity
- Software Development
title: Content
---
