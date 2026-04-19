---
description: Schema for an Amazon Comprehend entity detection result, representing named entities identified in text through NLP analysis.
layout: schema
name: Amazon Comprehend Entity
properties_list:
- description: A collection of entities identified in the input text.
  name: Entities
  type: array
- description: The inferred sentiment detected in the input text.
  name: Sentiment
  type: string
- description: The confidence scores for each sentiment type.
  name: SentimentScore
  type: object
- description: A collection of key phrases identified in the input text.
  name: KeyPhrases
  type: array
- description: The languages detected in the input text.
  name: Languages
  type: array
provider_name: Amazon Comprehend
provider_slug: amazon-comprehend
schema_file: json-schema/amazon-comprehend-entity-schema.json
slug: amazon-comprehend-entity
tags:
- AWS
- Machine Learning
- Natural Language Processing
- NLP
- Text Analysis
title: Amazon Comprehend Entity
---
