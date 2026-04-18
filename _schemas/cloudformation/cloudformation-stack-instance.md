---
description: ''
layout: schema
name: StackInstance
properties_list:
- description: ''
  name: StackSetId
  type: string
- description: ''
  name: Region
  type: string
- description: ''
  name: Account
  type: string
- description: ''
  name: StackId
  type: string
- description: ''
  name: ParameterOverrides
  type: array
- description: ''
  name: Status
  type: string
- description: ''
  name: StackInstanceStatus
  type: object
- description: ''
  name: StatusReason
  type: string
- description: ''
  name: DriftStatus
  type: string
- description: ''
  name: LastDriftCheckTimestamp
  type: string
provider_name: AWS CloudFormation
provider_slug: cloudformation
schema_file: json-schema/cloudformation-stack-instance-schema.json
slug: cloudformation-stack-instance
tags:
- Automation
- AWS
- Cloud Resources
- IaC
- Infrastructure As Code
- Stack Management
title: StackInstance
---
