---
api_count: 1
apis:
- description: API for creating and managing CloudTrail trails, event data stores, and channels for capturing AWS API activity and storing audit logs.
  name: Amazon CloudTrail API
  slug: ''
capabilities:
- description: Workflow for audit trail management using Amazon CloudTrail for Security Analyst personas.
  name: Amazon CloudTrail Audit Trail Management
  slug: audit-trail-management
common:
- title: ''
  type: Portal
  url: https://aws.amazon.com/
- title: ''
  type: Website
  url: https://aws.amazon.com/cloudtrail/
- title: ''
  type: Documentation
  url: https://docs.aws.amazon.com/awscloudtrail/latest/APIReference/
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
  url: https://aws.amazon.com/blogs/security/
- title: ''
  type: GitHubOrganization
  url: https://github.com/aws
- title: ''
  type: Console
  url: https://console.aws.amazon.com/cloudtrail/
- title: ''
  type: SignUp
  url: https://signin.aws.amazon.com/signup?request_type=register
- title: ''
  type: StatusPage
  url: https://health.aws.amazon.com/health/status
- title: ''
  type: YouTube
  url: https://www.youtube.com/user/AmazonWebServices
- title: ''
  type: StackOverflow
  url: https://stackoverflow.com/questions/tagged/aws-cloudtrail
- title: ''
  type: Contact
  url: https://aws.amazon.com/contact-us/
- title: ''
  type: Compliance
  url: https://aws.amazon.com/compliance/
- title: ''
  type: SpectralRules
  url: rules/amazon-cloudtrail-spectral-rules.yml
- title: ''
  type: Vocabulary
  url: vocabulary/amazon-cloudtrail-vocabulary.yaml
- title: ''
  type: NaftikoCapability
  url: capabilities/audit-trail-management.yaml
created: '2024-01-15'
description: AWS CloudTrail enables governance, compliance, operational auditing, and risk auditing of your AWS account by tracking user activity and API usage across AWS environments, hybrid setups, and multicloud deployments with immutable audit trails.
features:
- description: Consolidate activity events from AWS, external providers, on-premises, and SaaS into a unified audit trail.
  name: Event Aggregation
- description: Store audit-worthy events immutably to ensure tamper-proof compliance records.
  name: Immutable Audit Logs
- description: Detect unusual API activity patterns with anomaly detection on management and data events.
  name: CloudTrail Insights
- description: Investigate issues using SQL queries or natural language with Amazon Athena integration.
  name: SQL Query Support
- description: Create trails that capture events from all AWS regions in a single S3 bucket.
  name: Multi-Region Trails
image: https://kinlane-productions.s3.amazonaws.com/apis-json/apis-json-logo.jpg
integrations:
- description: Store CloudTrail logs in S3 buckets with lifecycle management.
  name: Amazon S3
- description: Query CloudTrail logs using SQL via Athena integration.
  name: Amazon Athena
- description: Stream CloudTrail events to CloudWatch Logs for real-time monitoring.
  name: Amazon CloudWatch
- description: Trigger Lambda functions based on CloudTrail events for automated response.
  name: AWS Lambda
- description: Send CloudTrail findings to Security Hub for centralized security management.
  name: AWS Security Hub
jsonld:
- class_count: 9
  name: Amazon Cloudtrail Context
  property_count: 21
  slug: amazon-cloudtrail-context
layout: provider
modified: '2026-04-19'
name: Amazon CloudTrail
rules:
- name: Amazon CloudTrail API Rules
  rule_count: 19
  severity_counts:
    error: 12
    hint: 0
    info: 1
    warn: 6
  slug: amazon-cloudtrail-spectral-rules
skills: []
slug: amazon-cloudtrail
solutions: []
tags:
- AWS
- CloudTrail
- Audit
- Compliance
- Governance
- Security
url: https://raw.githubusercontent.com/api-evangelist/amazon-cloudtrail/refs/heads/main/apis.yml
use_cases:
- description: Demonstrate adherence to SOC, PCI DSS, and HIPAA regulations with audit logs.
  name: Compliance Auditing
- description: Record and monitor user and API activity for security incident detection.
  name: Security Monitoring
- description: Investigate operational issues by querying historical API activity.
  name: Operational Debugging
- description: Track who made changes to AWS resources and when for governance accountability.
  name: Governance
---
