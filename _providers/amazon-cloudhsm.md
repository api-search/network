---
api_count: 1
apis:
- description: API for creating and managing CloudHSM clusters and HSM instances for dedicated hardware-based cryptographic key management.
  name: Amazon CloudHSM API
  slug: ''
capabilities:
- description: Workflow for cryptographic key management using Amazon CloudHSM for Security Engineer personas.
  name: Amazon CloudHSM Cryptographic Key Management
  slug: cryptographic-key-management
common:
- title: ''
  type: Portal
  url: https://aws.amazon.com/
- title: ''
  type: Website
  url: https://aws.amazon.com/cloudhsm/
- title: ''
  type: Documentation
  url: https://docs.aws.amazon.com/cloudhsm/latest/APIReference/
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
  url: https://console.aws.amazon.com/cloudhsm/
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
  url: https://stackoverflow.com/questions/tagged/aws-cloudhsm
- title: ''
  type: Contact
  url: https://aws.amazon.com/contact-us/
- title: ''
  type: Compliance
  url: https://aws.amazon.com/compliance/
- title: ''
  type: SpectralRules
  url: rules/amazon-cloudhsm-spectral-rules.yml
- title: ''
  type: Vocabulary
  url: vocabulary/amazon-cloudhsm-vocabulary.yaml
- title: ''
  type: NaftikoCapability
  url: capabilities/cryptographic-key-management.yaml
created: '2026-03-16'
description: AWS CloudHSM is a cloud-based hardware security module (HSM) that enables you to manage cryptographic keys on dedicated FIPS 140-2 Level 3 validated, single-tenant HSM instances running within your own VPC for regulatory compliance and data security.
features:
- description: Dedicated single-tenant HSM instances meeting the highest FIPS validation levels.
  name: FIPS 140-2 Level 3 Validated
- description: Complete control over cryptographic keys with no AWS access to key material.
  name: Full Key Control
- description: Add or remove HSMs from clusters as needed, paying only for active resources hourly.
  name: Elastic Capacity
- description: Multi-AZ HSM clusters provide redundancy and automatic failover.
  name: High Availability
- description: Supports PKCS#11, Java JCE, and Microsoft CNG APIs for application integration.
  name: Industry-Standard APIs
image: https://kinlane-productions.s3.amazonaws.com/apis-json/apis-json-logo.jpg
integrations:
- description: Use CloudHSM keys for Oracle TDE and SQL Server TDE in RDS.
  name: Amazon RDS
- description: Use CloudHSM as a custom key store for AWS KMS operations.
  name: AWS KMS
- description: HSM instances run inside your VPC for network isolation.
  name: Amazon VPC
- description: Control access to HSM cluster management operations.
  name: AWS IAM
- description: Audit HSM management API calls via CloudTrail.
  name: AWS CloudTrail
layout: provider
modified: '2026-04-19'
name: Amazon CloudHSM
rules:
- name: Amazon CloudHSM API Rules
  rule_count: 19
  severity_counts:
    error: 12
    hint: 0
    info: 1
    warn: 6
  slug: amazon-cloudhsm-spectral-rules
skills: []
slug: amazon-cloudhsm
solutions: []
tags:
- AWS
- CloudHSM
- Security
- Cryptography
- HSM
- Compliance
url: https://raw.githubusercontent.com/api-evangelist/amazon-cloudhsm/refs/heads/main/apis.yml
use_cases:
- description: Protect sensitive data with hardware-backed encryption keys.
  name: Data Encryption
- description: Manage SSL/TLS certificates and private keys in dedicated HSMs.
  name: SSL/TLS Offloading
- description: Secure private CA keys for organizations issuing their own certificates.
  name: Certificate Authority
- description: Support transparent data encryption (TDE) for Oracle and SQL Server databases.
  name: Database Encryption
- description: Meet PCI DSS, HIPAA, and other regulatory requirements for key management.
  name: Regulatory Compliance
---
