---
description: A QoS policy rule classifying traffic into QoS classes for bandwidth management and prioritization.
layout: schema
name: QosRule
properties_list:
- description: Unique name of the QoS rule.
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
- description: ''
  name: application
  type: object
- description: ''
  name: service
  type: object
- description: DSCP/TOS marking settings.
  name: dscp-tos
  type: object
- description: ''
  name: action
  type: object
- description: ''
  name: disabled
  type: string
- description: ''
  name: description
  type: string
provider_name: Palo Alto Networks
provider_slug: palo-alto-networks
schema_file: json-schema/pan-os-rest-api-qos-rule-schema.json
slug: pan-os-rest-api-qos-rule
tags:
- Cloud Security
- Cybersecurity
- Firewall
- Network Security
- SASE
- SOAR
- Threat Intelligence
- XDR
title: QosRule
---
