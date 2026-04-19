---
api_count: 1
apis:
- description: API for managing Amazon EBS volumes, snapshots, and related resources through the EC2 API.
  name: Amazon EBS API
  slug: ''
capabilities:
- description: Unified capability for managing EBS volumes, snapshots, and encryption for cloud storage administrators.
  name: Amazon EBS Block Storage Management
  slug: ebs-management
common:
- title: ''
  type: Portal
  url: https://aws.amazon.com/
- title: ''
  type: DeveloperPortal
  url: https://aws.amazon.com/
- title: ''
  type: Documentation
  url: https://docs.aws.amazon.com/
- title: ''
  type: TermsOfService
  url: https://aws.amazon.com/service-terms/
- title: ''
  type: PrivacyPolicy
  url: https://aws.amazon.com/privacy/
- title: ''
  type: Support
  url: https://aws.amazon.com/support/
- title: ''
  type: Blog
  url: https://aws.amazon.com/blogs/
- title: ''
  type: GitHubOrganization
  url: https://github.com/aws
- title: ''
  type: Console
  url: https://console.aws.amazon.com/
- title: ''
  type: SignUp
  url: https://portal.aws.amazon.com/billing/signup
- title: ''
  type: Login
  url: https://signin.aws.amazon.com/
- title: ''
  type: StatusPage
  url: https://status.aws.amazon.com/
- title: ''
  type: KnowledgeCenter
  url: https://repost.aws/knowledge-center
- title: ''
  type: YouTube
  url: https://www.youtube.com/user/AmazonWebServices
- title: ''
  type: StackOverflow
  url: https://stackoverflow.com/questions/tagged/amazon-web-services
- title: ''
  type: Contact
  url: https://aws.amazon.com/contact-us/
- title: ''
  type: Security
  url: https://aws.amazon.com/security/
- title: ''
  type: Compliance
  url: https://aws.amazon.com/compliance/
- title: ''
  type: SpectralRules
  url: rules/amazon-ebs-spectral-rules.yml
- title: ''
  type: Vocabulary
  url: vocabulary/amazon-ebs-vocabulary.yaml
- title: ''
  type: NaftikoCapability
  url: capabilities/ebs-management.yaml
created: '2024-01-15'
description: Amazon Elastic Block Store (EBS) provides persistent block storage volumes for use with Amazon EC2 instances. EBS volumes are highly available and reliable storage volumes that can be attached to any running instance in the same Availability Zone, offering consistent and low-latency performance for workloads that require persistent storage.
features:
- description: Choose from gp3, gp2, io2, io1, st1, sc1, and io2 Block Express volumes optimized for different workloads.
  name: Multiple Volume Types
- description: Point-in-time backups stored in Amazon S3 for disaster recovery, migration, and data sharing.
  name: EBS Snapshots
- description: AES-256 encryption at rest and in transit using AWS KMS customer-managed or AWS-managed keys.
  name: Encryption
- description: Dynamically modify volume size, performance, and type without detaching from instances.
  name: Elastic Volumes
- description: Automate snapshot creation, retention, deletion, and cross-account sharing with policy-based management.
  name: Data Lifecycle Manager
- description: Attach a single io2 volume to up to 16 EC2 instances simultaneously for high availability.
  name: Multi-Attach
image: https://a0.awsstatic.com/libra-css/images/logos/aws_logo_smile_1200x630.png
integrations:
- description: Attach EBS volumes to EC2 instances in the same Availability Zone for persistent storage.
  name: Amazon EC2
- description: Automate snapshot management and cross-account data sharing policies.
  name: Amazon Data Lifecycle Manager
- description: Centralized backup management for EBS volumes with configurable retention and compliance.
  name: AWS Backup
- description: Manage encryption keys for EBS volumes and snapshots.
  name: AWS Key Management Service
- description: Monitor EBS volume performance metrics including IOPS, throughput, and latency.
  name: Amazon CloudWatch
jsonld:
- class_count: 3
  name: Amazon Ebs Context
  property_count: 24
  slug: amazon-ebs-context
layout: provider
modified: '2026-04-19'
name: Amazon EBS
rules:
- name: Amazon EBS API Rules
  rule_count: 28
  severity_counts:
    error: 11
    hint: 0
    info: 4
    warn: 13
  slug: amazon-ebs-spectral-rules
skills: []
slug: amazon-ebs
solutions: []
tags:
- Amazon Web Services
- AWS
- Block Storage
- EBS
- EC2
- Snapshots
- Storage
- Volumes
url: https://aws.amazon.com/ebs/
use_cases:
- description: High-performance persistent storage for MySQL, PostgreSQL, Oracle, and SQL Server databases.
  name: Relational Databases
- description: Low-latency block storage for MongoDB, Cassandra, and other NoSQL workloads.
  name: NoSQL Databases
- description: SAN workload migration for I/O-intensive SAP, Oracle, and other enterprise applications.
  name: Enterprise Applications
- description: Resizable storage for Hadoop, Spark, and other big data cluster deployments.
  name: Big Data Analytics
- description: OS and application boot volumes for all EC2 instance types.
  name: Boot Volumes
---
