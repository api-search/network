---
description: CacheCluster schema from Amazon ElastiCache API
layout: schema
name: CacheCluster
properties_list:
- description: The user-supplied identifier of the cluster.
  name: CacheClusterId
  type: string
- description: The current state of this cluster.
  name: CacheClusterStatus
  type: string
- description: The name of the cache engine used for this cluster.
  name: Engine
  type: string
- description: The version of the cache engine that is used in this cluster.
  name: EngineVersion
  type: string
- description: The name of the compute and memory capacity node type for the cluster.
  name: CacheNodeType
  type: string
- description: The number of cache nodes in the cluster.
  name: NumCacheNodes
  type: integer
- description: The name of the Availability Zone in which the cluster is located.
  name: PreferredAvailabilityZone
  type: string
- description: The date and time when the cluster was created.
  name: CacheClusterCreateTime
  type: string
- description: Specifies the weekly time range during which maintenance on the cluster is performed.
  name: PreferredMaintenanceWindow
  type: string
- description: The name of the cache subnet group associated with the cluster.
  name: CacheSubnetGroupName
  type: string
- description: A list of cache nodes that are members of the cluster.
  name: CacheNodes
  type: array
- description: If true, then minor version patches are applied automatically.
  name: AutoMinorVersionUpgrade
  type: boolean
- description: A list of VPC Security Groups associated with the cluster.
  name: SecurityGroups
  type: array
- description: The replication group to which this cluster belongs.
  name: ReplicationGroupId
  type: string
- description: The number of days for which ElastiCache retains automatic cluster snapshots.
  name: SnapshotRetentionLimit
  type: integer
- description: The ARN of the cache cluster.
  name: ARN
  type: string
provider_name: Amazon ElastiCache
provider_slug: amazon-elasticache
schema_file: json-schema/amazon-elasticache-cache-cluster-schema.json
slug: amazon-elasticache-cache-cluster
tags:
- Amazon Web Services
- AWS
- Caching
- Database
- ElastiCache
- In-Memory
- Memcached
- Redis
title: CacheCluster
---
