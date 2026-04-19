---
api_count: 1
apis:
- description: The Amazon AppFlow API enables programmatic creation and management of data flows between SaaS applications and AWS services, including configuring connectors, flow definitions, triggers, and data map
  name: Amazon AppFlow API
  slug: ''
capabilities:
- description: Workflow capability for data engineers and integration architects who need to orchestrate, monitor, and manage SaaS-to-AWS data flows using Amazon AppFlow. Combines flow lifecycle management, connecto
  name: Amazon AppFlow Data Integration
  slug: data-integration
common:
- title: ''
  type: Portal
  url: https://console.aws.amazon.com/
- title: ''
  type: DeveloperPortal
  url: https://aws.amazon.com/appflow/
- title: ''
  type: Documentation
  url: https://docs.aws.amazon.com/appflow/
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
  url: https://aws.amazon.com/blogs/aws/category/application-integration/amazon-appflow/
- title: ''
  type: GitHubOrganization
  url: https://github.com/aws
- title: ''
  type: Console
  url: https://console.aws.amazon.com/appflow
- title: ''
  type: SignUp
  url: https://portal.aws.amazon.com/billing/signup
- title: ''
  type: Login
  url: https://signin.aws.amazon.com/
- title: ''
  type: StatusPage
  url: https://status.aws.amazon.com/
- title: ''
  type: FAQ
  url: https://repost.aws/knowledge-center
- title: ''
  type: YouTube
  url: https://www.youtube.com/user/AmazonWebServices
- title: ''
  type: StackOverflow
  url: https://stackoverflow.com/questions/tagged/amazon-appflow
- title: ''
  type: Contact
  url: https://aws.amazon.com/contact-us/
- title: ''
  type: Security
  url: https://aws.amazon.com/security/
- title: ''
  type: Compliance
  url: https://aws.amazon.com/compliance/
- title: ''
  type: SpectralRules
  url: rules/amazon-appflow-spectral-rules.yml
- title: ''
  type: Vocabulary
  url: vocabulary/amazon-appflow-vocabulary.yaml
- title: ''
  type: NaftikoCapability
  url: capabilities/data-integration.yaml
- title: ''
  type: NaftikoCapability
  url: capabilities/shared/appflow-api.yaml
created: '2024-01-15'
description: Amazon AppFlow is a fully managed integration service that enables you to securely transfer data between SaaS applications like Salesforce, SAP, Zendesk, Slack, and ServiceNow, and AWS services like Amazon S3 and Amazon Redshift, in just a few clicks.
features:
- description: Create data flows between SaaS applications and AWS services without writing code.
  name: No-Code Data Flows
- description: Schedule data flows to run at configurable intervals using cron or rate expressions.
  name: Scheduled Transfers
- description: Trigger data flows in response to business events from connected SaaS applications.
  name: Event-Triggered Flows
- description: Manually trigger data flows for ad-hoc data transfers.
  name: On-Demand Execution
- description: Apply field mapping, filtering, masking, merging, and arithmetic transformations during transfer.
  name: Data Transformations
- description: Transfer only new or changed records since the last flow run using datetime-based incremental pulls.
  name: Incremental Data Pull
- description: Register custom Lambda-backed connectors for proprietary or unsupported data sources.
  name: Custom Connectors
- description: Automatically catalog transferred data in AWS Glue Data Catalog for discoverability.
  name: Data Catalog Integration
- description: Encrypt data in transit and at rest using AWS KMS customer-managed keys.
  name: KMS Encryption
- description: Transfer data privately over AWS PrivateLink without traversing the public internet.
  name: Private Link Support
image: https://kinlane-productions.s3.amazonaws.com/apis-json/apis-json-logo.jpg
integrations:
- description: Bidirectional data transfer between Salesforce CRM and AWS services.
  name: Salesforce
- description: Transfer data from SAP ERP systems via SAPOData connector.
  name: SAP
- description: Sync ServiceNow ITSM data to AWS for analytics and reporting.
  name: ServiceNow
- description: Export Slack workspace data to Amazon S3.
  name: Slack
- description: Transfer Zendesk customer support tickets and data to AWS.
  name: Zendesk
- description: Import Marketo marketing automation data into Amazon Redshift or S3.
  name: Marketo
- description: Export Google Analytics data to Amazon S3 for custom analytics pipelines.
  name: Google Analytics
- description: Use Amazon S3 as both source and destination for AppFlow data flows.
  name: Amazon S3
- description: Load SaaS data directly into Amazon Redshift for SQL analytics.
  name: Amazon Redshift
- description: Send AppFlow data to Amazon EventBridge for event-driven architectures.
  name: Amazon EventBridge
- description: Catalog AppFlow output data automatically in AWS Glue Data Catalog.
  name: AWS Glue
- description: Feed SaaS data into SageMaker Data Wrangler for ML preparation.
  name: Amazon SageMaker
jsonld:
- class_count: 61
  name: Amazon Appflow Context
  property_count: 120
  slug: amazon-appflow-context
layout: provider
modified: '2026-04-19'
name: Amazon AppFlow
rules:
- name: Amazon AppFlow API Rules
  rule_count: 34
  severity_counts:
    error: 17
    hint: 0
    info: 2
    warn: 15
  slug: amazon-appflow-spectral-rules
skills: []
slug: amazon-appflow
solutions: []
tags:
- AWS
- Connectors
- Data Flow
- Data Integration
- ETL
- Integration
- SaaS
- Data Transfer
url: https://raw.githubusercontent.com/api-evangelist/amazon-appflow/refs/heads/main/apis.yml
use_cases:
- description: Consolidate marketing, sales, and support data from Salesforce, Marketo, and ServiceNow into Amazon Redshift or S3 for unified customer analytics.
  name: Customer 360
- description: Ingest SaaS data into Amazon SageMaker Data Wrangler for machine learning feature engineering and model training.
  name: ML Data Preparation
- description: Load SaaS application data into Amazon S3 data lakes for centralized analytics and reporting.
  name: Data Lake Ingestion
- description: Transfer Salesforce data in near real-time to Amazon Redshift for operational dashboards and BI reporting.
  name: Real-Time Analytics
- description: Automate workflows by triggering data flows when records are created or updated in SaaS applications.
  name: Cross-Application Automation
- description: Securely extract and archive regulated data from SaaS applications into encrypted AWS storage for compliance auditing.
  name: Data Compliance
---
