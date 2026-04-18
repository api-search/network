---
description: Site schema from Palo Alto Networks Prisma SD-WAN API
layout: schema
name: Site
properties_list:
- description: Unique identifier for the site.
  name: id
  type: string
- description: Name of the SD-WAN site.
  name: name
  type: string
- description: Optional description of the site.
  name: description
  type: string
- description: Administrative state of the site.
  name: admin_state
  type: string
- description: Role of the site in the SD-WAN topology.
  name: element_cluster_role
  type: string
- description: Physical address of the site.
  name: address
  type: object
- description: Geographic coordinates of the site.
  name: location
  type: object
- description: Tags for organizing and filtering sites.
  name: tags
  type: array
- description: ''
  name: created_at
  type: string
- description: ''
  name: updated_at
  type: string
provider_name: Palo Alto Networks
provider_slug: palo-alto-networks
schema_file: json-schema/prisma-sd-wan-api-site-schema.json
slug: prisma-sd-wan-api-site
tags:
- Cloud Security
- Cybersecurity
- Firewall
- Network Security
- SASE
- SOAR
- Threat Intelligence
- XDR
title: Site
---
