---
description: Represents a cluster of IBM WebSphere Application Server instances or Liberty collective members that work together to provide high availability, workload distribution, and failover capabilities.
layout: schema
name: WebSphere Cluster
properties_list:
- description: The unique name of the cluster.
  name: name
  type: string
- description: Human-readable display name for the cluster.
  name: displayName
  type: string
- description: Description of the cluster purpose and configuration.
  name: description
  type: string
- description: Overall cluster status based on member states.
  name: status
  type: string
- description: Type of cluster.
  name: clusterType
  type: string
- description: Name of the cell this cluster belongs to.
  name: cellName
  type: string
- description: Server instances that are members of this cluster.
  name: members
  type: array
- description: Total number of members in the cluster.
  name: memberCount
  type: integer
- description: Number of currently running members.
  name: membersStarted
  type: integer
- description: Whether to prefer routing requests to local cluster members.
  name: preferLocal
  type: boolean
- description: Load balancing configuration for the cluster.
  name: loadBalancingPolicy
  type: object
- description: Auto-scaling policy for the cluster.
  name: scalingPolicy
  type: object
- description: Service policy configuration.
  name: servicePolicy
  type: object
- description: Data replication configuration for the cluster.
  name: replicationDomain
  type: object
- description: Applications deployed to this cluster.
  name: applications
  type: array
- description: Date and time the cluster was created.
  name: createdDate
  type: string
- description: Date and time the cluster was last modified.
  name: lastModified
  type: string
- description: Additional metadata associated with the cluster.
  name: metadata
  type: object
provider_name: IBM WebSphere
provider_slug: websphere
schema_file: json-schema/cluster.json
slug: cluster
tags:
- Application Server
- Cloud Native
- Enterprise Java
- J2EE
- Microservices
- Middleware
title: WebSphere Cluster
---
