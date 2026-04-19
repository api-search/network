---
description: A source server registered with the Application Migration Service
layout: schema
name: SourceServer
properties_list:
- description: Unique identifier for the source server
  name: sourceServerID
  type: string
- description: ARN of the source server
  name: arn
  type: string
- description: Whether the source server is archived
  name: isArchived
  type: boolean
- description: Tags applied to the source server
  name: tags
  type: object
- description: lifeCycle
  name: lifeCycle
  type: string
- description: dataReplicationInfo
  name: dataReplicationInfo
  type: string
- description: sourceProperties
  name: sourceProperties
  type: string
- description: launchedInstance
  name: launchedInstance
  type: string
- description: ID of the application this server belongs to
  name: applicationID
  type: string
- description: ID of the vCenter client this server was discovered from
  name: vcenterClientID
  type: string
- description: Replication type for the source server
  name: replicationType
  type: string
- description: User-provided identifier for the source server
  name: userProvidedID
  type: string
- description: FQDN used for action framework connectivity
  name: fqdnForActionFramework
  type: string
provider_name: Amazon Application Migration Service
provider_slug: amazon-application-migration-service
schema_file: json-schema/application-migration-service-source-server-schema.json
slug: application-migration-service-source-server
tags:
- Amazon Application Migration Service
- Migration
- Lift And Shift
- AWS
- Cloud Migration
title: SourceServer
---
