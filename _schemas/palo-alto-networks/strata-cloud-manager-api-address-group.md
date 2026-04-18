---
description: A group of address objects. Can be static with an explicit member list or dynamic with a tag-based filter expression.
layout: schema
name: AddressGroup
properties_list:
- description: ''
  name: id
  type: string
- description: ''
  name: name
  type: string
- description: ''
  name: folder
  type: string
- description: List of address object names for static groups.
  name: static
  type: array
- description: ''
  name: dynamic
  type: object
- description: ''
  name: description
  type: string
- description: ''
  name: tag
  type: array
provider_name: Palo Alto Networks
provider_slug: palo-alto-networks
schema_file: json-schema/strata-cloud-manager-api-address-group-schema.json
slug: strata-cloud-manager-api-address-group
tags:
- Cloud Security
- Cybersecurity
- Firewall
- Network Security
- SASE
- SOAR
- Threat Intelligence
- XDR
title: AddressGroup
---
