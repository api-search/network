---
description: Represents a deployed application in IBM WebSphere Application Server or Liberty, including its configuration, modules, deployment targets, and runtime status.
layout: schema
name: WebSphere Application
properties_list:
- description: The unique name of the application within the server or cell.
  name: name
  type: string
- description: Human-readable display name for the application.
  name: displayName
  type: string
- description: Description of the application purpose and functionality.
  name: description
  type: string
- description: Current runtime status of the application.
  name: status
  type: string
- description: Application archive type.
  name: type
  type: string
- description: Context root for web modules within the application.
  name: contextRoot
  type: string
- description: File system location of the application archive or directory.
  name: location
  type: string
- description: Whether the application starts automatically when the server starts.
  name: autoStart
  type: boolean
- description: Name of the server where the application is deployed.
  name: targetServer
  type: string
- description: Name of the cluster where the application is deployed.
  name: targetCluster
  type: string
- description: Application modules contained within the deployment.
  name: modules
  type: array
- description: Class loader policy for the application.
  name: classloaderPolicy
  type: string
- description: Class loading delegation mode.
  name: classloaderMode
  type: string
- description: Security roles defined in the application.
  name: securityRoles
  type: array
- description: Session management configuration.
  name: sessionManagement
  type: object
- description: Application version identifier.
  name: version
  type: string
- description: Date and time the application was deployed.
  name: deployedDate
  type: string
- description: Date and time the application was last modified.
  name: lastModified
  type: string
- description: Additional metadata associated with the application.
  name: metadata
  type: object
provider_name: IBM WebSphere
provider_slug: websphere
schema_file: json-schema/application.json
slug: application
tags:
- Application Server
- Cloud Native
- Enterprise Java
- J2EE
- Microservices
- Middleware
title: WebSphere Application
---
