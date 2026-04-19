---
description: An SSM Parameter Store parameter containing configuration data.
layout: schema
name: Parameter
properties_list:
- description: The name of the parameter.
  name: Name
  type: string
- description: The type of parameter.
  name: Type
  type: string
- description: The parameter value.
  name: Value
  type: string
- description: The parameter version.
  name: Version
  type: integer
- description: The Amazon Resource Name (ARN) of the parameter.
  name: ARN
  type: string
- description: Date the parameter was last changed or updated.
  name: LastModifiedDate
  type: string
- description: The data type of the parameter.
  name: DataType
  type: string
- description: Either the version number or the label used to retrieve the parameter value.
  name: Selector
  type: string
- description: The raw result or response from the source.
  name: SourceResult
  type: string
provider_name: Amazon Systems Manager
provider_slug: amazon-systems-manager
schema_file: json-schema/amazon-systems-manager-parameter-schema.json
slug: amazon-systems-manager-parameter
tags:
- Automation
- AWS
- Management
- Operations
title: Parameter
---
