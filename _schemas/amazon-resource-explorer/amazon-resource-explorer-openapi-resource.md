---
description: Resource schema from openapi
layout: schema
name: Resource
properties_list:
- description: The Amazon Resource Name (ARN) of the resource.
  name: Arn
  type: string
- description: The date and time the resource was last updated.
  name: LastReportedAt
  type: string
- description: The AWS account ID of the account that owns the resource.
  name: OwningAccountId
  type: string
- description: The AWS Region where the resource exists.
  name: Region
  type: string
- description: The type of the resource.
  name: ResourceType
  type: string
- description: The AWS service that owns the resource.
  name: Service
  type: string
provider_name: Amazon Resource Explorer
provider_slug: amazon-resource-explorer
schema_file: json-schema/amazon-resource-explorer-openapi-resource-schema.json
slug: amazon-resource-explorer-openapi-resource
tags:
- AWS
- Discovery
- Inventory
- Operations
- Resource Management
title: Resource
---
