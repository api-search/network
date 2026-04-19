---
description: Schema representing an Amazon CloudFormation stack, which is a collection of AWS resources that you can manage as a single unit.
layout: schema
name: Amazon CloudFormation Stack
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
- description: A list of Parameter structures that specify input parameters for the stack.
  name: Parameters
  type: array
- description: The time at which the stack was created.
  name: CreationTime
  type: string
- description: The time the stack was deleted.
  name: DeletionTime
  type: string
- description: The time the stack was last updated.
  name: LastUpdatedTime
  type: string
- description: ''
  name: RollbackConfiguration
  type: object
- description: Current status of the stack.
  name: StackStatus
  type: string
- description: Success or failure message associated with the stack status.
  name: StackStatusReason
  type: string
- description: Boolean to enable or disable rollback on stack creation failures.
  name: DisableRollback
  type: boolean
- description: Amazon SNS topic ARNs to which stack related events are published.
  name: NotificationARNs
  type: array
- description: The amount of time within which stack creation should complete.
  name: TimeoutInMinutes
  type: integer
- description: The capabilities allowed in the stack.
  name: Capabilities
  type: array
- description: A list of output structures.
  name: Outputs
  type: array
- description: The Amazon Resource Name (ARN) of an IAM role that CloudFormation assumes to create the stack.
  name: RoleARN
  type: string
- description: A list of tags associated with the stack.
  name: Tags
  type: array
- description: Whether termination protection is enabled for the stack.
  name: EnableTerminationProtection
  type: boolean
- description: ''
  name: DriftInformation
  type: object
- description: A list of stack resources.
  name: Resources
  type: array
provider_name: Amazon CloudFormation
provider_slug: amazon-cloudformation
schema_file: json-schema/amazon-cloudformation-stack-schema.json
slug: amazon-cloudformation-stack
tags:
- AWS
- CloudFormation
- Infrastructure as Code
- DevOps
- IaC
title: Amazon CloudFormation Stack
---
