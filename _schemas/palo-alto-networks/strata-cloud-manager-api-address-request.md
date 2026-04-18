---
description: Request body for creating or updating an address object.
layout: schema
name: AddressRequest
properties_list:
- description: ''
  name: name
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
- description: Fully qualified domain name.
  name: fqdn
  type: string
- description: ''
  name: description
  type: string
- description: ''
  name: tag
  type: array
provider_name: Palo Alto Networks
provider_slug: palo-alto-networks
schema_file: json-schema/strata-cloud-manager-api-address-request-schema.json
slug: strata-cloud-manager-api-address-request
tags:
- Cloud Security
- Cybersecurity
- Firewall
- Network Security
- SASE
- SOAR
- Threat Intelligence
- XDR
title: AddressRequest
---
