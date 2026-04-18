---
consumed_apis:
- meraki
description: Unified network management workflow combining Meraki, Catalyst Center, and SD-WAN APIs for network administrators.
layout: capability
name: Cisco Network Management
operations:
- description: List organizations
  method: GET
  name: list-organizations
  path: /v1/organizations
- description: List networks
  method: GET
  name: list-networks
  path: /v1/networks
personas: []
provider_name: Cisco
provider_slug: cisco
search_terms:
- Network Admin
- networks
- list networks
- list organizations
- list meraki organizations
- security
- sd-wan
- cisco
- unified network management combining meraki and other cisco apis
- collaboration
- enterprise
- network management
- network administrators managing cisco infrastructure
- networking
- network organizations
- list devices in network
- list networks in organization
- list devices
slug: network-management
tags:
- Cisco
- Network Management
tools:
- description: List Meraki organizations
  hints:
    openWorld: true
    readOnly: true
  name: list-organizations
- description: List networks in organization
  hints:
    readOnly: true
  name: list-networks
- description: List devices in network
  hints:
    readOnly: true
  name: list-devices
---
