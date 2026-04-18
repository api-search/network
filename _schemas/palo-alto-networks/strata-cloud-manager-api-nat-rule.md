---
description: A NAT policy rule defining source or destination address translation for matching traffic flows.
layout: schema
name: NatRule
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
- description: ''
  name: position
  type: string
- description: Source zones.
  name: from
  type: array
- description: Destination zones.
  name: to
  type: array
- description: ''
  name: source
  type: array
- description: ''
  name: destination
  type: array
- description: Service object name or any.
  name: service
  type: string
- description: ''
  name: source_translation
  type: object
- description: ''
  name: destination_translation
  type: object
- description: ''
  name: nat_type
  type: string
- description: ''
  name: disabled
  type: boolean
- description: ''
  name: description
  type: string
- description: ''
  name: tag
  type: array
provider_name: Palo Alto Networks
provider_slug: palo-alto-networks
schema_file: json-schema/strata-cloud-manager-api-nat-rule-schema.json
slug: strata-cloud-manager-api-nat-rule
tags:
- Cloud Security
- Cybersecurity
- Firewall
- Network Security
- SASE
- SOAR
- Threat Intelligence
- XDR
title: NatRule
---
