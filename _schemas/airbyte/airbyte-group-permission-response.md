---
description: Provides details of a single group permission
layout: schema
name: GroupPermissionResponse
properties_list:
- description: The ID of the permission
  name: permissionId
  type: string
- description: The ID of the group
  name: groupId
  type: string
- description: ''
  name: permissionType
  type: object
- description: The workspace ID for workspace-scoped permissions
  name: workspaceId
  type: string
- description: The organization ID for organization-scoped permissions
  name: organizationId
  type: string
provider_name: Airbyte
provider_slug: airbyte
schema_file: json-schema/airbyte-group-permission-response-schema.json
slug: airbyte-group-permission-response
tags:
- Data Integration
- ETL
- ELT
- Open Source
- Data Pipeline
- Connectors
- Data
title: GroupPermissionResponse
---
