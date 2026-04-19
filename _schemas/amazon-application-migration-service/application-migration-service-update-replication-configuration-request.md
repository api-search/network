---
description: Request to update replication configuration
layout: schema
name: UpdateReplicationConfigurationRequest
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
- description: EC2 instance type for replication servers
  name: replicationServerInstanceType
  type: string
- description: Whether to use low bandwidth
  name: useLowBandwidthForReplication
  type: boolean
- description: Bandwidth throttling in Mbps
  name: bandwidthThrottling
  type: integer
- description: Data plane routing mode
  name: dataPlaneRouting
  type: string
- description: Whether to create public IP
  name: createPublicIP
  type: boolean
- description: Account ID for cross-account access
  name: accountID
  type: string
provider_name: Amazon Application Migration Service
provider_slug: amazon-application-migration-service
schema_file: json-schema/application-migration-service-update-replication-configuration-request-schema.json
slug: application-migration-service-update-replication-configuration-request
tags:
- Amazon Application Migration Service
- Migration
- Lift And Shift
- AWS
- Cloud Migration
title: UpdateReplicationConfigurationRequest
---
