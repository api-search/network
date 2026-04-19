---
api_count: 1
apis:
- description: REST API for AWS Application Migration Service covering source servers, replication configuration, launch configuration, jobs, applications, and waves for lift-and-shift cloud migration.
  name: Amazon Application Migration Service API
  slug: amazon-application-migration-service-api
capabilities:
- description: Workflow capability for executing lift-and-shift migrations from on-premises to AWS using Application Migration Service.
  name: Lift And Shift Migration Workflow
  slug: lift-and-shift-migration
common: []
created: '2026-03-16'
description: AWS Application Migration Service (MGN) is the primary migration service recommended for lift-and-shift migrations to AWS. It allows organizations to quickly realize the benefits of migrating applications to the cloud without changes and with minimal downtime.
features:
- Continuous block-level replication with near-zero RPO
- Automated lift-and-shift migration without application changes
- Test migration capability without impacting production servers
- Wave and application grouping for phased migration management
- Agentless migration via VMware vCenter connector
- Post-launch automation via AWS Systems Manager documents
- Right-sizing recommendations for target instance types
- Cross-account and cross-region migration support
- Integration with AWS Migration Hub for centralized tracking
- Automatic EC2 launch template creation for migrated servers
image: https://kinlane-productions.s3.amazonaws.com/apis-json/apis-json-logo.jpg
integrations:
- AWS Migration Hub
- Amazon EC2
- Amazon EBS
- AWS Systems Manager
- VMware vCenter
- AWS IAM
- Amazon CloudWatch
- AWS CloudTrail
- Amazon S3
- AWS KMS
jsonld:
- class_count: 100
  name: Amazon Application Migration Service Context
  property_count: 0
  slug: amazon-application-migration-service-context
layout: provider
modified: '2026-04-19'
name: Amazon Application Migration Service
rules:
- name: Amazon Application Migration Service API Rules
  rule_count: 21
  severity_counts:
    error: 13
    hint: 0
    info: 2
    warn: 6
  slug: amazon-application-migration-service-spectral-rules
skills: []
slug: amazon-application-migration-service
solutions: []
tags:
- Amazon Application Migration Service
- Migration
- Lift And Shift
- AWS
- Cloud Migration
url: https://raw.githubusercontent.com/api-evangelist/amazon-application-migration-service/refs/heads/main/apis.yml
use_cases:
- Migrate on-premises data center servers to AWS with minimal downtime
- Execute phased migrations organized by application waves
- Test migration outcomes before executing production cutover
- Migrate VMware virtual machines to EC2 instances without agent installation
- Standardize migration configuration across hundreds of servers with templates
- Automate post-migration software installation and configuration with SSM
---
