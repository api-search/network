---
description: A NAT policy rule defining source or destination address translation for matching traffic.
layout: schema
name: NatRule
properties_list:
- description: Unique name of the NAT rule.
  name: '@name'
  type: string
- description: ''
  name: from
  type: object
- description: ''
  name: to
  type: object
- description: ''
  name: source
  type: object
- description: ''
  name: destination
  type: object
- description: Service object or any.
  name: service
  type: string
- description: Source address translation settings.
  name: source-translation
  type: object
- description: Destination address translation settings.
  name: destination-translation
  type: object
- description: ''
  name: nat-type
  type: string
- description: ''
  name: disabled
  type: string
- description: ''
  name: description
  type: string
- description: ''
  name: tag
  type: object
provider_name: Palo Alto Networks
provider_slug: palo-alto-networks
schema_file: json-schema/pan-os-rest-api-nat-rule-schema.json
slug: pan-os-rest-api-nat-rule
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
