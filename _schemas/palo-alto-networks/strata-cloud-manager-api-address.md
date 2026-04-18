---
description: An address object representing an IP address, subnet, range, or FQDN used in security policy rules.
layout: schema
name: Address
properties_list:
- description: Unique identifier assigned by the system.
  name: id
  type: string
- description: Unique name of the address object within the folder scope.
  name: name
  type: string
- description: Configuration folder containing this object.
  name: folder
  type: string
- description: ''
  name: snippet
  type: string
- description: IP address with CIDR netmask (e.g., 10.0.0.0/24).
  name: ip_netmask
  type: string
- description: IP address range (e.g., 10.0.0.1-10.0.0.254).
  name: ip_range
  type: string
- description: IP wildcard mask notation.
  name: ip_wildcard
  type: string
- description: Fully qualified domain name (e.g., www.example.com).
  name: fqdn
  type: string
- description: ''
  name: description
  type: string
- description: Tags assigned to this address object.
  name: tag
  type: array
provider_name: Palo Alto Networks
provider_slug: palo-alto-networks
schema_file: json-schema/strata-cloud-manager-api-address-schema.json
slug: strata-cloud-manager-api-address
tags:
- Cloud Security
- Cybersecurity
- Firewall
- Network Security
- SASE
- SOAR
- Threat Intelligence
- XDR
title: Address
---
