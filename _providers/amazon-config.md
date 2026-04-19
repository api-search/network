---
api_count: 1
apis:
- description: The AWS Config API provides 92 operations for managing configuration recording, evaluating resource compliance against rules, querying resource configurations, tracking configuration history, managing
  name: Amazon Config API
  slug: ''
capabilities:
- description: Workflow capability for AWS resource configuration tracking, compliance evaluation, configuration history auditing, and automated remediation using Amazon Config. Used by security engineers and compli
  name: Amazon Config Compliance and Governance
  slug: compliance-governance
common:
- title: ''
  type: Portal
  url: https://aws.amazon.com/
- title: ''
  type: Website
  url: https://aws.amazon.com/config/
- title: ''
  type: Documentation
  url: https://docs.aws.amazon.com/config/
- title: ''
  type: TermsOfService
  url: https://aws.amazon.com/service-terms/
- title: ''
  type: PrivacyPolicy
  url: https://aws.amazon.com/privacy/
- title: ''
  type: Support
  url: https://aws.amazon.com/support/
- title: ''
  type: Blog
  url: https://aws.amazon.com/blogs/mt/
- title: ''
  type: GitHubOrganization
  url: https://github.com/aws
- title: ''
  type: Console
  url: https://console.aws.amazon.com/config/
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
  type: YouTube
  url: https://www.youtube.com/user/AmazonWebServices
- title: ''
  type: StackOverflow
  url: https://stackoverflow.com/questions/tagged/aws-config
- title: ''
  type: Contact
  url: https://aws.amazon.com/contact-us/
- title: ''
  type: SpectralRules
  url: rules/amazon-config-spectral-rules.yml
- title: ''
  type: NaftikoCapability
  url: capabilities/compliance-governance.yaml
- title: ''
  type: Vocabulary
  url: vocabulary/amazon-config-vocabulary.yaml
created: '2024-01-15'
description: AWS Config provides a detailed view of the configuration of AWS resources in your AWS account. This includes how the resources are related to one another and how they were configured in the past, enabling assessment, auditing, and evaluation of configurations for compliance and security governance. It records configuration changes continuously, evaluates compliance against rules, and supports automated remediation of noncompliant resources.
features:
- description: Continuously record configuration changes to all supported AWS resources in your account with detailed configuration items.
  name: Configuration Recording
- description: Evaluate AWS resource configurations against desired settings using AWS-managed or custom Lambda-based rules.
  name: Config Rules
- description: Deploy collections of Config rules and remediation actions as a single unit across an AWS Organization.
  name: Conformance Packs
- description: View detailed configuration history for any AWS resource including who changed what and when.
  name: Configuration History
- description: Maintain a complete inventory of all AWS resources in your account with current and past configurations.
  name: Resource Inventory
- description: Automatically remediate noncompliant resources using SSM Automation documents triggered by Config rules.
  name: Automated Remediation
- description: Aggregate configuration and compliance data from multiple accounts and regions into a single view.
  name: Multi-Account Aggregation
- description: Use SQL-like queries to search across resource configurations and compliance states.
  name: Advanced Query
image: https://kinlane-productions.s3.amazonaws.com/apis-json/apis-json-logo.jpg
integrations:
- description: Correlate Config configuration items with CloudTrail API activity to understand who made changes.
  name: AWS CloudTrail
- description: Send Config compliance findings to Security Hub for centralized security posture management.
  name: AWS Security Hub
- description: Deliver configuration snapshots and history to S3 for long-term storage and analysis.
  name: Amazon S3
- description: Send notifications for compliance changes and configuration changes via SNS topics.
  name: Amazon SNS
- description: Use SSM Automation documents as remediation targets for Config rules.
  name: AWS Systems Manager
- description: Deploy Config rules and conformance packs across entire AWS Organizations for governance at scale.
  name: AWS Organizations
- description: Create custom Config rules using Lambda functions for organization-specific compliance requirements.
  name: AWS Lambda
jsonld:
- class_count: 227
  name: Amazon Config Context
  property_count: 326
  slug: amazon-config-context
layout: provider
modified: '2026-04-19'
name: Amazon Config
rules:
- name: Amazon Config API Rules
  rule_count: 22
  severity_counts:
    error: 8
    hint: 0
    info: 4
    warn: 10
  slug: amazon-config-spectral-rules
skills: []
slug: amazon-config
solutions: []
tags:
- Auditing
- AWS
- Compliance
- Configuration Management
- Governance
- Security
url: https://raw.githubusercontent.com/api-evangelist/amazon-config/refs/heads/main/apis.yml
use_cases:
- description: Continuously audit AWS resource configurations against security benchmarks like CIS, PCI DSS, and HIPAA.
  name: Security and Compliance Auditing
- description: Track who changed what configuration on which resource and when for change management and troubleshooting.
  name: Change Management
- description: Maintain an always-current inventory of all AWS resources for asset management and CMDB purposes.
  name: Resource Inventory
- description: Detect configuration drift from approved baselines and trigger alerts or automated remediation.
  name: Drift Detection
- description: Reconstruct the configuration state of resources at any point in time to aid incident investigation.
  name: Incident Investigation
- description: Enforce organization-wide governance policies using conformance packs deployed across all accounts.
  name: Governance at Scale
---
