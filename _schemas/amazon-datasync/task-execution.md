---
description: A specific execution run of a DataSync task.
layout: schema
name: Task Execution
properties_list:
- description: The ARN of the task execution. This ARN uniquely identifies the execution.
  name: TaskExecutionArn
  type: string
- description: ''
  name: Status
  type: string
- description: ''
  name: StartTime
  type: string
- description: ''
  name: EstimatedFilesToTransfer
  type: integer
- description: ''
  name: FilesTransferred
  type: integer
- description: ''
  name: BytesTransferred
  type: integer
provider_name: Amazon DataSync
provider_slug: amazon-datasync
schema_file: json-schema/task-execution-schema.json
slug: task-execution
tags:
- AWS
- Data Transfer
- Migration
- Storage
- Automation
- Hybrid Cloud
title: Task Execution
---
