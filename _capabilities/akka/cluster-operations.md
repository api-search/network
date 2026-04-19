---
consumed_apis:
- akka-management
description: Workflow for monitoring and managing Akka cluster operations including health checks, member management, and cluster bootstrap. For platform engineers and SREs operating distributed Akka systems.
layout: capability
name: Akka Cluster Operations
operations:
- description: Node liveness check
  method: GET
  name: check-alive
  path: /v1/health
- description: Node readiness check
  method: GET
  name: check-ready
  path: /v1/health
- description: List cluster members
  method: GET
  name: list-members
  path: /v1/cluster/members
- description: Join a cluster member
  method: POST
  name: join-member
  path: /v1/cluster/members
personas: []
provider_name: Akka
provider_slug: akka
search_terms:
- manages akka cluster deployments and configurations
- node readiness check
- check liveness and readiness of akka cluster nodes
- join member
- SRE
- check alive
- monitor and manage akka cluster health and membership
- akka cluster membership and node lifecycle management
- add a new node to the akka cluster
- join a cluster member
- scala
- monitors cluster health and responds to incidents
- operations
- akka
- cluster management
- node liveness check
- cluster member management
- check cluster readiness
- list all current members of the akka cluster
- check if akka cluster nodes are ready to serve traffic
- list cluster members
- check ready
- distributed systems
- liveness and readiness health check monitoring
- microservices
- frameworks
- reactive
- actor model
- Platform Engineer
- check cluster health
- health monitoring
- java
- cluster health checks
- list members
- join cluster member
slug: cluster-operations
tags:
- Akka
- Cluster Management
- Distributed Systems
- Operations
- Health Monitoring
tools:
- description: Check liveness and readiness of Akka cluster nodes
  hints:
    openWorld: false
    readOnly: true
  name: check-cluster-health
- description: Check if Akka cluster nodes are ready to serve traffic
  hints:
    openWorld: false
    readOnly: true
  name: check-cluster-readiness
- description: List all current members of the Akka cluster
  hints:
    openWorld: false
    readOnly: true
  name: list-cluster-members
- description: Add a new node to the Akka cluster
  hints:
    destructive: false
    readOnly: false
  name: join-cluster-member
---
