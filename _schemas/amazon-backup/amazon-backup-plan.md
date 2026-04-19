---
description: Represents an AWS Backup plan with its associated rules, schedule, and lifecycle configuration.
layout: schema
name: Amazon Backup Plan
properties_list:
- description: The Amazon Resource Name (ARN) of the backup plan.
  name: backupPlanArn
  type: string
- description: Uniquely identifies a backup plan.
  name: backupPlanId
  type: string
- description: The display name of a backup plan.
  name: backupPlanName
  type: string
- description: The date and time the resource backup plan was created.
  name: creationDate
  type: string
- description: The last time a job to back up resources was run with this rule.
  name: lastExecutionDate
  type: string
- description: An array of BackupRule objects, each of which specifies a scheduled task to back up a selection of resources.
  name: rules
  type: array
- description: Advanced backup settings for the backup plan.
  name: advancedBackupSettings
  type: array
provider_name: Amazon Backup
provider_slug: amazon-backup
schema_file: json-schema/amazon-backup-plan-schema.json
slug: amazon-backup-plan
tags:
- AWS
- Backup
- Data Protection
- Disaster Recovery
- Storage
- Compliance
- Governance
- Business Continuity
title: Amazon Backup Plan
---
