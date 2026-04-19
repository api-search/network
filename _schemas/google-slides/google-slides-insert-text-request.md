---
description: Inserts text into a shape or a table cell.
layout: schema
name: InsertTextRequest
properties_list:
- description: The object ID of the shape or table cell.
  name: objectId
  type: string
- description: The text to be inserted. Inserting a newline character will implicitly create a new ParagraphMarker.
  name: text
  type: string
- description: The index where the text will be inserted, in Unicode code units of the UTF-16 encoding.
  name: insertionIndex
  type: integer
provider_name: Google Slides
provider_slug: google-slides
schema_file: json-schema/google-slides-insert-text-request-schema.json
slug: google-slides-insert-text-request
tags:
- Collaboration
- Google Workspace
- Presentations
- Productivity
- Slides
title: InsertTextRequest
---
