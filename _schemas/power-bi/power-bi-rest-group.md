---
description: A Power BI workspace (group)
layout: schema
name: Group
properties_list:
- description: The unique identifier of the workspace
  name: id
  type: string
- description: The display name of the workspace
  name: name
  type: string
- description: Whether the workspace is read-only
  name: isReadOnly
  type: boolean
- description: Whether the workspace is on a dedicated capacity
  name: isOnDedicatedCapacity
  type: boolean
- description: The capacity ID if on a dedicated capacity
  name: capacityId
  type: string
- description: The workspace type
  name: type
  type: string
- description: The workspace state
  name: state
  type: string
provider_name: Power BI
provider_slug: power-bi
schema_file: json-schema/power-bi-rest-group-schema.json
slug: power-bi-rest-group
tags:
- Analytics
- Business Intelligence
- Dashboards
- Data Analysis
- Reporting
- Visualization
title: Group
---
