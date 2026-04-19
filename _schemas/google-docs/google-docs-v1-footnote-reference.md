---
description: A ParagraphElement representing a footnote reference.
layout: schema
name: FootnoteReference
properties_list:
- description: The ID of the footnote that contains the content of this footnote reference.
  name: footnoteId
  type: string
- description: Output only. The rendered number of this footnote.
  name: footnoteNumber
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
schema_file: json-schema/google-docs-v1-footnote-reference-schema.json
slug: google-docs-v1-footnote-reference
tags:
- Collaboration
- Documents
- Google Workspace
- Productivity
- Word Processing
title: FootnoteReference
---
