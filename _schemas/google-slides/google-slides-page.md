---
description: A page in a presentation.
layout: schema
name: Page
properties_list:
- description: The object ID for this page. Object IDs used by Page and PageElement share the same namespace.
  name: objectId
  type: string
- description: The type of the page.
  name: pageType
  type: string
- description: The page elements rendered on the page.
  name: pageElements
  type: array
- description: Output only. The revision ID of the presentation containing this page. Can be used in update requests to assert the presentation revision has not changed since the last read operation.
  name: revisionId
  type: string
provider_name: Google Slides
provider_slug: google-slides
schema_file: json-schema/google-slides-page-schema.json
slug: google-slides-page
tags:
- Collaboration
- Google Workspace
- Presentations
- Productivity
- Slides
title: Page
---
