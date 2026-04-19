---
description: A ParagraphElement that represents a run of text that all has the same styling.
layout: schema
name: TextRun
properties_list:
- description: The text of this run. Any non-text elements in the run are replaced with the Unicode character U+E907.
  name: content
  type: string
- description: The suggested insertion IDs.
  name: suggestedInsertionIds
  type: array
- description: The suggested deletion IDs.
  name: suggestedDeletionIds
  type: array
- description: Suggested changes to the text style, keyed by suggestion ID.
  name: suggestedTextStyleChanges
  type: object
provider_name: Google Docs
provider_slug: google-docs
schema_file: json-schema/google-docs-v1-text-run-schema.json
slug: google-docs-v1-text-run
tags:
- Collaboration
- Documents
- Google Workspace
- Productivity
- Word Processing
title: TextRun
---
