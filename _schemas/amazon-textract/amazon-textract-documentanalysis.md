---
description: Schema for an Amazon Textract document analysis response containing detected blocks of text, tables, forms, and layout elements extracted from a document.
layout: schema
name: DocumentAnalysis
properties_list:
- description: Metadata about the analyzed document.
  name: DocumentMetadata
  type: object
- description: The items detected in the document, including text lines, words, tables, and form elements.
  name: Blocks
  type: array
- description: The version of the model used to analyze the document.
  name: AnalyzeDocumentModelVersion
  type: string
provider_name: Amazon Textract
provider_slug: amazon-textract
schema_file: json-schema/amazon-textract-documentanalysis-schema.json
slug: amazon-textract-documentanalysis
tags:
- AWS
- Document Processing
- Machine Learning
- OCR
title: DocumentAnalysis
---
