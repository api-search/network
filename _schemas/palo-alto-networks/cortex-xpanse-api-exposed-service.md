---
description: An internet-exposed network service discovered on an asset.
layout: schema
name: ExposedService
properties_list:
- description: ''
  name: service_id
  type: string
- description: Service name or protocol (e.g., HTTPS, SSH, RDP).
  name: service_name
  type: string
- description: ''
  name: service_type
  type: string
- description: ''
  name: ip_address
  type: array
- description: ''
  name: domain
  type: array
- description: TCP/UDP port number.
  name: port
  type: integer
- description: ''
  name: protocol
  type: string
- description: Cloud or hosting providers detected for this service.
  name: provider
  type: array
- description: ''
  name: business_units
  type: array
- description: Service first discovery timestamp as Unix epoch milliseconds.
  name: created
  type: integer
- description: ''
  name: last_observed
  type: integer
- description: ''
  name: is_active
  type: string
- description: ''
  name: discovery_type
  type: string
provider_name: Palo Alto Networks
provider_slug: palo-alto-networks
schema_file: json-schema/cortex-xpanse-api-exposed-service-schema.json
slug: cortex-xpanse-api-exposed-service
tags:
- Cloud Security
- Cybersecurity
- Firewall
- Network Security
- SASE
- SOAR
- Threat Intelligence
- XDR
title: ExposedService
---
