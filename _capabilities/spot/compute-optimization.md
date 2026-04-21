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
- autoscaling
- ocean kubernetes clusters
- get elastigroup activity logs
- ocean list clusters gke
- list aks ocean clusters
- list gcp elastigroups
- compute
- list elastigroups
- kubernetes
- elastigroup get group aws
- list ocean clusters
- elastigroup get status aws
- elastigroup compute groups
- list gke ocean clusters
- elastigroup get logs
- get an aws elastigroup by id
- finops
- ocean get cluster aws
- elastigroup list gcp
- list ocean spark clusters
- ocean list clusters aws
- elastigroup list azure
- elastigroup scale down aws
- get an aws ocean cluster
- get elastigroup instance status
- cloud infrastructure
- scale down an aws elastigroup
- ocean virtual node groups
- spot
- list all aws elastigroups
- list ocean virtual node groups
- containers
- elastigroup list groups aws
- list virtual node groups
- ocean get right sizing
- spot instances
- get elastigroup cost data
- scale up an aws elastigroup
- cost optimization
- get right-sizing suggestions for an ocean cluster
- ocean list clusters aks
- elastigroup scale up aws
- ocean list virtual node groups
- list aws ocean clusters
- elastigroup get costs
- list azure elastigroups
- list aws elastigroups
- ocean list spark clusters
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
