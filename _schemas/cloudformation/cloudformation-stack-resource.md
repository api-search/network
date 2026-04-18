---
description: ''
layout: schema
name: StackResource
properties_list:
- description: The name of the stack.
  name: StackName
  type: string
- description: Unique identifier of the stack.
  name: StackId
  type: string
- description: The logical name of the resource specified in the template.
  name: LogicalResourceId
  type: string
- description: The name or unique identifier of the physical resource.
  name: PhysicalResourceId
  type: string
- description: Type of AWS resource.
  name: ResourceType
  type: string
- description: Time the status was updated.
  name: Timestamp
  type: string
- description: Current status of the resource.
  name: ResourceStatus
  type: string
- description: Message associated with the resource status.
  name: ResourceStatusReason
  type: string
- description: User-defined description.
  name: Description
  type: string
provider_name: AWS CloudFormation
provider_slug: cloudformation
schema_file: json-schema/cloudformation-stack-resource-schema.json
slug: cloudformation-stack-resource
tags:
- Automation
- AWS
- Cloud Resources
- IaC
- Infrastructure As Code
- Stack Management
title: StackResource
---
