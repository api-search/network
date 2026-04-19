---
api_count: 1
apis:
- description: REST management API for Amazon Athena covering query executions, named queries, work groups, data catalogs, databases, table metadata, and prepared statements.
  name: Amazon Athena API
  slug: amazon-athena-api
capabilities:
- description: Workflow capability for running and managing SQL analytics queries with Amazon Athena including query execution, named queries, work groups, and data catalog management.
  name: SQL Analytics Workflow
  slug: sql-analytics
common: []
created: '2024-01-15'
description: Amazon Athena is an interactive query service that makes it easy to analyze data in Amazon S3 using standard SQL. Athena is serverless, so there is no infrastructure to manage, and you pay only for the queries that you run.
features:
- Serverless SQL query execution against Amazon S3 data
- Pay-per-query pricing with no infrastructure management
- Support for standard ANSI SQL with complex joins and window functions
- Integration with AWS Glue Data Catalog for schema management
- Named queries for saving and reusing SQL statements
- Work groups for query isolation and cost management
- Prepared statements for parameterized query execution
- Multiple data format support including Parquet, ORC, JSON, CSV
- Query result caching for improved performance and cost reduction
- Fine-grained access control with IAM and Lake Formation
image: https://kinlane-productions.s3.amazonaws.com/apis-json/apis-json-logo.jpg
integrations:
- Amazon S3
- AWS Glue
- Amazon QuickSight
- AWS Lake Formation
- Amazon CloudWatch
- AWS IAM
- Amazon DynamoDB
- AWS Step Functions
- Amazon SageMaker
- Apache Spark
jsonld:
- class_count: 11
  name: Amazon Athena Context
  property_count: 0
  slug: amazon-athena-context
layout: provider
modified: '2026-04-19'
name: Amazon Athena
rules:
- name: Amazon Athena API Rules
  rule_count: 19
  severity_counts:
    error: 12
    hint: 0
    info: 0
    warn: 7
  slug: amazon-athena-spectral-rules
skills: []
slug: amazon-athena
solutions: []
tags:
- Amazon Athena
- SQL
- Analytics
- Serverless
- AWS
url: https://raw.githubusercontent.com/api-evangelist/amazon-athena/refs/heads/main/apis.yml
use_cases:
- Analyze log files and clickstream data stored in S3
- Run ad-hoc SQL queries on data lake without ETL
- Build serverless data pipelines and reporting solutions
- Query AWS service logs including CloudTrail, ELB, and VPC Flow Logs
- Perform cost analysis on AWS Cost and Usage Reports
- Enable self-service analytics for business intelligence teams
---
