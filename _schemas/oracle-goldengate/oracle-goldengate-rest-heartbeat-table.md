---
description: ''
layout: schema
name: HeartbeatTable
properties_list:
- description: Schema owner of the heartbeat table
  name: owner
  type: string
- description: Heartbeat table name
  name: table
  type: string
- description: Retention time in days
  name: retentionTime
  type: integer
- description: Update frequency in seconds
  name: frequency
  type: integer
- description: Purge frequency in minutes
  name: purgeFrequency
  type: integer
provider_name: Oracle GoldenGate
provider_slug: oracle-goldengate
schema_file: json-schema/oracle-goldengate-rest-heartbeat-table-schema.json
slug: oracle-goldengate-rest-heartbeat-table
tags:
- CDC
- Data Integration
- Data Synchronization
- Database
- Enterprise
- Real-Time Replication
title: HeartbeatTable
---
