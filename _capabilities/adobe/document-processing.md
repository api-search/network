---
consumed_apis:
- pdf-services
description: Process PDF documents at scale including creation, conversion, extraction, manipulation, and accessibility tagging. Used by document automation engineers and content teams.
layout: capability
name: Adobe Document Processing
operations:
- description: Upload a document for processing
  method: POST
  name: upload-asset
  path: /v1/assets
- description: Get asset download URI
  method: GET
  name: get-asset
  path: /v1/assets
- description: Delete an asset
  method: DELETE
  name: delete-asset
  path: /v1/assets
- description: Create PDF from supported formats
  method: POST
  name: create-pdf
  path: /v1/convert
- description: Export PDF to other formats
  method: POST
  name: export-pdf
  path: /v1/export
- description: Extract structured content from PDF
  method: POST
  name: extract-pdf
  path: /v1/extract
- description: Get job status
  method: GET
  name: get-job-status
  path: /v1/jobs/{jobId}
personas: []
provider_name: Adobe
provider_slug: adobe
search_terms:
- compress pdf
- split pdf
- extract text, tables, and figures from a pdf
- experience cloud
- add password protection to a pdf
- remove protection
- extract structured content from pdf
- combine pdf
- adobe
- apply ocr to make scanned pdfs searchable
- delete asset
- ocr pdf
- optimize pdf for fast web viewing
- export pdf
- get job status
- analytics
- generative ai
- pdf content extraction
- get asset
- generate documents from templates with dynamic data
- reorder pages
- replace pages in a pdf with pages from another
- creative cloud
- delete pages
- linearize pdf
- e-commerce
- create pdf
- rotate pages in a pdf
- get asset download uri
- generate document
- extract pdf
- upload asset
- reorder pages within a pdf
- auto tag pdf
- remove password protection from a pdf
- digital asset management
- upload and manage document assets
- export pdf to other formats
- insert pages from one pdf into another
- insert pages
- check the status of an asynchronous pdf operation
- auto-tag pdf for accessibility compliance
- document services
- export pdf to docx, pptx, xlsx, or images
- documents
- split a pdf into multiple documents
- replace pages
- create pdf from supported formats
- rotate pages
- upload a document for processing
- get pdf properties
- marketing
- job status
- e-signatures
- delete an uploaded asset
- pdf conversion operations
- create a pdf from supported file formats
- delete an asset
- protect pdf
- compress a pdf to reduce file size
- get pdf metadata and document properties
- pdf
- work management
- automation
- pdf export operations
- delete specific pages from a pdf
- combine multiple pdfs into a single document
slug: document-processing
tags:
- Adobe
- Documents
- PDF
- Automation
tools:
- description: Upload a document for processing
  hints:
    readOnly: false
  name: upload-asset
- description: Get asset download URI
  hints:
    readOnly: true
  name: get-asset
- description: Delete an uploaded asset
  hints:
    destructive: true
    idempotent: true
  name: delete-asset
- description: Create a PDF from supported file formats
  hints:
    readOnly: false
  name: create-pdf
- description: Export PDF to DOCX, PPTX, XLSX, or images
  hints:
    readOnly: false
  name: export-pdf
- description: Combine multiple PDFs into a single document
  hints:
    readOnly: false
  name: combine-pdf
- description: Split a PDF into multiple documents
  hints:
    readOnly: false
  name: split-pdf
- description: Apply OCR to make scanned PDFs searchable
  hints:
    readOnly: false
  name: ocr-pdf
- description: Compress a PDF to reduce file size
  hints:
    readOnly: false
  name: compress-pdf
- description: Add password protection to a PDF
  hints:
    readOnly: false
  name: protect-pdf
- description: Remove password protection from a PDF
  hints:
    readOnly: false
  name: remove-protection
- description: Optimize PDF for fast web viewing
  hints:
    readOnly: false
  name: linearize-pdf
- description: Extract text, tables, and figures from a PDF
  hints:
    readOnly: true
  name: extract-pdf
- description: Auto-tag PDF for accessibility compliance
  hints:
    readOnly: false
  name: auto-tag-pdf
- description: Generate documents from templates with dynamic data
  hints:
    readOnly: false
  name: generate-document
- description: Get PDF metadata and document properties
  hints:
    readOnly: true
  name: get-pdf-properties
- description: Reorder pages within a PDF
  hints:
    readOnly: false
  name: reorder-pages
- description: Delete specific pages from a PDF
  hints:
    readOnly: false
  name: delete-pages
- description: Rotate pages in a PDF
  hints:
    readOnly: false
  name: rotate-pages
- description: Insert pages from one PDF into another
  hints:
    readOnly: false
  name: insert-pages
- description: Replace pages in a PDF with pages from another
  hints:
    readOnly: false
  name: replace-pages
- description: Check the status of an asynchronous PDF operation
  hints:
    idempotent: true
    readOnly: true
  name: get-job-status
---
