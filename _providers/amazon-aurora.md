---
api_count: 1
apis:
- description: REST management API for Amazon Aurora covering DB clusters, DB instances, cluster snapshots, parameter groups, custom endpoints, and global database management.
  name: Amazon Aurora API
  slug: amazon-aurora-api
capabilities:
- description: Workflow capability for managing Amazon Aurora relational database clusters including creation, scaling, snapshots, and global database configurations.
  name: Relational Database Management Workflow
  slug: relational-database-management
common: []
created: '2024-01-15'
description: Amazon Aurora is a MySQL and PostgreSQL-compatible relational database built for the cloud that combines the performance and availability of traditional enterprise databases with the simplicity and cost-effectiveness of open source databases.
features:
- MySQL and PostgreSQL compatible relational database engine
- Up to 5x throughput of standard MySQL and 3x of standard PostgreSQL
- Auto-scaling storage from 10GB to 128TB
- Up to 15 low-latency read replicas
- Aurora Serverless for intermittent and unpredictable workloads
- Aurora Global Database for multi-region deployments
- Continuous backup to Amazon S3 with point-in-time recovery
- Fast database cloning for testing and development
- Parallel query for faster analytical queries
- Machine learning integration through Aurora ML
image: https://kinlane-productions.s3.amazonaws.com/apis-json/apis-json-logo.jpg
integrations:
- Amazon RDS
- Amazon S3
- AWS Lambda
- Amazon CloudWatch
- AWS IAM
- Amazon VPC
- AWS KMS
- AWS Secrets Manager
- Amazon SageMaker
- AWS DMS
jsonld:
- class_count: 0
  name: Amazon Aurora Context
  property_count: 4
  slug: amazon-aurora-context
layout: provider
modified: '2026-04-19'
name: Amazon Aurora
rules:
- name: Amazon Aurora API Rules
  rule_count: 14
  severity_counts:
    error: 8
    hint: 0
    info: 0
    warn: 6
  slug: amazon-aurora-spectral-rules
skills: []
slug: amazon-aurora
solutions: []
tags:
- Amazon Aurora
- MySQL
- PostgreSQL
- Relational Database
- AWS
url: https://raw.githubusercontent.com/api-evangelist/amazon-aurora/refs/heads/main/apis.yml
use_cases:
- Enterprise applications requiring high availability and durability
- SaaS applications needing scalable multi-tenant databases
- E-commerce platforms with variable traffic patterns
- Financial applications requiring ACID compliance
- Global applications needing low-latency multi-region access
- Development and testing with fast database cloning
---
