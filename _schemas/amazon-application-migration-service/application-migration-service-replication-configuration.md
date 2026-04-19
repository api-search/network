---
description: Replication configuration for a source server
layout: schema
name: ReplicationConfiguration
properties_list:
- description: Source server ID
  name: sourceServerID
  type: string
- description: Configuration name
  name: name
  type: string
- description: Subnet ID for staging area
  name: stagingAreaSubnetId
  type: string
- description: Whether to associate default security group
  name: associateDefaultSecurityGroup
  type: boolean
- description: Security group IDs for replication servers
  name: replicationServersSecurityGroupsIDs
  type: array
- description: EC2 instance type for replication servers
  name: replicationServerInstanceType
  type: string
- description: Whether to use low bandwidth for replication
  name: useLowBandwidthForReplication
  type: boolean
- description: Data plane routing mode
  name: dataPlaneRouting
  type: string
- description: Whether to create public IP for replication servers
  name: createPublicIP
  type: boolean
- description: Tags for staging area resources
  name: stagingAreaTags
  type: object
- description: Replicated disk configurations
  name: replicatedDisks
  type: array
- description: Bandwidth throttling in Mbps (0 for unlimited)
  name: bandwidthThrottling
  type: integer
- description: Default EBS volume type for large staging disks
  name: defaultLargeStagingDiskType
  type: string
- description: EBS encryption setting
  name: ebsEncryption
  type: string
- description: KMS key ARN for EBS encryption
  name: ebsEncryptionKeyArn
  type: string
provider_name: Amazon Application Migration Service
provider_slug: amazon-application-migration-service
schema_file: json-schema/application-migration-service-replication-configuration-schema.json
slug: application-migration-service-replication-configuration
tags:
- Amazon Application Migration Service
- Migration
- Lift And Shift
- AWS
- Cloud Migration
title: ReplicationConfiguration
---
