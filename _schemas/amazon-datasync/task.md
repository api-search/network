---
description: A DataSync task defining source location, destination location, and transfer configuration.
layout: schema
name: Task
properties_list:
- description: The ARN of the DataSync task. This ARN uniquely identifies the task.
  name: TaskArn
  type: string
- description: The name of the task
  name: Name
  type: string
- description: ''
  name: Status
  type: string
- description: The ARN of the source location. This ARN uniquely identifies the location.
  name: SourceLocationArn
  type: string
- description: The ARN of the destination location. This ARN uniquely identifies the location.
  name: DestinationLocationArn
  type: string
- description: ''
  name: CurrentTaskExecutionArn
  type: string
- description: ''
  name: CloudWatchLogGroupArn
  type: string
provider_name: Amazon DataSync
provider_slug: amazon-datasync
schema_file: json-schema/task-schema.json
slug: task
tags:
- AWS
- Data Transfer
- Migration
- Storage
- Automation
- Hybrid Cloud
title: Task
---
