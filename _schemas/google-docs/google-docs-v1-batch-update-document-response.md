---
description: Response message for BatchUpdateDocument.
layout: schema
name: BatchUpdateDocumentResponse
properties_list:
- description: The ID of the document to which the updates were applied.
  name: documentId
  type: string
- description: The reply of the updates. This maps 1:1 with the updates, although replies to some requests may be empty.
  name: replies
  type: array
provider_name: Google Docs
provider_slug: google-docs
schema_file: json-schema/google-docs-v1-batch-update-document-response-schema.json
slug: google-docs-v1-batch-update-document-response
tags:
- Collaboration
- Documents
- Google Workspace
- Productivity
- Word Processing
title: BatchUpdateDocumentResponse
---
