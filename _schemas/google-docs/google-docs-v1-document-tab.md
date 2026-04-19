---
description: The content of a tab in a document, containing the body and associated document-level properties.
layout: schema
name: DocumentTab
properties_list:
- description: The headers in this tab, keyed by header ID.
  name: headers
  type: object
- description: The footers in this tab, keyed by footer ID.
  name: footers
  type: object
- description: The footnotes in this tab, keyed by footnote ID.
  name: footnotes
  type: object
- description: The lists in this tab, keyed by list ID.
  name: lists
  type: object
- description: The named ranges in this tab, keyed by name.
  name: namedRanges
  type: object
- description: The inline objects in this tab, keyed by object ID.
  name: inlineObjects
  type: object
- description: The positioned objects in this tab, keyed by object ID.
  name: positionedObjects
  type: object
provider_name: Google Docs
provider_slug: google-docs
schema_file: json-schema/google-docs-v1-document-tab-schema.json
slug: google-docs-v1-document-tab
tags:
- Collaboration
- Documents
- Google Workspace
- Productivity
- Word Processing
title: DocumentTab
---
