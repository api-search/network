---
description: Response object containing the results of document text detection or analysis, including detected blocks of text, tables, and forms.
layout: schema
name: DocumentAnalysis
properties_list:
- description: Metadata about the document.
  name: DocumentMetadata
  type: object
- description: The items detected in the document.
  name: Blocks
  type: array
- description: The version of the model used to analyze the document.
  name: AnalyzeDocumentModelVersion
  type: string
provider_name: Amazon Textract
provider_slug: amazon-textract
schema_file: json-schema/amazon-textract-document-analysis-schema.json
slug: amazon-textract-document-analysis
tags:
- AWS
- Document Processing
- Machine Learning
- OCR
title: DocumentAnalysis
---
