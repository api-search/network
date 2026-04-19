---
description: Replaces all instances of text matching a criteria with replace text.
layout: schema
name: ReplaceAllTextRequest
properties_list:
- description: The text that will replace the matched text.
  name: replaceText
  type: string
- description: If non-empty, limits the matches to page elements only on the given pages.
  name: pageObjectIds
  type: array
provider_name: Google Slides
provider_slug: google-slides
schema_file: json-schema/google-slides-replace-all-text-request-schema.json
slug: google-slides-replace-all-text-request
tags:
- Collaboration
- Google Workspace
- Presentations
- Productivity
- Slides
title: ReplaceAllTextRequest
---
