---
description: ''
layout: schema
name: JsonPatchOperation
properties_list:
- description: ''
  name: op
  type: string
- description: JSON Pointer path to the field
  name: path
  type: string
- description: New value for add/replace operations
  name: value
  type: string
- description: Source path for copy/move operations
  name: from
  type: string
provider_name: Azure DevOps
provider_slug: azure-devops
schema_file: json-schema/azure-devops-work-items-json-patch-operation-schema.json
slug: azure-devops-work-items-json-patch-operation
tags:
- Azure
- CI/CD
- DevOps
- Pipelines
- Work Items
title: JsonPatchOperation
---
