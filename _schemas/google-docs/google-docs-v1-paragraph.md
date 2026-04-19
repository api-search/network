---
description: A StructuralElement representing a paragraph. A paragraph is a range of content that is terminated with a newline character.
layout: schema
name: Paragraph
properties_list:
- description: The content of the paragraph, broken into its component parts.
  name: elements
  type: array
- description: Suggested changes to the paragraph style, keyed by suggestion ID.
  name: suggestedParagraphStyleChanges
  type: object
- description: Suggested changes to the bullet, keyed by suggestion ID.
  name: suggestedBulletChanges
  type: object
- description: The IDs of the positioned objects tethered to this paragraph.
  name: positionedObjectIds
  type: array
provider_name: Google Docs
provider_slug: google-docs
schema_file: json-schema/google-docs-v1-paragraph-schema.json
slug: google-docs-v1-paragraph
tags:
- Collaboration
- Documents
- Google Workspace
- Productivity
- Word Processing
title: Paragraph
---
