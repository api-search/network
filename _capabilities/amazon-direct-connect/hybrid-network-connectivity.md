---
consumed_apis:
- direct-connect
description: Workflow capability for network engineers and cloud architects to manage dedicated private connections between on-premises networks and AWS using Amazon Direct Connect. Covers connection provisioning, virtual interface management, gateway associations, LAG configuration, and network troubleshooting.
layout: capability
name: Amazon Direct Connect Hybrid Network Connectivity
operations:
- description: List all Direct Connect connections
  method: GET
  name: describe-connections
  path: /v1/connections
- description: Create a new dedicated connection
  method: POST
  name: create-connection
  path: /v1/connections
- description: List all virtual interfaces
  method: GET
  name: describe-virtual-interfaces
  path: /v1/virtual-interfaces
- description: Create a private virtual interface for VPC access
  method: POST
  name: create-private-vif
  path: /v1/virtual-interfaces
- description: Create a transit virtual interface for Transit Gateway
  method: POST
  name: create-transit-vif
  path: /v1/virtual-interfaces
- description: List Direct Connect gateways
  method: GET
  name: describe-gateways
  path: /v1/gateways
- description: Create a Direct Connect gateway
  method: POST
  name: create-gateway
  path: /v1/gateways
- description: List link aggregation groups
  method: GET
  name: describe-lags
  path: /v1/lags
- description: Create a link aggregation group
  method: POST
  name: create-lag
  path: /v1/lags
- description: List Direct Connect colocation facilities
  method: GET
  name: describe-locations
  path: /v1/locations
personas: []
provider_name: Amazon Direct Connect
provider_slug: amazon-direct-connect
search_terms:
- link aggregation groups for redundant connections
- hybrid cloud
- amazon direct connect
- delete connection
- direct connect gateways for multi-vpc and multi-region access
- list direct connect gateways for multi-region and multi-vpc connectivity
- list all virtual interfaces
- describe connections
- network engineering
- list all direct connect connections
- managing virtual interfaces and bgp peering
- create transit virtual interface
- list link aggregation groups
- create a private virtual interface for accessing a vpc via direct connect
- describe locations
- create private virtual interface
- list all available direct connect colocation facility locations
- direct connect
- networking
- delete a virtual interface from a direct connect connection
- create a new dedicated connection
- Network Engineer
- create a private virtual interface for vpc access
- describe virtual interfaces
- Cloud Architect
- create a link aggregation group
- dedicated physical connections to aws
- describe lags
- list all direct connect dedicated connections in the account
- create a link aggregation group to bundle multiple connections for redundancy
- create a new dedicated physical connection at a direct connect location
- end-to-end hybrid network management using amazon direct connect
- create lag
- list link aggregation groups providing redundant bundled connections
- delete virtual interface
- describe gateways
- create transit vif
- create a direct connect gateway
- create a transit virtual interface for accessing transit gateway via direct connect
- dedicated connection
- create connection
- list all virtual interfaces configured on direct connect connections
- create a direct connect gateway to attach multiple vpcs across regions
- delete a direct connect connection
- create private vif
- aws
- list direct connect colocation facilities
- multi-vpc and multi-region access via direct connect gateways
- available direct connect locations
- virtual interfaces providing network access
- list direct connect gateways
- create direct connect gateway
- provisioning and managing physical dedicated connections
- describe direct connect gateways
- create a transit virtual interface for transit gateway
- create gateway
- cloud architect designing hybrid network connectivity between on-premises and aws
- network engineer provisioning and managing dedicated connections and virtual interfaces
slug: hybrid-network-connectivity
tags:
- Amazon Direct Connect
- Hybrid Cloud
- Network Engineering
- Dedicated Connection
- AWS
tools:
- description: List all Direct Connect dedicated connections in the account
  hints:
    openWorld: true
    readOnly: true
  name: describe-connections
- description: Create a new dedicated physical connection at a Direct Connect location
  hints:
    destructive: false
    readOnly: false
  name: create-connection
- description: Delete a Direct Connect connection
  hints:
    destructive: true
    idempotent: true
    readOnly: false
  name: delete-connection
- description: List all virtual interfaces configured on Direct Connect connections
  hints:
    openWorld: true
    readOnly: true
  name: describe-virtual-interfaces
- description: Create a private virtual interface for accessing a VPC via Direct Connect
  hints:
    destructive: false
    readOnly: false
  name: create-private-virtual-interface
- description: Create a transit virtual interface for accessing Transit Gateway via Direct Connect
  hints:
    destructive: false
    readOnly: false
  name: create-transit-virtual-interface
- description: Delete a virtual interface from a Direct Connect connection
  hints:
    destructive: true
    idempotent: true
    readOnly: false
  name: delete-virtual-interface
- description: List Direct Connect gateways for multi-region and multi-VPC connectivity
  hints:
    openWorld: true
    readOnly: true
  name: describe-direct-connect-gateways
- description: Create a Direct Connect gateway to attach multiple VPCs across regions
  hints:
    destructive: false
    readOnly: false
  name: create-direct-connect-gateway
- description: List link aggregation groups providing redundant bundled connections
  hints:
    openWorld: true
    readOnly: true
  name: describe-lags
- description: Create a link aggregation group to bundle multiple connections for redundancy
  hints:
    destructive: false
    readOnly: false
  name: create-lag
- description: List all available Direct Connect colocation facility locations
  hints:
    openWorld: true
    readOnly: true
  name: describe-locations
---
