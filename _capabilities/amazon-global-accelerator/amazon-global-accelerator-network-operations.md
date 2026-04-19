---
consumed_apis:
- amazon-global-accelerator
description: Workflow capability for network engineers and DevOps teams managing Amazon Global Accelerator infrastructure. Covers accelerator lifecycle, listener configuration, endpoint group management, and traffic routing optimization.
layout: capability
name: Amazon Global Accelerator Network Operations
operations:
- description: List all accelerators
  method: GET
  name: list-accelerators
  path: /v1/accelerators
- description: Create a new accelerator with static IPs
  method: POST
  name: create-accelerator
  path: /v1/accelerators
- description: Get accelerator details and status
  method: GET
  name: describe-accelerator
  path: /v1/accelerators/{acceleratorArn}
- description: Create a new listener
  method: POST
  name: create-listener
  path: /v1/listeners
- description: List all listeners
  method: GET
  name: list-listeners
  path: /v1/listeners
- description: Create an endpoint group
  method: POST
  name: create-endpoint-group
  path: /v1/endpoint-groups
- description: List endpoint groups
  method: GET
  name: list-endpoint-groups
  path: /v1/endpoint-groups
personas: []
provider_name: Amazon Global Accelerator
provider_slug: amazon-global-accelerator
search_terms:
- load balancing
- performance
- manage endpoint groups for traffic routing
- create a new global accelerator with static anycast ip addresses
- availability
- amazon global accelerator
- manages application infrastructure and availability
- update endpoint group traffic settings and weights
- update listener configuration including ports and protocol
- describe accelerator
- delete accelerator
- create a listener for an accelerator specifying ports and protocol
- list all listeners
- manage listeners for accelerators
- get detailed status and configuration of a specific accelerator
- update accelerator configuration and settings
- get accelerator details and status
- list all global accelerator accelerators and their static ip addresses
- list listeners
- configures and optimizes global network traffic routing
- manage a specific accelerator
- DevOps Engineer
- global
- list all accelerators
- update accelerator
- aws
- update endpoint group
- list endpoint groups
- traffic routing
- update listener
- delete an accelerator
- create an endpoint group to route traffic to specific aws resources
- list all listeners configured for an accelerator
- create an endpoint group
- list accelerators
- list all endpoint groups for a listener
- create listener
- create accelerator
- create a new accelerator with static ips
- networking
- cdn
- Network Engineer
- create endpoint group
- create a new listener
- manage global accelerator accelerators
slug: amazon-global-accelerator-network-operations
tags:
- Amazon Global Accelerator
- Networking
- Performance
- Traffic Routing
- AWS
tools:
- description: List all Global Accelerator accelerators and their static IP addresses
  hints:
    openWorld: true
    readOnly: true
  name: list-accelerators
- description: Create a new Global Accelerator with static Anycast IP addresses
  hints:
    readOnly: false
  name: create-accelerator
- description: Get detailed status and configuration of a specific accelerator
  hints:
    readOnly: true
  name: describe-accelerator
- description: Update accelerator configuration and settings
  hints:
    idempotent: true
    readOnly: false
  name: update-accelerator
- description: Delete an accelerator
  hints:
    destructive: true
    readOnly: false
  name: delete-accelerator
- description: Create a listener for an accelerator specifying ports and protocol
  hints:
    readOnly: false
  name: create-listener
- description: List all listeners configured for an accelerator
  hints:
    readOnly: true
  name: list-listeners
- description: Update listener configuration including ports and protocol
  hints:
    idempotent: true
    readOnly: false
  name: update-listener
- description: Create an endpoint group to route traffic to specific AWS resources
  hints:
    readOnly: false
  name: create-endpoint-group
- description: List all endpoint groups for a listener
  hints:
    readOnly: true
  name: list-endpoint-groups
- description: Update endpoint group traffic settings and weights
  hints:
    idempotent: true
    readOnly: false
  name: update-endpoint-group
---
