---
description: JSON Schema for an Azure DevOps work item (Bug, Task, User Story, Epic, Feature, etc.).
layout: schema
name: Azure DevOps Work Item
properties_list:
- description: Work item ID
  name: id
  type: integer
- description: Work item revision number
  name: rev
  type: integer
- description: Work item field values keyed by reference name
  name: fields
  type: object
- description: Links to related work items and artifacts
  name: relations
  type: array
- description: API URL for the work item
  name: url
  type: string
provider_name: Azure DevOps
provider_slug: azure-devops
schema_file: json-schema/azure-devops-workitem-schema.json
slug: azure-devops-workitem
tags:
- Azure
- CI/CD
- DevOps
- Pipelines
- Work Items
title: Azure DevOps Work Item
---
