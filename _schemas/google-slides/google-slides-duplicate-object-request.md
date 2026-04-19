---
description: Duplicates a slide or page element. When duplicating a slide, the duplicate slide will be created immediately following the specified slide.
layout: schema
name: DuplicateObjectRequest
properties_list:
- description: The ID of the object to duplicate.
  name: objectId
  type: string
- description: The object being duplicated may contain other objects. This defines how the IDs of duplicated objects are generated.
  name: objectIds
  type: object
provider_name: Google Slides
provider_slug: google-slides
schema_file: json-schema/google-slides-duplicate-object-request-schema.json
slug: google-slides-duplicate-object-request
tags:
- Collaboration
- Google Workspace
- Presentations
- Productivity
- Slides
title: DuplicateObjectRequest
---
