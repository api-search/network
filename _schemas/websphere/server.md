---
description: Represents an IBM WebSphere Application Server or Liberty server instance, including its configuration, runtime status, resource allocations, and management properties.
layout: schema
name: WebSphere Server
properties_list:
- description: The unique name of the server instance.
  name: name
  type: string
- description: Human-readable display name for the server.
  name: displayName
  type: string
- description: Description of the server purpose.
  name: description
  type: string
- description: Type of server.
  name: serverType
  type: string
- description: Current runtime status of the server.
  name: status
  type: string
- description: Name of the node where this server resides.
  name: nodeName
  type: string
- description: Name of the cell this server belongs to.
  name: cellName
  type: string
- description: Name of the cluster this server is a member of, if any.
  name: clusterName
  type: string
- description: Hostname or IP address of the machine running this server.
  name: hostName
  type: string
- description: WebSphere product version.
  name: version
  type: string
- description: Product edition (e.g., Base, Network Deployment, Liberty).
  name: productEdition
  type: string
- description: Operating system process ID of the running server.
  name: pid
  type: integer
- description: Server uptime in milliseconds.
  name: uptime
  type: integer
- description: Installation directory path.
  name: installDirectory
  type: string
- description: Server-specific configuration directory path.
  name: serverDirectory
  type: string
- description: Network ports configured for this server.
  name: ports
  type: array
- description: JVM configuration for this server.
  name: jvmConfig
  type: object
- description: Enabled Liberty features (Liberty servers only).
  name: features
  type: array
- description: Web container configuration.
  name: webContainer
  type: object
- description: Logging configuration.
  name: logging
  type: object
- description: Applications deployed on this server.
  name: applications
  type: array
- description: Data sources configured on this server.
  name: dataSources
  type: array
- description: Date and time the server was created.
  name: createdDate
  type: string
- description: Date and time the server was last started.
  name: lastStarted
  type: string
- description: Additional metadata associated with the server.
  name: metadata
  type: object
provider_name: IBM WebSphere
provider_slug: websphere
schema_file: json-schema/server.json
slug: server
tags:
- Application Server
- Cloud Native
- Enterprise Java
- J2EE
- Microservices
- Middleware
title: WebSphere Server
---
