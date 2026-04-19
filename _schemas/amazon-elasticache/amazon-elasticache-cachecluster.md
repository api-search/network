---
description: Schema representing an Amazon ElastiCache cache cluster, which is a collection of cache nodes running Redis or Memcached cache engine software.
layout: schema
name: Amazon ElastiCache CacheCluster
properties_list:
- description: The user-supplied identifier of the cluster. This identifier is a unique key that identifies a cluster.
  name: CacheClusterId
  type: string
- description: The ARN (Amazon Resource Name) of the cache cluster.
  name: ARN
  type: string
- description: The current state of this cluster.
  name: CacheClusterStatus
  type: string
- description: The name of the cache engine used in this cluster.
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
- description: The name of the Availability Zone in which the cluster is located or "Multiple" if the cache nodes are located in different Availability Zones.
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
- description: Status of the cache parameter group.
  name: CacheParameterGroup
  type: object
- description: A list of cache nodes that are members of the cluster.
  name: CacheNodes
  type: array
- description: Represents a Memcached cluster endpoint which can be used by an application to connect to any node in the cluster.
  name: ConfigurationEndpoint
  type: object
- description: A list of VPC Security Groups associated with the cluster.
  name: SecurityGroups
  type: array
- description: The replication group to which this cluster belongs.
  name: ReplicationGroupId
  type:
  - string
  - 'null'
- description: The number of days for which ElastiCache retains automatic cluster snapshots.
  name: SnapshotRetentionLimit
  type: integer
- description: The daily time range (in UTC) during which ElastiCache begins taking a daily snapshot of your cluster.
  name: SnapshotWindow
  type: string
- description: If true, then minor version patches are applied automatically.
  name: AutoMinorVersionUpgrade
  type: boolean
- description: The port number on which each of the cache nodes accepts connections.
  name: Port
  type: integer
- description: Describes a notification topic and its status.
  name: NotificationConfiguration
  type: object
- description: A flag that enables in-transit encryption when set to true.
  name: TransitEncryptionEnabled
  type: boolean
- description: A flag that enables encryption at rest when set to true.
  name: AtRestEncryptionEnabled
  type: boolean
provider_name: Amazon ElastiCache
provider_slug: amazon-elasticache
schema_file: json-schema/amazon-elasticache-cachecluster-schema.json
slug: amazon-elasticache-cachecluster
tags:
- Amazon Web Services
- AWS
- Caching
- Database
- ElastiCache
- In-Memory
- Memcached
- Redis
title: Amazon ElastiCache CacheCluster
---
