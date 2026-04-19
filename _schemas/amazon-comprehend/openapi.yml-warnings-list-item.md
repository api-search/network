---
description: <p>The system identified one of the following warnings while processing the input document:</p> <ul> <li> <p>The document to classify is plain text, but the classifier is a native model.</p> </li> <li> <p>The document to classify is semi-structured, but the classifier is a plain-text model.</p> </li> </ul>
layout: schema
name: WarningsListItem
properties_list:
- description: ''
  name: Page
  type: object
- description: ''
  name: WarnCode
  type: object
- description: ''
  name: WarnMessage
  type: object
provider_name: Amazon Comprehend
provider_slug: amazon-comprehend
schema_file: json-schema/openapi.yml-warnings-list-item-schema.json
slug: openapi.yml-warnings-list-item
tags:
- AWS
- Machine Learning
- Natural Language Processing
- NLP
- Text Analysis
title: WarningsListItem
---
