---
consumed_apis:
- bigip-icontrol
description: Unified workflow for managing application delivery infrastructure including virtual servers, server pools, backend nodes, and traffic profiles on F5 BIG-IP. Used by network administrators and DevOps engineers for load balancing configuration and application traffic management.
layout: capability
name: F5 Application Delivery
operations:
- description: List all virtual servers
  method: GET
  name: list-virtual-servers
  path: /v1/virtual-servers
- description: Create a new virtual server
  method: POST
  name: create-virtual-server
  path: /v1/virtual-servers
- description: Get virtual server details
  method: GET
  name: get-virtual-server
  path: /v1/virtual-servers/{virtualName}
- description: Update a virtual server
  method: PUT
  name: update-virtual-server
  path: /v1/virtual-servers/{virtualName}
- description: Delete a virtual server
  method: DELETE
  name: delete-virtual-server
  path: /v1/virtual-servers/{virtualName}
- description: List all pools
  method: GET
  name: list-pools
  path: /v1/pools
- description: Create a new pool
  method: POST
  name: create-pool
  path: /v1/pools
- description: Get pool details
  method: GET
  name: get-pool
  path: /v1/pools/{poolName}
- description: Update a pool
  method: PUT
  name: update-pool
  path: /v1/pools/{poolName}
- description: Delete a pool
  method: DELETE
  name: delete-pool
  path: /v1/pools/{poolName}
- description: List pool members
  method: GET
  name: list-pool-members
  path: /v1/pools/{poolName}/members
- description: Add a pool member
  method: POST
  name: add-pool-member
  path: /v1/pools/{poolName}/members
- description: List all nodes
  method: GET
  name: list-nodes
  path: /v1/nodes
- description: Create a node
  method: POST
  name: create-node
  path: /v1/nodes
- description: Get node details
  method: GET
  name: get-node
  path: /v1/nodes/{nodeName}
- description: Update a node
  method: PUT
  name: update-node
  path: /v1/nodes/{nodeName}
- description: Delete a node
  method: DELETE
  name: delete-node
  path: /v1/nodes/{nodeName}
- description: List HTTP profiles
  method: GET
  name: list-http-profiles
  path: /v1/profiles
personas: []
provider_name: F5 Networks
provider_slug: f5-networks
search_terms:
- get pool details
- list all virtual servers
- load balancing
- get pool
- create pool
- delete a virtual server
- update pool
- network management
- update a node
- view traffic profiles
- get details of a specific virtual server
- get pool member
- update a pool member
- api gateway
- nginx
- waf
- update pool member
- list pools
- application delivery
- manage a specific pool
- create a new virtual server
- update virtual server
- manage a specific virtual server
- list all nodes
- list http profiles
- list pool members
- list members of a pool
- get virtual server details
- get details of a specific node
- update a virtual server
- list all virtual servers on the big-ip
- delete virtual server
- list http traffic profiles
- add pool member
- security
- list all server pools
- delete node
- list virtual servers
- list nodes
- get details of a pool member
- create a new pool
- update node
- manage a specific node
- add a member to a pool
- create a new backend node
- create node
- manage virtual servers that direct client traffic
- update a pool
- delete a pool
- kubernetes
- multi-cloud
- get details of a specific pool
- get node
- create virtual server
- list client ssl profiles
- list all pools
- delete pool
- f5
- automation
- manage backend nodes
- add a pool member
- list tcp profiles
- get node details
- delete pool member
- list tcp traffic profiles
- edge computing
- get virtual server
- manage server pools
- delete a node
- create a node
- remove a pool member
- list all backend nodes
- manage pool members
slug: application-delivery
tags:
- F5
- Application Delivery
- Load Balancing
- Network Management
tools:
- description: List all virtual servers on the BIG-IP
  hints:
    openWorld: true
    readOnly: true
  name: list-virtual-servers
- description: Get details of a specific virtual server
  hints:
    readOnly: true
  name: get-virtual-server
- description: Create a new virtual server
  hints:
    readOnly: false
  name: create-virtual-server
- description: Update a virtual server
  hints:
    idempotent: true
    readOnly: false
  name: update-virtual-server
- description: Delete a virtual server
  hints:
    destructive: true
    idempotent: true
  name: delete-virtual-server
- description: List all server pools
  hints:
    openWorld: true
    readOnly: true
  name: list-pools
- description: Get details of a specific pool
  hints:
    readOnly: true
  name: get-pool
- description: Create a new pool
  hints:
    readOnly: false
  name: create-pool
- description: Update a pool
  hints:
    idempotent: true
    readOnly: false
  name: update-pool
- description: Delete a pool
  hints:
    destructive: true
    idempotent: true
  name: delete-pool
- description: List members of a pool
  hints:
    readOnly: true
  name: list-pool-members
- description: Add a member to a pool
  hints:
    readOnly: false
  name: add-pool-member
- description: Get details of a pool member
  hints:
    readOnly: true
  name: get-pool-member
- description: Update a pool member
  hints:
    idempotent: true
    readOnly: false
  name: update-pool-member
- description: Remove a pool member
  hints:
    destructive: true
    idempotent: true
  name: delete-pool-member
- description: List all backend nodes
  hints:
    openWorld: true
    readOnly: true
  name: list-nodes
- description: Get details of a specific node
  hints:
    readOnly: true
  name: get-node
- description: Create a new backend node
  hints:
    readOnly: false
  name: create-node
- description: Update a node
  hints:
    idempotent: true
    readOnly: false
  name: update-node
- description: Delete a node
  hints:
    destructive: true
    idempotent: true
  name: delete-node
- description: List HTTP traffic profiles
  hints:
    readOnly: true
  name: list-http-profiles
- description: List TCP traffic profiles
  hints:
    readOnly: true
  name: list-tcp-profiles
- description: List client SSL profiles
  hints:
    readOnly: true
  name: list-client-ssl-profiles
---
