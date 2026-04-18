---
consumed_apis:
- azure-aks
- azure-acr
description: Unified workflow for Azure container infrastructure combining AKS cluster management and Container Registry operations. Used by platform engineers, DevOps teams, and SREs managing containerized workloads.
layout: capability
name: Azure Container Platform
operations:
- description: List AKS clusters
  method: GET
  name: list-clusters
  path: /v1/clusters
- description: List container repositories
  method: GET
  name: list-repositories
  path: /v1/repositories
personas: []
provider_name: Microsoft Azure
provider_slug: microsoft-azure
search_terms:
- cloud
- acr list repositories
- t1
- get cluster admin credentials
- list cluster agent pools
- list tags for a repository
- list manifests for a repository
- platform as a service
- acr get repository
- containers
- list aks clusters
- aks get cluster
- acr list manifests
- get repository attributes
- list aks managed clusters
- aks cluster management
- container repositories
- list container repositories
- get agent pool details
- aks get agent pool
- list clusters
- enterprise
- container registry
- get aks cluster details
- kubernetes
- aks list clusters
- aks get admin credentials
- cloud computing
- list repositories
- acr list tags
- aks list agent pools
- api management
- infrastructure as a service
- azure
slug: container-platform
tags:
- Azure
- Kubernetes
- Containers
- Container Registry
tools:
- description: List AKS managed clusters
  hints:
    openWorld: true
    readOnly: true
  name: aks-list-clusters
- description: Get AKS cluster details
  hints:
    readOnly: true
  name: aks-get-cluster
- description: List cluster agent pools
  hints:
    readOnly: true
  name: aks-list-agent-pools
- description: Get agent pool details
  hints:
    readOnly: true
  name: aks-get-agent-pool
- description: Get cluster admin credentials
  hints:
    readOnly: true
  name: aks-get-admin-credentials
- description: List container repositories
  hints:
    openWorld: true
    readOnly: true
  name: acr-list-repositories
- description: Get repository attributes
  hints:
    readOnly: true
  name: acr-get-repository
- description: List tags for a repository
  hints:
    readOnly: true
  name: acr-list-tags
- description: List manifests for a repository
  hints:
    readOnly: true
  name: acr-list-manifests
---
