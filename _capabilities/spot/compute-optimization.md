---
consumed_apis:
- spot-elastigroup
- spot-ocean
description: Unified workflow for managing cloud compute optimization across Elastigroup and Ocean, combining instance management, autoscaling, and Kubernetes infrastructure automation. Used by DevOps engineers and cloud infrastructure teams.
layout: capability
name: Spot Compute Optimization
operations:
- description: List AWS Elastigroups
  method: GET
  name: list-elastigroups
  path: /v1/elastigroups
- description: List AWS Ocean clusters
  method: GET
  name: list-ocean-clusters
  path: /v1/ocean-clusters
- description: List virtual node groups
  method: GET
  name: list-virtual-node-groups
  path: /v1/virtual-node-groups
personas: []
provider_name: Spot
provider_slug: spot
search_terms:
- list aws elastigroups
- cloud infrastructure
- finops
- elastigroup get costs
- ocean get right sizing
- elastigroup list azure
- cost optimization
- list all aws elastigroups
- list gcp elastigroups
- elastigroup compute groups
- elastigroup get logs
- ocean get cluster aws
- get elastigroup instance status
- ocean list clusters aks
- elastigroup scale down aws
- ocean list spark clusters
- get elastigroup cost data
- list aws ocean clusters
- list elastigroups
- get elastigroup activity logs
- list ocean virtual node groups
- ocean list clusters aws
- ocean kubernetes clusters
- elastigroup get group aws
- scale down an aws elastigroup
- containers
- spot
- compute
- list aks ocean clusters
- elastigroup list gcp
- get right-sizing suggestions for an ocean cluster
- elastigroup list groups aws
- list azure elastigroups
- ocean list clusters gke
- spot instances
- scale up an aws elastigroup
- get an aws ocean cluster
- list gke ocean clusters
- list ocean spark clusters
- elastigroup scale up aws
- ocean list virtual node groups
- list virtual node groups
- list ocean clusters
- autoscaling
- ocean virtual node groups
- get an aws elastigroup by id
- kubernetes
- elastigroup get status aws
slug: compute-optimization
tags:
- Spot
- Compute
- Autoscaling
- Kubernetes
tools:
- description: List all AWS Elastigroups
  hints:
    openWorld: true
    readOnly: true
  name: elastigroup-list-groups-aws
- description: Get an AWS Elastigroup by ID
  hints:
    readOnly: true
  name: elastigroup-get-group-aws
- description: Get Elastigroup instance status
  hints:
    readOnly: true
  name: elastigroup-get-status-aws
- description: Get Elastigroup cost data
  hints:
    readOnly: true
  name: elastigroup-get-costs
- description: Get Elastigroup activity logs
  hints:
    readOnly: true
  name: elastigroup-get-logs
- description: Scale up an AWS Elastigroup
  hints:
    readOnly: false
  name: elastigroup-scale-up-aws
- description: Scale down an AWS Elastigroup
  hints:
    readOnly: false
  name: elastigroup-scale-down-aws
- description: List Azure Elastigroups
  hints:
    readOnly: true
  name: elastigroup-list-azure
- description: List GCP Elastigroups
  hints:
    readOnly: true
  name: elastigroup-list-gcp
- description: List AWS Ocean clusters
  hints:
    openWorld: true
    readOnly: true
  name: ocean-list-clusters-aws
- description: Get an AWS Ocean cluster
  hints:
    readOnly: true
  name: ocean-get-cluster-aws
- description: Get right-sizing suggestions for an Ocean cluster
  hints:
    readOnly: true
  name: ocean-get-right-sizing
- description: List Ocean virtual node groups
  hints:
    readOnly: true
  name: ocean-list-virtual-node-groups
- description: List AKS Ocean clusters
  hints:
    readOnly: true
  name: ocean-list-clusters-aks
- description: List GKE Ocean clusters
  hints:
    readOnly: true
  name: ocean-list-clusters-gke
- description: List Ocean Spark clusters
  hints:
    readOnly: true
  name: ocean-list-spark-clusters
---
