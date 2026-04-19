---
api_count: 1
apis:
- description: The Amazon Inspector API provides programmatic access to vulnerability management for scanning EC2 instances, container images, and Lambda functions for software vulnerabilities and network exposure.
  name: AWS Amazon Inspector API
  slug: aws-inspector-api
capabilities:
- description: Unified capability for Security Engineer, Cloud Security Engineer to manage vulnerability scanning for ec2, container images, and lambda functions operations.
  name: Amazon Inspector - Security Vulnerability Management
  slug: security-vulnerability-management
common:
- title: ''
  type: Portal
  url: https://aws.amazon.com/inspector/
- title: ''
  type: Website
  url: https://aws.amazon.com/inspector/
- title: ''
  type: Documentation
  url: https://docs.aws.amazon.com/inspector/
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
  url: https://aws.amazon.com/blogs/security/category/security-identity-compliance/amazon-inspector/
- title: ''
  type: GitHubOrganization
  url: https://github.com/aws
- title: ''
  type: Console
  url: https://console.aws.amazon.com/inspector/v2/home
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
  url: rules/amazon-inspector-spectral-rules.yml
- title: ''
  type: NaftikoCapability
  url: capabilities/shared/inspector.yaml
- title: ''
  type: NaftikoCapability
  url: capabilities/security-vulnerability-management.yaml
- title: ''
  type: Vocabulary
  url: vocabulary/amazon-inspector-vocabulary.yaml
- title: ''
  type: JSONLD
  url: json-ld/amazon-inspector-context.jsonld
created: '2026-03-16'
description: Amazon Inspector is an automated vulnerability management service that continually scans AWS workloads for software vulnerabilities and unintended network exposure, providing detailed findings and prioritized remediation guidance.
features:
- description: Continuously scans EC2, container images, and Lambda functions for software vulnerabilities.
  name: Automated Vulnerability Scanning
- description: Ranks vulnerabilities by exploitability and impact to prioritize remediation.
  name: Risk Scoring
- description: Generates software bill of materials for scanned workloads.
  name: SBOM Export
- description: Manages vulnerability scanning across all accounts in an AWS Organization.
  name: Multi-Account Support
image: https://kinlane-productions.s3.amazonaws.com/apis-json/apis-json-logo.jpg
integrations:
- description: Automatically scans container images stored in Elastic Container Registry.
  name: Amazon ECR
- description: Sends all findings to Security Hub for centralized visibility.
  name: AWS Security Hub
- description: Manages Inspector across all organizational accounts.
  name: AWS Organizations
jsonld:
- class_count: 102
  name: Amazon Inspector Context
  property_count: 226
  slug: amazon-inspector-context
layout: provider
modified: '2026-04-19'
name: Amazon Inspector
rules:
- name: Amazon Inspector API Rules
  rule_count: 14
  severity_counts:
    error: 8
    hint: 0
    info: 1
    warn: 5
  slug: amazon-inspector-spectral-rules
skills: []
slug: amazon-inspector
solutions: []
tags:
- AWS
- Compliance
- Container Security
- EC2
- Lambda
- Security
- Vulnerability Scanning
url: https://raw.githubusercontent.com/api-evangelist/amazon-inspector/refs/heads/main/apis.yml
use_cases:
- description: Automatically scan container images in ECR during build pipelines.
  name: CI/CD Security Scanning
- description: Generate vulnerability reports for SOC 2, PCI DSS compliance.
  name: Compliance Reporting
- description: Prioritize OS patches based on exploitability scores.
  name: Patch Prioritization
---
