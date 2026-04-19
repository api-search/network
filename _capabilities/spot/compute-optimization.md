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
- ocean get cluster aws
- autoscaling
- finops
- containers
- elastigroup scale down aws
- cloud infrastructure
- elastigroup get group aws
- ocean list virtual node groups
- list elastigroups
- get an aws elastigroup by id
- list azure elastigroups
- spot
- ocean list clusters aws
- elastigroup list groups aws
- elastigroup get status aws
- elastigroup get logs
- list ocean spark clusters
- scale down an aws elastigroup
- get elastigroup cost data
- elastigroup list azure
- ocean virtual node groups
- elastigroup list gcp
- kubernetes
- cost optimization
- spot instances
- elastigroup get costs
- get elastigroup activity logs
- elastigroup scale up aws
- list gcp elastigroups
- list aks ocean clusters
- ocean list spark clusters
- list aws elastigroups
- elastigroup compute groups
- list all aws elastigroups
- scale up an aws elastigroup
- get an aws ocean cluster
- ocean get right sizing
- list ocean virtual node groups
- get right-sizing suggestions for an ocean cluster
- list gke ocean clusters
- ocean list clusters aks
- ocean list clusters gke
- compute
- list aws ocean clusters
- ocean kubernetes clusters
- get elastigroup instance status
- list ocean clusters
- list virtual node groups
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
