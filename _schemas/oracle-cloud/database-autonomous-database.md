---
description: An Oracle Autonomous Database.
layout: schema
name: AutonomousDatabase
properties_list:
- description: The OCID.
  name: id
  type: string
- description: The OCID of the compartment.
  name: compartmentId
  type: string
- description: User-friendly name.
  name: displayName
  type: string
- description: The database name.
  name: dbName
  type: string
- description: Number of CPU cores.
  name: cpuCoreCount
  type: integer
- description: Data storage size in terabytes.
  name: dataStorageSizeInTBs
  type: integer
- description: The workload type.
  name: dbWorkload
  type: string
- description: Current state.
  name: lifecycleState
  type: string
- description: Whether this is an Always Free resource.
  name: isFreeTier
  type: boolean
- description: Whether auto scaling is enabled.
  name: isAutoScalingEnabled
  type: boolean
- description: ''
  name: connectionUrls
  type: object
- description: ''
  name: timeCreated
  type: string
- description: ''
  name: freeformTags
  type: object
provider_name: Oracle Cloud Infrastructure
provider_slug: oracle-cloud
schema_file: json-schema/database-autonomous-database-schema.json
slug: database-autonomous-database
tags:
- Cloud Computing
- Enterprise Cloud
- Infrastructure as a Service
- Oracle
- Platform as a Service
title: AutonomousDatabase
---
