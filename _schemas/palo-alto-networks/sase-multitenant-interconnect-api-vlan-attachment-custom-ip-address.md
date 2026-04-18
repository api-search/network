---
description: Custom IP address configuration for VLAN attachment BGP peering. Both Cloud Router and Customer Router IP addresses must be provided together with matching prefix lengths (/29 or /30). IP addresses must not be in reserved ranges (RFC1918 private IPs, loopback, etc.) and must not be network or broadcast addresses.
layout: schema
name: VlanAttachmentCustomIpAddress
properties_list:
- description: Cloud Router IP address in CIDR notation (e.g., 169.254.1.1/29). Must have prefix length /29 or /30 and match the prefix length of candidateCustomerRouterIpAddress.
  name: candidateCloudRouterIpAddress
  type: string
- description: Customer Router IP address in CIDR notation (e.g., 169.254.1.2/29). Must have prefix length /29 or /30 and match the prefix length of candidateCloudRouterIpAddress.
  name: candidateCustomerRouterIpAddress
  type: string
provider_name: Palo Alto Networks
provider_slug: palo-alto-networks
schema_file: json-schema/sase-multitenant-interconnect-api-vlan-attachment-custom-ip-address-schema.json
slug: sase-multitenant-interconnect-api-vlan-attachment-custom-ip-address
tags:
- Cloud Security
- Cybersecurity
- Firewall
- Network Security
- SASE
- SOAR
- Threat Intelligence
- XDR
title: VlanAttachmentCustomIpAddress
---
