---
description: Schema representing an Oracle GoldenGate deployment including its services, processes, connections, and configuration. Covers both on-premises Microservices Architecture deployments and OCI GoldenGate cloud deployments.
layout: schema
name: Oracle GoldenGate Deployment
properties_list:
- description: Core deployment configuration
  name: deployment
  type: object
- description: Microservices within the deployment
  name: services
  type: array
- description: Extract processes for change data capture
  name: extracts
  type: array
- description: Replicat processes for data apply
  name: replicats
  type: array
- description: Database connections
  name: connections
  type: array
- description: Distribution paths for trail data delivery
  name: distributionPaths
  type: array
- description: Receiver/collector paths for receiving trail data
  name: receiverPaths
  type: array
- description: Data stream configurations
  name: dataStreams
  type: array
- description: Heartbeat table configuration for lag monitoring
  name: heartbeat
  type: object
- description: User-defined tags (free-form and defined tags for cloud deployments)
  name: tags
  type: object
provider_name: Oracle GoldenGate
provider_slug: oracle-goldengate
schema_file: json-schema/oracle-goldengate-deployment-schema.json
slug: oracle-goldengate-deployment
tags:
- CDC
- Data Integration
- Data Synchronization
- Database
- Enterprise
- Real-Time Replication
title: Oracle GoldenGate Deployment
---
