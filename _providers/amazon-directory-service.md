---
api_count: 1
apis:
- description: The AWS Directory Service API provides programmatic access to create and manage directories, trusts, snapshots, and domain controllers for Microsoft Active Directory in the AWS Cloud.
  name: AWS Directory Service API
  slug: aws-directory-service-api
capabilities:
- description: 'Workflow capability for identity engineers and cloud architects to manage AWS Managed Microsoft Active Directory, including directory provisioning, trust relationships, domain controllers, snapshots, '
  name: Amazon Directory Service Active Directory Management
  slug: active-directory-management
common:
- title: ''
  type: Portal
  url: https://aws.amazon.com/directoryservice/
- title: ''
  type: Website
  url: https://aws.amazon.com/directoryservice/
- title: ''
  type: Documentation
  url: https://docs.aws.amazon.com/directoryservice/
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
  url: https://aws.amazon.com/blogs/security/tag/aws-directory-service/
- title: ''
  type: GitHubOrganization
  url: https://github.com/aws
- title: ''
  type: Console
  url: https://console.aws.amazon.com/directoryservicev2/
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
  url: https://raw.githubusercontent.com/api-evangelist/amazon-directory-service/refs/heads/main/rules/amazon-directory-service-spectral-rules.yml
- title: ''
  type: Vocabulary
  url: https://raw.githubusercontent.com/api-evangelist/amazon-directory-service/refs/heads/main/vocabulary/amazon-directory-service-vocabulary.yaml
- title: ''
  type: NaftikoCapability
  url: https://raw.githubusercontent.com/api-evangelist/amazon-directory-service/refs/heads/main/capabilities/active-directory-management.yaml
created: '2026-03-16'
description: AWS Directory Service for Microsoft Active Directory, also known as AWS Managed Microsoft AD, enables your directory-aware workloads and AWS resources to use managed Active Directory in AWS. It provides a fully managed, highly available Microsoft Active Directory in the AWS Cloud, with features including trust relationships, domain controllers, LDAPS, and multi-account sharing.
features:
- description: Fully managed AWS Managed Microsoft Active Directory with automatic patching and monitoring
  name: Managed Microsoft AD
- description: Standalone managed directory powered by Samba 4 for basic AD functionality
  name: Simple AD
- description: Proxy service for connecting AWS applications to existing on-premises AD
  name: AD Connector
- description: One-way and two-way trust relationships between AWS and on-premises directories
  name: Trust Relationships
- description: Replicate your AWS Managed Microsoft AD across multiple AWS Regions
  name: Multi-Region Replication
- description: Share a single directory across multiple AWS accounts and VPCs
  name: Directory Sharing
image: https://kinlane-productions.s3.amazonaws.com/apis-json/apis-json-logo.jpg
integrations:
- description: Join WorkSpaces desktops to managed AD for enterprise desktop management
  name: Amazon WorkSpaces
- description: Enable Windows Authentication for SQL Server RDS instances via managed AD
  name: Amazon RDS
- description: Use managed AD as identity source for centralized access management
  name: AWS IAM Identity Center
- description: Audit all Directory Service API calls for compliance and security monitoring
  name: AWS CloudTrail
- description: Receive directory event notifications via SNS topic subscriptions
  name: Amazon SNS
jsonld:
- class_count: 26
  name: Amazon Directory Service Context
  property_count: 101
  slug: amazon-directory-service-context
layout: provider
modified: '2026-04-19'
name: Amazon Directory Service
rules:
- name: Amazon Directory Service API Rules
  rule_count: 18
  severity_counts:
    error: 11
    hint: 0
    info: 3
    warn: 4
  slug: amazon-directory-service-spectral-rules
skills: []
slug: amazon-directory-service
solutions: []
tags:
- Active Directory
- Authentication
- AWS
- Directory Services
- Identity Management
url: https://raw.githubusercontent.com/api-evangelist/amazon-directory-service/refs/heads/main/apis.yml
use_cases:
- description: Extend on-premises Active Directory into AWS for unified identity management
  name: Hybrid Identity
- description: Enable Windows and Linux workloads to join and authenticate against managed AD
  name: Workload Authentication
- description: Use managed AD for AWS WorkSpaces, RDS, and other AD-aware services
  name: AWS Application Integration
- description: Secure LDAP communications with certificates for compliance requirements
  name: LDAPS Encryption
- description: Use directory snapshots for point-in-time recovery of directory data
  name: Disaster Recovery
---
