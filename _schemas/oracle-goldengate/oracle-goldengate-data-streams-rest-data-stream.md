---
description: ''
layout: schema
name: DataStream
properties_list:
- description: Unique data stream name
  name: name
  type: string
- description: Stream description
  name: description
  type: string
- description: Current stream status
  name: status
  type: string
- description: Source configuration
  name: source
  type: object
- description: Target distribution configuration
  name: target
  type: object
- description: Table and operation filters
  name: filters
  type: array
- description: Path to the AsyncAPI specification
  name: asyncApiSpec
  type: string
- description: ''
  name: createdAt
  type: string
- description: ''
  name: updatedAt
  type: string
provider_name: Oracle GoldenGate
provider_slug: oracle-goldengate
schema_file: json-schema/oracle-goldengate-data-streams-rest-data-stream-schema.json
slug: oracle-goldengate-data-streams-rest-data-stream
tags:
- CDC
- Data Integration
- Data Synchronization
- Database
- Enterprise
- Real-Time Replication
title: DataStream
---
