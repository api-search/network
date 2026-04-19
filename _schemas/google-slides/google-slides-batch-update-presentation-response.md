---
description: Response message from a BatchUpdatePresentation request.
layout: schema
name: BatchUpdatePresentationResponse
properties_list:
- description: The presentation the updates were applied to.
  name: presentationId
  type: string
- description: The reply of the updates. This maps 1:1 with the updates, although replies to some requests may be empty.
  name: replies
  type: array
provider_name: Google Slides
provider_slug: google-slides
schema_file: json-schema/google-slides-batch-update-presentation-response-schema.json
slug: google-slides-batch-update-presentation-response
tags:
- Collaboration
- Google Workspace
- Presentations
- Productivity
- Slides
title: BatchUpdatePresentationResponse
---
