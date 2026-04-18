---
description: ''
layout: schema
name: Deployment
properties_list:
- description: Unique name of the deployment
  name: name
  type: string
- description: Current status of the deployment
  name: status
  type: string
- description: Description of the deployment
  name: description
  type: string
- description: Oracle GoldenGate home directory
  name: oggHome
  type: string
- description: GoldenGate software version
  name: oggVersion
  type: string
- description: ''
  name: environmentVariables
  type: object
- description: ''
  name: services
  type: array
provider_name: Oracle GoldenGate
provider_slug: oracle-goldengate
schema_file: json-schema/oracle-goldengate-rest-deployment-schema.json
slug: oracle-goldengate-rest-deployment
tags:
- CDC
- Data Integration
- Data Synchronization
- Database
- Enterprise
- Real-Time Replication
title: Deployment
---
