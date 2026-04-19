---
api_count: 1
apis:
- description: The AWS License Manager API provides programmatic access to create and manage license configurations, license associations, grants, tokens, and license reports for managing software licenses across AW
  name: AWS License Manager API
  slug: aws-license-manager-api
capabilities:
- description: Unified workflow capability for Amazon License Manager combining resource management and operations.
  name: Amazon License Manager Workflow
  slug: amazon-license-manager-workflow
common:
- title: ''
  type: Portal
  url: https://aws.amazon.com/license-manager/
- title: ''
  type: Portal
  url: https://aws.amazon.com/license-manager/
- title: ''
  type: Documentation
  url: https://docs.aws.amazon.com/license-manager/
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
  url: https://aws.amazon.com/blogs/mt/tag/aws-license-manager/
- title: ''
  type: GitHubOrganization
  url: https://github.com/aws
- title: ''
  type: Console
  url: https://console.aws.amazon.com/license-manager/
- title: ''
  type: SignUp
  url: https://portal.aws.amazon.com/billing/signup
- title: ''
  type: Login
  url: https://signin.aws.amazon.com/
- title: ''
  type: Status
  url: https://health.aws.amazon.com/health/status
- title: ''
  type: Contact
  url: https://aws.amazon.com/contact-us/
- title: ''
  type: SpectralRules
  url: rules/amazon-license-manager-spectral-rules.yml
- title: ''
  type: NaftikoCapability
  url: capabilities/amazon-license-manager-workflow.yaml
- title: ''
  type: Vocabulary
  url: vocabulary/amazon-license-manager-vocabulary.yaml
created: '2026-03-16'
description: AWS License Manager makes it easier to manage licenses in AWS and on-premises servers from software vendors such as Microsoft, SAP, Oracle, and IBM. It helps you control your licensing costs by letting you create rules that emulate the terms of your licensing agreements.
features:
- description: Define licensing rules based on software attributes and enforce them during instance launches.
  name: License Rule Enforcement
- description: Track license usage across AWS and on-premises environments from a central dashboard.
  name: License Tracking
- description: Discover software inventory across multiple AWS accounts in an AWS Organization.
  name: Cross-Account Discovery
- description: Generate license compliance reports for auditors and software vendors.
  name: Automated Compliance Reports
- description: Use existing on-premises software licenses on EC2 with BYOL programs.
  name: Bring Your Own License (BYOL)
image: https://kinlane-productions.s3.amazonaws.com/apis-json/apis-json-logo.jpg
integrations:
- description: Discover software inventory on EC2 instances using Systems Manager inventory.
  name: AWS Systems Manager
- description: Manage licenses across all accounts in an AWS Organization from a single pane.
  name: AWS Organizations
- description: Access software licenses purchased through AWS Marketplace.
  name: AWS Marketplace
jsonld:
- class_count: 1
  name: Amazon License Manager Context
  property_count: 7
  slug: amazon-license-manager-context
layout: provider
modified: '2026-04-19'
name: Amazon License Manager
rules:
- name: Amazon License Manager API Rules
  rule_count: 16
  severity_counts:
    error: 9
    hint: 0
    info: 0
    warn: 7
  slug: amazon-license-manager-spectral-rules
skills: []
slug: amazon-license-manager
solutions: []
tags:
- AWS
- Compliance
- Cost Management
- License Management
- Software Licensing
url: https://raw.githubusercontent.com/api-evangelist/amazon-license-manager/refs/heads/main/apis.yml
use_cases:
- description: Ensure software deployments comply with license agreements across your AWS estate.
  name: License Compliance
- description: Track license usage to identify unused licenses and optimize software spend.
  name: Cost Optimization
- description: Generate detailed license reports for software vendor audits.
  name: Vendor Audit Preparation
---
