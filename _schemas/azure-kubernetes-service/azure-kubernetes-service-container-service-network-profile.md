---
description: Profile of network configuration.
layout: schema
name: ContainerServiceNetworkProfile
properties_list:
- description: Network plugin used for building the Kubernetes network.
  name: networkPlugin
  type: string
- description: The mode the network plugin should use.
  name: networkPluginMode
  type: string
- description: Network policy used for building the Kubernetes network.
  name: networkPolicy
  type: string
- description: Network dataplane used in the Kubernetes cluster.
  name: networkDataplane
  type: string
- description: A CIDR notation IP range from which to assign pod IPs.
  name: podCidr
  type: string
- description: A CIDR notation IP range from which to assign service cluster IPs.
  name: serviceCidr
  type: string
- description: An IP address assigned to the Kubernetes DNS service. It must be within the Kubernetes service address range.
  name: dnsServiceIP
  type: string
- description: The outbound (egress) routing method.
  name: outboundType
  type: string
- description: The load balancer sku for the managed cluster.
  name: loadBalancerSku
  type: string
- description: IP families used to specify IP versions available to the cluster.
  name: ipFamilies
  type: array
provider_name: Azure Kubernetes Service
provider_slug: azure-kubernetes-service
schema_file: json-schema/azure-kubernetes-service-container-service-network-profile-schema.json
slug: azure-kubernetes-service-container-service-network-profile
tags:
- Azure
- Cloud
- Containers
- DevOps
- Kubernetes
- Orchestration
title: ContainerServiceNetworkProfile
---
