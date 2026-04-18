---
description: ''
layout: schema
name: Replicat
properties_list:
- description: Replicat process name
  name: name
  type: string
- description: ''
  name: type
  type: string
- description: ''
  name: status
  type: string
- description: Source trail file
  name: trail
  type: string
- description: Big data handler type
  name: handler
  type: string
- description: Parameter file content including handler configuration
  name: config
  type: array
- description: Path to handler properties file
  name: handlerProperties
  type: string
provider_name: Oracle GoldenGate
provider_slug: oracle-goldengate
schema_file: json-schema/oracle-goldengate-big-data-rest-replicat-schema.json
slug: oracle-goldengate-big-data-rest-replicat
tags:
- CDC
- Data Integration
- Data Synchronization
- Database
- Enterprise
- Real-Time Replication
title: Replicat
---
