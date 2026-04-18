---
consumed_apis:
- hf-endpoints
- hf-tgi
description: Unified workflow for deploying, scaling, and operating ML model inference endpoints on dedicated infrastructure. Combines Inference Endpoints management with TGI server monitoring. Used by ML platform engineers and DevOps teams.
layout: capability
name: Hugging Face Deployment and Operations
operations:
- description: List all endpoints
  method: GET
  name: list-endpoints
  path: /v1/endpoints/{namespace}
- description: Create a new endpoint
  method: POST
  name: create-endpoint
  path: /v1/endpoints/{namespace}
- description: Get endpoint details
  method: GET
  name: get-endpoint
  path: /v1/endpoints/{namespace}/{endpoint_name}
- description: Update endpoint configuration
  method: PUT
  name: update-endpoint
  path: /v1/endpoints/{namespace}/{endpoint_name}
- description: Delete an endpoint
  method: DELETE
  name: delete-endpoint
  path: /v1/endpoints/{namespace}/{endpoint_name}
- description: Pause a running endpoint
  method: POST
  name: pause-endpoint
  path: /v1/endpoints/{namespace}/{endpoint_name}/pause
- description: Resume a paused endpoint
  method: POST
  name: resume-endpoint
  path: /v1/endpoints/{namespace}/{endpoint_name}/resume
- description: Get endpoint logs
  method: GET
  name: get-logs
  path: /v1/endpoints/{namespace}/{endpoint_name}/logs
- description: Get endpoint metrics
  method: GET
  name: get-metrics
  path: /v1/endpoints/{namespace}/{endpoint_name}/metrics
- description: Check TGI server health
  method: GET
  name: health-check
  path: /v1/server/health
- description: Get TGI server info
  method: GET
  name: get-info
  path: /v1/server/info
- description: List available cloud providers
  method: GET
  name: list-providers
  path: /v1/providers
personas: []
provider_name: Hugging Face
provider_slug: hugging-face
search_terms:
- get tgi server info
- tgi server info
- list available cloud providers
- get endpoint
- get metrics for an endpoint.
- tgi metrics
- create a new endpoint
- get endpoint details
- pause a running endpoint to stop billing.
- create endpoint
- pause an endpoint
- scale an endpoint to zero replicas.
- pause endpoint
- tgi server health
- resume an endpoint
- health check
- get info
- update endpoint
- list all dedicated inference endpoints for a namespace.
- check if the tgi server is healthy and responding.
- tgi health check
- delete a dedicated inference endpoint.
- get prometheus metrics from the tgi server.
- cloud providers
- hugging face
- mlops
- infrastructure
- check tgi server health
- update endpoint configuration
- delete endpoint
- list providers
- list available cloud providers and hardware options.
- create a new dedicated inference endpoint.
- resume endpoint
- scale to zero
- resume a paused endpoint
- get endpoint metrics
- get metrics
- manage inference endpoints
- deployment
- pause a running endpoint
- get logs
- get information about the deployed model and tgi server.
- get endpoint logs
- get details of a specific endpoint.
- get logs for an endpoint.
- update an existing endpoint configuration.
- resume a paused endpoint.
- operations
- list all endpoints
- delete an endpoint
- individual endpoint operations
- list endpoints
slug: deployment-and-operations
tags:
- Hugging Face
- Deployment
- Operations
- Infrastructure
- MLOps
tools:
- description: List all dedicated inference endpoints for a namespace.
  hints:
    openWorld: true
    readOnly: true
  name: list-endpoints
- description: Create a new dedicated inference endpoint.
  hints:
    readOnly: false
  name: create-endpoint
- description: Get details of a specific endpoint.
  hints:
    openWorld: true
    readOnly: true
  name: get-endpoint
- description: Update an existing endpoint configuration.
  hints:
    idempotent: true
    readOnly: false
  name: update-endpoint
- description: Delete a dedicated inference endpoint.
  hints:
    destructive: true
    readOnly: false
  name: delete-endpoint
- description: Pause a running endpoint to stop billing.
  hints:
    readOnly: false
  name: pause-endpoint
- description: Resume a paused endpoint.
  hints:
    readOnly: false
  name: resume-endpoint
- description: Scale an endpoint to zero replicas.
  hints:
    readOnly: false
  name: scale-to-zero
- description: Get logs for an endpoint.
  hints:
    readOnly: true
  name: get-endpoint-logs
- description: Get metrics for an endpoint.
  hints:
    readOnly: true
  name: get-endpoint-metrics
- description: List available cloud providers and hardware options.
  hints:
    readOnly: true
  name: list-providers
- description: Check if the TGI server is healthy and responding.
  hints:
    readOnly: true
  name: tgi-health-check
- description: Get information about the deployed model and TGI server.
  hints:
    readOnly: true
  name: tgi-server-info
- description: Get Prometheus metrics from the TGI server.
  hints:
    readOnly: true
  name: tgi-metrics
---
