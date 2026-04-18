---
description: ''
layout: schema
name: Deployment
properties_list:
- description: OCID of the deployment
  name: id
  type: string
- description: ''
  name: displayName
  type: string
- description: ''
  name: description
  type: string
- description: ''
  name: compartmentId
  type: string
- description: ''
  name: subnetId
  type: string
- description: ''
  name: licenseModel
  type: string
- description: ''
  name: fqdn
  type: string
- description: ''
  name: cpuCoreCount
  type: integer
- description: ''
  name: isAutoScalingEnabled
  type: boolean
- description: ''
  name: isPublic
  type: boolean
- description: ''
  name: publicIpAddress
  type: string
- description: ''
  name: privateIpAddress
  type: string
- description: ''
  name: deploymentUrl
  type: string
- description: ''
  name: lifecycleState
  type: string
- description: ''
  name: oggData
  type: object
- description: ''
  name: timeCreated
  type: string
- description: ''
  name: timeUpdated
  type: string
- description: ''
  name: freeformTags
  type: object
- description: ''
  name: definedTags
  type: object
provider_name: Oracle GoldenGate
provider_slug: oracle-goldengate
schema_file: json-schema/oracle-goldengate-cloud-service-deployment-schema.json
slug: oracle-goldengate-cloud-service-deployment
tags:
- CDC
- Data Integration
- Data Synchronization
- Database
- Enterprise
- Real-Time Replication
title: Deployment
---
