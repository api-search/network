---
description: ''
layout: schema
name: ChangeSetSummary
properties_list:
- description: The ID of the stack with which the change set is associated.
  name: StackId
  type: string
- description: ''
  name: StackName
  type: string
- description: The ARN of the change set.
  name: ChangeSetId
  type: string
- description: ''
  name: ChangeSetName
  type: string
- description: ''
  name: ExecutionStatus
  type: string
- description: ''
  name: Status
  type: string
- description: ''
  name: StatusReason
  type: string
- description: ''
  name: CreationTime
  type: string
- description: ''
  name: Description
  type: string
- description: ''
  name: IncludeNestedStacks
  type: boolean
- description: ''
  name: ImportExistingResources
  type: boolean
- description: ''
  name: ParentChangeSetId
  type: string
- description: ''
  name: RootChangeSetId
  type: string
provider_name: AWS CloudFormation
provider_slug: cloudformation
schema_file: json-schema/cloudformation-change-set-summary-schema.json
slug: cloudformation-change-set-summary
tags:
- Automation
- AWS
- Cloud Resources
- IaC
- Infrastructure As Code
- Stack Management
title: ChangeSetSummary
---
