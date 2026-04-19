---
description: Represents a connection to a data source or target in Informatica Intelligent Cloud Services.
layout: schema
name: Connection
properties_list:
- description: The resource type identifier.
  name: '@type'
  type: string
- description: The unique identifier for the connection.
  name: id
  type: string
- description: The organization ID that owns the connection.
  name: orgId
  type: string
- description: The name of the connection.
  name: name
  type: string
- description: A description of the connection.
  name: description
  type: string
- description: The connection type (e.g., Oracle, Salesforce, MySQL, SqlServer, FTP, CSVFile).
  name: type
  type: string
- description: The time the connection was created.
  name: createTime
  type: string
- description: The time the connection was last updated.
  name: updateTime
  type: string
- description: The user who created the connection.
  name: createdBy
  type: string
- description: The user who last updated the connection.
  name: updatedBy
  type: string
- description: The ID of the Secure Agent associated with the connection.
  name: agentId
  type: string
- description: The ID of the runtime environment associated with the connection.
  name: runtimeEnvironmentId
  type: string
- description: The hostname or IP address for the connection. Applicable to database and server-based connections.
  name: host
  type: string
- description: The port number for the connection. Applicable to database and server-based connections.
  name: port
  type: integer
- description: The database name or service name for the connection.
  name: database
  type: string
- description: The database schema name.
  name: schema
  type: string
- description: The username for authentication.
  name: username
  type: string
- description: The password for authentication.
  name: password
  type: string
- description: The authentication method used by the connection.
  name: authenticationType
  type: string
- description: The service endpoint URL. Applicable to web service and cloud application connections.
  name: serviceUrl
  type: string
- description: The character encoding for the connection (e.g., UTF-8).
  name: codepage
  type: string
- description: Additional connection parameters specific to the connection type. Contains attributes not listed as top-level fields.
  name: connParams
  type: object
provider_name: Informatica
provider_slug: informatica
schema_file: json-schema/informatica-platform-rest-connection-schema.json
slug: informatica-platform-rest-connection
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
title: Connection
---
