---
api_count: 1
apis:
- description: The Amazon DataZone API provides programmatic access to create and manage data domains, data assets, data catalogs, projects, subscriptions, and governance policies for enterprise-wide data management
  name: Amazon DataZone API
  slug: amazon-datazone-api
capabilities:
- description: ''
  name: Data Catalog Operations
  slug: data-catalog-operations
common:
- title: ''
  type: Portal
  url: https://aws.amazon.com/datazone/
- title: ''
  type: DeveloperPortal
  url: https://aws.amazon.com/datazone/
- title: ''
  type: Documentation
  url: https://docs.aws.amazon.com/datazone/
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
  url: https://aws.amazon.com/blogs/big-data/
- title: ''
  type: GitHubOrganization
  url: https://github.com/aws
- title: ''
  type: Console
  url: https://console.aws.amazon.com/datazone/
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
  url: rules/amazon-datazone-spectral-rules.yml
- title: ''
  type: Vocabulary
  url: vocabulary/amazon-datazone-vocabulary.yaml
- title: ''
  type: NaftikoCapability
  url: capabilities/data-catalog-operations.yaml
- title: ''
  type: NaftikoCapability
  url: capabilities/shared/datazone.yaml
created: '2026-03-16'
description: Amazon DataZone is a data management service that helps you catalog, discover, govern, share, and analyze your data across your organization and beyond. It enables data producers and consumers to collaborate, with built-in governance, data catalog capabilities, and a business data catalog to organize and share data across your AWS environment. DataZone provides domain-based governance, project workspaces, subscription-based access control, and integration with AWS analytics services.
features:
- description: Central catalog where data producers publish assets and data consumers can discover, understand, and request access to data products.
  name: Business Data Catalog
- description: Organize data assets, users, and governance policies within domains that reflect your organizational structure and data ownership.
  name: Domain-Based Governance
- description: Built-in request/approval workflow for data consumers to request access to data assets with business justification and audit trail.
  name: Subscription Workflow
- description: Isolated project containers within domains where teams organize their data assets, environments, and members.
  name: Project Workspaces
- description: Automatically provision data access environments with Athena, Glue, Redshift, or other tools when subscriptions are approved.
  name: Analytics Environment Provisioning
- description: Automatically discover and import tables from AWS Glue Data Catalog into DataZone for cataloging and governance.
  name: Glue Data Catalog Integration
- description: Track data lineage across assets to understand data origins, transformations, and dependencies for trust and compliance.
  name: Data Lineage
image: https://kinlane-productions.s3.amazonaws.com/apis-json/apis-json-logo.jpg
integrations:
- description: DataZone integrates with Glue Data Catalog to automatically discover, import, and catalog Glue tables for sharing and governance.
  name: AWS Glue
- description: Catalog Redshift tables and views and govern cross-cluster data sharing through DataZone subscription workflows.
  name: Amazon Redshift
- description: DataZone environments provision Athena as a query engine for subscribers accessing S3-based data assets.
  name: Amazon Athena
- description: Catalog S3-based datasets in DataZone and control access through subscription-based Lake Formation permissions.
  name: Amazon S3
- description: DataZone uses Lake Formation for fine-grained column and row-level access control when subscriptions are approved.
  name: AWS Lake Formation
- description: IAM roles provide domain execution context and identity-based access control for DataZone resources and catalog operations.
  name: AWS IAM
jsonld:
- class_count: 0
  name: Amazon Datazone Context
  property_count: 26
  slug: amazon-datazone-context
layout: provider
modified: '2026-04-19'
name: Amazon DataZone
rules:
- name: Amazon DataZone API Rules
  rule_count: 20
  severity_counts:
    error: 13
    hint: 0
    info: 2
    warn: 5
  slug: amazon-datazone-spectral-rules
skills: []
slug: amazon-datazone
solutions: []
tags:
- AWS
- Data Catalog
- Data Governance
- Data Management
- Data Sharing
- Analytics
url: https://raw.githubusercontent.com/api-evangelist/amazon-datazone/refs/heads/main/apis.yml
use_cases:
- description: Build an internal data marketplace where business units publish their data products for discovery and consumption by other teams.
  name: Enterprise Data Marketplace
- description: Implement governed data access with approval workflows ensuring data consumers have proper authorization and business justification.
  name: Data Access Governance
- description: Share data assets across AWS accounts within an organization using DataZone's subscription and access management capabilities.
  name: Cross-Account Data Sharing
- description: Enable analysts to discover and access data independently through the DataZone catalog with automatic environment provisioning.
  name: Self-Service Analytics
- description: Maintain audit trails of data access, govern sensitive data assets, and enforce data residency policies through domain governance.
  name: Regulatory Data Compliance
---
