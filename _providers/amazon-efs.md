---
api_count: 1
apis:
- description: API for managing Amazon EFS file systems, mount targets, and related resources.
  name: Amazon EFS API
  slug: ''
capabilities:
- description: Unified capability for managing EFS file systems, mount targets, and access points for storage administrators.
  name: Amazon EFS Elastic File System Management
  slug: efs-management
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
  url: rules/amazon-efs-spectral-rules.yml
- title: ''
  type: Vocabulary
  url: vocabulary/amazon-efs-vocabulary.yaml
- title: ''
  type: NaftikoCapability
  url: capabilities/efs-management.yaml
created: '2024-01-15'
description: Amazon Elastic File System (EFS) provides a simple, serverless, set-and-forget elastic file system for use with AWS cloud services and on-premises resources. EFS is built to scale on demand to petabytes without disrupting applications, growing and shrinking automatically as you add and remove files.
features:
- description: Automatically grows and shrinks as you add and remove files with no provisioning required.
  name: Elastic Scalability
- description: Standard, Infrequent Access, and Archive storage classes with automatic lifecycle management.
  name: Multiple Storage Classes
- description: Data automatically replicated across multiple Availability Zones for 99.999999999% durability.
  name: Multi-AZ Replication
- description: Thousands of EC2 instances and Lambda functions can access the same file system simultaneously.
  name: Concurrent Access
- description: Application-specific entry points with customized directory access and POSIX permissions.
  name: EFS Access Points
- description: Centralized backup management for EFS file systems with policy-based retention.
  name: AWS Backup Integration
image: https://a0.awsstatic.com/libra-css/images/logos/aws_logo_smile_1200x630.png
integrations:
- description: Mount EFS file systems on EC2 instances using the NFS protocol.
  name: Amazon EC2
- description: Provide persistent shared storage for ECS tasks with EFS volume drivers.
  name: Amazon ECS
- description: Use the Amazon EFS CSI driver to mount EFS file systems as Kubernetes persistent volumes.
  name: Amazon EKS
- description: Access EFS file systems from Lambda functions for shared data storage and large model loading.
  name: AWS Lambda
- description: Automated backup of EFS file systems with centralized policy management.
  name: AWS Backup
jsonld:
- class_count: 4
  name: Amazon Efs Context
  property_count: 30
  slug: amazon-efs-context
layout: provider
modified: '2026-04-19'
name: Amazon EFS
rules:
- name: Amazon EFS API Rules
  rule_count: 28
  severity_counts:
    error: 11
    hint: 0
    info: 4
    warn: 13
  slug: amazon-efs-spectral-rules
skills: []
slug: amazon-efs
solutions: []
tags:
- Amazon Web Services
- AWS
- EFS
- Elastic File System
- File Storage
- NFS
- Serverless
- Storage
url: https://aws.amazon.com/efs/
use_cases:
- description: Persistent shared storage for containerized applications running on ECS or EKS.
  name: Containerized Application Storage
- description: Shared training data storage accessible simultaneously by multiple compute instances.
  name: Machine Learning
- description: Shared file storage for web servers and CMS platforms requiring concurrent file access.
  name: Content Management
- description: Centralized code and configuration storage accessible by development teams and CI/CD pipelines.
  name: DevOps and Code Sharing
- description: High-throughput shared storage for analytics workloads requiring parallel data access.
  name: Big Data Analytics
---
