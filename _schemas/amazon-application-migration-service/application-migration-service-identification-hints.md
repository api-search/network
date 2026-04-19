---
description: Hints used to identify the source server
layout: schema
name: IdentificationHints
properties_list:
- description: Fully qualified domain name
  name: fqdn
  type: string
- description: Hostname
  name: hostname
  type: string
- description: VMware UUID
  name: vmWareUuid
  type: string
- description: AWS instance ID if previously in AWS
  name: awsInstanceID
  type: string
- description: VMware path
  name: vmPath
  type: string
provider_name: Amazon Application Migration Service
provider_slug: amazon-application-migration-service
schema_file: json-schema/application-migration-service-identification-hints-schema.json
slug: application-migration-service-identification-hints
tags:
- Amazon Application Migration Service
- Migration
- Lift And Shift
- AWS
- Cloud Migration
title: IdentificationHints
---
