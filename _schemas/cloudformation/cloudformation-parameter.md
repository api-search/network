---
description: ''
layout: schema
name: Parameter
properties_list:
- description: The key associated with the parameter.
  name: ParameterKey
  type: string
- description: The input value associated with the parameter.
  name: ParameterValue
  type: string
- description: Use the existing parameter value during stack updates.
  name: UsePreviousValue
  type: boolean
- description: The value that resolves to for SSM parameter types.
  name: ResolvedValue
  type: string
provider_name: AWS CloudFormation
provider_slug: cloudformation
schema_file: json-schema/cloudformation-parameter-schema.json
slug: cloudformation-parameter
tags:
- Automation
- AWS
- Cloud Resources
- IaC
- Infrastructure As Code
- Stack Management
title: Parameter
---
