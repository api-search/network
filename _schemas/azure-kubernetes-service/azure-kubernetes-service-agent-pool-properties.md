---
description: Properties for the container service agent pool profile.
layout: schema
name: AgentPoolProperties
properties_list:
- description: The current deployment or provisioning state.
  name: provisioningState
  type: string
- description: Number of agents (VMs) to host docker containers. Allowed values must be in the range of 0 to 1000 (inclusive) for user pools and in the range of 1 to 1000 (inclusive) for system pools. The default va
  name: count
  type: integer
- description: The size of the agent VMs.
  name: vmSize
  type: string
- description: OS Disk Size in GB.
  name: osDiskSizeGB
  type: integer
- description: The OS disk type.
  name: osDiskType
  type: string
- description: Kubelet disk type.
  name: kubeletDiskType
  type: string
- description: The maximum number of pods that can run on a node.
  name: maxPods
  type: integer
- description: The operating system type.
  name: osType
  type: string
- description: Specifies the OS SKU used by the agent pool.
  name: osSKU
  type: string
- description: The type of Agent Pool.
  name: type
  type: string
- description: A cluster must have at least one System agent pool at all times.
  name: mode
  type: string
- description: The version of Kubernetes running on the Agent Pool.
  name: orchestratorVersion
  type: string
- description: The running Kubernetes version on the Agent Pool.
  name: currentOrchestratorVersion
  type: string
- description: The version of node image.
  name: nodeImageVersion
  type: string
- description: Whether to enable auto-scaler.
  name: enableAutoScaling
  type: boolean
- description: The minimum number of nodes for auto-scaling.
  name: minCount
  type: integer
- description: The maximum number of nodes for auto-scaling.
  name: maxCount
  type: integer
- description: The Virtual Machine Scale Set priority.
  name: scaleSetPriority
  type: string
- description: The Virtual Machine Scale Set eviction policy.
  name: scaleSetEvictionPolicy
  type: string
- description: The maximum price for spot instances.
  name: spotMaxPrice
  type: number
- description: Describes how VMs are added to or removed from Agent Pools.
  name: scaleDownMode
  type: string
- description: The ID of the subnet for agent pool nodes.
  name: vnetSubnetID
  type: string
- description: The ID of the subnet for pods.
  name: podSubnetID
  type: string
- description: Whether each node gets its own public IP.
  name: enableNodePublicIP
  type: boolean
- description: The public IP prefix ID for the nodes.
  name: nodePublicIPPrefixID
  type: string
- description: Whether to enable host-based encryption.
  name: enableEncryptionAtHost
  type: boolean
- description: Whether to use FIPS-enabled OS.
  name: enableFIPS
  type: boolean
- description: Whether to enable UltraSSD.
  name: enableUltraSSD
  type: boolean
- description: The node labels to be persisted across all nodes.
  name: nodeLabels
  type: object
- description: The taints added to new nodes.
  name: nodeTaints
  type: array
- description: The tags to persist on the VMSS.
  name: tags
  type: object
- description: The ID for Proximity Placement Group.
  name: proximityPlacementGroupID
  type: string
- description: The list of Availability zones to use for nodes.
  name: availabilityZones
  type: array
- description: The type of workload a node can run.
  name: workloadRuntime
  type: string
- description: A base64-encoded message of the day for Linux nodes.
  name: messageOfTheDay
  type: string
provider_name: Azure Kubernetes Service
provider_slug: azure-kubernetes-service
schema_file: json-schema/azure-kubernetes-service-agent-pool-properties-schema.json
slug: azure-kubernetes-service-agent-pool-properties
tags:
- Azure
- Cloud
- Containers
- DevOps
- Kubernetes
- Orchestration
title: AgentPoolProperties
---
