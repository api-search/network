---
description: Migration result for an individual zone during evacuation
layout: schema
name: EvacuationMigrationResult
properties_list:
- description: Name of the evacuated zone
  name: zoneName
  type: string
- description: Whether the zone was successfully evacuated
  name: evacuated
  type: boolean
- description: Remote host where the zone was migrated
  name: evacuationTarget
  type: string
- description: Status of the individual zone migration
  name: migrationStatus
  type: string
- description: Error details if migration failed
  name: migrationError
  type: object
provider_name: Solaris Zones
provider_slug: solaris-zones
schema_file: json-schema/solaris-rad-zonemgr-evacuation-migration-result-schema.json
slug: solaris-rad-zonemgr-evacuation-migration-result
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
title: EvacuationMigrationResult
---
