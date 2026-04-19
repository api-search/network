---
description: Provides control over how write requests are executed. When a write request is made, the requiredRevisionId can be specified to indicate that the write should only succeed if the presentation's current revision matches the specified value.
layout: schema
name: WriteControl
properties_list:
- description: The revision ID of the presentation required for the write request. If specified, the write request is only processed if the current revision ID of the presentation matches this value.
  name: requiredRevisionId
  type: string
provider_name: Google Slides
provider_slug: google-slides
schema_file: json-schema/google-slides-write-control-schema.json
slug: google-slides-write-control
tags:
- Collaboration
- Google Workspace
- Presentations
- Productivity
- Slides
title: WriteControl
---
