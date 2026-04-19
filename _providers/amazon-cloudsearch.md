---
api_count: 1
apis:
- description: API for creating and managing CloudSearch domains, uploading documents, configuring search fields and suggesters, and executing search queries.
  name: Amazon CloudSearch API
  slug: ''
capabilities:
- description: Workflow for search domain management using Amazon CloudSearch for Application Developer personas.
  name: Amazon CloudSearch Search Domain Management
  slug: search-management
common:
- title: ''
  type: Portal
  url: https://aws.amazon.com/
- title: ''
  type: Website
  url: https://aws.amazon.com/cloudsearch/
- title: ''
  type: Documentation
  url: https://docs.aws.amazon.com/cloudsearch/latest/developerguide/what-is-cloudsearch.html
- title: ''
  type: TermsOfService
  url: https://aws.amazon.com/service-terms/
- title: ''
  type: PrivacyPolicy
  url: https://aws.amazon.com/privacy/
- title: ''
  type: Support
  url: https://aws.amazon.com/premiumsupport/
- title: ''
  type: Blog
  url: https://aws.amazon.com/blogs/compute/
- title: ''
  type: GitHubOrganization
  url: https://github.com/aws
- title: ''
  type: Console
  url: https://console.aws.amazon.com/cloudsearch/
- title: ''
  type: SignUp
  url: https://signin.aws.amazon.com/signup?request_type=register
- title: ''
  type: StatusPage
  url: https://health.aws.amazon.com/health/status
- title: ''
  type: YouTube
  url: https://www.youtube.com/user/AmazonWebServices
- title: ''
  type: StackOverflow
  url: https://stackoverflow.com/questions/tagged/amazon-cloudsearch
- title: ''
  type: Contact
  url: https://aws.amazon.com/contact-us/
- title: ''
  type: Compliance
  url: https://aws.amazon.com/compliance/
- title: ''
  type: SpectralRules
  url: rules/amazon-cloudsearch-spectral-rules.yml
- title: ''
  type: Vocabulary
  url: vocabulary/amazon-cloudsearch-vocabulary.yaml
- title: ''
  type: NaftikoCapability
  url: capabilities/search-management.yaml
created: '2024-01-15'
description: Amazon CloudSearch is a managed search service that makes it easy to set up, manage, and scale a search solution for your website or application. Supports full-text search, Boolean search, faceted search, autocomplete, geospatial search, and 34 languages.
features:
- description: Set up, manage, and scale search without becoming a search expert.
  name: Managed Search Infrastructure
- description: Full-text search across 34 languages with language-specific analyzers.
  name: Multi-Language Support
- description: Narrow search results by category with faceted navigation.
  name: Faceted Search
- description: Real-time search suggestions as users type.
  name: Autocomplete Suggestions
- description: Automatically scale resources as data volume and query traffic change.
  name: Automatic Scaling
- description: Distribute search traffic across multiple availability zones with Multi-AZ.
  name: High Availability
image: https://a0.awsstatic.com/libra-css/images/logos/aws_logo_smile_1200x630.png
integrations:
- description: Index documents stored in S3 buckets.
  name: Amazon S3
- description: Search DynamoDB data by exporting to CloudSearch.
  name: Amazon DynamoDB
- description: Control access to search domains with IAM policies.
  name: AWS IAM
- description: Cache search results at CloudFront edge for lower latency.
  name: Amazon CloudFront
jsonld:
- class_count: 9
  name: Amazon Cloudsearch Context
  property_count: 16
  slug: amazon-cloudsearch-context
layout: provider
modified: '2026-04-19'
name: Amazon CloudSearch
rules:
- name: Amazon CloudSearch API Rules
  rule_count: 19
  severity_counts:
    error: 12
    hint: 0
    info: 1
    warn: 6
  slug: amazon-cloudsearch-spectral-rules
skills: []
slug: amazon-cloudsearch
solutions: []
tags:
- AWS
- CloudSearch
- Search
- Full-Text Search
- Managed
url: https://aws.amazon.com/cloudsearch/
use_cases:
- description: Add powerful full-text search capabilities to websites and web applications.
  name: Website Search
- description: Enable customers to find products with faceted filtering and relevance ranking.
  name: E-Commerce Product Search
- description: Search across large document repositories with Boolean and proximity search.
  name: Document Search
- description: Find resources by location with geospatial search queries.
  name: Geospatial Search
---
