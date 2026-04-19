---
description: Specifies a contiguous range of text.
layout: schema
name: Range
properties_list:
- description: The ID of the header, footer, or footnote that this range is contained in. An empty segment ID signifies the document body.
  name: segmentId
  type: string
- description: The zero-based start index of this range, in UTF-16 code units.
  name: startIndex
  type: integer
- description: The zero-based end index of this range, exclusive, in UTF-16 code units.
  name: endIndex
  type: integer
- description: The tab that contains this range.
  name: tabId
  type: string
provider_name: Google Docs
provider_slug: google-docs
schema_file: json-schema/google-docs-v1-range-schema.json
slug: google-docs-v1-range
tags:
- Collaboration
- Documents
- Google Workspace
- Productivity
- Word Processing
title: Range
---
