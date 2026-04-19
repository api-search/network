---
api_count: 1
apis:
- description: RESTful API for AWS Storage Gateway enabling management of gateways, volumes, tapes, file shares, and cached storage for hybrid cloud storage architectures.
  name: Amazon Storage Gateway REST API
  slug: ''
capabilities: []
common:
- title: ''
  type: Portal
  url: https://aws.amazon.com/storagegateway/
- title: ''
  type: Documentation
  url: https://docs.aws.amazon.com/storagegateway/latest/APIReference/Welcome.html
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
  url: https://aws.amazon.com/blogs/storage/
- title: ''
  type: GitHubOrganization
  url: https://github.com/aws
- title: ''
  type: Console
  url: https://console.aws.amazon.com/storagegateway/
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
  url: rules/amazon-storage-gateway-spectral-rules.yml
- title: ''
  type: Vocabulary
  url: vocabulary/amazon-storage-gateway-vocabulary.yaml
- title: ''
  type: NaftikoCapability
  url: capabilities/shared/amazon-storage-gateway.yaml
created: '2024-01-15'
description: AWS Storage Gateway is a hybrid cloud storage service that provides on-premises access to virtually unlimited cloud storage. It seamlessly connects on-premises environments to AWS cloud storage, providing low-latency data access with local caching.
features:
- description: Provides NFS and SMB access to objects stored in Amazon S3.
  name: File Gateway
- description: Provides iSCSI block storage backed by Amazon S3 and Glacier.
  name: Volume Gateway
- description: Virtual tape library backed by S3 and Glacier for backup.
  name: Tape Gateway
- description: Seamlessly integrate on-premises environments with AWS storage.
  name: Hybrid Storage
- description: Cache frequently accessed data locally for low-latency access.
  name: Local Caching
image: https://a0.awsstatic.com/libra-css/images/logos/aws_logo_smile_1200x630.png
integrations:
- description: Store all gateway data in S3 with intelligent tiering.
  name: Amazon S3
- description: Archive tape data to Glacier for long-term retention.
  name: Amazon Glacier
- description: Centralized backup of Storage Gateway volumes and file shares.
  name: AWS Backup
- description: Monitor gateway metrics and set alarms via CloudWatch.
  name: Amazon CloudWatch
- description: Audit all Storage Gateway API calls for compliance.
  name: AWS CloudTrail
jsonld:
- class_count: 205
  name: Amazon Storage Gateway Context
  property_count: 220
  slug: amazon-storage-gateway-context
layout: provider
modified: '2026-04-19'
name: Amazon Storage Gateway
rules:
- name: Amazon Storage Gateway API Rules
  rule_count: 19
  severity_counts:
    error: 11
    hint: 0
    info: 1
    warn: 7
  slug: amazon-storage-gateway-spectral-rules
skills: []
slug: amazon-storage-gateway
solutions: []
tags:
- AWS
- Backup
- File Storage
- Gateway
- Hybrid Cloud
- Storage
url: https://aws.amazon.com/storagegateway/
use_cases:
- description: Back up on-premises data to AWS using existing backup workflows.
  name: Cloud Backup
- description: Store data in AWS for disaster recovery with low RTO.
  name: Disaster Recovery
- description: Archive cold data to Amazon Glacier through virtual tape library.
  name: Data Archiving
- description: Share files between on-premises and cloud with NFS/SMB access.
  name: Hybrid File Storage
---
