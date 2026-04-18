---
description: A virtual system (vsys) on the PAN-OS firewall.
layout: schema
name: VirtualSystem
properties_list:
- description: Virtual system name (e.g., vsys1, vsys2).
  name: '@name'
  type: string
- description: Human-readable display name for the vsys.
  name: display-name
  type: string
- description: Imported network resources for this vsys.
  name: import
  type: object
provider_name: Palo Alto Networks
provider_slug: palo-alto-networks
schema_file: json-schema/pan-os-rest-api-virtual-system-schema.json
slug: pan-os-rest-api-virtual-system
tags:
- Cloud Security
- Cybersecurity
- Firewall
- Network Security
- SASE
- SOAR
- Threat Intelligence
- XDR
title: VirtualSystem
---
