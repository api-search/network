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
- word processing
- convert document
- graph get document
- insert a new table into the document.
- list comments in the document.
- get metadata for a word document stored in onedrive/sharepoint.
- graph list permissions
- list permissions.
- insert html content into the document.
- search for word documents in onedrive/sharepoint.
- list permissions
- document management
- addin get body
- list comments.
- create a new word document.
- list comments
- manages document templates, reviews, and publishing workflows.
- Automation Engineer
- search for text within the document.
- search for documents.
- get document
- delete document
- graph search documents
- comment operations.
- addin list paragraphs
- get the body content of an open word document.
- office
- addin list content controls
- create a new word document server-side using open xml.
- list version history of a document.
- delete a document from onedrive/sharepoint.
- paragraph operations.
- get document metadata.
- list tables.
- graph list files
- list versions
- microsoft 365
- addin insert text
- create a sharing link for a document.
- graph create folder
- openxml convert document
- automation
- list sharing permissions on a document.
- openxml create document
- addin insert table
- get document body content.
- list tables
- document lifecycle operations.
- list files and folders in a onedrive directory.
- creates and edits word documents, manages formatting and content.
- list tables in the document.
- list paragraphs.
- table operations.
- Content Manager
- builds automated document generation and processing pipelines.
- add a paragraph to a document server-side.
- microsoft word
- graph delete document
- documents
- openxml add paragraph
- Document Author
- list version history.
- graph share document
- document content operations.
- version history operations.
- search documents
- insert text into the document body.
- document search.
- convert a word document to pdf or other format.
- unified document lifecycle management combining cloud storage, content manipulation, and server-side processing.
- addin insert html
- addin list tables
- get content
- addin search text
- productivity
- graph list versions
- list content controls in the document.
- delete a document.
- convert to another format.
- individual document operations.
- list paragraphs
- create document
- permission and sharing operations.
- list all paragraphs in the document.
- document format conversion.
- collaboration
- addin list comments
- create a new folder in onedrive.
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
