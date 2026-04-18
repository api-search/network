---
description: Represents a zone migration operation in Oracle Solaris, including migration type, state, progress tracking, connection details, and encryption cipher configuration for live and cold migrations between hosts.
layout: schema
name: Oracle Solaris Zone Migration
properties_list:
- description: Name of the zone being migrated
  name: zoneName
  type: string
- description: Destination host for the migration
  name: host
  type: string
- description: Migration type
  name: type
  type: string
- description: Current migration state
  name: state
  type: string
- description: Encryption cipher used for the migration data transfer
  name: cipher
  type:
  - string
  - 'null'
- description: ''
  name: progress
  type: object
- description: ''
  name: error
  type: object
- description: ''
  name: connection
  type: object
provider_name: Solaris Zones
provider_slug: solaris-zones
schema_file: json-schema/solaris-zone-migration-schema.json
slug: solaris-zone-migration
tags:
- Containers
- Kernel Zones
- Operating Systems
- Oracle
- RAD
- Resource Management
- Solaris
- StatsStore
- Virtualization
- Zones
title: Oracle Solaris Zone Migration
---
