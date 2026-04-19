---
api_count: 3
apis:
- description: The Amazon Redshift API for managing clusters, snapshots, and configurations.
  name: Amazon Redshift API
  slug: ''
- description: The Amazon Redshift Data API for running SQL statements without managing connections. Supports asynchronous execution with IAM and Secrets Manager authentication.
  name: Amazon Redshift Data API
  slug: ''
- description: The Amazon Redshift Serverless API for managing serverless data warehouse workgroups, namespaces, and capacity without provisioning clusters.
  name: Amazon Redshift Serverless API
  slug: ''
capabilities:
- description: Data warehouse analytics workflow combining Redshift Data API for SQL execution, statement management, and database metadata exploration. Used by data analysts and engineers for ad-hoc queries, ETL pr
  name: Amazon Redshift Data Warehouse Analytics
  slug: data-warehouse-analytics
common:
- title: ''
  type: Blog
  url: https://aws.amazon.com/blogs/big-data/category/database/amazon-redshift/
- title: ''
  type: Support
  url: https://aws.amazon.com/premiumsupport/
- title: ''
  type: TermsOfService
  url: https://aws.amazon.com/service-terms/
- title: ''
  type: PrivacyPolicy
  url: https://aws.amazon.com/privacy/
- title: ''
  type: Documentation
  url: https://docs.aws.amazon.com/redshift/
- title: ''
  type: GettingStarted
  url: https://aws.amazon.com/redshift/getting-started/
- title: ''
  type: FAQ
  url: https://aws.amazon.com/redshift/faqs/
- title: ''
  type: Pricing
  url: https://aws.amazon.com/redshift/pricing/
- title: ''
  type: Console
  url: https://console.aws.amazon.com/redshift/
- title: ''
  type: StatusPage
  url: https://status.aws.amazon.com/
created: '2024-01-01'
description: Amazon Redshift is a fast, fully managed cloud data warehouse that makes it simple and cost-effective to analyze all your data using standard SQL and your existing Business Intelligence (BI) tools.
features:
- description: Distributed query execution across multiple nodes for petabyte-scale analytics with sub-second response times.
  name: Massively Parallel Processing
- description: Auto-scaling compute capacity without cluster provisioning, paying only for compute used during queries.
  name: Serverless Data Warehouse
- description: Run SQL statements without managing database connections using IAM-based authentication and asynchronous execution.
  name: Data API
- description: Query data across Amazon RDS, Aurora, and S3 data lakes without moving data using federated query capabilities.
  name: Federated Query
- description: Build, train, and deploy ML models directly in Redshift using SQL with Amazon SageMaker integration.
  name: Machine Learning Integration
- description: Automatically add transient capacity to handle bursts of concurrent queries without performance degradation.
  name: Concurrency Scaling
image: https://a0.awsstatic.com/libra-css/images/logos/aws_logo_smile_1200x630.png
integrations:
- description: Load data from and query data in S3 using COPY commands, Redshift Spectrum, and data lake integration.
  name: Amazon S3
- description: Automated ETL job orchestration and data catalog integration for data warehouse loading.
  name: AWS Glue
- description: Connect QuickSight directly to Redshift for serverless BI dashboards and visualizations.
  name: Amazon QuickSight
- description: Trigger Lambda functions from Redshift Data API results for event-driven data processing workflows.
  name: AWS Lambda
- description: Provision and manage Redshift clusters and serverless workgroups using Terraform infrastructure-as-code.
  name: Terraform
jsonld:
- class_count: 0
  name: Amazon Redshift Context
  property_count: 6
  slug: amazon-redshift-context
- class_count: 0
  name: Amazon Redshift Data Context
  property_count: 0
  slug: amazon-redshift-data-context
layout: provider
modified: '2026-04-18'
name: Amazon Redshift
rules:
- name: Amazon Redshift API Rules
  rule_count: 7
  severity_counts:
    error: 7
    hint: 0
    info: 0
    warn: 0
  slug: amazon-redshift-spectral-rules
skills: []
slug: amazon-redshift
solutions: []
tags:
- Analytics
- Big Data
- Cloud
- Data Lake
- Data Warehouse
- ETL
- Machine Learning
- Serverless
- SQL
url: https://raw.githubusercontent.com/api-evangelist/amazon-redshift/refs/heads/main/apis.yml
use_cases:
- description: Run complex analytical queries across petabytes of structured data for BI dashboards and reporting.
  name: Business Intelligence Analytics
- description: Query data directly in Amazon S3 using Redshift Spectrum without loading it into the warehouse.
  name: Data Lake Analytics
- description: Ingest streaming data and run near-real-time analytics on operational data for instant insights.
  name: Real-Time Analytics
- description: Transform and load large datasets using SQL-based ETL operations within the data warehouse.
  name: ETL Pipeline Processing
- description: Run on-demand analytical queries without provisioning clusters using Redshift Serverless and Data API.
  name: Serverless Ad-Hoc Queries
---
