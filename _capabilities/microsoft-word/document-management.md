---
consumed_apis:
- graph-api
- javascript-api
- open-xml-sdk
description: Unified workflow for Word document creation, editing, collaboration, conversion, and lifecycle management. Combines Microsoft Graph for cloud storage and sharing, JavaScript API for content manipulation, and Open XML SDK for server-side processing. Used by document authors, content managers, and automation engineers.
layout: capability
name: Microsoft Word Document Management
operations:
- description: Create a new Word document.
  method: POST
  name: create-document
  path: /v1/documents
- description: Get document metadata.
  method: GET
  name: get-document
  path: /v1/documents/{document-id}
- description: Delete a document.
  method: DELETE
  name: delete-document
  path: /v1/documents/{document-id}
- description: Get document body content.
  method: GET
  name: get-content
  path: /v1/documents/{document-id}/content
- description: List paragraphs.
  method: GET
  name: list-paragraphs
  path: /v1/documents/{document-id}/paragraphs
- description: List tables.
  method: GET
  name: list-tables
  path: /v1/documents/{document-id}/tables
- description: List comments.
  method: GET
  name: list-comments
  path: /v1/documents/{document-id}/comments
- description: List permissions.
  method: GET
  name: list-permissions
  path: /v1/documents/{document-id}/permissions
- description: List version history.
  method: GET
  name: list-versions
  path: /v1/documents/{document-id}/versions
- description: Convert to another format.
  method: POST
  name: convert-document
  path: /v1/documents/{document-id}/convert
- description: Search for documents.
  method: GET
  name: search-documents
  path: /v1/search
personas: []
provider_name: Microsoft Word
provider_slug: microsoft-word
search_terms:
- Content Manager
- productivity
- document lifecycle operations.
- list tables in the document.
- addin list comments
- graph search documents
- permission and sharing operations.
- get document metadata.
- version history operations.
- addin insert html
- create a new word document server-side using open xml.
- addin get body
- list version history.
- openxml convert document
- list comments in the document.
- list comments.
- builds automated document generation and processing pipelines.
- table operations.
- collaboration
- list sharing permissions on a document.
- document management
- create a sharing link for a document.
- list permissions.
- insert html content into the document.
- paragraph operations.
- list content controls in the document.
- search for documents.
- graph delete document
- delete a document from onedrive/sharepoint.
- list permissions
- graph get document
- create a new folder in onedrive.
- unified document lifecycle management combining cloud storage, content manipulation, and server-side processing.
- automation
- list versions
- comment operations.
- graph list permissions
- list version history of a document.
- addin search text
- graph share document
- search for text within the document.
- document format conversion.
- get document body content.
- list tables
- document search.
- documents
- microsoft 365
- office
- addin list tables
- individual document operations.
- delete document
- convert a word document to pdf or other format.
- graph list files
- list paragraphs
- convert to another format.
- openxml create document
- document content operations.
- list all paragraphs in the document.
- addin list paragraphs
- convert document
- manages document templates, reviews, and publishing workflows.
- microsoft word
- search documents
- openxml add paragraph
- search for word documents in onedrive/sharepoint.
- get the body content of an open word document.
- add a paragraph to a document server-side.
- get document
- delete a document.
- list paragraphs.
- list files and folders in a onedrive directory.
- addin list content controls
- addin insert table
- Document Author
- create a new word document.
- get metadata for a word document stored in onedrive/sharepoint.
- insert text into the document body.
- insert a new table into the document.
- graph create folder
- list comments
- creates and edits word documents, manages formatting and content.
- get content
- create document
- graph list versions
- list tables.
- Automation Engineer
- word processing
- addin insert text
slug: document-management
tags:
- Microsoft Word
- Document Management
- Collaboration
- Automation
tools:
- description: Get metadata for a Word document stored in OneDrive/SharePoint.
  hints:
    idempotent: true
    readOnly: true
  name: graph-get-document
- description: List files and folders in a OneDrive directory.
  hints:
    idempotent: true
    readOnly: true
  name: graph-list-files
- description: Search for Word documents in OneDrive/SharePoint.
  hints:
    idempotent: true
    readOnly: true
  name: graph-search-documents
- description: Create a new folder in OneDrive.
  hints:
    readOnly: false
  name: graph-create-folder
- description: Create a sharing link for a document.
  hints:
    readOnly: false
  name: graph-share-document
- description: List sharing permissions on a document.
  hints:
    idempotent: true
    readOnly: true
  name: graph-list-permissions
- description: List version history of a document.
  hints:
    idempotent: true
    readOnly: true
  name: graph-list-versions
- description: Delete a document from OneDrive/SharePoint.
  hints:
    destructive: true
    idempotent: true
    readOnly: false
  name: graph-delete-document
- description: Get the body content of an open Word document.
  hints:
    idempotent: true
    readOnly: true
  name: addin-get-body
- description: Insert text into the document body.
  hints:
    readOnly: false
  name: addin-insert-text
- description: Insert HTML content into the document.
  hints:
    readOnly: false
  name: addin-insert-html
- description: List all paragraphs in the document.
  hints:
    idempotent: true
    readOnly: true
  name: addin-list-paragraphs
- description: List content controls in the document.
  hints:
    idempotent: true
    readOnly: true
  name: addin-list-content-controls
- description: List tables in the document.
  hints:
    idempotent: true
    readOnly: true
  name: addin-list-tables
- description: Insert a new table into the document.
  hints:
    readOnly: false
  name: addin-insert-table
- description: List comments in the document.
  hints:
    idempotent: true
    readOnly: true
  name: addin-list-comments
- description: Search for text within the document.
  hints:
    idempotent: true
    readOnly: true
  name: addin-search-text
- description: Create a new Word document server-side using Open XML.
  hints:
    readOnly: false
  name: openxml-create-document
- description: Convert a Word document to PDF or other format.
  hints:
    readOnly: false
  name: openxml-convert-document
- description: Add a paragraph to a document server-side.
  hints:
    readOnly: false
  name: openxml-add-paragraph
---
