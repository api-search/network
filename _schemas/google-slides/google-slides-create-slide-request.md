---
description: Creates a new slide.
layout: schema
name: CreateSlideRequest
properties_list:
- description: A user-supplied object ID. If specified, the ID must be unique among all pages and page elements in the presentation.
  name: objectId
  type: string
- description: The optional zero-based index indicating where in the presentation to insert the slide.
  name: insertionIndex
  type: integer
- description: An optional list of object ID mappings from the placeholder(s) on the layout to the placeholders that are created on the new slide.
  name: placeholderIdMappings
  type: array
provider_name: Google Slides
provider_slug: google-slides
schema_file: json-schema/google-slides-create-slide-request-schema.json
slug: google-slides-create-slide-request
tags:
- Collaboration
- Google Workspace
- Presentations
- Productivity
- Slides
title: CreateSlideRequest
---
