---
description: Settings for upgrading an agentpool.
layout: schema
name: AgentPoolUpgradeSettings
properties_list:
- description: The maximum number or percentage of nodes that are surged during upgrade. This can either be set to an integer (e.g. 5) or a percentage (e.g. 50%). If a percentage is specified, it is the percentage o
  name: maxSurge
  type: string
- description: The amount of time (in minutes) to wait on eviction of pods and graceful termination per node.
  name: drainTimeoutInMinutes
  type: integer
- description: The amount of time (in minutes) to wait after draining a node and before reimaging it and moving on to the next node.
  name: nodeSoakDurationInMinutes
  type: integer
provider_name: Azure Kubernetes Service
provider_slug: azure-kubernetes-service
schema_file: json-schema/azure-kubernetes-service-agent-pool-upgrade-settings-schema.json
slug: azure-kubernetes-service-agent-pool-upgrade-settings
tags:
- Azure
- Cloud
- Containers
- DevOps
- Kubernetes
- Orchestration
title: AgentPoolUpgradeSettings
---
