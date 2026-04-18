---
description: Azure DevOps work item
layout: schema
name: WorkItem
properties_list:
- description: Work item ID
  name: id
  type: integer
- description: Revision number
  name: rev
  type: integer
- description: Work item field values
  name: fields
  type: object
- description: ''
  name: relations
  type: array
- description: ''
  name: url
  type: string
provider_name: Azure DevOps
provider_slug: azure-devops
schema_file: json-schema/azure-devops-work-items-work-item-schema.json
slug: azure-devops-work-items-work-item
tags:
- Azure
- CI/CD
- DevOps
- Pipelines
- Work Items
title: WorkItem
---
