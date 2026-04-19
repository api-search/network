---
consumed_apis:
- fargate
description: Workflow capability for deploying and managing serverless container workloads on Amazon Fargate. Combines cluster management, task definitions, task execution, and service deployment for platform engineers and DevOps teams.
layout: capability
name: Amazon Fargate Container Orchestration
operations:
- description: List all ECS clusters
  method: GET
  name: list-clusters
  path: /v1/clusters
- description: Create a new cluster
  method: POST
  name: create-cluster
  path: /v1/clusters
- description: Get cluster details
  method: GET
  name: describe-clusters
  path: /v1/clusters/{cluster}
- description: Delete a cluster
  method: DELETE
  name: delete-cluster
  path: /v1/clusters/{cluster}
- description: List task definitions
  method: GET
  name: list-task-definitions
  path: /v1/task-definitions
- description: Register a task definition
  method: POST
  name: register-task-definition
  path: /v1/task-definitions
- description: List tasks
  method: GET
  name: list-tasks
  path: /v1/tasks
- description: Run a task
  method: POST
  name: run-task
  path: /v1/tasks
- description: List services
  method: GET
  name: list-services
  path: /v1/services
- description: Create a service
  method: POST
  name: create-service
  path: /v1/services
personas: []
provider_name: Amazon Fargate
provider_slug: amazon-fargate
search_terms:
- devops
- manage task execution
- create a service
- list all ecs clusters
- list services
- launch a fargate task with specified cpu, memory, and networking
- deploying and scaling microservices architectures
- run task
- containers
- list all ecs clusters for fargate workloads
- amazon fargate
- describe services
- describe clusters
- list all registered task definitions
- list tasks
- list clusters
- register task definition
- scale or update a fargate service task count or definition
- register a task definition
- remove a fargate service from a cluster
- register a task definition specifying container images, cpu, memory, and networking
- eks
- stop a running fargate task
- get status and details of running tasks
- manage task definitions
- update service
- list task definitions
- delete a fargate cluster
- deploy a persistent fargate service with load balancing and auto-scaling
- running workloads without managing infrastructure
- delete a cluster
- list tasks in a cluster with status filtering
- get detailed cluster information
- run a task
- create a new ecs cluster
- describe task definition
- create service
- deregister a task definition revision
- delete service
- DevOps Engineer
- delete cluster
- engineers building container platforms and infrastructure
- stop task
- serverless
- get cluster details
- aws
- microservices
- manage specific cluster
- create a new cluster
- manage ecs clusters
- Cloud Architect
- engineers deploying and operating containerized applications
- get deployment status and health of fargate services
- managing container lifecycle from definition to deployment
- Platform Engineer
- create cluster
- architects designing serverless container solutions
- compute
- get details of a task definition
- list all services running in a fargate cluster
- deregister task definition
- describe tasks
- ecs
- manage services
- full lifecycle management of serverless container workloads
slug: amazon-fargate-container-orchestration
tags:
- Amazon Fargate
- Containers
- Serverless
- ECS
- DevOps
tools:
- description: List all ECS clusters for Fargate workloads
  hints:
    openWorld: true
    readOnly: true
  name: list-clusters
- description: Create a new ECS cluster
  hints:
    readOnly: false
  name: create-cluster
- description: Get detailed cluster information
  hints:
    readOnly: true
  name: describe-clusters
- description: Delete a Fargate cluster
  hints:
    destructive: true
    readOnly: false
  name: delete-cluster
- description: Register a task definition specifying container images, CPU, memory, and networking
  hints:
    readOnly: false
  name: register-task-definition
- description: Get details of a task definition
  hints:
    readOnly: true
  name: describe-task-definition
- description: List all registered task definitions
  hints:
    readOnly: true
  name: list-task-definitions
- description: Deregister a task definition revision
  hints:
    destructive: true
    readOnly: false
  name: deregister-task-definition
- description: Launch a Fargate task with specified CPU, memory, and networking
  hints:
    readOnly: false
  name: run-task
- description: Stop a running Fargate task
  hints:
    destructive: true
    readOnly: false
  name: stop-task
- description: Get status and details of running tasks
  hints:
    readOnly: true
  name: describe-tasks
- description: List tasks in a cluster with status filtering
  hints:
    readOnly: true
  name: list-tasks
- description: Deploy a persistent Fargate service with load balancing and auto-scaling
  hints:
    readOnly: false
  name: create-service
- description: Get deployment status and health of Fargate services
  hints:
    readOnly: true
  name: describe-services
- description: List all services running in a Fargate cluster
  hints:
    readOnly: true
  name: list-services
- description: Scale or update a Fargate service task count or definition
  hints:
    readOnly: false
  name: update-service
- description: Remove a Fargate service from a cluster
  hints:
    destructive: true
    readOnly: false
  name: delete-service
---
