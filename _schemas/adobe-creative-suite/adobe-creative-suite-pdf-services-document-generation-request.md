---
description: Request body for generating a document from a template
layout: schema
name: DocumentGenerationRequest
properties_list:
- description: Asset ID of the Word document template
  name: assetID
  type: string
- description: Output format of the generated document
  name: outputFormat
  type: string
- description: JSON data object whose keys map to template tags in the document
  name: jsonDataForMerge
  type: object
- description: Whether to include non-tagged content as plain text additions
  name: notTaggedAdds
  type: boolean
provider_name: Adobe Creative Suite
provider_slug: adobe-creative-suite
schema_file: json-schema/adobe-creative-suite-pdf-services-document-generation-request-schema.json
slug: adobe-creative-suite-pdf-services-document-generation-request
tags:
- Creative
- Design
- Graphics
- Photography
- Video
title: DocumentGenerationRequest
---
