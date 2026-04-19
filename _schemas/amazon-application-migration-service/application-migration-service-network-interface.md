---
description: Network interface on a source server
layout: schema
name: NetworkInterface
properties_list:
- description: MAC address
  name: macAddress
  type: string
- description: IP addresses
  name: ips
  type: array
- description: Whether this is the primary interface
  name: isPrimary
  type: boolean
provider_name: Amazon Application Migration Service
provider_slug: amazon-application-migration-service
schema_file: json-schema/application-migration-service-network-interface-schema.json
slug: application-migration-service-network-interface
tags:
- Amazon Application Migration Service
- Migration
- Lift And Shift
- AWS
- Cloud Migration
title: NetworkInterface
---
