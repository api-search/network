---
description: Connection schema from Oracle Integration Developer API.
layout: schema
name: Connection
properties_list:
- description: Connection identifier.
  name: id
  type: string
- description: Connection display name.
  name: name
  type: string
- description: Connection description.
  name: description
  type: string
- description: Connection status.
  name: status
  type: string
- description: Type of adapter used by the connection.
  name: adapterType
  type: string
- description: Percentage of connection configuration completion.
  name: percentageComplete
  type: integer
- description: Whether the connection is locked.
  name: lockedFlag
  type: boolean
- description: Last test status.
  name: testStatus
  type: string
- description: User who last updated the connection.
  name: lastUpdatedBy
  type: string
- description: Last update timestamp.
  name: lastUpdated
  type: string
provider_name: Oracle Integration
provider_slug: oracle-integration
schema_file: json-schema/developer-api-connection-schema.json
slug: developer-api-connection
tags:
- API Management
- Automation
- B2B Integration
- Cloud Integration
- Enterprise Integration
- Integration
- iPaaS
- Process Automation
title: Connection
---
