---
description: A ParagraphElement representing a spot in the text that is dynamically replaced with content that can change over time, like a page number.
layout: schema
name: AutoText
properties_list:
- description: The type of this auto text.
  name: type
  type: string
- description: ''
  name: suggestedInsertionIds
  type: array
- description: ''
  name: suggestedDeletionIds
  type: array
- description: ''
  name: suggestedTextStyleChanges
  type: object
provider_name: Google Docs
provider_slug: google-docs
schema_file: json-schema/google-docs-v1-auto-text-schema.json
slug: google-docs-v1-auto-text
tags:
- Collaboration
- Documents
- Google Workspace
- Productivity
- Word Processing
title: AutoText
---
