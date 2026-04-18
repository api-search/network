---
description: Profile of the managed cluster NAT gateway.
layout: schema
name: ManagedClusterNATGatewayProfile
properties_list:
- description: The managed outbound IP profile of the NAT gateway.
  name: managedOutboundIPProfile
  type: object
- description: The effective outbound IP resources of the NAT gateway.
  name: effectiveOutboundIPs
  type: array
- description: Desired outbound flow idle timeout in minutes.
  name: idleTimeoutInMinutes
  type: integer
provider_name: Azure Kubernetes Service
provider_slug: azure-kubernetes-service
schema_file: json-schema/azure-kubernetes-service-managed-cluster-nat-gateway-profile-schema.json
slug: azure-kubernetes-service-managed-cluster-nat-gateway-profile
tags:
- Azure
- Cloud
- Containers
- DevOps
- Kubernetes
- Orchestration
title: ManagedClusterNATGatewayProfile
---
