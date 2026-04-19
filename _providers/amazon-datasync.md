---
api_count: 1
apis:
- description: RESTful API for AWS DataSync enabling management of data transfer tasks, locations, agents, and task executions for automated data movement between on-premises storage systems and AWS cloud storage. S
  name: Amazon DataSync REST API
  slug: amazon-datasync-api
capabilities:
- description: ''
  name: Data Transfer Operations
  slug: data-transfer-operations
common:
- title: ''
  type: Portal
  url: https://aws.amazon.com/datasync/
- title: ''
  type: DeveloperPortal
  url: https://aws.amazon.com/datasync/
- title: ''
  type: Documentation
  url: https://docs.aws.amazon.com/datasync/
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
  url: https://console.aws.amazon.com/datasync/
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
  type: YouTube
  url: https://www.youtube.com/user/AmazonWebServices
- title: ''
  type: StackOverflow
  url: https://stackoverflow.com/questions/tagged/aws-datasync
- title: ''
  type: SpectralRules
  url: rules/amazon-datasync-spectral-rules.yml
- title: ''
  type: Vocabulary
  url: vocabulary/amazon-datasync-vocabulary.yaml
- title: ''
  type: NaftikoCapability
  url: capabilities/data-transfer-operations.yaml
- title: ''
  type: NaftikoCapability
  url: capabilities/shared/datasync.yaml
created: '2024-01-15'
description: AWS DataSync is an online data transfer service that simplifies, automates, and accelerates moving data between on-premises storage systems, AWS storage services, and other cloud storage. DataSync can transfer data at speeds up to 10 times faster than open-source tools by using purpose-built network protocol and parallel multi-threaded architecture. It supports NFS, SMB, HDFS, S3, EFS, FSx, and more as transfer endpoints.
features:
- description: Transfer data at speeds up to 10 times faster than open-source tools using purpose-built multi-threaded network protocol over TLS.
  name: High-Speed Data Transfer
- description: Connect to NFS, SMB, HDFS, Amazon S3, Amazon EFS, FSx for Windows, FSx for Lustre, and FSx for NetApp ONTAP as transfer endpoints.
  name: Multi-Protocol Support
- description: Automatically verify data integrity using checksums at both source and destination to ensure byte-for-byte data consistency after transfer.
  name: Automated Data Validation
- description: Configure recurring scheduled transfers on hourly, daily, or weekly cadences for ongoing data synchronization between systems.
  name: Scheduled Transfers
- description: Deploy the DataSync agent VM on-premises to connect local NFS and SMB storage to AWS without opening inbound firewall ports.
  name: On-Premises Agent
- description: Control the network bandwidth consumed by DataSync transfers to minimize impact on production workloads during business hours.
  name: Bandwidth Throttling
- description: Monitor transfer metrics, task execution history, and set up alarms for failed transfers using Amazon CloudWatch.
  name: CloudWatch Integration
image: https://kinlane-productions.s3.amazonaws.com/apis-json/apis-json-logo.jpg
integrations:
- description: Primary cloud storage destination supporting all S3 storage classes including Glacier for cost-effective data archival.
  name: Amazon S3
- description: Transfer data to and from Amazon Elastic File System for shared file storage accessible from multiple EC2 instances.
  name: Amazon EFS
- description: Integrate with FSx for Windows, FSx for Lustre, and FSx for NetApp ONTAP as high-performance managed file system destinations.
  name: Amazon FSx
- description: Receive DataSync task execution metrics, transfer rates, and error alerts in CloudWatch for monitoring and incident response.
  name: Amazon CloudWatch
- description: Use Snowball for initial bulk data transfer followed by DataSync for ongoing incremental synchronization after migration.
  name: AWS Snowball
- description: Combine Storage Gateway for cache-based hybrid access with DataSync for bulk data movement between on-premises and cloud.
  name: AWS Storage Gateway
jsonld:
- class_count: 0
  name: Amazon Datasync Context
  property_count: 3
  slug: amazon-datasync-context
layout: provider
modified: '2026-04-19'
name: Amazon DataSync
rules:
- name: Amazon DataSync API Rules
  rule_count: 18
  severity_counts:
    error: 13
    hint: 0
    info: 1
    warn: 4
  slug: amazon-datasync-spectral-rules
skills: []
slug: amazon-datasync
solutions: []
tags:
- AWS
- Data Transfer
- Migration
- Storage
- Automation
- Hybrid Cloud
url: https://raw.githubusercontent.com/api-evangelist/amazon-datasync/refs/heads/main/apis.yml
use_cases:
- description: Migrate petabytes of data from on-premises NAS and SAN systems to Amazon S3 or EFS during cloud adoption and data center exit projects.
  name: Data Center Migration
- description: Keep on-premises and cloud storage in sync on a scheduled basis for hybrid cloud architectures and distributed workloads.
  name: Ongoing Hybrid Synchronization
- description: Transfer on-premises file data to Amazon S3 Glacier for cost-effective long-term archival and backup storage.
  name: Backup and Archive to Cloud
- description: Transfer datasets between AWS Regions or across AWS accounts for data sharing, disaster recovery, or multi-region analytics.
  name: Data Distribution
- description: Stage large datasets from S3 or on-premises storage to FSx for Lustre for high-performance computing workloads on AWS.
  name: HPC Data Staging
---
