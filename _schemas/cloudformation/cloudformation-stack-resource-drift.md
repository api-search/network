---
description: ''
layout: schema
name: StackResourceDrift
properties_list:
- description: ''
  name: StackId
  type: string
- description: ''
  name: LogicalResourceId
  type: string
- description: ''
  name: PhysicalResourceId
  type: string
- description: ''
  name: PhysicalResourceIdContext
  type: array
- description: ''
  name: ResourceType
  type: string
- description: A JSON string of the expected property values as defined in the template.
  name: ExpectedProperties
  type: string
- description: A JSON string of the actual property values of the resource.
  name: ActualProperties
  type: string
- description: ''
  name: PropertyDifferences
  type: array
- description: ''
  name: StackResourceDriftStatus
  type: string
- description: ''
  name: Timestamp
  type: string
provider_name: AWS CloudFormation
provider_slug: cloudformation
schema_file: json-schema/cloudformation-stack-resource-drift-schema.json
slug: cloudformation-stack-resource-drift
tags:
- Automation
- AWS
- Cloud Resources
- IaC
- Infrastructure As Code
- Stack Management
title: StackResourceDrift
---
