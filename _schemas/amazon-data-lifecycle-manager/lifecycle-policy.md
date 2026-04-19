---
description: A complete lifecycle policy definition for automating EBS snapshot or AMI management.
layout: schema
name: Lifecycle Policy
properties_list:
- description: The identifier of the lifecycle policy
  name: PolicyId
  type: string
- description: ''
  name: Description
  type: string
- description: ''
  name: State
  type: string
- description: The ARN of the IAM role used by DLM
  name: ExecutionRoleArn
  type: string
- description: ''
  name: DateCreated
  type: string
- description: ''
  name: DateModified
  type: string
- description: ''
  name: PolicyDetails
  type: object
provider_name: Amazon Data Lifecycle Manager
provider_slug: amazon-data-lifecycle-manager
schema_file: json-schema/lifecycle-policy-schema.json
slug: lifecycle-policy
tags:
- AWS
- Backup
- EBS Snapshots
- Lifecycle Management
- Storage
- Automation
- Compliance
title: Lifecycle Policy
---
