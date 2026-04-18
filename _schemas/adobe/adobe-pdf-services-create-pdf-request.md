---
description: ''
layout: schema
name: CreatePDFRequest
properties_list:
- description: The asset ID of the source file to convert to PDF.
  name: assetID
  type: string
- description: The language of the source document for OCR processing.
  name: documentLanguage
  type: string
- description: Options specific to DOCX to PDF conversion.
  name: createPDFFromDOCXOptions
  type: object
- description: Options specific to PPTX to PDF conversion.
  name: createPDFFromPPTXOptions
  type: object
- description: Options specific to XLSX to PDF conversion.
  name: createPDFFromXLSXOptions
  type: object
- description: Options specific to HTML to PDF conversion.
  name: createPDFFromHTMLOptions
  type: object
provider_name: Adobe
provider_slug: adobe
schema_file: json-schema/adobe-pdf-services-create-pdf-request-schema.json
slug: adobe-pdf-services-create-pdf-request
tags:
- Analytics
- Creative Cloud
- Digital Asset Management
- Document Services
- E-Commerce
- E-Signatures
- Experience Cloud
- Generative AI
- Marketing
- PDF
- Work Management
title: CreatePDFRequest
---
