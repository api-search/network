---
description: The general text content. The text must reside in a compatible shape (e.g., text box or rectangle) or a table cell in a page.
layout: schema
name: TextContent
properties_list:
- description: The text contents broken down into text elements.
  name: textElements
  type: array
- description: The bulleted lists contained in this text, keyed by list ID.
  name: lists
  type: object
provider_name: Google Slides
provider_slug: google-slides
schema_file: json-schema/google-slides-text-content-schema.json
slug: google-slides-text-content
tags:
- Collaboration
- Google Workspace
- Presentations
- Productivity
- Slides
title: TextContent
---
