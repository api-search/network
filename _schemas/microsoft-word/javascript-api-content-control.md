---
description: Represents a content control in a Word document.
layout: schema
name: ContentControl
properties_list:
- description: Unique identifier of the content control.
  name: id
  type: string
- description: Tag to identify the content control.
  name: tag
  type: string
- description: Title of the content control.
  name: title
  type: string
- description: Type of content control.
  name: type
  type: string
- description: Text content of the content control.
  name: text
  type: string
- description: Visual appearance.
  name: appearance
  type: string
- description: Whether the content control can be deleted.
  name: cannotDelete
  type: boolean
- description: Whether the content control can be edited.
  name: cannotEdit
  type: boolean
provider_name: Microsoft Word
provider_slug: microsoft-word
schema_file: json-schema/javascript-api-content-control-schema.json
slug: javascript-api-content-control
tags:
- Documents
- Microsoft 365
- Office
- Productivity
- Word Processing
title: ContentControl
---
