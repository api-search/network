---
consumed_apis:
- cloudflare-workers
- cloudflare-pages
- cloudflare-durable-objects
- cloudflare-queues
description: Deploy and manage serverless applications on Cloudflare's edge network combining Workers scripts, Pages deployments, Durable Objects for state, and Queues for async messaging. Used by developers and platform engineers building edge-first applications.
layout: capability
name: Cloudflare Serverless Compute
operations:
- description: List all Workers.
  method: GET
  name: list-workers
  path: /v1/workers
- description: List Worker scripts.
  method: GET
  name: list-worker-scripts
  path: /v1/scripts
- description: List Worker deployments.
  method: GET
  name: list-deployments
  path: /v1/deployments
- description: List Pages projects.
  method: GET
  name: list-pages-projects
  path: /v1/pages-projects
- description: List Pages deployments.
  method: GET
  name: list-pages-deployments
  path: /v1/pages-deployments
- description: List Durable Object namespaces.
  method: GET
  name: list-durable-object-namespaces
  path: /v1/durable-object-namespaces
- description: List queues.
  method: GET
  name: list-queues
  path: /v1/queues
personas: []
provider_name: Cloudflare
provider_slug: cloudflare
search_terms:
- list pages deployments.
- cloudflare
- list pages projects
- rollback a pages deployment.
- web performance
- queues list queues
- worker script management.
- workers list secrets
- send a message to a queue.
- list durable objects in a namespace.
- pages get project
- platform
- create a pages project.
- api gateway
- pages list deployments
- queues pull messages
- durable object namespace management.
- pages create project
- list message queues.
- list all workers for an account.
- delete a queue.
- cloud
- serverless
- workers list scripts
- workers upload script
- list pages projects.
- pages rollback deployment
- durable objects list objects
- ddos protection
- pages project management.
- list durable object namespaces
- list queues.
- workers list deployments
- workers list workers
- edge computing
- workers delete script
- workers create deployment
- list worker routes.
- pull messages from a queue.
- ai gateway
- object storage
- pages list projects
- durable objects list namespaces
- queues send message
- list pages deployments
- list deployments
- create a message queue.
- security
- dns
- edge
- cdn
- create a worker deployment.
- queue management.
- list worker scripts
- list queues
- deployment
- queues delete queue
- list all workers.
- get pages project details.
- worker deployment management.
- workers list routes
- containers
- pages deployment management.
- list durable object namespaces.
- queues create queue
- upload a worker script.
- real-time communication
- artificial intelligence
- list worker scripts.
- list worker secrets.
- delete a worker script.
- list workers
- list worker deployments.
slug: serverless-compute
tags:
- Cloudflare
- Serverless
- Edge Computing
- Deployment
tools:
- description: List all Workers for an account.
  hints:
    openWorld: true
    readOnly: true
  name: workers-list-workers
- description: List Worker scripts.
  hints:
    readOnly: true
  name: workers-list-scripts
- description: Upload a Worker script.
  hints:
    idempotent: true
    readOnly: false
  name: workers-upload-script
- description: Delete a Worker script.
  hints:
    destructive: true
    idempotent: true
  name: workers-delete-script
- description: List Worker deployments.
  hints:
    readOnly: true
  name: workers-list-deployments
- description: Create a Worker deployment.
  hints:
    readOnly: false
  name: workers-create-deployment
- description: List Worker routes.
  hints:
    readOnly: true
  name: workers-list-routes
- description: List Worker secrets.
  hints:
    readOnly: true
  name: workers-list-secrets
- description: List Pages projects.
  hints:
    openWorld: true
    readOnly: true
  name: pages-list-projects
- description: Create a Pages project.
  hints:
    readOnly: false
  name: pages-create-project
- description: Get Pages project details.
  hints:
    readOnly: true
  name: pages-get-project
- description: List Pages deployments.
  hints:
    readOnly: true
  name: pages-list-deployments
- description: Rollback a Pages deployment.
  hints:
    readOnly: false
  name: pages-rollback-deployment
- description: List Durable Object namespaces.
  hints:
    openWorld: true
    readOnly: true
  name: durable-objects-list-namespaces
- description: List Durable Objects in a namespace.
  hints:
    readOnly: true
  name: durable-objects-list-objects
- description: List message queues.
  hints:
    openWorld: true
    readOnly: true
  name: queues-list-queues
- description: Create a message queue.
  hints:
    readOnly: false
  name: queues-create-queue
- description: Send a message to a queue.
  hints:
    readOnly: false
  name: queues-send-message
- description: Pull messages from a queue.
  hints:
    readOnly: true
  name: queues-pull-messages
- description: Delete a queue.
  hints:
    destructive: true
    idempotent: true
  name: queues-delete-queue
---
