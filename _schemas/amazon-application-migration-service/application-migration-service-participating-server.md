---
description: A server participating in a migration job
layout: schema
name: ParticipatingServer
properties_list:
- description: Source server ID
  name: sourceServerID
  type: string
- description: Launch status
  name: launchStatus
  type: string
- description: Launched EC2 instance ID
  name: launchedEc2InstanceID
  type: string
- description: postLaunchActionsStatus
  name: postLaunchActionsStatus
  type: string
provider_name: Amazon Application Migration Service
provider_slug: amazon-application-migration-service
schema_file: json-schema/application-migration-service-participating-server-schema.json
slug: application-migration-service-participating-server
tags:
- Amazon Application Migration Service
- Migration
- Lift And Shift
- AWS
- Cloud Migration
title: ParticipatingServer
---
