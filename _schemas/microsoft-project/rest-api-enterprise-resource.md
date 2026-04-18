---
description: Enterprise resource schema from Microsoft Project Online REST API
layout: schema
name: EnterpriseResource
properties_list:
- description: Resource identifier
  name: Id
  type: string
- description: Resource name
  name: Name
  type: string
- description: Resource email address
  name: Email
  type: string
- description: Resource type (0=Material, 1=Work, 2=Cost)
  name: ResourceType
  type: integer
- description: Whether the resource is active
  name: IsActive
  type: boolean
- description: Whether this is a generic resource
  name: IsGeneric
  type: boolean
- description: Maximum assignment units
  name: MaxUnits
  type: number
- description: Standard billing rate
  name: StandardRate
  type: number
- description: Cost center code
  name: CostCenter
  type: string
- description: Resource group
  name: Group
  type: string
- description: Base calendar name
  name: BaseCalendar
  type: string
provider_name: Microsoft Project
provider_slug: microsoft-project
schema_file: json-schema/rest-api-enterprise-resource-schema.json
slug: rest-api-enterprise-resource
tags:
- Budgeting
- Gantt Charts
- Microsoft
- Portfolio Management
- Project Management
- Resource Management
- Scheduling
- Task Management
title: EnterpriseResource
---
