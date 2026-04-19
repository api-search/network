---
consumed_apis:
- nxapi-rest
description: Unified workflow for network administrators to configure and monitor Cisco Nexus switches including interfaces, VLANs, routing, and system features via the NX-API REST DME object model.
layout: capability
name: Cisco Nexus Switch Management
operations:
- description: Get system information
  method: GET
  name: get-system-info
  path: /v1/system
- description: List all physical interfaces
  method: GET
  name: list-interfaces
  path: /v1/interfaces
- description: Get interface details
  method: GET
  name: get-interface
  path: /v1/interfaces/{interfaceId}
- description: List all VLANs
  method: GET
  name: list-vlans
  path: /v1/vlans
- description: Create a VLAN
  method: POST
  name: create-vlan
  path: /v1/vlans
- description: Get VLAN details
  method: GET
  name: get-vlan
  path: /v1/vlans/{vlanEncap}
- description: Delete a VLAN
  method: DELETE
  name: delete-vlan
  path: /v1/vlans/{vlanEncap}
- description: List all static routes
  method: GET
  name: list-routes
  path: /v1/routes
personas: []
provider_name: Cisco Nexus Dashboard
provider_slug: cisco-nexus
search_terms:
- list interfaces
- configure system
- interface management
- network management
- apply system-level configuration changes
- configure svi
- delete vlan
- configure features
- get vlan details
- list all vlan bridge domains on the switch
- get the full bgp configuration tree
- static route management
- enable or disable nx-os features (interface-vlan, bgp, ospf, lacp)
- get svi
- create or modify a vlan bridge domain
- list static routes
- infrastructure
- get system info
- get system information
- get configuration and operational state of a physical interface
- cisco
- vlan management
- sdn
- configure a physical ethernet interface (admin state, speed, vlan, etc.)
- single interface operations
- configure static route
- create a vlan
- get switch virtual interface configuration
- nexus
- get interface
- get interface details
- network automation
- list routes
- list all static routes
- data center
- delete a vlan
- create or modify ipv4 static routes
- configure interface
- get vlan
- list all vlans
- get vlan bridge domain details
- create or modify a switch virtual interface for layer 3 routing
- list all ipv4 static routes across all vrfs
- list all physical ethernet interfaces on the switch
- single vlan operations
- create vlan
- get bgp config
- switches
- get nexus switch system information including hostname, serial, and nx-os version
- list vlans
- get static route
- list all physical interfaces
- get a specific static route by vrf and prefix
- networking
- delete a vlan bridge domain from the switch
- system information
slug: switch-management
tags:
- Cisco
- Nexus
- Network Management
- Data Center
tools:
- description: Get Nexus switch system information including hostname, serial, and NX-OS version
  hints:
    openWorld: true
    readOnly: true
  name: get-system-info
- description: List all physical Ethernet interfaces on the switch
  hints:
    readOnly: true
  name: list-interfaces
- description: Get configuration and operational state of a physical interface
  hints:
    readOnly: true
  name: get-interface
- description: Configure a physical Ethernet interface (admin state, speed, VLAN, etc.)
  hints:
    idempotent: true
    readOnly: false
  name: configure-interface
- description: List all VLAN bridge domains on the switch
  hints:
    readOnly: true
  name: list-vlans
- description: Create or modify a VLAN bridge domain
  hints:
    readOnly: false
  name: create-vlan
- description: Get VLAN bridge domain details
  hints:
    readOnly: true
  name: get-vlan
- description: Delete a VLAN bridge domain from the switch
  hints:
    destructive: true
  name: delete-vlan
- description: Get Switch Virtual Interface configuration
  hints:
    readOnly: true
  name: get-svi
- description: Create or modify a Switch Virtual Interface for Layer 3 routing
  hints:
    readOnly: false
  name: configure-svi
- description: List all IPv4 static routes across all VRFs
  hints:
    readOnly: true
  name: list-static-routes
- description: Create or modify IPv4 static routes
  hints:
    readOnly: false
  name: configure-static-route
- description: Get a specific static route by VRF and prefix
  hints:
    readOnly: true
  name: get-static-route
- description: Get the full BGP configuration tree
  hints:
    readOnly: true
  name: get-bgp-config
- description: Enable or disable NX-OS features (interface-vlan, BGP, OSPF, LACP)
  hints:
    readOnly: false
  name: configure-features
- description: Apply system-level configuration changes
  hints:
    readOnly: false
  name: configure-system
---
