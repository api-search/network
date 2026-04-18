---
description: ''
layout: schema
name: Application
properties_list:
- description: Application name
  name: name
  type: string
- description: Current application status
  name: status
  type: string
- description: Context root for web modules
  name: contextRoot
  type: string
- description: Target server or cluster
  name: targetServer
  type: string
- description: ''
  name: deployedModules
  type: array
- description: Last modification timestamp
  name: lastModified
  type: string
provider_name: IBM WebSphere
provider_slug: websphere
schema_file: json-schema/websphere-admin-rest-application-schema.json
slug: websphere-admin-rest-application
tags:
- Application Server
- Cloud Native
- Enterprise Java
- J2EE
- Microservices
- Middleware
title: Application
---
