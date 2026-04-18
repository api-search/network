---
description: Request body for auto-tagging a PDF for accessibility
layout: schema
name: AutoTagRequest
properties_list:
- description: Asset ID of the PDF to auto-tag
  name: assetID
  type: string
- description: Whether to generate an accessibility report alongside the tagged PDF
  name: generateReport
  type: boolean
- description: Whether to shift heading levels in the output for better document structure
  name: shiftHeadings
  type: boolean
provider_name: Adobe Creative Suite
provider_slug: adobe-creative-suite
schema_file: json-schema/adobe-creative-suite-pdf-services-auto-tag-request-schema.json
slug: adobe-creative-suite-pdf-services-auto-tag-request
tags:
- Creative
- Design
- Graphics
- Photography
- Video
title: AutoTagRequest
---
