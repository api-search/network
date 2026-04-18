---
description: Workload Auto-scaler profile for the managed cluster.
layout: schema
name: ManagedClusterWorkloadAutoScalerProfile
properties_list:
- description: KEDA (Kubernetes Event-driven Autoscaling) settings.
  name: keda
  type: object
- description: VPA (Vertical Pod Autoscaler) settings.
  name: verticalPodAutoscaler
  type: object
provider_name: Azure Kubernetes Service
provider_slug: azure-kubernetes-service
schema_file: json-schema/azure-kubernetes-service-managed-cluster-workload-auto-scaler-profile-schema.json
slug: azure-kubernetes-service-managed-cluster-workload-auto-scaler-profile
tags:
- Azure
- Cloud
- Containers
- DevOps
- Kubernetes
- Orchestration
title: ManagedClusterWorkloadAutoScalerProfile
---
