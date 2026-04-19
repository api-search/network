---
description: A hypertext link.
layout: schema
name: Link
properties_list:
- description: If set, indicates this is a link to the external web page at this URL.
  name: url
  type: string
- description: If set, indicates this is a link to a slide in this presentation, addressed by its position.
  name: relativeLink
  type: string
- description: If set, indicates this is a link to the specific page in this presentation with this ID.
  name: pageObjectId
  type: string
- description: If set, indicates this is a link to the slide at this zero-based index in the presentation.
  name: slideIndex
  type: integer
provider_name: Google Slides
provider_slug: google-slides
schema_file: json-schema/google-slides-link-schema.json
slug: google-slides-link
tags:
- Collaboration
- Google Workspace
- Presentations
- Productivity
- Slides
title: Link
---
