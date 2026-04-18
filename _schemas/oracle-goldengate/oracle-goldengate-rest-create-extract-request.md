---
description: ''
layout: schema
name: CreateExtractRequest
properties_list:
- description: ''
  name: type
  type: string
- description: ''
  name: description
  type: string
- description: Begin position (NOW, SCN value, or timestamp)
  name: begin
  type: string
- description: Trail file prefix (e.g., aa)
  name: trail
  type: string
- description: Trail file size in MB (default 500)
  name: trailSize
  type: integer
- description: Parameter file content
  name: config
  type: array
- description: ''
  name: registration
  type: string
- description: ''
  name: credentials
  type: object
provider_name: Oracle GoldenGate
provider_slug: oracle-goldengate
schema_file: json-schema/oracle-goldengate-rest-create-extract-request-schema.json
slug: oracle-goldengate-rest-create-extract-request
tags:
- CDC
- Data Integration
- Data Synchronization
- Database
- Enterprise
- Real-Time Replication
title: CreateExtractRequest
---
