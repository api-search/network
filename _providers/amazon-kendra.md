---
api_count: 1
apis:
- description: The Amazon Kendra API provides programmatic access to create and manage intelligent search indexes, configure data source connectors, submit queries, and manage relevance tuning for ML-powered enterpr
  name: Amazon Kendra API
  slug: ''
capabilities:
- description: 'Unified workflow capability for Amazon Kendra enterprise search, combining index management, data source connectivity, document indexing, and intelligent query operations for knowledge management and '
  name: Amazon Kendra Enterprise Search
  slug: amazon-kendra-enterprise-search
common:
- title: ''
  type: Blog
  url: https://aws.amazon.com/blogs/machine-learning/category/artificial-intelligence/amazon-kendra/
- title: ''
  type: Support
  url: https://aws.amazon.com/premiumsupport/
- title: ''
  type: Console
  url: https://console.aws.amazon.com/kendra/home
- title: ''
  type: CLI
  url: https://docs.aws.amazon.com/cli/latest/reference/kendra/
- title: ''
  type: SDK
  url: https://aws.amazon.com/tools/
- title: ''
  type: StatusPage
  url: https://status.aws.amazon.com/
- title: ''
  type: Compliance
  url: https://aws.amazon.com/compliance/
- title: ''
  type: TermsOfService
  url: https://aws.amazon.com/service-terms/
- title: ''
  type: Portal
  url: https://aws.amazon.com/kendra/
- title: ''
  type: Documentation
  url: https://docs.aws.amazon.com/kendra/
- title: ''
  type: Pricing
  url: https://aws.amazon.com/kendra/pricing/
- title: ''
  type: GettingStarted
  url: https://aws.amazon.com/kendra/getting-started/
- title: ''
  type: FAQ
  url: https://aws.amazon.com/kendra/faqs/
- title: ''
  type: PrivacyPolicy
  url: https://aws.amazon.com/privacy/
- title: ''
  type: SignUp
  url: https://portal.aws.amazon.com/billing/signup
- title: ''
  type: GitHubOrganization
  url: https://github.com/aws
- title: ''
  type: SpectralRules
  url: rules/amazon-kendra-spectral-rules.yml
- title: ''
  type: NaftikoCapability
  url: capabilities/amazon-kendra-enterprise-search.yaml
- title: ''
  type: Vocabulary
  url: vocabulary/amazon-kendra-vocabulary.yaml
created: '2024-01-15'
description: Amazon Kendra is an intelligent enterprise search service powered by machine learning that enables organizations to index and search across multiple data sources, delivering highly accurate and relevant answers to natural language queries.
features:
- description: ML-powered semantic search that understands natural language queries and context to return highly accurate answers from enterprise content.
  name: Intelligent Search
- description: Kendra Retriever API enables retrieval-augmented generation workflows with optimized passage chunking and ACL-based filtering for LLM integration.
  name: GenAI RAG Support
- description: Native connectors for Amazon S3, SharePoint, Salesforce, ServiceNow, Google Drive, Confluence, and many more data repositories.
  name: Data Source Connectors
- description: Fine-tune search results based on document freshness, authoritative sources, and custom synonyms without ML expertise.
  name: Relevance Tuning
- description: No-code visual interface to build, customize, and launch search applications with drag-and-drop components.
  name: Experience Builder
- description: Visibility into quality and usability metrics and user interaction patterns to identify content gaps.
  name: Search Analytics Dashboard
- description: Preprocessing capabilities for metadata enrichment, document classification, entity extraction, and AWS AI service integration.
  name: Custom Document Enrichment
- description: Learns from user interactions and feedback to promote preferred documents to the top of search results over time.
  name: Incremental Learning
image: https://a0.awsstatic.com/libra-css/images/logos/aws_logo_smile_1200x630.png
integrations:
- description: Use Kendra GenAI indices as knowledge bases in Amazon Bedrock for building generative AI applications.
  name: Amazon Bedrock
- description: Integrate Kendra indices with Amazon Q Business for AI-powered enterprise assistant experiences.
  name: Amazon Q Business
- description: Power Lex chatbots with Kendra search for FAQ-based conversational experiences.
  name: Amazon Lex
- description: Native data source connector for indexing documents stored in Amazon S3 buckets.
  name: Amazon S3
- description: Native connector to index and search SharePoint Online and SharePoint Server content.
  name: Microsoft SharePoint
- description: Index Salesforce objects and knowledge articles for enterprise search.
  name: Salesforce
- description: Connect to ServiceNow to index knowledge base articles and service catalog items.
  name: ServiceNow
- description: Use Comprehend for entity extraction and metadata enrichment during custom document enrichment.
  name: Amazon Comprehend
jsonld:
- class_count: 4
  name: Amazon Kendra Context
  property_count: 16
  slug: amazon-kendra-context
layout: provider
modified: '2026-04-19'
name: Amazon Kendra
rules:
- name: Amazon Kendra API Rules
  rule_count: 17
  severity_counts:
    error: 10
    hint: 0
    info: 0
    warn: 7
  slug: amazon-kendra-spectral-rules
skills: []
slug: amazon-kendra
solutions: []
tags:
- AI
- AWS
- Enterprise Search
- Knowledge Management
- Machine Learning
- Natural Language
url: https://aws.amazon.com/kendra/
use_cases:
- description: Help employees find accurate answers and data-driven insights across internal knowledge bases and document repositories.
  name: Employee Productivity
- description: Power self-service chatbots and agent-assist solutions for contact centers with intelligent search.
  name: Customer Service
- description: Integrate intelligent search and conversational AI into customer-facing applications via the Kendra API.
  name: SaaS Application Integration
- description: Use Kendra GenAI indices in Amazon Q Business and Amazon Bedrock knowledge bases to build RAG applications.
  name: Generative AI Applications
- description: Index and search across multiple heterogeneous data sources to create a unified knowledge search experience.
  name: Enterprise Knowledge Management
---
