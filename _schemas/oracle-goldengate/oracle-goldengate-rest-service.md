---
description: ''
layout: schema
name: Service
properties_list:
- description: Service name
  name: name
  type: string
- description: Service type
  name: type
  type: string
- description: Service status
  name: status
  type: string
- description: Service listening port
  name: port
  type: integer
- description: Whether the service uses SSL/TLS
  name: secure
  type: boolean
provider_name: Oracle GoldenGate
provider_slug: oracle-goldengate
schema_file: json-schema/oracle-goldengate-rest-service-schema.json
slug: oracle-goldengate-rest-service
tags:
- CDC
- Data Integration
- Data Synchronization
- Database
- Enterprise
- Real-Time Replication
title: Service
---
