---
description: ''
layout: schema
name: ModuleInfo
properties_list:
- description: A concatenated list of the module type hierarchy. For modules within other modules the format is Module1::Module2.
  name: TypeHierarchy
  type: string
- description: A concatenated list of the logical IDs of the module.
  name: LogicalIdHierarchy
  type: string
provider_name: AWS CloudFormation
provider_slug: cloudformation
schema_file: json-schema/cloudformation-module-info-schema.json
slug: cloudformation-module-info
tags:
- Automation
- AWS
- Cloud Resources
- IaC
- Infrastructure As Code
- Stack Management
title: ModuleInfo
---
