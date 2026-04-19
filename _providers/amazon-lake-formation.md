---
api_count: 1
apis:
- description: The AWS Lake Formation API provides programmatic access to create and manage data lakes, configure data permissions and access controls, register data sources, and manage data catalog resources for ce
  name: Amazon Lake Formation API
  slug: ''
capabilities:
- description: Unified workflow capability for Amazon Lake Formation combining resource management and operations.
  name: Amazon Lake Formation Workflow
  slug: amazon-lake-formation-workflow
common:
- title: ''
  type: Blog
  url: https://aws.amazon.com/blogs/big-data/category/analytics/aws-lake-formation/
- title: ''
  type: Support
  url: https://aws.amazon.com/premiumsupport/
- title: ''
  type: Console
  url: https://console.aws.amazon.com/lakeformation/home
- title: ''
  type: CLI
  url: https://docs.aws.amazon.com/cli/latest/reference/lakeformation/
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
  url: https://aws.amazon.com/lake-formation/
- title: ''
  type: Documentation
  url: https://docs.aws.amazon.com/lake-formation/
- title: ''
  type: Pricing
  url: https://aws.amazon.com/lake-formation/pricing/
- title: ''
  type: GettingStarted
  url: https://aws.amazon.com/lake-formation/getting-started/
- title: ''
  type: FAQ
  url: https://aws.amazon.com/lake-formation/faqs/
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
  url: rules/amazon-lake-formation-spectral-rules.yml
- title: ''
  type: NaftikoCapability
  url: capabilities/amazon-lake-formation-workflow.yaml
- title: ''
  type: Vocabulary
  url: vocabulary/amazon-lake-formation-vocabulary.yaml
created: '2024-01-15'
description: AWS Lake Formation is a service that makes it easy to set up a secure data lake in days, providing centralized governance and security for data stored in Amazon S3 and other AWS data stores with fine-grained access control.
features:
- description: Grant table, column, row, and cell-level permissions to data in your data lake.
  name: Fine-Grained Access Control
- description: Centrally define and manage security, governance, and auditing policies across the data lake.
  name: Centralized Governance
- description: Integrates with AWS Glue Data Catalog to discover, catalog, and share metadata.
  name: Data Catalog Integration
- description: Securely share data across AWS accounts without copying it.
  name: Cross-Account Data Sharing
- description: ACID transactions and automatic compaction for governed tables stored in S3.
  name: Governed Tables
image: https://a0.awsstatic.com/libra-css/images/logos/aws_logo_smile_1200x630.png
integrations:
- description: Manage and secure data stored in S3 as the data lake storage layer.
  name: Amazon S3
- description: Use Glue Data Catalog as the metadata store and Glue ETL for data transformation.
  name: AWS Glue
- description: Query data lake data using Athena with Lake Formation access controls enforced.
  name: Amazon Athena
- description: Use Redshift Spectrum to query data lake with Lake Formation permissions.
  name: Amazon Redshift
jsonld:
- class_count: 2
  name: Amazon Lake Formation Context
  property_count: 7
  slug: amazon-lake-formation-context
layout: provider
modified: '2026-04-19'
name: Amazon Lake Formation
rules:
- name: Amazon Lake Formation API Rules
  rule_count: 16
  severity_counts:
    error: 9
    hint: 0
    info: 0
    warn: 7
  slug: amazon-lake-formation-spectral-rules
skills: []
slug: amazon-lake-formation
solutions: []
tags:
- Access Control
- Analytics
- AWS
- Data Governance
- Data Lake
- S3
url: https://aws.amazon.com/lake-formation/
use_cases:
- description: Implement fine-grained access control for data stored in S3 with row and column-level security.
  name: Data Lake Security
- description: Enable business users to discover and access approved data without manual provisioning.
  name: Self-Service Analytics
- description: Share data lake resources across AWS accounts and organizations.
  name: Cross-Account Data Sharing
---
