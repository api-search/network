---
description: The top level Log Analytics Workspace resource container.
layout: schema
name: Workspace
properties_list:
- description: Fully qualified resource ID.
  name: id
  type: string
- description: The name of the resource.
  name: name
  type: string
- description: The type of the resource.
  name: type
  type: string
- description: The geo-location where the resource lives.
  name: location
  type: string
- description: Resource tags.
  name: tags
  type: object
- description: The etag of the workspace.
  name: etag
  type: string
- description: Workspace properties.
  name: properties
  type: object
provider_name: Azure Log Analytics
provider_slug: azure-log-analytics
schema_file: json-schema/management-api-workspace-schema.json
slug: management-api-workspace
tags:
- Analytics
- Azure
- Cloud
- Logging
- Monitoring
title: Workspace
---
