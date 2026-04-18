---
description: Represents a machine pool within a cluster, defining a group of compute nodes with shared configuration.
layout: schema
name: MachinePool
properties_list:
- description: The unique identifier of the machine pool.
  name: id
  type: string
- description: The cloud provider instance type for nodes in this pool.
  name: instance_type
  type: string
- description: The fixed number of nodes in this machine pool.
  name: replicas
  type: integer
- description: Autoscaling configuration for the machine pool.
  name: autoscaling
  type: object
- description: The availability zones where nodes will be placed.
  name: availability_zones
  type: array
- description: Kubernetes labels applied to nodes in this pool.
  name: labels
  type: object
- description: Kubernetes taints applied to nodes in this pool.
  name: taints
  type: array
provider_name: Red Hat
provider_slug: red-hat
schema_file: json-schema/red-hat-openshift-cluster-manager-machine-pool-schema.json
slug: red-hat-openshift-cluster-manager-machine-pool
tags:
- Cloud
- Containers
- Enterprise
- Hybrid Cloud
- Kubernetes
- Linux
- Open Source
title: MachinePool
---
