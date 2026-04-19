---
description: '<p>Provides configuration parameters to override the default actions for extracting text from PDF documents and image files. </p> <p> By default, Amazon Comprehend performs the following actions to extract text from files, based on the input file type: </p> <ul> <li> <p> <b>Word files</b> - Amazon Comprehend parser extracts the text. </p> </li> <li> <p> <b>Digital PDF files</b> - Amazon Comprehend parser extracts the text. </p> </li> <li> <p> <b>Image files and scanned PDF files</b> - Amazon Comprehend uses the Amazon Textract <code>DetectDocumentText</code> API to extract the text. </p> </li> </ul> <p> <code>DocumentReaderConfig</code> does not apply to plain text files or Word files.</p> <p> For image files and PDF documents, you can override these default actions using the fields listed below. For more information, see <a href="https://docs.aws.amazon.com/comprehend/latest/dg/idp-set-textract-options.html"> Setting text extraction options</a> in the Comprehend Developer
  Guide. </p>'
layout: schema
name: DocumentReaderConfig
properties_list:
- description: ''
  name: DocumentReadAction
  type: object
- description: ''
  name: DocumentReadMode
  type: object
- description: ''
  name: FeatureTypes
  type: object
provider_name: Amazon Comprehend
provider_slug: amazon-comprehend
schema_file: json-schema/openapi.yml-document-reader-config-schema.json
slug: openapi.yml-document-reader-config
tags:
- AWS
- Machine Learning
- Natural Language Processing
- NLP
- Text Analysis
title: DocumentReaderConfig
---
