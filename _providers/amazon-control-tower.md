---
api_count: 1
apis:
- description: The AWS Control Tower API provides programmatic access to manage landing zones, organizational units, accounts, controls (guardrails), and baselines within your AWS environment, enabling automated gov
  name: AWS Control Tower API
  slug: aws-control-tower-api
capabilities:
- description: ''
  name: Governance Operations
  slug: governance-operations
common:
- title: ''
  type: Portal
  url: https://aws.amazon.com/controltower/
- title: ''
  type: DeveloperPortal
  url: https://aws.amazon.com/controltower/
- title: ''
  type: Documentation
  url: https://docs.aws.amazon.com/controltower/
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
  url: https://aws.amazon.com/blogs/mt/category/management-tools/aws-control-tower/
- title: ''
  type: GitHubOrganization
  url: https://github.com/aws
- title: ''
  type: Console
  url: https://console.aws.amazon.com/controltower/
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
  type: Pricing
  url: https://aws.amazon.com/controltower/pricing/
- title: ''
  type: SpectralRules
  url: rules/amazon-control-tower-spectral-rules.yml
- title: ''
  type: Vocabulary
  url: vocabulary/amazon-control-tower-vocabulary.yaml
- title: ''
  type: NaftikoCapability
  url: capabilities/governance-operations.yaml
- title: ''
  type: NaftikoCapability
  url: capabilities/shared/control-tower.yaml
created: '2026-03-16'
description: AWS Control Tower provides the easiest way to set up and govern a secure, multi-account AWS environment based on best practices. It establishes a landing zone with pre-configured governance and guardrails, enabling organizations to maintain compliance and manage accounts at scale. With over 750 preconfigured controls, it automates account creation, OU registration, and compliance enforcement across the entire AWS organization.
features:
- description: Create, configure, update, reset, and delete AWS Control Tower landing zones programmatically via API, automating multi-account environment setup.
  name: Landing Zone Management
- description: Over 750 preconfigured controls (guardrails) covering security, operations, and compliance. Enable or disable controls on organizational units via API.
  name: Controls (Guardrails) Library
- description: Apply and manage baselines on organizational units (OUs) to register them with AWS Control Tower and enforce standard configurations programmatically.
  name: Baseline Registration
- description: Automate creation of AWS accounts with built-in governance, policies, and security controls through integration with AWS Organizations.
  name: Multi-Account Governance
- description: Deploy preventive, detective, and proactive controls to enforce compliance standards including CIS, NIST, PCI-DSS, HIPAA, and SOC 2.
  name: Compliance Enforcement
- description: Centralized audit logging to Amazon S3 and AWS CloudTrail integration for full visibility into API calls and governance actions.
  name: Audit and Logging
- description: Seamlessly integrate third-party security, compliance, and ITSM tools at scale to enhance your AWS multi-account environment.
  name: Third-Party Integrations
image: https://kinlane-productions.s3.amazonaws.com/apis-json/apis-json-logo.jpg
integrations:
- description: Native integration with AWS Organizations for multi-account structure, OU management, and account creation within a Control Tower landing zone.
  name: AWS Organizations
- description: Account Factory integration through AWS Service Catalog for self-service account provisioning with pre-approved configurations.
  name: AWS Service Catalog
- description: All Control Tower API calls are logged to AWS CloudTrail for audit trails, security investigations, and compliance reporting.
  name: AWS CloudTrail
- description: Detective controls are implemented using AWS Config rules to continuously evaluate resource compliance within managed accounts.
  name: AWS Config
- description: Integrate Control Tower findings with AWS Security Hub for centralized security posture management and cross-account visibility.
  name: AWS Security Hub
- description: Launch landing zones and enable controls using CloudFormation templates and resource providers for infrastructure-as-code governance.
  name: AWS CloudFormation
- description: Community-supported Terraform providers for managing Control Tower landing zones, controls, and account factory configurations.
  name: Terraform
jsonld:
- class_count: 46
  name: Amazon Control Tower Context
  property_count: 36
  slug: amazon-control-tower-context
layout: provider
modified: '2026-04-19'
name: Amazon Control Tower
rules:
- name: Amazon Control Tower API Rules
  rule_count: 27
  severity_counts:
    error: 13
    hint: 0
    info: 4
    warn: 10
  slug: amazon-control-tower-spectral-rules
skills: []
slug: amazon-control-tower
solutions: []
tags:
- AWS
- Compliance
- Governance
- Landing Zone
- Multi-Account
- Security
- Controls
url: https://raw.githubusercontent.com/api-evangelist/amazon-control-tower/refs/heads/main/apis.yml
use_cases:
- description: Quickly set up a secure, well-architected multi-account AWS environment with landing zone configuration completed in under 30 minutes.
  name: Multi-Account Environment Setup
- description: Deploy preconfigured controls to enforce regulatory compliance standards such as PCI-DSS, HIPAA, NIST, and SOC 2 across all accounts.
  name: Compliance Automation
- description: Automate provisioning of new AWS accounts with built-in security policies, IAM roles, and governance configurations using Account Factory.
  name: Account Vending
- description: Programmatically register organizational units with Control Tower baselines and apply targeted controls for department-specific governance.
  name: OU Governance
- description: Continuously monitor compliance posture across all accounts and receive alerts when controls are violated or drift is detected.
  name: Risk and Posture Management
---
