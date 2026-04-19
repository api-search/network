---
description: Request body for creating a group permission
layout: schema
name: GroupPermissionCreateRequest
properties_list:
- description: ''
  name: permissionType
  type: object
- description: Required for workspace-scoped permissions
  name: workspaceId
  type: string
- description: Required for organization-scoped permissions
  name: organizationId
  type: string
provider_name: Airbyte
provider_slug: airbyte
schema_file: json-schema/airbyte-group-permission-create-request-schema.json
slug: airbyte-group-permission-create-request
tags:
- Data Integration
- ETL
- ELT
- Open Source
- Data Pipeline
- Connectors
- Data
title: GroupPermissionCreateRequest
---
