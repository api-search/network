---
api_count: 1
apis:
- description: REST management API for Amazon Audit Manager covering assessments, frameworks, controls, evidence, assessment reports, and account settings.
  name: Amazon Audit Manager API
  slug: amazon-audit-manager-api
capabilities:
- description: Workflow capability for conducting continuous compliance auditing with Amazon Audit Manager including assessment creation, evidence collection, and report generation.
  name: Compliance Auditing Workflow
  slug: compliance-auditing
common: []
created: '2026-03-16'
description: AWS Audit Manager helps you continuously audit your AWS usage to simplify how you assess risk and compliance with regulations and industry standards.
features:
- Continuous compliance monitoring with automated evidence collection
- Pre-built frameworks for SOC 2, PCI DSS, HIPAA, GDPR, and more
- Custom framework and control creation for internal policies
- Automated evidence collection from AWS Config, Security Hub, and CloudTrail
- Evidence folder organization by control and control set
- Assessment delegation to process owners and resource owners
- Assessment report generation in PDF format
- Multi-account support through AWS Organizations
- Evidence finder for cross-assessment evidence search
- Integration with AWS Security Hub for security findings
image: https://kinlane-productions.s3.amazonaws.com/apis-json/apis-json-logo.jpg
integrations:
- AWS Config
- AWS Security Hub
- AWS CloudTrail
- AWS IAM
- Amazon S3
- Amazon SNS
- AWS Organizations
- AWS KMS
- Amazon CloudWatch
- AWS Systems Manager
jsonld:
- class_count: 6
  name: Amazon Audit Manager Context
  property_count: 0
  slug: amazon-audit-manager-context
layout: provider
modified: '2026-04-19'
name: Amazon Audit Manager
rules:
- name: Amazon Audit Manager API Rules
  rule_count: 15
  severity_counts:
    error: 10
    hint: 0
    info: 0
    warn: 5
  slug: amazon-audit-manager-spectral-rules
skills: []
slug: amazon-audit-manager
solutions: []
tags:
- Amazon Audit Manager
- Compliance
- Audit
- Risk Management
- AWS
url: https://raw.githubusercontent.com/api-evangelist/amazon-audit-manager/refs/heads/main/apis.yml
use_cases:
- Automate SOC 2 compliance evidence collection
- Prepare for PCI DSS and HIPAA audits with continuous monitoring
- Build custom compliance frameworks for internal policies
- Delegate control reviews to business process owners
- Generate audit-ready reports for external auditors
- Monitor compliance posture across multiple AWS accounts
---
