---
description: ''
layout: schema
name: ContentBlueprintDraft
properties_list:
- description: The version for the new content.
  name: version
  type: object
- description: The title of the content. If you don't want to change the title, set this to the current title of the draft.
  name: title
  type: string
- description: The type of content. Set this to `page`.
  name: type
  type: string
- description: The status of the content. Set this to `current` or omit it altogether.
  name: status
  type: string
- description: The space for the content.
  name: space
  type: object
- description: The new ancestor (i.e. parent page) for the content. If you have specified an ancestor, you must also specify a `space` property in the request body for the space that the ancestor is in. Note, if you
  name: ancestors
  type: array
provider_name: Atlassian
provider_slug: atlassian
schema_file: json-schema/atlassian-confluence-content-content-blueprint-draft-schema.json
slug: atlassian-confluence-content-content-blueprint-draft
tags:
- Code
- Collaboration
- Platform
- Productivity
- Software Development
title: ContentBlueprintDraft
---
