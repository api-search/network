---
consumed_apis:
- akamai-edgeworkers
- akamai-network-lists
description: Unified workflow for managing Akamai edge platform resources including EdgeWorkers serverless functions, network lists, and property configurations. For platform engineers and DevOps teams managing Akamai delivery configurations.
layout: capability
name: Akamai Edge Platform Management
operations:
- description: List EdgeWorker identifiers
  method: GET
  name: list-edgeworkers
  path: /v1/edgeworkers
- description: Create EdgeWorker
  method: POST
  name: create-edgeworker
  path: /v1/edgeworkers
- description: List network lists
  method: GET
  name: list-network-lists
  path: /v1/network-lists
personas: []
provider_name: Akamai
provider_slug: akamai
search_terms:
- create edgeworker
- create a new akamai edgeworker serverless function
- network lists and access control for ip and geographic filtering
- network security
- platform
- networks
- security
- DevOps Engineer
- edgeworkers serverless execution and edgekv storage at the edge
- content delivery property management and configuration
- list edgeworker identifiers
- network list management
- list all akamai network lists for ip and geographic access control
- akamai
- cloud
- Platform Engineer
- edge computing
- edgeworker serverless function management
- manages akamai property configurations and edge deployments
- automates akamai configuration deployment via ci/cd pipelines
- list all akamai edgeworker serverless functions
- list network lists
- platform management
- cdn
- manage akamai edge platform including edgeworkers and network lists
- list edgeworkers
slug: edge-platform-management
tags:
- Akamai
- CDN
- Edge Computing
- Platform Management
- Network Security
tools:
- description: List all Akamai EdgeWorker serverless functions
  hints:
    openWorld: true
    readOnly: true
  name: list-edgeworkers
- description: Create a new Akamai EdgeWorker serverless function
  hints:
    destructive: false
    readOnly: false
  name: create-edgeworker
- description: List all Akamai network lists for IP and geographic access control
  hints:
    openWorld: true
    readOnly: true
  name: list-network-lists
---
