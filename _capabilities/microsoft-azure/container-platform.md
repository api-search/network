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
- aks get agent pool
- get aks cluster details
- get cluster admin credentials
- aks get admin credentials
- enterprise
- kubernetes
- aks get cluster
- list manifests for a repository
- cloud
- aks list agent pools
- list clusters
- get agent pool details
- list tags for a repository
- t1
- azure
- list repositories
- acr get repository
- aks list clusters
- acr list manifests
- list container repositories
- infrastructure as a service
- container registry
- list cluster agent pools
- container repositories
- containers
- list aks clusters
- acr list repositories
- acr list tags
- cloud computing
- platform as a service
- get repository attributes
- api management
- aks cluster management
- list aks managed clusters
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
