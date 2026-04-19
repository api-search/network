---
description: Discovered properties of the source server
layout: schema
name: SourceProperties
properties_list:
- description: Date/time properties were last updated
  name: lastUpdatedDateTime
  type: string
- description: AWS instance type recommended for this server
  name: recommendedInstanceType
  type: string
- description: identificationHints
  name: identificationHints
  type: string
- description: Network interfaces on the source server
  name: networkInterfaces
  type: array
- description: Disks on the source server
  name: disks
  type: array
- description: CPUs on the source server
  name: cpus
  type: array
- description: RAM in bytes
  name: ramBytes
  type: integer
- description: os
  name: os
  type: string
provider_name: Amazon Application Migration Service
provider_slug: amazon-application-migration-service
schema_file: json-schema/application-migration-service-source-properties-schema.json
slug: application-migration-service-source-properties
tags:
- Amazon Application Migration Service
- Migration
- Lift And Shift
- AWS
- Cloud Migration
title: SourceProperties
---
