---
description: Request to update a replication configuration template
layout: schema
name: UpdateReplicationConfigurationTemplateRequest
properties_list:
- description: Template ID to update
  name: replicationConfigurationTemplateID
  type: string
- description: stagingAreaSubnetId
  name: stagingAreaSubnetId
  type: string
- description: associateDefaultSecurityGroup
  name: associateDefaultSecurityGroup
  type: boolean
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
provider_name: Amazon Application Migration Service
provider_slug: amazon-application-migration-service
schema_file: json-schema/application-migration-service-update-replication-configuration-template-request-schema.json
slug: application-migration-service-update-replication-configuration-template-request
tags:
- Amazon Application Migration Service
- Migration
- Lift And Shift
- AWS
- Cloud Migration
title: UpdateReplicationConfigurationTemplateRequest
---
