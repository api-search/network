---
api_count: 1
apis:
- description: The Amazon Data Lifecycle Manager API enables programmatic management of lifecycle policies for automating the creation, retention, and deletion of EBS snapshots and AMIs to meet backup and compliance
  name: Amazon Data Lifecycle Manager API
  slug: amazon-dlm-api
capabilities:
- description: ''
  name: Backup Automation Operations
  slug: backup-automation-operations
common:
- title: ''
  type: Portal
  url: https://aws.amazon.com/ebs/data-lifecycle-manager/
- title: ''
  type: DeveloperPortal
  url: https://aws.amazon.com/ebs/data-lifecycle-manager/
- title: ''
  type: Documentation
  url: https://docs.aws.amazon.com/dlm/
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
  type: GitHubOrganization
  url: https://github.com/aws
- title: ''
  type: Console
  url: https://console.aws.amazon.com/ec2/v2/home#Lifecycle
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
  url: rules/amazon-data-lifecycle-manager-spectral-rules.yml
- title: ''
  type: Vocabulary
  url: vocabulary/amazon-data-lifecycle-manager-vocabulary.yaml
- title: ''
  type: NaftikoCapability
  url: capabilities/backup-automation-operations.yaml
- title: ''
  type: NaftikoCapability
  url: capabilities/shared/data-lifecycle-manager.yaml
created: '2026-03-16'
description: Amazon Data Lifecycle Manager provides an automated way to manage the lifecycle of your AWS resources. Using lifecycle policies, you can automate the creation, retention, and deletion of Amazon EBS snapshots and EBS-backed AMIs, reducing storage costs and simplifying backup management. Policies target EBS volumes and EC2 instances using tags, execute on configurable schedules, and apply flexible retention rules based on count or age.
features:
- description: Automatically create, copy, and delete EBS snapshots on configurable schedules using tag-based targeting of volumes across AWS accounts.
  name: EBS Snapshot Automation
- description: Automate the creation and deregistration of Amazon Machine Images from EC2 instances on schedules to maintain a library of AMIs.
  name: AMI Lifecycle Management
- description: Retain snapshots by count (keep the last N) or by age (keep for N days/weeks/months/years), automatically deleting older snapshots.
  name: Flexible Retention Rules
- description: Target EBS volumes or EC2 instances using resource tags for policy scope, enabling granular backup control without managing resource lists.
  name: Tag-Based Targeting
- description: Configure schedules to copy snapshots to other AWS regions for disaster recovery and geographic redundancy automatically.
  name: Cross-Region Copy
- description: Enable fast snapshot restore on snapshots created by DLM policies to dramatically reduce EBS volume initialization time.
  name: Fast Snapshot Restore
- description: Trigger snapshot sharing and copying workflows in response to CloudWatch Events for cross-account snapshot automation.
  name: Event-Based Policies
image: https://kinlane-productions.s3.amazonaws.com/apis-json/apis-json-logo.jpg
integrations:
- description: Native integration with Amazon EBS for snapshot creation, retention, and deletion of volumes across the AWS account.
  name: Amazon EBS
- description: Target EC2 instances with IMAGE_MANAGEMENT policies to automate AMI creation from running or stopped instances.
  name: Amazon EC2
- description: Event-based DLM policies are triggered by Amazon CloudWatch Events for cross-account snapshot sharing scenarios.
  name: Amazon CloudWatch
- description: Complementary to DLM, AWS Backup provides centralized backup management across multiple AWS services including EBS, RDS, and DynamoDB.
  name: AWS Backup
- description: DLM uses IAM execution roles to assume permissions for creating and deleting snapshots on behalf of the lifecycle policy.
  name: AWS IAM
- description: Cross-account snapshot sharing policies use AWS Organizations to share EBS snapshots with member accounts automatically.
  name: AWS Organizations
jsonld:
- class_count: 0
  name: Amazon Data Lifecycle Manager Context
  property_count: 34
  slug: amazon-data-lifecycle-manager-context
layout: provider
modified: '2026-04-19'
name: Amazon Data Lifecycle Manager
rules:
- name: Amazon Data Lifecycle Manager API Rules
  rule_count: 21
  severity_counts:
    error: 13
    hint: 0
    info: 3
    warn: 5
  slug: amazon-data-lifecycle-manager-spectral-rules
skills: []
slug: amazon-data-lifecycle-manager
solutions: []
tags:
- AWS
- Backup
- EBS Snapshots
- Lifecycle Management
- Storage
- Automation
- Compliance
url: https://raw.githubusercontent.com/api-evangelist/amazon-data-lifecycle-manager/refs/heads/main/apis.yml
use_cases:
- description: Schedule daily EBS volume snapshots with automated retention of the last 7 or 30 days of backups without manual intervention.
  name: Automated Daily Backups
- description: Meet regulatory backup retention requirements by defining long-term retention policies (monthly/yearly) for compliance snapshots.
  name: Compliance and Audit Retention
- description: Automatically copy EBS snapshots to secondary AWS regions to enable cross-region disaster recovery with minimal RTO and RPO.
  name: Disaster Recovery
- description: Automate the creation of hardened EC2 AMI images from approved instances and manage their lifecycle for deployment fleets.
  name: Golden AMI Pipeline
- description: Reduce EBS snapshot storage costs by automatically deleting outdated snapshots based on configurable age or count retention rules.
  name: Storage Cost Optimization
---
