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
- manage a specific node
- kubernetes
- create node
- list nodes
- create a node
- get pool
- network management
- list http traffic profiles
- list all nodes
- update virtual server
- manage a specific pool
- waf
- load balancing
- get node
- list client ssl profiles
- get node details
- create virtual server
- update a pool
- manage pool members
- list all virtual servers
- view traffic profiles
- list all backend nodes
- update a virtual server
- update pool
- delete a node
- list all server pools
- get pool member
- get pool details
- f5
- create a new backend node
- application delivery
- list pools
- create a new virtual server
- create pool
- add a pool member
- get details of a specific virtual server
- delete node
- get virtual server details
- update a node
- add a member to a pool
- security
- get details of a specific pool
- api gateway
- manage virtual servers that direct client traffic
- list pool members
- update a pool member
- delete virtual server
- update node
- get details of a pool member
- list all virtual servers on the big-ip
- edge computing
- delete pool member
- nginx
- manage a specific virtual server
- list members of a pool
- list http profiles
- remove a pool member
- add pool member
- list all pools
- list virtual servers
- get details of a specific node
- create a new pool
- manage server pools
- delete a virtual server
- update pool member
- delete pool
- manage backend nodes
- list tcp profiles
- automation
- list tcp traffic profiles
- delete a pool
- multi-cloud
- get virtual server
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
