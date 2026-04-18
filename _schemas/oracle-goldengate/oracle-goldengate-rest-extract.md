---
description: ''
layout: schema
name: Extract
properties_list:
- description: Extract process name
  name: name
  type: string
- description: Type of extract
  name: type
  type: string
- description: Current process status
  name: status
  type: string
- description: ''
  name: description
  type: string
- description: Begin position (NOW, SCN value, or timestamp)
  name: begin
  type: string
- description: Trail file path
  name: trail
  type: string
- description: Trail file size in MB
  name: trailSize
  type: integer
- description: Parameter file content lines
  name: config
  type: array
- description: Database registration alias
  name: registration
  type: string
- description: ''
  name: credentials
  type: object
provider_name: Oracle GoldenGate
provider_slug: oracle-goldengate
schema_file: json-schema/oracle-goldengate-rest-extract-schema.json
slug: oracle-goldengate-rest-extract
tags:
- CDC
- Data Integration
- Data Synchronization
- Database
- Enterprise
- Real-Time Replication
title: Extract
---
