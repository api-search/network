---
description: Represents a cluster of compute resources in a FinSpace kdb environment.
layout: schema
name: KxCluster
properties_list:
- description: ''
  name: clusterName
  type: string
- description: ''
  name: status
  type: string
- description: ''
  name: statusReason
  type: string
- description: ''
  name: clusterType
  type: string
- description: ''
  name: tickerplantLogConfiguration
  type: object
- description: ''
  name: volumes
  type: array
- description: ''
  name: databases
  type: array
- description: ''
  name: cacheStorageConfigurations
  type: array
- description: ''
  name: autoScalingConfiguration
  type: object
- description: ''
  name: clusterDescription
  type: string
- description: ''
  name: capacityConfiguration
  type: object
- description: ''
  name: releaseLabel
  type: string
- description: ''
  name: vpcConfiguration
  type: object
- description: ''
  name: initializationScript
  type: string
- description: ''
  name: commandLineArguments
  type: array
- description: ''
  name: code
  type: object
- description: ''
  name: executionRole
  type: string
- description: ''
  name: lastModifiedTimestamp
  type: string
- description: ''
  name: savedownStorageConfiguration
  type: object
- description: ''
  name: azMode
  type: string
- description: ''
  name: availabilityZoneId
  type: string
- description: ''
  name: createdTimestamp
  type: string
- description: ''
  name: tags
  type: object
provider_name: Amazon FinSpace
provider_slug: amazon-finspace
schema_file: json-schema/amazon-finspace-kx-cluster-schema.json
slug: amazon-finspace-kx-cluster
tags:
- AWS
- Capital Markets
- Data Analytics
- Data Management
- Financial Services
title: KxCluster
---
