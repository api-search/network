---
description: ''
layout: schema
name: CreateReplicatRequest
properties_list:
- description: ''
  name: type
  type: string
- description: ''
  name: description
  type: string
- description: Source trail file prefix
  name: trail
  type: string
- description: Checkpoint table in format schema.table
  name: checkpointTable
  type: string
- description: ''
  name: begin
  type: string
- description: Parameter file content
  name: config
  type: array
- description: ''
  name: credentials
  type: object
provider_name: Oracle GoldenGate
provider_slug: oracle-goldengate
schema_file: json-schema/oracle-goldengate-rest-create-replicat-request-schema.json
slug: oracle-goldengate-rest-create-replicat-request
tags:
- CDC
- Data Integration
- Data Synchronization
- Database
- Enterprise
- Real-Time Replication
title: CreateReplicatRequest
---
