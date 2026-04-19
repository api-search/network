---
description: A Google Slides presentation.
layout: schema
name: Presentation
properties_list:
- description: The ID of the presentation.
  name: presentationId
  type: string
- description: The title of the presentation.
  name: title
  type: string
- description: The slides in the presentation. A slide inherits properties from a slide layout.
  name: slides
  type: array
- description: The slide masters in the presentation. A slide master contains all common page elements and the common properties for a set of layouts.
  name: masters
  type: array
- description: The layouts in the presentation. A layout is a template that determines how content is arranged and styled on the slides that inherit from that layout.
  name: layouts
  type: array
- description: The locale of the presentation as an IETF BCP 47 language tag.
  name: locale
  type: string
- description: 'Output only. The revision ID of the presentation. Can be used in update requests to assert that the presentation revision has not changed since the last read operation. Only populated if the user has '
  name: revisionId
  type: string
provider_name: Google Slides
provider_slug: google-slides
schema_file: json-schema/google-slides-presentation-schema.json
slug: google-slides-presentation
tags:
- Collaboration
- Google Workspace
- Presentations
- Productivity
- Slides
title: Presentation
---
