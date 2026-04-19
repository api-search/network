---
api_count: 1
apis:
- description: API for managing Amazon ElastiCache clusters, replication groups, parameter groups, and related caching infrastructure resources.
  name: Amazon ElastiCache API
  slug: ''
capabilities:
- description: Unified capability for managing Amazon ElastiCache resources. Combines Amazon ElastiCache APIs for Backend Developer workflows in Data Caching.
  name: Amazon ElastiCache Management
  slug: amazon-elasticache-capability
common:
- title: ''
  type: Portal
  url: https://aws.amazon.com/
- title: ''
  type: DeveloperPortal
  url: https://aws.amazon.com/elasticache/
- title: ''
  type: Documentation
  url: https://docs.aws.amazon.com/elasticache/
- title: ''
  type: Blog
  url: https://aws.amazon.com/blogs/
- title: ''
  type: GitHubOrganization
  url: https://github.com/aws
- title: ''
  type: Console
  url: https://console.aws.amazon.com/elasticache/
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
  type: Support
  url: https://aws.amazon.com/support/
- title: ''
  type: FAQ
  url: https://aws.amazon.com/elasticache/faqs/
- title: ''
  type: TermsOfService
  url: https://aws.amazon.com/service-terms/
- title: ''
  type: PrivacyPolicy
  url: https://aws.amazon.com/privacy/
- title: ''
  type: Compliance
  url: https://aws.amazon.com/compliance/
- title: ''
  type: Security
  url: https://aws.amazon.com/security/
- title: ''
  type: YouTube
  url: https://www.youtube.com/user/AmazonWebServices
- title: ''
  type: StackOverflow
  url: https://stackoverflow.com/questions/tagged/elasticache
- title: ''
  type: KnowledgeCenter
  url: https://repost.aws/knowledge-center
- title: ''
  type: Contact
  url: https://aws.amazon.com/contact-us/
- title: ''
  type: SpectralRules
  url: rules/amazon-elasticache-spectral-rules.yml
- title: ''
  type: NaftikoCapability
  url: capabilities/amazon-elasticache-capability.yaml
- title: ''
  type: NaftikoCapability
  url: capabilities/shared/api.yaml
- title: ''
  type: Vocabulary
  url: vocabulary/amazon-elasticache-vocabulary.yaml
created: '2024-01-15'
description: Amazon ElastiCache is a fully managed in-memory caching service supporting Redis and Memcached. ElastiCache makes it easy to deploy, operate, and scale popular open-source compatible in-memory data stores, improving the performance of web applications.
features:
- description: Fully managed Redis with replication, clustering, and persistence
  name: Redis Support
- description: Fully managed Memcached for simple distributed caching
  name: Memcached Support
- description: Automatic failover with Multi-AZ replication groups
  name: Multi-AZ Replication
- description: Encryption at-rest and in-transit for compliance requirements
  name: Encryption
- description: Scheduled automatic backups with point-in-time recovery
  name: Automatic Backups
image: https://a0.awsstatic.com/libra-css/images/logos/aws_logo_smile_1200x630.png
integrations:
- description: Connect ElastiCache clusters to EC2-hosted applications
  name: Amazon EC2
- description: Cache RDS query results to reduce database load
  name: Amazon RDS
- description: Access ElastiCache from serverless Lambda functions
  name: Amazon Lambda
- description: Use ElastiCache as shared cache for Kubernetes workloads
  name: Amazon EKS
jsonld:
- class_count: 0
  name: Amazon Elasticache Context
  property_count: 3
  slug: amazon-elasticache-context
layout: provider
modified: '2026-04-19'
name: Amazon ElastiCache
rules:
- name: Amazon ElastiCache API Rules
  rule_count: 20
  severity_counts:
    error: 10
    hint: 0
    info: 1
    warn: 9
  slug: amazon-elasticache-spectral-rules
skills: []
slug: amazon-elasticache
solutions: []
tags:
- Amazon Web Services
- AWS
- Caching
- Database
- ElastiCache
- In-Memory
- Memcached
- Redis
url: https://aws.amazon.com/elasticache/
use_cases:
- description: Store and manage user session data for web applications
  name: Session Management
- description: Cache expensive database queries to reduce latency
  name: Database Query Caching
- description: Process and cache real-time data streams for analytics dashboards
  name: Real-Time Analytics
- description: Build real-time leaderboards and gaming backends with Redis sorted sets
  name: Leaderboards and Gaming
---
