---
description: ''
layout: schema
name: Replicat
properties_list:
- description: Replicat process name
  name: name
  type: string
- description: Type of replicat
  name: type
  type: string
- description: Current process status
  name: status
  type: string
- description: ''
  name: description
  type: string
- description: Source trail file path
  name: trail
  type: string
- description: Checkpoint table name
  name: checkpointTable
  type: string
- description: Parameter file content lines
  name: config
  type: array
- description: ''
  name: credentials
  type: object
provider_name: Oracle GoldenGate
provider_slug: oracle-goldengate
schema_file: json-schema/oracle-goldengate-rest-replicat-schema.json
slug: oracle-goldengate-rest-replicat
tags:
- CDC
- Data Integration
- Data Synchronization
- Database
- Enterprise
- Real-Time Replication
title: Replicat
---
