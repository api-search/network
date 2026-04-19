---
consumed_apis:
- allianz-platform-services
description: Workflow capability for platform engineering and DevOps teams operating the Allianz Future Cloud Platform, combining service management, deployment automation, observability, and infrastructure provisioning.
layout: capability
name: Allianz Cloud Platform Operations
operations:
- description: List all platform services
  method: GET
  name: list-services
  path: /v1/services
- description: Register a new microservice
  method: POST
  name: register-service
  path: /v1/services
- description: List deployment history
  method: GET
  name: list-deployments
  path: /v1/services/{service_id}/deployments
- description: Trigger a deployment
  method: POST
  name: deploy-service
  path: /v1/services/{service_id}/deployments
- description: Get platform metrics
  method: GET
  name: get-metrics
  path: /v1/observability/metrics
- description: Provision infrastructure resource
  method: POST
  name: provision-resource
  path: /v1/infrastructure/resources
personas: []
provider_name: Allianz Future Cloud Platform
provider_slug: allianz-future-cloud-platform
search_terms:
- devops
- deploy service
- provision resource
- get details and status of a specific platform service
- list services
- platform engineering
- list platform services
- list all microservices registered on the allianz future cloud platform
- provision redis, rds, msk, or s3 resources for insurance microservices
- list service deployments
- financial services
- get platform metrics
- get metrics
- platform observability metrics
- register a new microservice
- register a new insurance microservice on the kubernetes platform
- engineer deploying and operating insurance microservices on the platform
- insurance
- microservice lifecycle management
- list deployment history for a platform service including version and status
- get service metrics
- infrastructure provisioning
- get platform service
- developer building insurance microservices on the allianz future cloud platform
- metrics, monitoring, and alerting for platform health
- provision infrastructure resource
- kubernetes
- cloud platform
- deployment management for services
- deploy platform service
- list platform namespaces
- trigger a deployment
- DevOps Engineer
- get cpu, memory, request rate, error rate, and latency metrics for a service
- cloud resource provisioning for microservice dependencies
- list kubernetes namespaces and their team ownership on the platform
- Platform Engineer
- list deployments
- gitops-based deployment pipelines for microservice updates
- observability
- list deployment history
- enterprise
- list all platform services
- register service
- register platform service
- trigger a rolling, blue-green, or canary deployment for a microservice
- engineer responsible for maintaining and evolving the allianz future cloud platform
- registration and lifecycle management of insurance microservices
- Insurance Product Developer
- end-to-end platform operations for devops teams
slug: cloud-platform-operations
tags:
- Cloud Platform
- DevOps
- Platform Engineering
- Kubernetes
- Observability
tools:
- description: List all microservices registered on the Allianz Future Cloud Platform
  hints:
    openWorld: false
    readOnly: true
  name: list-platform-services
- description: Register a new insurance microservice on the Kubernetes platform
  hints:
    openWorld: false
    readOnly: false
  name: register-platform-service
- description: Get details and status of a specific platform service
  hints:
    openWorld: false
    readOnly: true
  name: get-platform-service
- description: List deployment history for a platform service including version and status
  hints:
    openWorld: false
    readOnly: true
  name: list-service-deployments
- description: Trigger a rolling, blue-green, or canary deployment for a microservice
  hints:
    destructive: false
    idempotent: false
    readOnly: false
  name: deploy-platform-service
- description: List Kubernetes namespaces and their team ownership on the platform
  hints:
    openWorld: false
    readOnly: true
  name: list-platform-namespaces
- description: Get CPU, memory, request rate, error rate, and latency metrics for a service
  hints:
    openWorld: false
    readOnly: true
  name: get-service-metrics
- description: Provision Redis, RDS, MSK, or S3 resources for insurance microservices
  hints:
    destructive: false
    idempotent: false
    readOnly: false
  name: provision-infrastructure-resource
---
