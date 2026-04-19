---
api_count: 1
apis:
- description: The Amazon Comprehend API provides programmatic access to natural language processing capabilities including sentiment analysis, entity recognition, key phrase extraction, language detection, topic mo
  name: Amazon Comprehend API
  slug: ''
capabilities:
- description: Workflow capability for natural language processing analysis including entity recognition, sentiment analysis, key phrase extraction, language detection, PII detection, and custom text classification.
  name: Amazon Comprehend NLP Analysis
  slug: nlp-analysis
common:
- title: ''
  type: Portal
  url: https://aws.amazon.com/
- title: ''
  type: Website
  url: https://aws.amazon.com/comprehend/
- title: ''
  type: Documentation
  url: https://docs.aws.amazon.com/comprehend/
- title: ''
  type: TermsOfService
  url: https://aws.amazon.com/service-terms/
- title: ''
  type: PrivacyPolicy
  url: https://aws.amazon.com/privacy/
- title: ''
  type: Support
  url: https://aws.amazon.com/support/
- title: ''
  type: Blog
  url: https://aws.amazon.com/blogs/machine-learning/
- title: ''
  type: GitHubOrganization
  url: https://github.com/aws
- title: ''
  type: Console
  url: https://console.aws.amazon.com/comprehend/
- title: ''
  type: SignUp
  url: https://portal.aws.amazon.com/billing/signup
- title: ''
  type: Login
  url: https://signin.aws.amazon.com/
- title: ''
  type: StatusPage
  url: https://health.aws.amazon.com/health/status
- title: ''
  type: YouTube
  url: https://www.youtube.com/user/AmazonWebServices
- title: ''
  type: StackOverflow
  url: https://stackoverflow.com/questions/tagged/amazon-comprehend
- title: ''
  type: Contact
  url: https://aws.amazon.com/contact-us/
- title: ''
  type: SpectralRules
  url: rules/amazon-comprehend-spectral-rules.yml
- title: ''
  type: NaftikoCapability
  url: capabilities/nlp-analysis.yaml
- title: ''
  type: Vocabulary
  url: vocabulary/amazon-comprehend-vocabulary.yaml
created: '2024-01-15'
description: Amazon Comprehend is a natural language processing (NLP) service that uses machine learning to uncover information in unstructured data. The service can identify critical elements in data, including references to language, people, and places. It provides entity recognition, sentiment analysis, key phrase extraction, language detection, topic modeling, PII detection, and custom classification capabilities for text documents at scale.
features:
- description: Identify named entities such as people, places, organizations, dates, and quantities in text.
  name: Entity Recognition
- description: Detect positive, negative, neutral, or mixed sentiment in text documents.
  name: Sentiment Analysis
- description: Extract key noun phrases and concepts from unstructured text.
  name: Key Phrase Extraction
- description: Automatically detect the dominant language of input text from 100+ supported languages.
  name: Language Detection
- description: Identify and optionally redact personally identifiable information from documents.
  name: PII Detection and Redaction
- description: Discover latent topics in large collections of documents using unsupervised learning.
  name: Topic Modeling
- description: Train custom document classifiers using your own labeled training data.
  name: Custom Classification
- description: Train custom entity recognizers to identify domain-specific entities in text.
  name: Custom Entity Recognition
- description: Analyze the syntax of text including parts of speech tagging and tokenization.
  name: Syntax Analysis
- description: Continuously improve custom models with new training data using the Flywheel feature.
  name: Flywheel
image: https://kinlane-productions.s3.amazonaws.com/apis-json/apis-json-logo.jpg
integrations:
- description: Process documents stored in S3 buckets using async batch analysis jobs.
  name: Amazon S3
- description: Integrate custom Comprehend models with SageMaker for advanced ML workflows.
  name: Amazon SageMaker
- description: Trigger real-time Comprehend analysis from Lambda functions in event-driven architectures.
  name: AWS Lambda
- description: Analyze streaming text data from Kinesis Data Streams and Firehose.
  name: Amazon Kinesis
- description: Enrich OpenSearch indexes with Comprehend-detected entities and topics for better search.
  name: Amazon OpenSearch
- description: Use Comprehend in AWS Glue ETL jobs for large-scale document processing pipelines.
  name: AWS Glue
jsonld:
- class_count: 235
  name: Amazon Comprehend Context
  property_count: 216
  slug: amazon-comprehend-context
layout: provider
modified: '2026-04-19'
name: Amazon Comprehend
rules:
- name: Amazon Comprehend API Rules
  rule_count: 23
  severity_counts:
    error: 8
    hint: 0
    info: 4
    warn: 11
  slug: amazon-comprehend-spectral-rules
skills: []
slug: amazon-comprehend
solutions: []
tags:
- AWS
- Machine Learning
- Natural Language Processing
- NLP
- Text Analysis
url: https://raw.githubusercontent.com/api-evangelist/amazon-comprehend/refs/heads/main/apis.yml
use_cases:
- description: Analyze customer reviews, support tickets, and survey responses to understand sentiment and extract actionable insights.
  name: Customer Feedback Analysis
- description: Detect and filter inappropriate content, hate speech, or PII from user-generated content.
  name: Content Moderation
- description: Extract entities, key information, and classifications from contracts, reports, and medical records.
  name: Document Processing
- description: Mine customer interactions for trends, topics, and sentiment to improve products and services.
  name: Voice of Customer Analytics
- description: Automatically detect and redact PII from documents to meet GDPR, HIPAA, and other compliance requirements.
  name: Compliance and PII Redaction
- description: Enrich search indexes with entities, key phrases, and topics to improve search relevance.
  name: Search Enhancement
---
