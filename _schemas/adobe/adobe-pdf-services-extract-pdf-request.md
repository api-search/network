---
description: ''
layout: schema
name: ExtractPDFRequest
properties_list:
- description: The asset ID of the PDF to extract from.
  name: assetID
  type: string
- description: The types of elements to extract from the PDF.
  name: elementsToExtract
  type: array
- description: Rendition types to generate for extracted elements.
  name: elementsToExtractRenditions
  type: array
- description: The output format for extracted tables.
  name: tableOutputFormat
  type: string
- description: Whether to include styling information (font, color, etc.) in the extraction output.
  name: getStylingInfo
  type: boolean
- description: Whether to include character-level bounding box information.
  name: addCharInfo
  type: boolean
provider_name: Adobe
provider_slug: adobe
schema_file: json-schema/adobe-pdf-services-extract-pdf-request-schema.json
slug: adobe-pdf-services-extract-pdf-request
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
title: ExtractPDFRequest
---
