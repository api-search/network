---
description: Represents a single paragraph in a Word document.
layout: schema
name: Paragraph
properties_list:
- description: Unique identifier of the paragraph.
  name: id
  type: string
- description: Plain text content of the paragraph.
  name: text
  type: string
- description: Style name applied to the paragraph.
  name: style
  type: string
- description: Text alignment (Left, Centered, Right, Justified).
  name: alignment
  type: string
- description: First line indent value in points.
  name: firstLineIndent
  type: number
- description: Line spacing in points.
  name: lineSpacing
  type: number
- description: Outline level of the paragraph.
  name: outlineLevel
  type: integer
- description: Whether the paragraph is part of a list.
  name: isListItem
  type: boolean
provider_name: Microsoft Word
provider_slug: microsoft-word
schema_file: json-schema/javascript-api-paragraph-schema.json
slug: javascript-api-paragraph
tags:
- Documents
- Microsoft 365
- Office
- Productivity
- Word Processing
title: Paragraph
---
