---
description: StackResource schema
layout: schema
name: StackResource
properties_list:
- description: The name associated with the stack.
  name: StackName
  type: string
- description: Unique identifier of the stack.
  name: StackId
  type: string
- description: The logical name of the resource specified in the template.
  name: LogicalResourceId
  type: string
- description: The name or unique identifier of the resource.
  name: PhysicalResourceId
  type: string
- description: Type of resource (e.g., AWS::EC2::Instance).
  name: ResourceType
  type: string
- description: Time the status was updated.
  name: Timestamp
  type: string
- description: Current status of the resource.
  name: ResourceStatus
  type: string
- description: Success or failure message associated with the resource.
  name: ResourceStatusReason
  type: string
- description: User defined description associated with the resource.
  name: Description
  type: string
- description: ''
  name: DriftInformation
  type: object
provider_name: Amazon CloudFormation
provider_slug: amazon-cloudformation
schema_file: json-schema/cloudformation-stack-resource-schema.json
slug: cloudformation-stack-resource
tags:
- AWS
- CloudFormation
- Infrastructure as Code
- DevOps
- IaC
title: StackResource
---
