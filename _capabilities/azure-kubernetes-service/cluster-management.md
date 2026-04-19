---
consumed_apis:
- aks-rest
description: Workflow for managing AKS clusters and agent pools including lifecycle operations, upgrades, scaling, and credentials. Used by DevOps engineers and platform administrators.
layout: capability
name: Azure Kubernetes Service Cluster Management
operations:
- description: List all managed clusters
  method: GET
  name: list-clusters
  path: /v1/clusters
- description: Get cluster details
  method: GET
  name: get-cluster
  path: /v1/clusters/{resourceName}
- description: Create or update a cluster
  method: PUT
  name: create-or-update-cluster
  path: /v1/clusters/{resourceName}
- description: Delete a cluster
  method: DELETE
  name: delete-cluster
  path: /v1/clusters/{resourceName}
- description: List agent pools in a cluster
  method: GET
  name: list-agent-pools
  path: /v1/clusters/{resourceName}/agent-pools
personas: []
provider_name: Azure Kubernetes Service
provider_slug: azure-kubernetes-service
search_terms:
- devops
- azure
- get details of an aks cluster
- list agent pools in a cluster
- get agent pool details
- containers
- get upgrade profile
- create or update agent pool
- list clusters
- get cluster
- stop a running aks cluster
- cluster management
- delete a cluster
- stop cluster
- single cluster operations
- get the upgrade profile for a cluster
- create or update a cluster
- orchestration
- kubernetes
- delete cluster
- get cluster details
- start cluster
- list all aks managed clusters in a subscription
- create or update an aks managed cluster
- delete an agent pool from a cluster
- cloud
- start a stopped aks cluster
- delete an aks managed cluster
- list agent pools
- list all managed clusters
- get agent pool
- create or update an agent pool
- cluster lifecycle operations
- agent pool operations
- create or update cluster
- delete agent pool
slug: cluster-management
tags:
- Azure
- Kubernetes
- Cluster Management
- DevOps
tools:
- description: List all AKS managed clusters in a subscription
  hints:
    idempotent: true
    readOnly: true
  name: list-clusters
- description: Get details of an AKS cluster
  hints:
    idempotent: true
    readOnly: true
  name: get-cluster
- description: Create or update an AKS managed cluster
  hints:
    idempotent: true
    readOnly: false
  name: create-or-update-cluster
- description: Delete an AKS managed cluster
  hints:
    destructive: true
    idempotent: true
    readOnly: false
  name: delete-cluster
- description: Get the upgrade profile for a cluster
  hints:
    idempotent: true
    readOnly: true
  name: get-upgrade-profile
- description: Stop a running AKS cluster
  hints:
    idempotent: true
    readOnly: false
  name: stop-cluster
- description: Start a stopped AKS cluster
  hints:
    idempotent: true
    readOnly: false
  name: start-cluster
- description: List agent pools in a cluster
  hints:
    idempotent: true
    readOnly: true
  name: list-agent-pools
- description: Get agent pool details
  hints:
    idempotent: true
    readOnly: true
  name: get-agent-pool
- description: Create or update an agent pool
  hints:
    idempotent: true
    readOnly: false
  name: create-or-update-agent-pool
- description: Delete an agent pool from a cluster
  hints:
    destructive: true
    idempotent: true
    readOnly: false
  name: delete-agent-pool
---
