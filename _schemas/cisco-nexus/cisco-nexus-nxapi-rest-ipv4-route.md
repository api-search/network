---
description: IPv4 static route managed object. DN format is sys/ipv4/inst/dom-{vrfName}/rt-[{prefix}].
layout: schema
name: Ipv4Route
properties_list:
- description: ''
  name: attributes
  type: object
- description: Child next-hop objects
  name: children
  type: array
provider_name: Cisco Nexus Dashboard
provider_slug: cisco-nexus
schema_file: json-schema/cisco-nexus-nxapi-rest-ipv4-route-schema.json
slug: cisco-nexus-nxapi-rest-ipv4-route
tags:
- Data Center
- Infrastructure
- Network Automation
- Networking
- SDN
- Switches
title: Ipv4Route
---
