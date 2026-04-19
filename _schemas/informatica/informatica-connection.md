---
description: Schema for an Informatica Intelligent Cloud Services (IICS) connection resource. Connections define the configuration required to access data sources and targets including databases, flat files, cloud applications, and SaaS services through the Platform REST API.
layout: schema
name: Informatica IICS Connection
properties_list:
- description: The resource type identifier for the IICS REST API. Always set to 'connection' for connection resources.
  name: '@type'
  type: string
- description: The unique identifier for the connection, assigned by the platform upon creation.
  name: id
  type: string
- description: The organization ID that owns this connection.
  name: orgId
  type: string
- description: The display name of the connection. Must be unique within the organization. Spaces in the name are encoded as %20 when used in URI paths.
  name: name
  type: string
- description: A human-readable description of the connection and its purpose.
  name: description
  type: string
- description: The connection type that determines which data source or target the connection accesses. Each type requires specific configuration properties.
  name: type
  type: string
- description: The ISO 8601 timestamp when the connection was created.
  name: createTime
  type: string
- description: The ISO 8601 timestamp when the connection was last updated.
  name: updateTime
  type: string
- description: The username of the user who created the connection.
  name: createdBy
  type: string
- description: The username of the user who last updated the connection.
  name: updatedBy
  type: string
- description: The ID of the Secure Agent associated with the connection. The Secure Agent provides the runtime execution environment on-premises or in a private cloud.
  name: agentId
  type: string
- description: The ID of the runtime environment associated with the connection. Determines where connection operations are executed.
  name: runtimeEnvironmentId
  type: string
- description: The hostname or IP address of the data source server. Required for database and server-based connection types such as Oracle, MySQL, and SqlServer.
  name: host
  type: string
- description: The port number for the data source server. Required for database connections.
  name: port
  type: integer
- description: 'The database name, service name, or SID for the connection. The meaning varies by connection type: for Oracle this is the service name or SID, for MySQL and SqlServer this is the database name.'
  name: database
  type: string
- description: The database schema name. Used to narrow the scope of accessible objects within the database.
  name: schema
  type: string
- description: The username for authenticating with the data source.
  name: username
  type: string
- description: The password for authenticating with the data source. This value is write-only and is not returned in GET responses.
  name: password
  type: string
- description: The authentication method used by the connection. Available values depend on the connection type.
  name: authenticationType
  type: string
- description: The service endpoint URL. Required for web service and cloud application connections such as Salesforce, WebServicesConsumer, and TOOLKIT connections.
  name: serviceUrl
  type: string
- description: The character encoding used for the connection. Determines how character data is read from and written to the source or target.
  name: codepage
  type: string
- description: Additional connection parameters specific to the connection type. Contains configuration attributes that are not represented as top-level properties. The available parameters vary by connection type.
  name: connParams
  type: object
provider_name: Informatica
provider_slug: informatica
schema_file: json-schema/informatica-connection-schema.json
slug: informatica-connection
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
title: Informatica IICS Connection
---
