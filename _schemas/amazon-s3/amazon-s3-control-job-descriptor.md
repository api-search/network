---
description: ''
layout: schema
name: JobDescriptor
properties_list:
- description: ''
  name: JobId
  type: string
- description: ''
  name: Description
  type: string
- description: ''
  name: Operation
  type: object
- description: ''
  name: Manifest
  type: object
- description: ''
  name: Priority
  type: integer
- description: ''
  name: RoleArn
  type: string
- description: ''
  name: Status
  type: string
- description: ''
  name: CreationTime
  type: string
- description: ''
  name: TerminationDate
  type: string
- description: ''
  name: ProgressSummary
  type: object
- description: ''
  name: FailureReasons
  type: array
- description: ''
  name: Report
  type: object
- description: ''
  name: ConfirmationRequired
  type: boolean
- description: ''
  name: StatusUpdateReason
  type: string
- description: ''
  name: SuspendedDate
  type: string
- description: ''
  name: SuspendedCause
  type: string
provider_name: Amazon S3
provider_slug: amazon-s3
schema_file: json-schema/amazon-s3-control-job-descriptor-schema.json
slug: amazon-s3-control-job-descriptor
tags:
- Archive
- AWS
- Backup
- Cloud Storage
- Data Storage
- Object Storage
- Scalable Storage
title: JobDescriptor
---
