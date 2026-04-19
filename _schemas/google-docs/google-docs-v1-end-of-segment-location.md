---
description: Location at the end of a body, header, footer, or footnote.
layout: schema
name: EndOfSegmentLocation
properties_list:
- description: The ID of the header, footer, or footnote the location is in. An empty segment ID signifies the document body.
  name: segmentId
  type: string
- description: The tab that the location is in.
  name: tabId
  type: string
provider_name: Google Docs
provider_slug: google-docs
schema_file: json-schema/google-docs-v1-end-of-segment-location-schema.json
slug: google-docs-v1-end-of-segment-location
tags:
- Collaboration
- Documents
- Google Workspace
- Productivity
- Word Processing
title: EndOfSegmentLocation
---
