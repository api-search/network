---
api_count: 1
apis:
- description: The AWS IAM Access Analyzer API provides programmatic access to create and manage analyzers, findings, archive rules, and policy validations to identify and remediate unintended resource access across
  name: AWS IAM Access Analyzer API
  slug: aws-access-analyzer-api
capabilities:
- description: Unified capability for security teams to manage access analyzers, review findings, validate policies, and enforce least-privilege access controls across AWS accounts.
  name: Amazon IAM Access Analyzer - Access Security Management
  slug: access-security-management
common:
- title: ''
  type: Portal
  url: https://aws.amazon.com/iam/features/analyze-access/
- title: ''
  type: Website
  url: https://aws.amazon.com/iam/
- title: ''
  type: Documentation
  url: https://docs.aws.amazon.com/IAM/latest/UserGuide/what-is-access-analyzer.html
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
  url: https://aws.amazon.com/blogs/security/tag/iam-access-analyzer/
- title: ''
  type: GitHubOrganization
  url: https://github.com/aws
- title: ''
  type: Console
  url: https://console.aws.amazon.com/access-analyzer/
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
  url: rules/amazon-iam-access-analyzer-spectral-rules.yml
- title: ''
  type: NaftikoCapability
  url: capabilities/shared/iam-access-analyzer.yaml
- title: ''
  type: NaftikoCapability
  url: capabilities/access-security-management.yaml
- title: ''
  type: Vocabulary
  url: vocabulary/amazon-iam-access-analyzer-vocabulary.yaml
- title: ''
  type: JSONLD
  url: json-ld/amazon-iam-access-analyzer-context.jsonld
created: '2026-03-16'
description: AWS IAM Access Analyzer helps you set, verify, and refine your IAM policies by providing a suite of capabilities including findings for external, internal, and unused access, basic and custom policy checks for validating policies, and policy generation to generate fine-grained policies. It uses automated reasoning to identify resources shared with external entities and helps implement least privilege access across your AWS environment.
features:
- description: Identifies resources shared with external entities outside your AWS organization using automated reasoning.
  name: External Access Analysis
- description: Identifies which principals within your organization have access to selected resources.
  name: Internal Access Analysis
- description: Identifies unused IAM roles, access keys, console passwords, and unused service permissions.
  name: Unused Access Analysis
- description: Validates IAM policies against best practices and custom security standards before deployment.
  name: Policy Validation
- description: Generates fine-grained IAM policies based on actual access activity logged in AWS CloudTrail.
  name: Policy Generation
- description: Preview public and cross-account access to resources before deploying permission changes.
  name: Access Preview
- description: Automatically archive findings that match specified criteria to reduce noise.
  name: Archive Rules
image: https://kinlane-productions.s3.amazonaws.com/apis-json/apis-json-logo.jpg
integrations:
- description: Uses CloudTrail activity logs to generate least-privilege IAM policies based on actual usage.
  name: AWS CloudTrail
- description: Publishes Access Analyzer findings to Security Hub for centralized security monitoring.
  name: AWS Security Hub
- description: Analyzes access across all accounts in an AWS Organization for comprehensive governance.
  name: AWS Organizations
- description: Triggers re-scanning of resources when configuration changes are detected.
  name: AWS Config
- description: Publishes finding events to EventBridge for automated security workflow responses.
  name: Amazon EventBridge
jsonld:
- class_count: 116
  name: Amazon Iam Access Analyzer Context
  property_count: 146
  slug: amazon-iam-access-analyzer-context
layout: provider
modified: '2026-04-19'
name: Amazon IAM Access Analyzer
rules:
- name: Amazon IAM Access Analyzer API Rules
  rule_count: 23
  severity_counts:
    error: 10
    hint: 0
    info: 3
    warn: 10
  slug: amazon-iam-access-analyzer-spectral-rules
skills: []
slug: amazon-iam-access-analyzer
solutions: []
tags:
- Access Control
- AWS
- Compliance
- IAM
- Policy Management
- Security
url: https://raw.githubusercontent.com/api-evangelist/amazon-iam-access-analyzer/refs/heads/main/apis.yml
use_cases:
- description: Analyze actual API activity to generate minimal permission policies that implement least privilege access.
  name: Least Privilege Enforcement
- description: Continuously monitor for unintended external access to sensitive resources like S3 buckets and IAM roles.
  name: Security Compliance Auditing
- description: Integrate policy checks into deployment pipelines to catch overpermissive policies before they reach production.
  name: CI/CD Policy Validation
- description: Identify and remediate unused access across IAM users, roles, and service accounts organization-wide.
  name: Access Governance
- description: Identify all resources shared across AWS accounts and validate the intent of each cross-account permission.
  name: Cross-Account Access Review
---
