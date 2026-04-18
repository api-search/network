---
description: ''
layout: schema
name: Stack
properties_list:
- description: Unique identifier of the stack.
  name: StackId
  type: string
- description: The name associated with the stack.
  name: StackName
  type: string
- description: The unique ID of the change set.
  name: ChangeSetId
  type: string
- description: A user-defined description associated with the stack.
  name: Description
  type: string
- description: The time the stack was created.
  name: CreationTime
  type: string
- description: The time the stack was deleted.
  name: DeletionTime
  type: string
- description: The time the stack was last updated.
  name: LastUpdatedTime
  type: string
- description: Explanation for the current stack status.
  name: StackStatusReason
  type: string
- description: Whether rollback on stack creation failures is disabled.
  name: DisableRollback
  type: boolean
- description: Amazon SNS topic ARNs for stack event notifications.
  name: NotificationARNs
  type: array
- description: Time allowed for stack creation before failure.
  name: TimeoutInMinutes
  type: integer
- description: The capabilities allowed in the stack.
  name: Capabilities
  type: array
- description: A list of output structures.
  name: Outputs
  type: array
- description: The IAM role ARN used by CloudFormation.
  name: RoleARN
  type: string
- description: Tags associated with the stack.
  name: Tags
  type: array
- description: Whether termination protection is enabled.
  name: EnableTerminationProtection
  type: boolean
- description: A list of parameter structures.
  name: Parameters
  type: array
- description: For nested stacks, the stack ID of the direct parent.
  name: ParentId
  type: string
- description: For nested stacks, the stack ID of the top-level stack.
  name: RootId
  type: string
- description: ''
  name: DeletionMode
  type: string
- description: ''
  name: DetailedStatus
  type: string
- description: ''
  name: RetainExceptOnCreate
  type: boolean
provider_name: AWS CloudFormation
provider_slug: cloudformation
schema_file: json-schema/cloudformation-stack-schema.json
slug: cloudformation-stack
tags:
- Automation
- AWS
- Cloud Resources
- IaC
- Infrastructure As Code
- Stack Management
title: Stack
---
