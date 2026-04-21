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
- search for word documents in onedrive/sharepoint.
- addin list comments
- addin list content controls
- create a new word document.
- list content controls in the document.
- list tables.
- list comments.
- addin insert text
- list comments in the document.
- table operations.
- search for documents.
- permission and sharing operations.
- collaboration
- microsoft 365
- list permissions.
- create a new word document server-side using open xml.
- paragraph operations.
- creates and edits word documents, manages formatting and content.
- microsoft word
- list paragraphs
- list tables in the document.
- document search.
- add a paragraph to a document server-side.
- list permissions
- version history operations.
- insert html content into the document.
- delete a document from onedrive/sharepoint.
- insert a new table into the document.
- convert to another format.
- graph create folder
- get metadata for a word document stored in onedrive/sharepoint.
- list comments
- graph share document
- get document body content.
- graph delete document
- delete a document.
- list version history.
- document management
- list files and folders in a onedrive directory.
- create document
- graph list versions
- openxml create document
- individual document operations.
- document content operations.
- addin get body
- convert document
- graph search documents
- create a new folder in onedrive.
- Automation Engineer
- create a sharing link for a document.
- list tables
- openxml add paragraph
- list sharing permissions on a document.
- search for text within the document.
- productivity
- Content Manager
- graph list permissions
- unified document lifecycle management combining cloud storage, content manipulation, and server-side processing.
- list version history of a document.
- comment operations.
- office
- list paragraphs.
- graph list files
- document lifecycle operations.
- addin insert table
- Document Author
- documents
- convert a word document to pdf or other format.
- get the body content of an open word document.
- addin list tables
- graph get document
- get document metadata.
- manages document templates, reviews, and publishing workflows.
- insert text into the document body.
- automation
- word processing
- delete document
- search documents
- document format conversion.
- list versions
- addin search text
- list all paragraphs in the document.
- addin insert html
- openxml convert document
- builds automated document generation and processing pipelines.
- get content
- addin list paragraphs
- get document
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
