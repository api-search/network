---
description: Request body for creating a new connection.
layout: schema
name: ConnectionCreateRequest
properties_list:
- description: The resource type identifier. Must be set to "connection".
  name: '@type'
  type: string
- description: The name for the new connection.
  name: name
  type: string
- description: A description of the connection.
  name: description
  type: string
- description: The connection type.
  name: type
  type: string
- description: The runtime environment ID for the connection.
  name: runtimeEnvironmentId
  type: string
- description: The hostname or IP address.
  name: host
  type: string
- description: The port number.
  name: port
  type: integer
- description: The database name or service name.
  name: database
  type: string
- description: The database schema.
  name: schema
  type: string
- description: The username for authentication.
  name: username
  type: string
- description: The password for authentication.
  name: password
  type: string
- description: The authentication method.
  name: authenticationType
  type: string
- description: The service endpoint URL.
  name: serviceUrl
  type: string
- description: The character encoding.
  name: codepage
  type: string
- description: Additional connection-type-specific parameters.
  name: connParams
  type: object
provider_name: Informatica
provider_slug: informatica
schema_file: json-schema/informatica-platform-rest-connection-create-request-schema.json
slug: informatica-platform-rest-connection-create-request
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
title: ConnectionCreateRequest
---
