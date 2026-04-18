---
description: ''
layout: schema
name: PolicySchedule
properties_list:
- description: Name of the schedule
  name: scheduleName
  type: string
- description: Type of backup for this schedule
  name: scheduleType
  type: string
- description: Frequency in seconds between backup runs
  name: frequency
  type: integer
- description: ''
  name: retentionPeriod
  type: object
- description: Name of the storage unit for this schedule
  name: storageUnit
  type: string
- description: ''
  name: backupWindow
  type: object
- description: Maximum number of concurrent backup streams to a single device
  name: mediaMultiplexing
  type: integer
- description: Whether this schedule creates synthetic backups
  name: syntheticBackup
  type: boolean
provider_name: Veritas NetBackup
provider_slug: veritas-netbackup
schema_file: json-schema/veritas-netbackup-rest-policy-schedule-schema.json
slug: veritas-netbackup-rest-policy-schedule
tags:
- Backup
- Data Protection
- Disaster Recovery
- Enterprise
- Recovery
- Storage
title: PolicySchedule
---
