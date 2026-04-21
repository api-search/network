---
consumed_apis:
- rest-api
description: Unified platform management capability for OpenShift clusters including projects, builds, deployments, routes, and monitoring. Used by platform engineers and cluster administrators.
layout: capability
name: OpenShift Platform Management
operations:
- description: List projects
  method: GET
  name: list-projects
  path: /v1/projects
personas: []
provider_name: OpenShift
provider_slug: openshift
search_terms:
- list nodes
- get pod
- enterprise
- list config maps
- list services
- list image streams
- list pods
- platform
- kubernetes
- list cluster nodes
- list openshift projects
- get project details
- list installed operators
- project management
- devops
- get pod details
- list configmaps
- paas
- list deployments
- get project
- list projects
- cloud native
- list builds
- list routes
- list operators
- list storage
- containers
- list persistent volumes
- ci/cd
- openshift
- list images
slug: platform-management
tags:
- OpenShift
- Kubernetes
- Platform
- DevOps
tools:
- description: List OpenShift projects
  hints:
    openWorld: true
    readOnly: true
  name: list-projects
- description: Get project details
  hints:
    readOnly: true
  name: get-project
- description: List builds
  hints:
    readOnly: true
  name: list-builds
- description: List routes
  hints:
    readOnly: true
  name: list-routes
- description: List deployments
  hints:
    readOnly: true
  name: list-deployments
- description: List pods
  hints:
    readOnly: true
  name: list-pods
- description: Get pod details
  hints:
    readOnly: true
  name: get-pod
- description: List services
  hints:
    readOnly: true
  name: list-services
- description: List config maps
  hints:
    readOnly: true
  name: list-configmaps
- description: List cluster nodes
  hints:
    readOnly: true
  name: list-nodes
- description: List installed operators
  hints:
    readOnly: true
  name: list-operators
- description: List image streams
  hints:
    readOnly: true
  name: list-images
- description: List persistent volumes
  hints:
    readOnly: true
  name: list-storage
---
