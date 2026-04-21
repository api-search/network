---
consumed_apis:
- docs-api
description: Unified workflow for creating, reading, and editing Google Docs documents including content manipulation, formatting, and template automation. Used by developers automating document workflows.
layout: capability
name: Google Docs Document Management
operations:
- description: Create a new document.
  method: POST
  name: create-document
  path: /v1/documents
- description: Get a document by ID.
  method: GET
  name: get-document
  path: /v1/documents/{id}
- description: Apply batch updates to a document.
  method: POST
  name: batch-update-document
  path: /v1/documents/{id}/batch-update
personas: []
provider_name: Google Docs
provider_slug: google-docs
search_terms:
- retrieve a google docs document by its id.
- create a new google docs document with a title.
- document batch updates.
- document retrieval and updates.
- google docs
- apply batch updates to insert, replace, or delete content in a document.
- productivity
- batch update document
- document management
- automation
- word processing
- create document
- get a document by id.
- create a new document.
- collaboration
- google workspace
- apply batch updates to a document.
- documents
- document creation.
- get document
slug: document-management
tags:
- Google Docs
- Document Management
- Google Workspace
- Automation
tools:
- description: Create a new Google Docs document with a title.
  hints:
    readOnly: false
  name: create-document
- description: Retrieve a Google Docs document by its ID.
  hints:
    idempotent: true
    readOnly: true
  name: get-document
- description: Apply batch updates to insert, replace, or delete content in a document.
  hints:
    readOnly: false
  name: batch-update-document
---
