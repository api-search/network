---
api_count: 1
apis:
- description: The AWS Data Pipeline API provides a web service for processing and moving data between different AWS compute and storage services as well as on-premises data sources at specified intervals. The API a
  name: AWS Data Pipeline API
  slug: aws-data-pipeline-api
capabilities:
- description: ''
  name: Etl Pipeline Operations
  slug: etl-pipeline-operations
common:
- title: ''
  type: Portal
  url: https://aws.amazon.com/datapipeline/
- title: ''
  type: DeveloperPortal
  url: https://aws.amazon.com/datapipeline/
- title: ''
  type: Documentation
  url: https://docs.aws.amazon.com/datapipeline/
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
  type: GitHubOrganization
  url: https://github.com/aws
- title: ''
  type: Console
  url: https://console.aws.amazon.com/datapipeline/
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
  type: Contact
  url: https://aws.amazon.com/contact-us/
- title: ''
  type: SpectralRules
  url: rules/amazon-data-pipeline-spectral-rules.yml
- title: ''
  type: Vocabulary
  url: vocabulary/amazon-data-pipeline-vocabulary.yaml
- title: ''
  type: NaftikoCapability
  url: capabilities/etl-pipeline-operations.yaml
- title: ''
  type: NaftikoCapability
  url: capabilities/shared/data-pipeline.yaml
created: '2024-01-15'
description: AWS Data Pipeline is a web service that helps you reliably process and move data between different AWS compute and storage services, as well as on-premises data sources, at specified intervals. With AWS Data Pipeline, you can regularly access your data where it is stored, transform and process it at scale, and efficiently transfer the results to AWS services such as Amazon S3, Amazon RDS, Amazon DynamoDB, and Amazon EMR. It supports data-driven workflows with retry, failure handling, and scheduling capabilities.
features:
- description: Define complex data processing workflows with activities, data nodes, schedules, and preconditions using a declarative pipeline definition.
  name: Data-Driven Workflows
- description: Move and transform data between Amazon S3, Amazon RDS, Amazon DynamoDB, Amazon Redshift, and Amazon EMR in a single pipeline.
  name: Multi-Service Integration
- description: Schedule pipeline runs at fixed intervals (hourly, daily, weekly) or trigger them based on data availability preconditions.
  name: Flexible Scheduling
- description: Configure automatic retries for failed activities with configurable retry intervals, timeout settings, and failure notifications.
  name: Automated Retry and Failure Handling
- description: Process data from on-premises databases and file systems using the Data Pipeline Task Runner agent installed locally.
  name: On-Premises Data Support
- description: Launch and manage Amazon EMR clusters as pipeline resources to run Hive, Pig, and MapReduce jobs as part of data workflows.
  name: EMR Integration
- description: Manage active and latest pipeline definition versions, enabling updates to running pipelines without disrupting current execution.
  name: Pipeline Versioning
image: https://kinlane-productions.s3.amazonaws.com/apis-json/apis-json-logo.jpg
integrations:
- description: Primary data node type for reading input data and writing output data in pipeline ETL activities using S3DataNode.
  name: Amazon S3
- description: Managed Hadoop/Spark cluster resource for running large-scale data processing activities including Hive, Pig, and MapReduce jobs.
  name: Amazon EMR
- description: Relational database data node for SQL-based data extraction and loading between RDS instances and S3 or Redshift.
  name: Amazon RDS
- description: NoSQL data node for importing and exporting DynamoDB table data in pipeline activities for batch processing workflows.
  name: Amazon DynamoDB
- description: Data warehouse target for loading processed pipeline output data for business intelligence and analytics queries.
  name: Amazon Redshift
- description: Modern alternative managed ETL service that can complement or replace Data Pipeline for serverless data transformation workflows.
  name: AWS Glue
- description: Monitor pipeline execution status, set up alarms for pipeline failures, and track activity completion metrics.
  name: Amazon CloudWatch
jsonld:
- class_count: 0
  name: Amazon Data Pipeline Context
  property_count: 30
  slug: amazon-data-pipeline-context
layout: provider
modified: '2026-04-19'
name: Amazon Data Pipeline
rules:
- name: Amazon Data Pipeline API Rules
  rule_count: 22
  severity_counts:
    error: 13
    hint: 0
    info: 4
    warn: 5
  slug: amazon-data-pipeline-spectral-rules
skills: []
slug: amazon-data-pipeline
solutions: []
tags:
- AWS
- Data Processing
- ETL
- Workflows
- Data Pipeline
- Automation
url: https://raw.githubusercontent.com/api-evangelist/amazon-data-pipeline/refs/heads/main/apis.yml
use_cases:
- description: Schedule daily extraction, transformation, and loading of data from relational databases into S3 or Redshift for analytics processing.
  name: Daily ETL Workflows
- description: Process application and server log files from S3 using EMR activities to generate aggregated reports and analytics datasets.
  name: Log Processing Pipelines
- description: Migrate data between on-premises databases and AWS managed database services using scheduled pipeline activities.
  name: Database Migration
- description: Automate the ingestion and transformation of raw data into structured formats in S3 data lakes for downstream analytics.
  name: Data Lake Ingestion
- description: Replicate DynamoDB tables or S3 data across AWS regions using scheduled pipeline copy activities for disaster recovery.
  name: Cross-Region Data Replication
---
