---
description: Updates the position of slides in the presentation.
layout: schema
name: UpdateSlidesPositionRequest
properties_list:
- description: The IDs of the slides in the presentation that should be moved.
  name: slideObjectIds
  type: array
- description: The index where the slides should be inserted, based on the slide arrangement before the move takes place.
  name: insertionIndex
  type: integer
provider_name: Google Slides
provider_slug: google-slides
schema_file: json-schema/google-slides-update-slides-position-request-schema.json
slug: google-slides-update-slides-position-request
tags:
- Collaboration
- Google Workspace
- Presentations
- Productivity
- Slides
title: UpdateSlidesPositionRequest
---
