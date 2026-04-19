---
description: Request body for updating an existing connection.
layout: schema
name: ConnectionUpdateRequest
properties_list:
- description: The resource type identifier. Must be set to "connection".
  name: '@type'
  type: string
- description: The updated name for the connection.
  name: name
  type: string
- description: An updated description of the connection.
  name: description
  type: string
- description: The updated hostname or IP address.
  name: host
  type: string
- description: The updated port number.
  name: port
  type: integer
- description: The updated database name.
  name: database
  type: string
- description: The updated database schema.
  name: schema
  type: string
- description: The updated username.
  name: username
  type: string
- description: The updated password.
  name: password
  type: string
- description: The updated authentication method.
  name: authenticationType
  type: string
- description: The updated service endpoint URL.
  name: serviceUrl
  type: string
- description: The updated character encoding.
  name: codepage
  type: string
- description: Updated connection-type-specific parameters.
  name: connParams
  type: object
provider_name: Informatica
provider_slug: informatica
schema_file: json-schema/informatica-platform-rest-connection-update-request-schema.json
slug: informatica-platform-rest-connection-update-request
tags:
- Address Verification
- B2B Gateway
- Cloud Services
- Data Governance
- Data Integration
- Data Profiling
- Data Quality
- Enterprise Software
- ETL
- IDMC
- IICS
- Master Data Management
- Reference Data Management
title: ConnectionUpdateRequest
---
