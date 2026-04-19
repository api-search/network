---
description: A document to be included in an envelope. Documents can be provided as base64-encoded content or by reference.
layout: schema
name: Document
properties_list:
- description: A unique identifier for the document within the envelope, assigned by the sender. Must be unique within the envelope.
  name: documentId
  type: string
- description: The name of the document.
  name: name
  type: string
- description: The file extension of the document. DocuSign uses this to determine the correct content type.
  name: fileExtension
  type: string
- description: The base64-encoded content of the document.
  name: documentBase64
  type: string
- description: URL from which to retrieve the document content.
  name: remoteUrl
  type: string
- description: The order of the document in the envelope.
  name: order
  type: string
- description: The number of pages in the document.
  name: pages
  type: string
- description: Display setting for the document.
  name: display
  type: string
- description: Whether to include this document in downloads.
  name: includeInDownload
  type: string
- description: When true, DocuSign transforms PDF form fields into DocuSign tabs.
  name: transformPdfFields
  type: string
provider_name: Docusign
provider_slug: docusign
schema_file: json-schema/docusign-esignature-document-schema.json
slug: docusign-esignature-document
tags:
- Agreements
- Contracts
- Digital Transaction Management
- Documents
- Electronic Signatures
- eSignature
title: Document
---
