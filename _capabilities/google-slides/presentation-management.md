---
consumed_apis:
- slides-api
description: Unified presentation management workflow for creating, reading, editing, and generating thumbnails of Google Slides presentations for content creators and automation engineers.
layout: capability
name: Google Slides Presentation Management
operations:
- description: Create a new presentation.
  method: POST
  name: create-presentation
  path: /v1/presentations
- description: Get a presentation by ID.
  method: GET
  name: get-presentation
  path: /v1/presentations
- description: Apply batch updates.
  method: POST
  name: batch-update
  path: /v1/presentations
- description: Get a specific page.
  method: GET
  name: get-page
  path: /v1/pages
- description: Get a page thumbnail.
  method: GET
  name: get-page-thumbnail
  path: /v1/pages
personas: []
provider_name: Google Slides
provider_slug: google-slides
search_terms:
- productivity
- access individual pages and thumbnails.
- collaboration
- get page thumbnail
- apply batch updates.
- presentations
- create a new presentation.
- slides
- get a presentation by id.
- create presentation
- google workspace
- create and manage presentations.
- batch update
- get presentation
- google
- content creation
- get a presentation by id with all slides, masters, and layouts.
- get a specific page.
- create a new blank google slides presentation.
- get page
- apply batch updates to a presentation (add slides, insert text, create shapes, embed images).
- batch update presentation
- get a page thumbnail.
- get a thumbnail image of a presentation page.
- get a specific page from a presentation.
slug: presentation-management
tags:
- Google
- Slides
- Presentations
- Content Creation
tools:
- description: Create a new blank Google Slides presentation.
  hints:
    readOnly: false
  name: create-presentation
- description: Get a presentation by ID with all slides, masters, and layouts.
  hints:
    readOnly: true
  name: get-presentation
- description: Apply batch updates to a presentation (add slides, insert text, create shapes, embed images).
  hints:
    readOnly: false
  name: batch-update-presentation
- description: Get a specific page from a presentation.
  hints:
    readOnly: true
  name: get-page
- description: Get a thumbnail image of a presentation page.
  hints:
    readOnly: true
  name: get-page-thumbnail
---
