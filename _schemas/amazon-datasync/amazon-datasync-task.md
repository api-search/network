---
description: Schema representing an AWS DataSync task resource. A task defines the source location, destination location, and the options to use for transferring data.
layout: schema
name: Amazon DataSync Task
properties_list:
- description: The Amazon Resource Name (ARN) of the task.
  name: TaskArn
  type: string
- description: The name of the task.
  name: Name
  type: string
- description: The status of the task.
  name: Status
  type: string
- description: The ARN of the source location for the task.
  name: SourceLocationArn
  type: string
- description: The ARN of the destination location for the task.
  name: DestinationLocationArn
  type: string
- description: The ARN of the most recent task execution.
  name: CurrentTaskExecutionArn
  type: string
- description: ''
  name: Options
  type: object
- description: ''
  name: Schedule
  type: object
- description: Errors that DataSync encountered during execution of the task.
  name: ErrorCode
  type: string
- description: Detailed description of an error that was encountered during the task execution.
  name: ErrorDetail
  type: string
- description: The time that the task was created.
  name: CreationTime
  type: string
- description: The tags associated with the task.
  name: Tags
  type: array
provider_name: Amazon DataSync
provider_slug: amazon-datasync
schema_file: json-schema/amazon-datasync-task-schema.json
slug: amazon-datasync-task
tags:
- AWS
- Data Transfer
- Migration
- Storage
- Automation
- Hybrid Cloud
title: Amazon DataSync Task
---
