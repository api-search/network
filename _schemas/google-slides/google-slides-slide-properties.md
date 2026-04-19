---
description: The properties of a Page that are only relevant for pages with pageType SLIDE.
layout: schema
name: SlideProperties
properties_list:
- description: The object ID of the layout that this slide is based on.
  name: layoutObjectId
  type: string
- description: The object ID of the master that this slide is based on.
  name: masterObjectId
  type: string
- description: Whether the slide is skipped in the presentation mode.
  name: isSkipped
  type: boolean
provider_name: Google Slides
provider_slug: google-slides
schema_file: json-schema/google-slides-slide-properties-schema.json
slug: google-slides-slide-properties
tags:
- Collaboration
- Google Workspace
- Presentations
- Productivity
- Slides
title: SlideProperties
---
