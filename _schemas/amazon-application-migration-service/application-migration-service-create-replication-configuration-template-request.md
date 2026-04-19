---
description: Request to create a replication configuration template
layout: schema
name: CreateReplicationConfigurationTemplateRequest
properties_list:
- description: Subnet ID
  name: stagingAreaSubnetId
  type: string
- description: Associate default security group
  name: associateDefaultSecurityGroup
  type: boolean
- description: replicationServersSecurityGroupsIDs
  name: replicationServersSecurityGroupsIDs
  type: array
- description: replicationServerInstanceType
  name: replicationServerInstanceType
  type: string
- description: useLowBandwidthForReplication
  name: useLowBandwidthForReplication
  type: boolean
- description: dataPlaneRouting
  name: dataPlaneRouting
  type: string
- description: createPublicIP
  name: createPublicIP
  type: boolean
- description: stagingAreaTags
  name: stagingAreaTags
  type: object
- description: defaultLargeStagingDiskType
  name: defaultLargeStagingDiskType
  type: string
- description: ebsEncryption
  name: ebsEncryption
  type: string
- description: bandwidthThrottling
  name: bandwidthThrottling
  type: integer
- description: tags
  name: tags
  type: object
provider_name: Amazon Application Migration Service
provider_slug: amazon-application-migration-service
schema_file: json-schema/application-migration-service-create-replication-configuration-template-request-schema.json
slug: application-migration-service-create-replication-configuration-template-request
tags:
- Amazon Application Migration Service
- Migration
- Lift And Shift
- AWS
- Cloud Migration
title: CreateReplicationConfigurationTemplateRequest
---
