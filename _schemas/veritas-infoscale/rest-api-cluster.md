---
description: Cluster schema from Veritas InfoScale REST API
layout: schema
name: Cluster
properties_list:
- description: Unique cluster identifier
  name: clusterId
  type: string
- description: Name of the cluster
  name: clusterName
  type: string
- description: Current cluster state
  name: state
  type: string
- description: Number of nodes in the cluster
  name: nodeCount
  type: integer
- description: InfoScale cluster version
  name: clusterVersion
  type: string
- description: I/O fencing mode
  name: fencingMode
  type: string
- description: Cluster uptime duration
  name: uptime
  type: string
- description: Last configuration change timestamp
  name: lastModified
  type: string
provider_name: Veritas InfoScale
provider_slug: veritas-infoscale
schema_file: json-schema/rest-api-cluster-schema.json
slug: rest-api-cluster
tags:
- Clustering
- Data Management
- Disaster Recovery
- High Availability
- Storage Management
- Virtualization
title: Cluster
---
