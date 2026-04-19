---
consumed_apis:
- comprehend
description: Workflow capability for natural language processing analysis including entity recognition, sentiment analysis, key phrase extraction, language detection, PII detection, and custom text classification. Used by data scientists and application developers to extract insights from unstructured text.
layout: capability
name: Amazon Comprehend NLP Analysis
operations:
- description: Detect named entities in text.
  method: POST
  name: detect-entities
  path: /v1/analyze/entities
- description: Detect sentiment in text.
  method: POST
  name: detect-sentiment
  path: /v1/analyze/sentiment
- description: Extract key phrases from text.
  method: POST
  name: detect-key-phrases
  path: /v1/analyze/key-phrases
- description: Detect the dominant language of text.
  method: POST
  name: detect-language
  path: /v1/analyze/language
- description: Detect PII entities in text.
  method: POST
  name: detect-pii
  path: /v1/analyze/pii
- description: List available document classifiers.
  method: GET
  name: list-classifiers
  path: /v1/classify
- description: Detect entities in multiple documents.
  method: POST
  name: batch-detect-entities
  path: /v1/batch/entities
- description: Detect sentiment in multiple documents.
  method: POST
  name: batch-detect-sentiment
  path: /v1/batch/sentiment
personas: []
provider_name: Amazon Comprehend
provider_slug: amazon-comprehend
search_terms:
- Application Developer
- batch detect sentiment
- machine learning
- sentiment analysis.
- list available document classifiers.
- detect personally identifiable information (pii) entities in text using amazon comprehend.
- named entity recognition.
- detect pii
- detect named entities in text.
- detect sentiment in multiple documents.
- uses comprehend for bulk text analysis, topic modeling, and custom model training.
- batch sentiment analysis.
- language detection.
- entity recognition
- batch detect entities
- list classifiers
- text analysis
- key phrase extraction.
- natural language processing
- detect language
- detect syntax
- batch entity detection.
- aws
- sentiment analysis
- detect pii entities in text.
- detect entities in multiple text documents in one batch call.
- amazon
- detect the dominant language of input text using amazon comprehend.
- end-to-end nlp analysis using entity, sentiment, key phrase, and pii detection.
- detect entities
- detect named entities (people, places, organizations, dates) in text using amazon comprehend.
- detect key phrases
- detect sentiment in text.
- get properties and status of a specific document classifier.
- analyze syntax and parts of speech in text using amazon comprehend.
- describe classifier
- detect entities in multiple documents.
- pii detection.
- custom text classification.
- detect sentiment
- analyze the sentiment of text (positive, negative, neutral, or mixed) using amazon comprehend.
- extract key phrases from text.
- extract key noun phrases from text using amazon comprehend.
- detect sentiment in multiple text documents in one batch call.
- Data Scientist
- list custom document classifiers trained in amazon comprehend.
- integrates comprehend nlp apis into applications for real-time text analysis.
- detect the dominant language of text.
- nlp
slug: nlp-analysis
tags:
- Amazon
- AWS
- Natural Language Processing
- NLP
- Machine Learning
- Text Analysis
- Sentiment Analysis
- Entity Recognition
tools:
- description: Detect named entities (people, places, organizations, dates) in text using Amazon Comprehend.
  hints:
    openWorld: true
    readOnly: true
  name: detect-entities
- description: Analyze the sentiment of text (POSITIVE, NEGATIVE, NEUTRAL, or MIXED) using Amazon Comprehend.
  hints:
    openWorld: true
    readOnly: true
  name: detect-sentiment
- description: Extract key noun phrases from text using Amazon Comprehend.
  hints:
    openWorld: true
    readOnly: true
  name: detect-key-phrases
- description: Detect the dominant language of input text using Amazon Comprehend.
  hints:
    openWorld: true
    readOnly: true
  name: detect-language
- description: Analyze syntax and parts of speech in text using Amazon Comprehend.
  hints:
    openWorld: true
    readOnly: true
  name: detect-syntax
- description: Detect personally identifiable information (PII) entities in text using Amazon Comprehend.
  hints:
    openWorld: true
    readOnly: true
  name: detect-pii
- description: Detect entities in multiple text documents in one batch call.
  hints:
    readOnly: true
  name: batch-detect-entities
- description: Detect sentiment in multiple text documents in one batch call.
  hints:
    readOnly: true
  name: batch-detect-sentiment
- description: List custom document classifiers trained in Amazon Comprehend.
  hints:
    readOnly: true
  name: list-classifiers
- description: Get properties and status of a specific document classifier.
  hints:
    readOnly: true
  name: describe-classifier
---
