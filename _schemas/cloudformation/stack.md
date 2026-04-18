---
description: Represents an AWS CloudFormation stack, which is a collection of AWS resources that you can manage as a single unit. A stack is created from a CloudFormation template and provisions the defined resources in the correct order based on dependency relationships.
layout: schema
name: AWS CloudFormation Stack
properties_list:
- description: Unique identifier of the stack, formatted as an Amazon Resource Name (ARN).
  name: StackId
  type: string
- description: The name associated with the stack. Must be unique within a region.
  name: StackName
  type: string
- description: The unique ID of the change set associated with this stack.
  name: ChangeSetId
  type: string
- description: A user-defined description associated with the stack.
  name: Description
  type:
  - string
  - 'null'
- description: The time at which the stack was created.
  name: CreationTime
  type: string
- description: The time the stack was deleted.
  name: DeletionTime
  type:
  - string
  - 'null'
- description: The time the stack was last updated. This field is only returned if the stack has been updated at least once.
  name: LastUpdatedTime
  type:
  - string
  - 'null'
- description: Current status of the stack.
  name: StackStatus
  type: string
- description: Success or failure message associated with the stack status.
  name: StackStatusReason
  type:
  - string
  - 'null'
- description: Boolean to enable or disable rollback on stack creation failures.
  name: DisableRollback
  type: boolean
- description: Amazon SNS topic ARNs to which stack related events are published.
  name: NotificationARNs
  type: array
- description: The amount of time within which stack creation should complete.
  name: TimeoutInMinutes
  type:
  - integer
  - 'null'
- description: The capabilities allowed in the stack.
  name: Capabilities
  type: array
- description: A list of output structures containing stack outputs.
  name: Outputs
  type: array
- description: The Amazon Resource Name (ARN) of an IAM role that CloudFormation assumes to create the stack.
  name: RoleARN
  type:
  - string
  - 'null'
- description: A list of tags associated with this stack.
  name: Tags
  type: array
- description: Whether termination protection is enabled for the stack.
  name: EnableTerminationProtection
  type: boolean
- description: A list of parameter structures.
  name: Parameters
  type: array
- description: ''
  name: RollbackConfiguration
  type: object
- description: For nested stacks, the stack ID of the direct parent of this stack.
  name: ParentId
  type:
  - string
  - 'null'
- description: For nested stacks, the stack ID of the top-level stack to which this stack belongs.
  name: RootId
  type:
  - string
  - 'null'
- description: ''
  name: DriftInformation
  type: object
- description: Specifies the deletion mode for the stack.
  name: DeletionMode
  type: string
- description: The detailed status of the resource or stack.
  name: DetailedStatus
  type:
  - string
  - 'null'
- description: When true, newly created resources are deleted when the operation rolls back.
  name: RetainExceptOnCreate
  type: boolean
provider_name: AWS CloudFormation
provider_slug: cloudformation
schema_file: json-schema/stack.json
slug: stack
tags:
- Automation
- AWS
- Cloud Resources
- IaC
- Infrastructure As Code
- Stack Management
title: AWS CloudFormation Stack
---
