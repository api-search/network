---
description: ''
layout: schema
name: CollectiveCluster
properties_list:
- description: Cluster name
  name: name
  type: string
- description: Cluster description
  name: description
  type: string
- description: Number of members in the cluster
  name: memberCount
  type: integer
- description: Number of started members
  name: membersStarted
  type: integer
- description: List of member server names
  name: members
  type: array
provider_name: IBM WebSphere
provider_slug: websphere
schema_file: json-schema/websphere-liberty-collective-controller-rest-collective-cluster-schema.json
slug: websphere-liberty-collective-controller-rest-collective-cluster
tags:
- Application Server
- Cloud Native
- Enterprise Java
- J2EE
- Microservices
- Middleware
title: CollectiveCluster
---
