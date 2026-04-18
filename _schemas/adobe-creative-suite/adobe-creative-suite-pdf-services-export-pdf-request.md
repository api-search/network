---
description: Request body for exporting a PDF to another format
layout: schema
name: ExportPDFRequest
properties_list:
- description: Asset ID of the PDF to export
  name: assetID
  type: string
- description: Target output format for the exported file
  name: targetFormat
  type: string
- description: Locale for OCR during export, if the PDF contains scanned text
  name: exportOCRLocale
  type: string
provider_name: Adobe Creative Suite
provider_slug: adobe-creative-suite
schema_file: json-schema/adobe-creative-suite-pdf-services-export-pdf-request-schema.json
slug: adobe-creative-suite-pdf-services-export-pdf-request
tags:
- Creative
- Design
- Graphics
- Photography
- Video
title: ExportPDFRequest
---
