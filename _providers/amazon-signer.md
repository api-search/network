---
api_count: 1
apis:
- description: The AWS Signer API provides programmatic access to create and manage signing profiles, signing jobs, and signing platform permissions for code signing of Lambda functions and IoT device software.
  name: AWS Signer API
  slug: aws-signer-api
capabilities: []
common:
- title: ''
  type: Portal
  url: https://aws.amazon.com/signer/
- title: ''
  type: Documentation
  url: https://docs.aws.amazon.com/signer/
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
  url: https://aws.amazon.com/blogs/compute/tag/aws-signer/
- title: ''
  type: GitHubOrganization
  url: https://github.com/aws
- title: ''
  type: Console
  url: https://console.aws.amazon.com/signer/
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
  url: rules/amazon-signer-spectral-rules.yml
- title: ''
  type: Vocabulary
  url: vocabulary/amazon-signer-vocabulary.yaml
- title: ''
  type: NaftikoCapability
  url: capabilities/shared/amazon-signer.yaml
created: '2026-03-16'
description: AWS Signer is a fully managed code-signing service to ensure the trust and integrity of your code. It manages the code-signing certificate public and private keys and enables central management and deployment of code signing certificates for Lambda functions and IoT devices.
features:
- description: Security administrators define signing policies and which IAM roles can sign code.
  name: Centralized Code Signing
- description: Automatically manages code-signing certificate public and private keys.
  name: Certificate Management
- description: Central management and deployment of code-signing certificates.
  name: Lifecycle Management
- description: Integration with AWS CloudTrail tracks who generates signatures for compliance.
  name: Compliance Tracking
- description: No infrastructure to maintain — fully managed code signing service.
  name: Fully Managed
- description: Revoke signing profiles and individual signatures with effective timestamps.
  name: Signature Revocation
image: https://kinlane-productions.s3.amazonaws.com/apis-json/apis-json-logo.jpg
integrations:
- description: Sign Lambda deployment packages; Lambda verifies signatures at deployment.
  name: AWS Lambda
- description: Sign firmware images for IoT microcontrollers and OTA updates.
  name: Amazon FreeRTOS
- description: Sign container images using Notation CLI stored in ECR registry.
  name: Amazon ECR
- description: Verify image ownership and integrity at Kubernetes deployment time.
  name: Amazon EKS
- description: Create or import SSL/TLS certificates used for code signing.
  name: AWS Certificate Manager
- description: Record and audit all API calls to AWS Signer for compliance.
  name: AWS CloudTrail
- description: Sign code for IoT devices managed by AWS IoT Device Management.
  name: AWS IoT Device Management
jsonld:
- class_count: 60
  name: Amazon Signer Context
  property_count: 69
  slug: amazon-signer-context
layout: provider
modified: '2026-04-19'
name: Amazon Signer
rules:
- name: Amazon Signer API Rules
  rule_count: 25
  severity_counts:
    error: 12
    hint: 0
    info: 4
    warn: 9
  slug: amazon-signer-spectral-rules
skills: []
slug: amazon-signer
solutions: []
tags:
- AWS
- Code Signing
- IoT
- Lambda
- Security
url: https://raw.githubusercontent.com/api-evangelist/amazon-signer/refs/heads/main/apis.yml
use_cases:
- description: Sign Lambda deployment packages to ensure only trusted code is deployed.
  name: Lambda Code Signing
- description: Sign firmware images for microcontrollers and over-the-air (OTA) updates via Amazon FreeRTOS.
  name: IoT Firmware Signing
- description: Sign container images using Notation CLI with Amazon ECR and verify at EKS deployment.
  name: Container Image Signing
- description: Track all signing operations via CloudTrail for audit and compliance requirements.
  name: Audit and Compliance
---
