---
description: Represents a resource within an AWS CloudFormation stack. Each resource corresponds to a physical AWS service resource (such as an EC2 instance, S3 bucket, or Lambda function) that is provisioned and managed as part of the stack lifecycle.
layout: schema
name: AWS CloudFormation Stack Resource
properties_list:
- description: The name of the stack the resource belongs to.
  name: StackName
  type:
  - string
  - 'null'
- description: Unique identifier of the stack.
  name: StackId
  type:
  - string
  - 'null'
- description: The logical name of the resource as specified in the template.
  name: LogicalResourceId
  type: string
- description: The name or unique identifier that corresponds to a physical instance ID of the resource.
  name: PhysicalResourceId
  type:
  - string
  - 'null'
- description: The type of the resource (e.g. AWS::EC2::Instance, AWS::S3::Bucket).
  name: ResourceType
  type: string
- description: The time the status was updated.
  name: Timestamp
  type: string
- description: Current status of the resource.
  name: ResourceStatus
  type: string
- description: Success or failure message associated with the resource.
  name: ResourceStatusReason
  type:
  - string
  - 'null'
- description: User-defined description associated with the resource.
  name: Description
  type:
  - string
  - 'null'
- description: ''
  name: DriftInformation
  type: object
- description: ''
  name: ModuleInfo
  type: object
provider_name: AWS CloudFormation
provider_slug: cloudformation
schema_file: json-schema/resource.json
slug: resource
tags:
- Automation
- AWS
- Cloud Resources
- IaC
- Infrastructure As Code
- Stack Management
title: AWS CloudFormation Stack Resource
---
