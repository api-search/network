---
description: A VMware vCenter client registered with the Application Migration Service
layout: schema
name: VcenterClient
properties_list:
- description: vCenter client ID
  name: vcenterClientID
  type: string
- description: ARN of the vCenter client
  name: arn
  type: string
- description: vCenter server hostname
  name: hostname
  type: string
- description: vCenter UUID
  name: vcenterUUID
  type: string
- description: Datacenter name
  name: datacenterName
  type: string
- description: Date/time client was last seen
  name: lastSeenDatetime
  type: string
- description: Tags applied to source servers discovered by this client
  name: sourceServerTags
  type: object
- description: Tags on the vCenter client
  name: tags
  type: object
provider_name: Amazon Application Migration Service
provider_slug: amazon-application-migration-service
schema_file: json-schema/application-migration-service-vcenter-client-schema.json
slug: application-migration-service-vcenter-client
tags:
- Amazon Application Migration Service
- Migration
- Lift And Shift
- AWS
- Cloud Migration
title: VcenterClient
---
