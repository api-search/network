---
description: A group of address objects. Can be static with an explicit member list or dynamic with a tag-based filter expression.
layout: schema
name: AddressGroup
properties_list:
- description: Unique name of the address group.
  name: '@name'
  type: string
- description: Static address group with explicit members.
  name: static
  type: object
- description: Dynamic address group with tag-based filter.
  name: dynamic
  type: object
- description: ''
  name: description
  type: string
- description: ''
  name: tag
  type: object
provider_name: Palo Alto Networks
provider_slug: palo-alto-networks
schema_file: json-schema/pan-os-rest-api-address-group-schema.json
slug: pan-os-rest-api-address-group
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
