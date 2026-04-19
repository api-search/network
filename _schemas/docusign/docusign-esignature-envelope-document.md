---
description: Metadata about a document within an envelope.
layout: schema
name: EnvelopeDocument
properties_list:
- description: The unique identifier of the document.
  name: documentId
  type: string
- description: The name of the document.
  name: name
  type: string
- description: The document type.
  name: type
  type: string
- description: URI for retrieving the document.
  name: uri
  type: string
- description: The order of the document in the envelope.
  name: order
  type: string
- description: Array of page objects for the document.
  name: pages
  type: array
- description: Whether the document contains PDF form fields.
  name: containsPdfFormFields
  type: string
- description: Display setting for the document.
  name: display
  type: string
- description: Whether to include this document in downloads.
  name: includeInDownload
  type: string
provider_name: Docusign
provider_slug: docusign
schema_file: json-schema/docusign-esignature-envelope-document-schema.json
slug: docusign-esignature-envelope-document
tags:
- Agreements
- Contracts
- Digital Transaction Management
- Documents
- Electronic Signatures
- eSignature
title: EnvelopeDocument
---
