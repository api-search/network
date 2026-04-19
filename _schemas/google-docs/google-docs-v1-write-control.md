---
description: Provides control over how write requests are executed. When set on a request, it provides a way to detect conflicts.
layout: schema
name: WriteControl
properties_list:
- description: The optional revision ID of the document the write request is applied to. If this is not the latest revision of the document, the request is not processed and returns a 400 bad request error.
  name: requiredRevisionId
  type: string
- description: The optional target revision ID of the document the write request is applied to. If collaborator changes have occurred after the document was read using the API, the changes produced by this write req
  name: targetRevisionId
  type: string
provider_name: Google Docs
provider_slug: google-docs
schema_file: json-schema/google-docs-v1-write-control-schema.json
slug: google-docs-v1-write-control
tags:
- Collaboration
- Documents
- Google Workspace
- Productivity
- Word Processing
title: WriteControl
---
