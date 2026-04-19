---
description: Template for default replication configuration settings
layout: schema
name: ReplicationConfigurationTemplate
properties_list:
- description: Template ID
  name: replicationConfigurationTemplateID
  type: string
- description: ARN of the template
  name: arn
  type: string
- description: Subnet ID for staging area
  name: stagingAreaSubnetId
  type: string
- description: Whether to associate default security group
  name: associateDefaultSecurityGroup
  type: boolean
- description: Security group IDs
  name: replicationServersSecurityGroupsIDs
  type: array
- description: EC2 instance type for replication servers
  name: replicationServerInstanceType
  type: string
- description: Whether to use low bandwidth
  name: useLowBandwidthForReplication
  type: boolean
- description: Data plane routing mode
  name: dataPlaneRouting
  type: string
- description: Whether to create public IP
  name: createPublicIP
  type: boolean
- description: Tags for staging resources
  name: stagingAreaTags
  type: object
- description: Bandwidth throttling in Mbps
  name: bandwidthThrottling
  type: integer
- description: Default disk type for large disks
  name: defaultLargeStagingDiskType
  type: string
- description: EBS encryption setting
  name: ebsEncryption
  type: string
- description: Tags on the template
  name: tags
  type: object
provider_name: Amazon Application Migration Service
provider_slug: amazon-application-migration-service
schema_file: json-schema/application-migration-service-replication-configuration-template-schema.json
slug: application-migration-service-replication-configuration-template
tags:
- Amazon Application Migration Service
- Migration
- Lift And Shift
- AWS
- Cloud Migration
title: ReplicationConfigurationTemplate
---
