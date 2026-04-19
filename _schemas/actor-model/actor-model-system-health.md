---
description: Overall health status of the actor system
layout: schema
name: SystemHealth
properties_list:
- description: Overall health
  name: status
  type: string
- description: Total active actors
  name: activeActors
  type: integer
- description: Current message throughput
  name: messagesPerSecond
  type: number
- description: Error rate (messages failed / total)
  name: errorRate
  type: number
- description: Messages sent to dead letter queue
  name: deadLetters
  type: integer
- description: Number of cluster nodes
  name: clusterSize
  type: integer
- description: System uptime in seconds
  name: uptime
  type: integer
provider_name: Actor Model
provider_slug: actor-model
schema_file: json-schema/actor-model-system-health-schema.json
slug: actor-model-system-health
tags:
- Actor Model
- Concurrency
- Distributed Systems
title: SystemHealth
---
