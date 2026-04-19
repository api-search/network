---
api_count: 1
apis:
- description: REST management API for Amazon Aurora DSQL covering cluster creation, configuration, multi-region deployments, and connection endpoint management.
  name: Amazon Aurora DSQL API
  slug: amazon-aurora-dsql-api
capabilities:
- description: Workflow capability for creating and managing distributed SQL clusters with Amazon Aurora DSQL including multi-region configurations.
  name: Distributed SQL Management Workflow
  slug: distributed-sql-management
common: []
created: '2026-03-16'
description: Amazon Aurora DSQL is a distributed SQL database service optimized for transactional workloads. It provides a serverless, fully managed PostgreSQL-compatible database with built-in high availability, scalability, and global distribution capabilities.
features:
- Serverless PostgreSQL-compatible distributed SQL database
- Automatic scaling with no database instances to manage
- Multi-region active-active replication for global distribution
- Built-in high availability with automatic failover
- Pay-per-use pricing based on I/O and storage
- Standard PostgreSQL client compatibility
- Transactional consistency across distributed nodes
- Integrated with AWS IAM for authentication
- Automatic software patching and maintenance
- Point-in-time recovery with continuous backups
image: https://kinlane-productions.s3.amazonaws.com/apis-json/apis-json-logo.jpg
integrations:
- Amazon VPC
- AWS IAM
- Amazon CloudWatch
- AWS CloudTrail
- Amazon RDS
- AWS KMS
- Amazon Route 53
- AWS PrivateLink
- Amazon S3
- AWS Secrets Manager
jsonld:
- class_count: 4
  name: Amazon Aurora Dsql Context
  property_count: 0
  slug: amazon-aurora-dsql-context
layout: provider
modified: '2026-04-19'
name: Amazon Aurora DSQL
rules:
- name: Amazon Aurora DSQL API Rules
  rule_count: 10
  severity_counts:
    error: 5
    hint: 0
    info: 0
    warn: 5
  slug: amazon-aurora-dsql-spectral-rules
skills: []
slug: amazon-aurora-dsql
solutions: []
tags:
- Amazon Aurora DSQL
- Distributed SQL
- PostgreSQL
- Serverless
- AWS
url: https://raw.githubusercontent.com/api-evangelist/amazon-aurora-dsql/refs/heads/main/apis.yml
use_cases:
- Build globally distributed transactional applications
- Run PostgreSQL workloads without managing instances
- Deploy active-active multi-region database architectures
- Migrate PostgreSQL applications to serverless infrastructure
- Build applications requiring strong consistency at global scale
- Implement high-throughput transactional microservices
---
