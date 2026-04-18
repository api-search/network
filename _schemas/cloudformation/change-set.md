---
description: Represents an AWS CloudFormation change set. A change set allows you to preview the changes CloudFormation will make to your stack before executing them. You can create a change set, review the proposed changes, and then choose to execute or delete it.
layout: schema
name: AWS CloudFormation Change Set
properties_list:
- description: The ARN of the change set.
  name: ChangeSetId
  type: string
- description: The name of the change set.
  name: ChangeSetName
  type: string
- description: The ID of the stack associated with the change set.
  name: StackId
  type: string
- description: The name of the stack associated with the change set.
  name: StackName
  type: string
- description: Information about the change set.
  name: Description
  type:
  - string
  - 'null'
- description: A list of parameter values for the change set.
  name: Parameters
  type: array
- description: The start time when the change set was created.
  name: CreationTime
  type: string
- description: The execution status of the change set.
  name: ExecutionStatus
  type: string
- description: The current status of the change set.
  name: Status
  type: string
- description: A description of the change set's status, such as why the change set failed.
  name: StatusReason
  type:
  - string
  - 'null'
- description: The ARNs of the Amazon SNS topics associated with the change set.
  name: NotificationARNs
  type: array
- description: ''
  name: RollbackConfiguration
  type: object
- description: The capabilities that are allowed in the change set.
  name: Capabilities
  type: array
- description: Tags associated with the change set.
  name: Tags
  type: array
- description: A list of structures that describe the resources and the actions that CloudFormation will perform.
  name: Changes
  type: array
- description: Whether the change set includes changes to nested stacks.
  name: IncludeNestedStacks
  type: boolean
- description: Whether the change set imports resources that already exist.
  name: ImportExistingResources
  type: boolean
- description: The parent change set ID for nested stack change sets.
  name: ParentChangeSetId
  type:
  - string
  - 'null'
- description: The root change set ID for nested stack change sets.
  name: RootChangeSetId
  type:
  - string
  - 'null'
- description: The type of change set operation.
  name: ChangeSetType
  type: string
provider_name: AWS CloudFormation
provider_slug: cloudformation
schema_file: json-schema/change-set.json
slug: change-set
tags:
- Automation
- AWS
- Cloud Resources
- IaC
- Infrastructure As Code
- Stack Management
title: AWS CloudFormation Change Set
---
