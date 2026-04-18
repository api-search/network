---
description: Profile of the managed cluster load balancer.
layout: schema
name: ManagedClusterLoadBalancerProfile
properties_list:
- description: Desired managed outbound IPs for the cluster load balancer.
  name: managedOutboundIPs
  type: object
- description: Desired outbound IP Prefix resources for the cluster load balancer.
  name: outboundIPPrefixes
  type: object
- description: Desired outbound IP resources for the cluster load balancer.
  name: outboundIPs
  type: object
- description: The effective outbound IP resources of the cluster load balancer.
  name: effectiveOutboundIPs
  type: array
- description: The desired number of allocated SNAT ports per VM.
  name: allocatedOutboundPorts
  type: integer
- description: Desired outbound flow idle timeout in minutes.
  name: idleTimeoutInMinutes
  type: integer
provider_name: Azure Kubernetes Service
provider_slug: azure-kubernetes-service
schema_file: json-schema/azure-kubernetes-service-managed-cluster-load-balancer-profile-schema.json
slug: azure-kubernetes-service-managed-cluster-load-balancer-profile
tags:
- Azure
- Cloud
- Containers
- DevOps
- Kubernetes
- Orchestration
title: ManagedClusterLoadBalancerProfile
---
