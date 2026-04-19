---
description: A role with associated permissions
layout: schema
name: Role
properties_list:
- description: Role identifier
  name: id
  type: string
- description: Role name
  name: name
  type: string
- description: Role description
  name: description
  type: string
- description: List of permissions assigned to this role
  name: permissions
  type: array
provider_name: Acceldata
provider_slug: acceldata
schema_file: json-schema/adoc-api-role-schema.json
slug: adoc-api-role
tags:
- AI Agents
- Data Management
- Data Observability
- Data Pipeline
- Data Quality
- Intelligence
- Observability
title: Role
---
