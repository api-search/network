---
description: Provides details of a single group
layout: schema
name: GroupResponse
properties_list:
- description: The ID of the group
  name: groupId
  type: string
- description: The name of the group
  name: name
  type: string
- description: Optional description of the group
  name: description
  type: string
- description: The ID of the organization the group belongs to
  name: organizationId
  type: string
- description: The number of members in the group
  name: memberCount
  type: integer
provider_name: Airbyte
provider_slug: airbyte
schema_file: json-schema/airbyte-group-response-schema.json
slug: airbyte-group-response
tags:
- Data Integration
- ETL
- ELT
- Open Source
- Data Pipeline
- Connectors
- Data
title: GroupResponse
---
