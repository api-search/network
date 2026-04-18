---
description: ''
layout: schema
name: Pipeline
properties_list:
- description: Pipeline unique identifier
  name: id
  type: string
- description: Pipeline display name
  name: name
  type: string
- description: ''
  name: description
  type: string
- description: Current pipeline status
  name: status
  type: string
- description: ''
  name: createdBy
  type: string
- description: ''
  name: createdAt
  type: string
- description: ''
  name: updatedAt
  type: string
- description: ''
  name: sources
  type: array
- description: ''
  name: targets
  type: array
- description: ''
  name: stages
  type: array
provider_name: Oracle GoldenGate
provider_slug: oracle-goldengate
schema_file: json-schema/oracle-goldengate-stream-analytics-rest-pipeline-schema.json
slug: oracle-goldengate-stream-analytics-rest-pipeline
tags:
- CDC
- Data Integration
- Data Synchronization
- Database
- Enterprise
- Real-Time Replication
title: Pipeline
---
