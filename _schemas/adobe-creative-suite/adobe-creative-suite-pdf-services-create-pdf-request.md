---
description: Request body for creating a PDF from another format
layout: schema
name: CreatePDFRequest
properties_list:
- description: Asset ID of the source file to convert to PDF
  name: assetID
  type: string
- description: BCP 47 language code of the source document for better conversion
  name: documentLanguage
  type: string
provider_name: Adobe Creative Suite
provider_slug: adobe-creative-suite
schema_file: json-schema/adobe-creative-suite-pdf-services-create-pdf-request-schema.json
slug: adobe-creative-suite-pdf-services-create-pdf-request
tags:
- Creative
- Design
- Graphics
- Photography
- Video
title: CreatePDFRequest
---
