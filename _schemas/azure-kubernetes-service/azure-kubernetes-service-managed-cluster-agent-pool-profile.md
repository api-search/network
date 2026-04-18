---
description: Profile for the container service agent pool.
layout: schema
name: ManagedClusterAgentPoolProfile
properties_list:
- description: The unique name of the agent pool profile in the context of the subscription and resource group.
  name: name
  type: string
- description: Number of agents (VMs) to host docker containers. Allowed values must be in the range of 0 to 1000 (inclusive) for user pools and in the range of 1 to 1000 (inclusive) for system pools.
  name: count
  type: integer
- description: 'The size of the agent VMs. Example: Standard_DS2_v2'
  name: vmSize
  type: string
- description: OS Disk Size in GB to be used to specify the disk size for every machine in the master/agent pool.
  name: osDiskSizeGB
  type: integer
- description: The OS disk type to be used for machines in the agent pool.
  name: osDiskType
  type: string
- description: Determines the placement of emptyDir volumes, container runtime data root, and Kubelet ephemeral storage.
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
- description: The mode of an agent pool. A cluster must have at least one System agent pool at all times.
  name: mode
  type: string
- description: The version of Kubernetes running on the Agent Pool.
  name: orchestratorVersion
  type: string
- description: The version of Kubernetes the Agent Pool is running.
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
- description: The maximum price (in US Dollars) you are willing to pay for spot instances. Possible values are any decimal value greater than zero or -1 which indicates that default price is up-to on-demand.
  name: spotMaxPrice
  type: number
- description: Describes how VMs are added to or removed from Agent Pools.
  name: scaleDownMode
  type: string
- description: The ID of the subnet which agent pool nodes and optionally pods will join on startup.
  name: vnetSubnetID
  type: string
- description: The ID of the subnet which pods will join when launched.
  name: podSubnetID
  type: string
- description: Whether each node is allocated its own public IP.
  name: enableNodePublicIP
  type: boolean
- description: The public IP prefix ID for the nodes in the agent pool.
  name: nodePublicIPPrefixID
  type: string
- description: Whether to enable host-based OS and data drive encryption.
  name: enableEncryptionAtHost
  type: boolean
- description: Whether to use a FIPS-enabled OS.
  name: enableFIPS
  type: boolean
- description: Whether to enable UltraSSD.
  name: enableUltraSSD
  type: boolean
- description: The node labels to be persisted across all nodes in agent pool.
  name: nodeLabels
  type: object
- description: The taints added to new nodes during node pool create and scale.
  name: nodeTaints
  type: array
- description: The tags to be persisted on the agent pool virtual machine scale set.
  name: tags
  type: object
- description: The ID for Proximity Placement Group.
  name: proximityPlacementGroupID
  type: string
- description: The list of Availability zones to use for nodes. This can only be specified if the AgentPoolType property is VirtualMachineScaleSets.
  name: availabilityZones
  type: array
- description: Determines the type of workload a node can run.
  name: workloadRuntime
  type: string
- description: A base64-encoded string which will be written to /etc/motd after decoding. Applicable only for Linux nodes.
  name: messageOfTheDay
  type: string
provider_name: Azure Kubernetes Service
provider_slug: azure-kubernetes-service
schema_file: json-schema/azure-kubernetes-service-managed-cluster-agent-pool-profile-schema.json
slug: azure-kubernetes-service-managed-cluster-agent-pool-profile
tags:
- Azure
- Cloud
- Containers
- DevOps
- Kubernetes
- Orchestration
title: ManagedClusterAgentPoolProfile
---
