---
description: Contains properties describing the look and feel of a list bullet at a given level of nesting.
layout: schema
name: NestingLevel
properties_list:
- description: The alignment of the bullet within the space allotted for rendering.
  name: bulletAlignment
  type: string
- description: The format string used by bullets at this level of nesting.
  name: glyphFormat
  type: string
- description: The number of the first list item at this nesting level.
  name: startNumber
  type: integer
- description: The type of glyph used by bullets at this nesting level.
  name: glyphType
  type: string
- description: A custom glyph symbol used by bullets at this nesting level.
  name: glyphSymbol
  type: string
provider_name: Google Docs
provider_slug: google-docs
schema_file: json-schema/google-docs-v1-nesting-level-schema.json
slug: google-docs-v1-nesting-level
tags:
- Collaboration
- Documents
- Google Workspace
- Productivity
- Word Processing
title: NestingLevel
---
