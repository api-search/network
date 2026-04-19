---
description: ChangeSet schema
layout: schema
name: ChangeSet
properties_list:
- description: The ARN of the change set.
  name: ChangeSetId
  type: string
- description: The name of the change set.
  name: ChangeSetName
  type: string
- description: The ARN of the stack associated with the change set.
  name: StackId
  type: string
- description: The name of the stack associated with the change set.
  name: StackName
  type: string
- description: Information about the change set.
  name: Description
  type: string
- description: The execution status of the change set.
  name: ExecutionStatus
  type: string
- description: The current status of the change set.
  name: Status
  type: string
- description: A description of the current status of the change set.
  name: StatusReason
  type: string
- description: The start time when the change set was created.
  name: CreationTime
  type: string
- description: A list of structures that describe the resources and their changes.
  name: Changes
  type: array
provider_name: Amazon CloudFormation
provider_slug: amazon-cloudformation
schema_file: json-schema/cloudformation-change-set-schema.json
slug: cloudformation-change-set
tags:
- AWS
- CloudFormation
- Infrastructure as Code
- DevOps
- IaC
title: ChangeSet
---
