---
description: Parameters to be applied to the cluster-autoscaler.
layout: schema
name: ManagedClusterAutoScalerProfile
properties_list:
- description: Detects similar node pools and balances the number of nodes between them.
  name: balance-similar-node-groups
  type: string
- description: If set to true, all daemonset pods on empty nodes will be evicted before deletion of the node.
  name: daemonset-eviction-for-empty-nodes
  type: boolean
- description: If set to true, all daemonset pods on occupied nodes will be evicted before deletion of the node.
  name: daemonset-eviction-for-occupied-nodes
  type: boolean
- description: The expander to use when scaling up.
  name: expander
  type: string
- description: The maximum number of empty nodes that can be deleted at the same time.
  name: max-empty-bulk-delete
  type: string
- description: Maximum number of seconds the cluster autoscaler waits for pod termination when trying to scale down a node.
  name: max-graceful-termination-sec
  type: string
- description: The maximum time the autoscaler waits for a node to be provisioned.
  name: max-node-provision-time
  type: string
- description: Maximum percentage of unready nodes in the cluster. After this percentage is exceeded, the cluster autoscaler halts operations.
  name: max-total-unready-percentage
  type: string
- description: For scenarios like burst/batch scale where you do not want CA to act before the kubernetes scheduler could schedule all the pods.
  name: new-pod-scale-up-delay
  type: string
- description: Number of allowed unready nodes, irrespective of max-total-unready-percentage.
  name: ok-total-unready-count
  type: string
- description: How often the cluster is reevaluated for scale up or down.
  name: scan-interval
  type: string
- description: How long after scale up that scale down evaluation resumes.
  name: scale-down-delay-after-add
  type: string
- description: How long after node deletion that scale down evaluation resumes.
  name: scale-down-delay-after-delete
  type: string
- description: How long after scale down failure that scale down evaluation resumes.
  name: scale-down-delay-after-failure
  type: string
- description: How long a node should be unneeded before it is eligible for scale down.
  name: scale-down-unneeded-time
  type: string
- description: How long an unready node should be unneeded before it is eligible for scale down.
  name: scale-down-unready-time
  type: string
- description: Node utilization level, defined as sum of requested resources divided by capacity, below which a node can be considered for scale down.
  name: scale-down-utilization-threshold
  type: string
- description: Whether the cluster autoscaler will skip deleting nodes with pods with local storage.
  name: skip-nodes-with-local-storage
  type: string
- description: Whether the cluster autoscaler will skip deleting nodes with pods from kube-system (except for DaemonSet or mirror pods).
  name: skip-nodes-with-system-pods
  type: string
provider_name: Azure Kubernetes Service
provider_slug: azure-kubernetes-service
schema_file: json-schema/azure-kubernetes-service-managed-cluster-auto-scaler-profile-schema.json
slug: azure-kubernetes-service-managed-cluster-auto-scaler-profile
tags:
- Azure
- Cloud
- Containers
- DevOps
- Kubernetes
- Orchestration
title: ManagedClusterAutoScalerProfile
---
