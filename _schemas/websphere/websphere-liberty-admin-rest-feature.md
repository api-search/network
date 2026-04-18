---
description: ''
layout: schema
name: Feature
properties_list:
- description: Feature symbolic name
  name: name
  type: string
- description: Human-readable feature name
  name: displayName
  type: string
- description: Feature version
  name: version
  type: string
- description: Feature description
  name: description
  type: string
- description: Whether the feature is currently enabled
  name: enabled
  type: boolean
- description: List of dependent feature names
  name: dependencies
  type: array
provider_name: IBM WebSphere
provider_slug: websphere
schema_file: json-schema/websphere-liberty-admin-rest-feature-schema.json
slug: websphere-liberty-admin-rest-feature
tags:
- Application Server
- Cloud Native
- Enterprise Java
- J2EE
- Microservices
- Middleware
title: Feature
---
