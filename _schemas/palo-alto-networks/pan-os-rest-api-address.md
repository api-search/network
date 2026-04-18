---
description: An address object representing an IP address, subnet, range, wildcard mask, or FQDN used in security policy rules.
layout: schema
name: Address
properties_list:
- description: Unique name of the address object.
  name: '@name'
  type: string
- description: IP address with CIDR netmask (e.g., 10.0.0.0/24).
  name: ip-netmask
  type: string
- description: IP address range (e.g., 10.0.0.1-10.0.0.254).
  name: ip-range
  type: string
- description: IP wildcard mask (e.g., 10.20.1.0/0.0.248.255).
  name: ip-wildcard
  type: string
- description: Fully qualified domain name (e.g., www.example.com).
  name: fqdn
  type: string
- description: Description of the address object.
  name: description
  type: string
- description: ''
  name: tag
  type: object
provider_name: Palo Alto Networks
provider_slug: palo-alto-networks
schema_file: json-schema/pan-os-rest-api-address-schema.json
slug: pan-os-rest-api-address
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
