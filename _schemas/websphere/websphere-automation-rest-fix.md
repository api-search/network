---
description: ''
layout: schema
name: Fix
properties_list:
- description: Fix identifier
  name: id
  type: string
- description: Fix name
  name: name
  type: string
- description: ''
  name: type
  type: string
- description: ''
  name: description
  type: string
- description: CVEs resolved by this fix
  name: resolvedCVEs
  type: array
- description: WebSphere versions this fix applies to
  name: applicableVersions
  type: array
- description: ''
  name: downloadURL
  type: string
- description: ''
  name: releaseDate
  type: string
- description: Fix size in bytes
  name: size
  type: integer
provider_name: IBM WebSphere
provider_slug: websphere
schema_file: json-schema/websphere-automation-rest-fix-schema.json
slug: websphere-automation-rest-fix
tags:
- Application Server
- Cloud Native
- Enterprise Java
- J2EE
- Microservices
- Middleware
title: Fix
---
